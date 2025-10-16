# Code Contributions

!!! note "Prerequisites"
    This guide assumes you are already familiar with our [setup guide](./setup.md).

## Development Workflow

Create a new branch for your code changes:

```sh
git checkout -b fix/your-fix-name     # for bug fixes
# or
git checkout -b site/website-name     # for new site scrapers
# or
git checkout -b feature/feature-name  # for new features
```

After making your changes commit them:

```bash
git add -p  # Review changes before adding them
git commit -m "meaningful commit message"
git push origin your-branch-name
```

Then create a Pull Request back to the [main repository](https://github.com/hhursev/recipe-scrapers) from your fork.


## Development Guidelines

While we're working on comprehensive documentation, the codebase is designed to
be self-explanatory. As a developer, you can understand our patterns and expectations
by taking a look at existing scrapers in the `recipe_scrapers/` directory.


## Hints

!!! tip "Generator Tool"
    If you're adding a new site scraper, you can use our generator command to create a template:

```sh
    python generate.py <ClassName> <URL>
```

    Where:

    - `ClassName`: The name of your new scraper class (e.g., `BBCGoodFood`)
    - `URL`: A sample recipe URL from the target site. This will be saved in `test_data/`
    for testing.


## Examples

!!! warning "Work in Progress"

    This contributing guide is currently being developed. Meanwhile, you can check these
    PRs as examples of good contribution standards:

    - [#1414](https://github.com/hhursev/recipe-scrapers/pull/1414/) - Adding a new site scraper
    - [#1432](https://github.com/hhursev/recipe-scrapers/pull/1432/) - Fixing broken functionality
    - [#1434](https://github.com/hhursev/recipe-scrapers/pull/1434/) - Test improvements
    - [#1345](https://github.com/hhursev/recipe-scrapers/pull/1345/) - CI Improvements
