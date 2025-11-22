"""
GreenKode Analyzer
------------------
This module performs static analysis on Python code to detect potential
energy inefficiencies using the Abstract Syntax Tree (AST).
"""

import ast
import os
from typing import List, Union

class CodeInspector:
    """
    Analyzes code for energy-inefficient patterns.
    """
    def __init__(self, source: Union[str, bytes]):
        """
        Args:
            source (str | bytes): The source code or filename to analyze.
        """
        self.suggestions: List[str] = []
        if os.path.exists(source) and os.path.isfile(source):
            with open(source, "r", encoding="utf-8") as f:
                self.source_code = f.read()
        else:
            self.source_code = source
        
        try:
            self.tree = ast.parse(self.source_code)
        except SyntaxError as e:
            self.suggestions.append(f"Syntax Error: Could not parse code. {e}")
            self.tree = None

    def analyze(self) -> List[str]:
        """
        Runs all detection methods and returns a list of suggestions.
        """
        if not self.tree:
            return self.suggestions
            
        self.detect_nested_loops(self.tree)
        self.detect_heavy_imports(self.tree)
        return self.suggestions

    def detect_nested_loops(self, node: ast.AST, depth: int = 0) -> None:
        """
        Recursively checks for nested loops (O(n^2) or worse).
        """
        if isinstance(node, (ast.For, ast.While)):
            if depth > 0:
                self.suggestions.append(
                    f"Line {node.lineno}: Nested loop detected. This may have O(n^{depth+1}) complexity. "
                    "Consider vectorization or algorithmic optimization."
                )
            # Continue checking children with increased depth
            for child in ast.iter_child_nodes(node):
                self.detect_nested_loops(child, depth + 1)
        else:
            # Continue checking children without increasing depth (unless it's a loop)
            # But we need to be careful not to reset depth if we are inside a loop but traversing non-loop nodes
            # Actually, the prompt asks to check for For inside For.
            # A simple traversal keeping track of loop depth is better.
            for child in ast.iter_child_nodes(node):
                self.detect_nested_loops(child, depth)

    def detect_heavy_imports(self, node: ast.AST) -> None:
        """
        Checks for heavy library imports that might be unnecessary if not fully used.
        """
        heavy_libs = {"pandas", "tensorflow", "torch", "numpy", "scikit-learn"}
        
        for child in ast.walk(node):
            if isinstance(child, ast.Import):
                for alias in child.names:
                    if alias.name in heavy_libs:
                        self.suggestions.append(
                            f"Line {child.lineno}: Heavy library '{alias.name}' imported. "
                            "Ensure you are using it efficiently or consider lighter alternatives if possible."
                        )
            elif isinstance(child, ast.ImportFrom):
                if child.module in heavy_libs:
                    self.suggestions.append(
                        f"Line {child.lineno}: Heavy library '{child.module}' imported. "
                        "Ensure you are using it efficiently."
                    )
