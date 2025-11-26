# 🤝 Contributing to GreenKode

Thank you for your interest in contributing to GreenKode! We are building a tool to help 8 billion people (and their developers) save energy.

## 🌟 How to Contribute

We welcome contributions of all forms:
-   **Bug Fixes**: Found a crash? Fix it!
-   **New Features**: Want to detect a new inefficient pattern?
-   **Documentation**: Typos, unclear guides, or translations.
-   **Ideas**: Open an issue to discuss new concepts.

## 🛠️ Development Setup

1.  **Fork & Clone**
    ```bash
    git clone https://github.com/YOUR_USERNAME/greenkode.git
    cd greenkode
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -e .[dev]
    ```

## 🧪 Running Tests

We use `pytest` for testing. Ensure all tests pass before submitting a PR.

```bash
pytest
```

## 📝 Coding Standards

-   **Style**: We follow PEP 8.
-   **Formatting**: Please run `black .` before committing.
-   **Type Hints**: Use type hints for function arguments and return values.

## 🚀 Submitting a Pull Request (PR)

1.  Create a new branch: `git checkout -b feature/my-new-feature`.
2.  Commit your changes: `git commit -m "Add amazing new feature"`.
3.  Push to the branch: `git push origin feature/my-new-feature`.
4.  Open a Pull Request on GitHub.

## 📜 Code of Conduct

Please be respectful and inclusive. We are all here to learn and save the planet. Harassment of any kind will not be tolerated.

---
*Happy Coding & Happy Planet!* 🌍
