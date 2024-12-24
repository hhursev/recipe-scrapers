# Contributing to Documentation

!!! note "Prerequisites"
    This guide assumes you have basic familiarity with Python development, including using `pip`,
    `virtual environments`, and `git`. Teaching these core concepts is beyond the scope of this
    documentation - please ensure you're comfortable with them before proceeding.

!!! warning "Python Version Requirement"
    We strongly recommend using Python 3.11 or above for all development work related to `recipe-scrapers`.
    This version comes with `tomllib` support built-in, which is essential for the project's configuration handling.

The documentation for `recipe-scrapers` is hosted at [docs.recipe-scrapers.com](https://docs.recipe-scrapers.com).
We welcome contributions to improve and expand our documentation! This guide will help you get started with making
documentation changes.

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

Create a new branch for your documentation changes:
```bash
git checkout -b docs/your-feature-name
```

## Previewing Documentation Changes

!!! example "Local Development"
    1. From the project root directory, start the MkDocs development server:
       ```bash
       mkdocs serve
       ```
    2. Open your browser and navigate to `http://127.0.0.1:8000`

The preview will automatically update as you make changes to the documentation files.

## Making Documentation Changes

!!! info "Documentation Structure"
    - Documentation source files are written in Markdown and located in the `docs/` directory
    - Images and other assets should be placed in the `docs/assets/` directory
    - The documentation structure is defined in `mkdocs.yaml` at the root of the repository

## Submitting Your Changes

1. Commit your changes with a descriptive message:
   ```bash
   git add docs/
   git commit -m "docs: describe your changes here"
   ```

2. Push your changes to your fork:
   ```bash
   git push origin docs/your-feature-name
   ```

3. Create a Pull Request (PR) from your fork to the main [recipe-scrapers](https://github.com/hhursev/recipe-scrapers) repository.

!!! success "PR Preview"
    When you create a PR, a special preview URL will be generated where your documentation changes can be reviewed. This will make it easy for maintainers to see your changes in action.

## Documentation Style Guidelines

!!! note "Style Guide"
    - Use clear, concise language
    - Include code examples where appropriate
    - Follow the existing documentation structure
    - Add screenshots or diagrams when they help explain concepts
    - Ensure all links are working
    - Use proper Markdown formatting

## Need Help?

!!! question "Getting Support"
    If you have questions or need assistance with documentation contributions, please:

    - Open an [issue on GitHub](https://github.com/hhursev/recipe-scrapers/issues)
    - Check existing documentation for reference
