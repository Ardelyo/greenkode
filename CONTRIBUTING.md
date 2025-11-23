# Contributing to GreenKode 🌿

First off, thank you for considering contributing to GreenKode! It's people like you that make the open-source community such an amazing place to learn, inspire, and create.

GreenKode is more than just a tool; it's a movement towards **Sustainable Software Engineering**. By contributing, you are helping developers worldwide reduce their digital carbon footprint.

## 🤝 How Can You Contribute?

### 1. Report Bugs 🐛
Found a bug? Great! (Well, not great, but we want to know).
-   **Check existing issues** to see if it's already reported.
-   **Open a new issue** with a clear title and description.
-   Include a minimal reproduction code snippet if possible.

### 2. Suggest Enhancements 💡
Have an idea to make GreenKode smarter?
-   We love new ideas for **AST analysis rules**!
-   Open an issue with the tag `enhancement`.
-   Describe the inefficient pattern and the proposed solution.

### 3. Pull Requests 🚀
Ready to write some code?
1.  **Fork** the repository.
2.  **Clone** your fork locally.
3.  **Create a branch** for your feature (`git checkout -b feature/amazing-feature`).
4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
5.  **Make your changes**.
6.  **Run tests** (we use `pytest`):
    ```bash
    pytest
    ```
7.  **Commit** your changes with a descriptive message.
8.  **Push** to your branch.
9.  **Open a Pull Request**.

## 📐 Coding Standards

To keep our codebase clean and "Green", please follow these rules:

-   **Style**: We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/).
-   **Type Hints**: Please use Python type hints for all function arguments and return values.
    ```python
    def calculate_impact(energy: float) -> float: ...
    ```
-   **Docstrings**: Document your classes and functions using the Google style guide.
-   **Complexity**: Keep functions small and focused. If a function is $O(n^2)$, you better have a good excuse! 😉

## 🧪 Testing

-   Add a test case for any new feature or bug fix.
-   Ensure all existing tests pass before submitting.

## 📜 Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

---

**"The greenest code is the code you don't write. The second greenest is the code you optimize."**
