# Contributing to Our Documentation

We're excited to have you help improve our documentation! Here's a step-by-step guide to get you started.


### Setting Up Your Local Environment
First, let's set up your development environment:

```bash
git clone git@github.com:hhursev/recipe-scrapers.git &&
cd recipe-scrapers &&
python -m venv .venv &&
source .venv/bin/activate &&
python -m pip install --upgrade pip &&
pip install -e ".[docs]"
```

### Viewing the Documentation Locally

Start the documentation server with:

```
mkdocs serve
```

You can now view the documentation at http://localhost:8000/.
The server will automatically refresh when you make changes.


### Making Your Contributions

1. Navigate to the `docs/` directory where all documentation files are stored
2. Make your desired changes to the documentation files
3. If needed, update the navigation structure in mkdocs.yml (particularly the nav section)
4. Preview your changes in real-time through the local server
5. Once you're satisfied with your updates, create a pull request

We appreciate your contributions to making our documentation better!
If you have any questions during this process, please don't hesitate to reach out.
