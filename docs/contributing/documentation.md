# Contributing to Documentation

!!! note "Prerequisites"
    This guide assumes you are already familiar with our [setup guide](./setup.md).

Create a new branch for your documentation changes:
```sh
git checkout -b docs/your-feature-name
```

## Previewing Documentation Changes

!!! example "Local Development"
    1. From the project root directory, start the MkDocs development server:
```sh
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
```sh
   git add docs/
   git commit -m "docs: describe your changes here"
```

2. Push your changes to your fork:
```sh
   git push origin docs/your-feature-name
```

3. Create a Pull Request (PR) from your fork to the main
[recipe-scrapers](https://github.com/hhursev/recipe-scrapers) repository.

!!! success "PR Preview"
    When you create a PR, a special preview URL will be generated where your documentation
    changes can be reviewed. This will make it easy for maintainers to see your changes in action.

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
