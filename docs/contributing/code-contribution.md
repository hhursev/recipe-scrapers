# Code Contribution

!!! note "Prerequisites"
    This guide assumes you have basic familiarity with Python development, including using `pip`,
    `virtual environments`, and `git`. Teaching these core concepts is beyond the scope of this
    documentation - please ensure you're comfortable with them before proceeding.

!!! warning "Python Version Requirement"
    We strongly recommend using Python 3.11 or above for all development work related to `recipe-scrapers`.
    This version comes with `tomllib` support built-in, which is essential for the project's configuration handling.

We welcome various types of code contributions to `recipe-scrapers`, including:

- Bug fixes
- New recipe site scrapers
- Performance improvements
- Feature enhancements
- Test coverage improvements

## Initial Setup

Fork the [recipe-scrapers repository](https://github.com/hhursev/recipe-scrapers) on GitHub and follow these setup steps:

!!! tip "Quick Setup"
    ```bash
    # Clone your fork
    git clone https://github.com/YOUR-USERNAME/recipe-scrapers.git
    cd recipe-scrapers

    # Set up Python environment
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    python -m pip install --upgrade pip
    pip install -e ".[all]"
    ```

!!! note "Virtual Environment"
    Remember to activate your virtual environment each time you work on the project:
    ```bash
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

## Development Workflow

Create a new branch for your changes:
```bash
git checkout -b feature/your-feature-name  # for new features
# or
git checkout -b fix/your-fix-name      # for bug fixes
# or
git checkout -b site/website-name      # for new site scrapers
```

After making your changes commit them:

```bash
git add -p  # Review changes before adding them
git commit -m "meaningful commit message"
git push origin your-branch-name
```

Then create a Pull Request back to the [main repository](https://github.com/hhursev/recipe-scrapers) from your fork.

### Pre-commit Hooks

The project uses pre-commit hooks to ensure code quality and consistency. These hooks run
automatically when you commit changes, handling tasks like:

- Code formatting (black, isort)
- Linting (flake8)
- Type checking
- Other code quality checks


## What happens after a PR

When you submit your PR:

1. Our CI suite will run against your code to ensure everything works as expected. You can run the tests locally before submitting:
    ```bash
    python -m unittest
    # or
    unittest-parallel --level test
    ```

2. Community members and core contributors will review your code. They may:
    - Request changes or improvements
    - Suggest alternative approaches
    - Provide feedback on test coverage
    - Ask for documentation updates

3. Once approved, a core contributor will merge your PR
    - Your contribution will be included in the next release
    - Feel free to tackle any follow-up improvements in subsequent PRs

Don't worry if your first PR needs some adjustments - this is normal and part of the collaborative development process!


## Development Guidelines (Coming Soon)

While we're working on comprehensive documentation, the codebase is designed to
be self-explanatory. As a developer, you can understand our patterns and expectations
by taking a look at existing scrapers in the `recipe_scrapers/` directory.

!!! tip "Generator Tool"
    If you're adding a new site scraper, you can use our generator command to create a template:

    ```bash
    python generate.py <ClassName> <URL>
    ```

    Where:

    - `ClassName`: The name of your new scraper class (e.g., `BBCGoodFood`)
    - `URL`: A sample recipe URL from the target site. This will be saved in `test_data/` for testing.

!!! warning "Work in Progress"
    This contributing guide is currently being developed. Meanwhile, you can check these PRs as examples of good contribution standards:

    - [#1414](https://github.com/hhursev/recipe-scrapers/pull/1414/) - Adding a new site scraper
    - [#1432](https://github.com/hhursev/recipe-scrapers/pull/1432/) - Fixing broken functionality
    - [#1434](https://github.com/hhursev/recipe-scrapers/pull/1434/) - Test improvements
    - [#1345](https://github.com/hhursev/recipe-scrapers/pull/1345/) - CI Improvements
