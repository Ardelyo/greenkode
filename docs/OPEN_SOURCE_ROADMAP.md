# 🌿 GreenKode Open Source Roadmap

## Vision
To transform GreenKode from a student project into a robust, community-driven tool for sustainable software engineering. The goal is to make it **Smarter**, **Informative**, **Realistic**, **Consistent**, and **Always Learning**.

---

## 🧠 Phase 1: Smarter (Enhanced Intelligence)
*Current State: Basic O(n^2) and import detection.*
*Goal: Detect a wider range of energy inefficiencies.*

### 1.1. Advanced AST Analysis
-   **String Concatenation**: Detect `s += "string"` inside loops (recommend `.join()`).
-   **File I/O**: Detect `f.read()` on large files (recommend line-by-line iteration).
-   **Global Variables**: Warn against excessive use of global state (memory/cache inefficiency).
-   **Regex Compilation**: Detect `re.search()` inside loops (recommend `re.compile()` outside).

### 1.2. Complexity Estimation
-   Implement a `ComplexityVisitor` that attempts to estimate Cyclomatic Complexity and Big-O notation for functions, flagging anything above $O(n^2)$.

---

## 📚 Phase 2: Always Learning (Extensibility)
*Current State: Hardcoded rules in `analyzer.py`.*
*Goal: Decouple rules from code to allow easy updates.*

### 2.1. The "Green Knowledge Base"
-   Create `data/rules.json` (or YAML) to store detection patterns.
-   **Structure**:
    ```json
    {
      "id": "GK001",
      "name": "Nested Loop",
      "severity": "High",
      "description": "Detected nested loops which may cause O(n^2) complexity.",
      "remediation": "Use vectorization (NumPy) or a hash map."
    }
    ```

### 2.2. Dynamic Rule Loader
-   Refactor `CodeInspector` to load rules from the JSON file.
-   **Future Feature**: `greenkode update` command to fetch the latest rules from the GitHub repository without reinstalling the package.

---

## 📊 Phase 3: Informative (Better UX)
*Current State: Basic table output.*
*Goal: Provide actionable insights and educational value.*

### 3.1. "Why This Matters"
-   Expand the CLI output to include a "Why" section for each error, explaining the energy impact.
-   Example: *"Inefficient string concatenation creates a new string object for every iteration, causing memory spikes and CPU churn."*

### 3.2. Real-World Equivalents
-   Translate `kgCO2` into relatable metrics:
    -   📱 Smartphones charged.
    -   🚗 Miles driven.
    -   💡 Hours of a lightbulb.

### 3.3. Export Options
-   Add `--json` and `--html` flags to `greenkode run` and `check` for integration with CI/CD pipelines (GitHub Actions).

---

## 🌍 Phase 4: Realistic (Robust Engine)
*Current State: Relies on CodeCarbon/RAPL.*
*Goal: Handle edge cases and diverse environments.*

### 4.1. Simulation Mode
-   If Intel RAPL is unavailable (e.g., MacOS M1/M2, some VMs), fallback to a "Simulation Mode" that estimates energy based on CPU utilization and time.

### 4.2. Regional Awareness
-   Add a `--region` flag (e.g., `greenkode run --region US-CA`) to use specific carbon intensity factors for more accurate CO2 calculations.

---

## 🤝 Phase 5: Consistent (Community Ready)
*Current State: Student project structure.*
*Goal: Professional open-source standard.*

### 5.1. Documentation
-   **`CONTRIBUTING.md`**: Guidelines for PRs, setting up dev environment, and code style.
-   **`CODE_OF_CONDUCT.md`**: Standard Contributor Covenant.
-   **`governance.md`**: How decisions are made.

### 5.2. Quality Assurance
-   **Pre-commit Hooks**: Setup `black`, `isort`, and `flake8` to run on every commit.
-   **Type Hints**: Ensure 100% type coverage with `mypy`.
-   **Unit Tests**: Expand `tests/` coverage to >80%.

### 5.3. GitHub Workflows
-   Create `.github/workflows/test.yml` to run tests on Push.
-   Create `.github/workflows/publish.yml` to auto-publish to PyPI on release.

---

## 🗓️ Execution Plan (Immediate Next Steps)

1.  **Refactor `analyzer.py`**: Move hardcoded rules to a dictionary/constant structure (precursor to JSON).
2.  **Add `CONTRIBUTING.md`**: Essential for the competition and open source.
3.  **Implement "String Concatenation" Check**: A quick win for "Smarter".
