# Setup

Thank you for your interest in contributing to this project!

Follow these steps to set up your environment for development.

!!! note "Prerequisites"
    This guide assumes you have basic familiarity with Python development, including using `pip`,
    `virtual environments`, and `git`. These core concepts are beyond the scope of this documentation.


!!! warning "Python Version Requirement"
    We strongly recommend using Python 3.11 or above for all development work related to `recipe-scrapers`.
    This version includes built-in `tomllib` support, which is essential for the project's configuration handling.


We welcome various types of code contributions to `recipe-scrapers`, including:

- Bug fixes
- New recipe site scrapers
- Performance improvements
- Feature enhancements
- Test coverage improvements


## Fork the Repository

1. Navigate to [our repository on GitHub](https://github.com/hhursev/recipe-scrapers).
2. Click the "Fork" button in the top right corner to create your own copy of the repository.


## Clone Your Fork

```sh
git clone https://github.com/<your-username>/recipe-scrapers.git
cd recipe-scrapers
```

## Set Upstream Remote

!!! tip "Upstream Remote"
    Setting the upstream remote allows you to sync changes from the original repository to your fork.
    This is useful to keep your fork up-to-date with the latest changes.

```sh
git remote add upstream https://github.com/hhursev/recipe-scrapers.git
```


## Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies. You can create one using `venv`

```sh
python -m venv .venv
source .venv/bin/activate  # On Windows: `.venv\Scripts\activate`
```

!!! tip "Virtual Environment"
    Remember to activate your virtual environment each time you work on the project:
```sh
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

## Install Dependencies

Install the required dependencies using `pip`

```sh
pip install -e ".[all]"
```

Our pyproject.toml file lists the installed dependencies and their purposes.


## Development Workflow

Create a new branch for your changes:
```sh
git checkout -b fix/your-fix-name     # for bug fixes
# or
git checkout -b site/website-name     # for new site scrapers
# or
git checkout -b docs/your-addition    # for docs updates
# or
git checkout -b feature/feature-name  # for new features
```

After making your changes, commit them:

```sh
git add -p  # Review changes before adding them
git commit -m "meaningful commit message"
git push origin your-branch-name
```

### Pre-commit Hooks

The project uses pre-commit hooks to ensure code quality and consistency. These hooks run
automatically when you commit changes, handling tasks like:

- Code formatting (black, isort)
- Linting (flake8)
- Type checking
- Other code quality checks


## Syncing Your Fork

To keep your fork up-to-date with the original repository, you can fetch and merge changes from
the upstream remote:

```sh
git fetch upstream
git merge upstream/main
```

Then create a Pull Request back to the [main repository](https://github.com/hhursev/recipe-scrapers)
from your fork.


If you have troubles check out [Submitting A  Pull Request Section](#submitting-a-pull-request).


## Submitting a Pull Request

1. Navigate to your fork on GitHub.
2. Click the "New pull request" button.
3. Ensure the base fork is the original repository and the base branch is `main`.
4. Fill out the pull request template and submit.


## Thank you for contributing!

### What happens after a PR

When you submit your PR:

1. Our CI suite will run against your code to ensure everything works as expected. You can run the
2. tests locally before submitting:
```sh
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
    - Tackle any follow-up improvements in subsequent PRs

Don't worry if your first PR needs some adjustments - this is normal and part of the collaborative
development process!
