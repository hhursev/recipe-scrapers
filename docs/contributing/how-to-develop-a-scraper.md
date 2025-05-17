# How To Develop a New Scraper

!!! warning "Under Construction"
    This section is being updated. Some information may be outdated or inaccurate.


## Find a website

First, check if the website is already supported:

- Check the [Supported Sites](../getting-started/supported-sites.md)
- Or verify programmatically:

```python
from recipe_scrapers import SCRAPERS
# Check if site is supported
print(SCRAPERS.get("bbcgoodfood.com"))
```

!!! note "Track Your Progress"
    Create an [issue](https://github.com/hhursev/recipe-scrapers/issues/new/choose) to track
    your work.

## Setup Repository

Fork the [recipe-scrapers repository](https://github.com/hhursev/recipe-scrapers) on GitHub and
follow these steps:

!!! tip "Quick Setup"
    ```sh
    # Clone your fork
    git clone https://github.com/YOUR-USERNAME/recipe-scrapers.git
    cd recipe-scrapers

    # Set up Python environment
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    python -m pip install --upgrade pip
    pip install -e ".[all]"
    ```

Create a new branch:

```sh
git checkout -b site/website-name
```

!!! tip "Run Tests"
    ```sh
    python -m unittest

    # Optional: Parallel testing
    pip install unittest-parallel
    unittest-parallel --level test
    ```

## Generate Scraper Files

### 1. Select Recipe URL

!!! tip "Recipe Selection"
    Choose a recipe with multiple instructions when possible. Single-instruction recipes may
    indicate parsing errors, unless [explicitly handled](https://github.com/hhursev/recipe-scrapers/blob/98ead6fc6e9653805b01539a3f46fbfb4e096136/tests/test_allrecipes.py#L147-L150).

### 2. Check Schema Support

Test if the site uses [Recipe Schema](https://schema.org/Recipe):

```python
from recipe_scrapers import scrape_html

scraper = scrape_html(html, url, wild_mode=True)
print(scraper.schema.data)  # Empty dict if schema not supported
```

### 3. Generate Files

```sh
python generate.py <ClassName> <URL>
```

This creates:

- Scraper file in `recipe_scrapers/`
- Test files in `tests/test_data/<host>/`

## Implementation

=== "With Recipe Schema"
    ```python
    from recipe_scrapers import scrape_html

    scraper = scrape_html(html, url)
    print(scraper.title())
    print(scraper.ingredients())
    ```

=== "Without Recipe Schema"
    ```python
    def title(self):
        return self.soup.find('h1').get_text()
    ```

!!! info "Resources"
    - [Scraper Functions Guide](in-depth-guide-scraper-functions.md)
    - [HTML Scraping Guide](in-depth-guide-html-scraping.md)
    - [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Testing

### 1. Update Test Data

Edit `tests/test_data/<host>/test.json`:
```json
{
    "host": "<host>",
    "canonical_url": "...",
    "site_name": "...",
    "author": "...",
    "language": "...",
    "title": "...",
    "ingredients": "...",
    "instructions_list": "...",
    "total_time": "...",
    "yields": "...",
    "image": "...",
    "description": "..."
}
```

### 2. Run Tests

```sh
python -m unittest -k <ClassName.lower()>
```

!!! warning "Edge Cases"
    Test with multiple recipes to catch potential edge cases.

## Submit Changes

1. Commit your work:
```sh
git add -p  # Review changes
git commit -m "Add scraper for example.com"
git push origin site/website-name
```

2. Create a pull request at [recipe-scrapers](https://github.com/hhursev/recipe-scrapers/pulls)
