# Examples

!!! important
    `recipe-scrapers` is designed to focus **exclusively on HTML parsing**.

    This core principle guides our development and support. You'll need to implement your own solution
    for fetching recipe HTML files and managing network requests. The library works best when you
    provide both the HTML content and its source domain.


## Basic Usage

Here's a simple example of how to use the library:

```python title="Basic Usage Example" linenums="1"
from urllib.request import urlopen
from recipe_scrapers import scrape_html

url = "https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/"
html = urlopen(url).read().decode("utf-8")  # retrieves the recipe webpage HTML
scraper = scrape_html(html, org_url=url)

# Extract recipe information
scraper.title()
scraper.instructions()
scraper.links()
scraper.to_json()
scraper.nutrients()

# To see all available methods
help(scraper)
```

For optimal results, always provide both the HTML content and its original URL.
This helps the library correctly parse website-specific elements.

## Available Methods

Recipe websites vary in the amount of information they provide. While some offer
comprehensive details like nutritional information (`.nutrients()`), others may
not.

### Core Methods

These methods should be available for all supported websites:

!!! warning "Under Construction"
    This documentation section is currently being updated and improved.

::: tests.MANDATORY_TESTS
    options:
        heading_level: 4


### Optional Methods

These additional methods are available for some websites:

!!! warning "Under Construction"
    This documentation section is currently being updated and improved.

::: tests.OPTIONAL_TESTS
    options:
      heading_level: 4


## Common Patterns

!!! warning "Under Construction"
    This documentation section is currently being updated and improved.
