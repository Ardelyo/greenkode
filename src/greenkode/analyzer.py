"""
GreenKode Analyzer
------------------
This module performs static analysis on Python code to detect potential
energy inefficiencies using the Abstract Syntax Tree (AST).
It loads detection rules dynamically from a JSON database.
"""

import ast
import os
import json
from typing import List, Union, Dict, Any

class CodeInspector:
    """
    Analyzes code for energy-inefficient patterns using dynamic rules.
    """
    def __init__(self, source: Union[str, bytes]):
        """
        Args:
            source (str | bytes): The source code or filename to analyze.
        """
        self.suggestions: List[Dict[str, Any]] = []
        self.rules = self._load_rules()
        
        if os.path.exists(source) and os.path.isfile(source):
            with open(source, "r", encoding="utf-8") as f:
                self.source_code = f.read()
        else:
            self.source_code = source
        
        try:
            self.tree = ast.parse(self.source_code)
        except SyntaxError as e:
            # Syntax error is a special case, not in rules.json yet
            self.suggestions.append({
                "id": "ERR",
                "name": "Syntax Error",
                "severity": "Critical",
                "line": e.lineno or 0,
                "message": f"Could not parse code: {e}",
                "remediation": "Fix syntax errors before analysis."
            })
            self.tree = None

    def _load_rules(self) -> Dict[str, Dict[str, str]]:
        """Loads rules from the data/rules.json file."""
        rules = {}
        try:
            # Locate rules.json relative to this file
            base_path = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(base_path, "data", "rules.json")
            
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for rule in data:
                    rules[rule["id"]] = rule
        except Exception as e:
            print(f"Warning: Could not load rules.json: {e}")
        return rules

    def _add_issue(self, rule_id: str, node: ast.AST, **kwargs):
        """Helper to add an issue based on a rule ID."""
        rule = self.rules.get(rule_id)
        if rule:
            message = rule["description"].format(**kwargs)
            # Calculate depth for nested loop message if needed
            if rule_id == "GK001" and "depth" in kwargs:
                 message = message.replace("{depth}", str(kwargs["depth"] + 1))

            self.suggestions.append({
                "id": rule_id,
                "name": rule["name"],
                "severity": rule["severity"],
                "line": node.lineno,
                "message": message,
                "remediation": rule["remediation"]
            })

    def analyze(self) -> List[Dict[str, Any]]:
        """
        Runs all detection methods and returns a list of structured suggestions.
        """
        if not self.tree:
            return self.suggestions
            
        self.detect_nested_loops(self.tree)
        self.detect_heavy_imports(self.tree)
        self.detect_loop_inefficiencies(self.tree)
        return self.suggestions

    def detect_nested_loops(self, node: ast.AST, depth: int = 0) -> None:
        """Recursively checks for nested loops."""
        if isinstance(node, (ast.For, ast.While)):
            if depth > 0:
                self._add_issue("GK001", node, depth=depth)
            for child in ast.iter_child_nodes(node):
                self.detect_nested_loops(child, depth + 1)
        else:
            for child in ast.iter_child_nodes(node):
                self.detect_nested_loops(child, depth)

    def detect_heavy_imports(self, node: ast.AST) -> None:
        """Checks for heavy library imports."""
        heavy_libs = {"pandas", "tensorflow", "torch", "numpy", "scikit-learn"}
        
        for child in ast.walk(node):
            if isinstance(child, ast.Import):
                for alias in child.names:
                    if alias.name in heavy_libs:
                        self._add_issue("GK002", child, library=alias.name)
            elif isinstance(child, ast.ImportFrom):
                if child.module in heavy_libs:
                    self._add_issue("GK002", child, library=child.module)

    def detect_loop_inefficiencies(self, node: ast.AST, in_loop: bool = False) -> None:
        """Checks for inefficient operations inside loops."""
        if isinstance(node, (ast.For, ast.While)):
            in_loop = True

        if in_loop:
            # GK003: String Concatenation
            if isinstance(node, ast.AugAssign) and isinstance(node.op, ast.Add):
                is_string_op = False
                if isinstance(node.value, (ast.Str, ast.Constant)): 
                    if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                        is_string_op = True
                    elif isinstance(node.value, ast.Str):
                        is_string_op = True
                
                if isinstance(node.target, ast.Name):
                    if any(hint in node.target.id.lower() for hint in ['str', 'text', 'html', 'json', 'xml', 'csv', 'log', 's']):
                        is_string_op = True

                if is_string_op:
                    self._add_issue("GK003", node)

            # GK004: Regex calls
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute):
                    if isinstance(node.func.value, ast.Name) and node.func.value.id == 're':
                        if node.func.attr in {'search', 'match', 'findall', 'sub', 'split'}:
                            self._add_issue("GK004", node, func=node.func.attr)

        for child in ast.iter_child_nodes(node):
            self.detect_loop_inefficiencies(child, in_loop)
