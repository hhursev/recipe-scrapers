# Migrating from v14 to v15

!!! warning "Under Construction"
    This documentation section is currently being updated and improved.

## Overview

Version 15 introduces important changes to the core API of recipe-scrapers, particularly regarding
how recipes are scraped from websites. The main change is the deprecation of the `scrape_me`
function in favor of more explicit HTML parsing methods.

## Key Changes

### 1. Deprecation of `scrape_me`

The `scrape_me` function, which was the primary method for scraping recipes in v14, is being
deprecated. While it still works in v15, you'll receive deprecation warnings when using it:

```python
# Old v14 approach (deprecated)
from recipe_scrapers import scrape_me
scraper = scrape_me('https://example.com/recipe')  # Will show deprecation warning
```

### 2. New Recommended Approach

The new approach separates HTML fetching from parsing:

```python
# New v15 approach
from urllib.request import urlopen
from recipe_scrapers import scrape_html

# Fetch HTML (you can use any HTTP client)
url = "https://example.com/recipe"
html = urlopen(url).read().decode("utf-8")

# Parse HTML
scraper = scrape_html(html, org_url=url)
```

## Why This Change?

1. **Better Separation of Concerns**: The library now focuses solely on HTML parsing, letting
you handle HTTP requests as you see fit
2. **More Flexibility**: You can use your preferred HTTP client (requests, httpx, aiohttp, etc.)
3. **Better Error Handling**: Separate networking issues from parsing issues

## Migration Steps

1. Replace `scrape_me` imports:
   ```python
   # Before
   from recipe_scrapers import scrape_me

   # After
   from recipe_scrapers import scrape_html
   ```

2. Update scraping code:
   ```python
   # Before
   scraper = scrape_me('https://example.com/recipe')

   # After
   from urllib.request import urlopen

   url = 'https://example.com/recipe'
   html = urlopen(url).read().decode("utf-8")
   scraper = scrape_html(html, org_url=url)
   ```

3. If you're using a web framework or need to handle many requests, consider using a more
robust HTTP client:
   ```python
   # Example with requests
   import requests
   from recipe_scrapers import scrape_html

   def get_recipe(url):
       response = requests.get(url)
       response.raise_for_status()
       return scrape_html(response.text, org_url=url)
   ```

## Timeline

- v14.x.x: Still supported but will only receive critical bug fixes
- v15.x.x: Current stable version with new API
- Future versions: Will build upon the v15 API structure

## Getting Help

If you encounter issues during migration:

1. Check the [GitHub issues](https://github.com/hhursev/recipe-scrapers/issues) for similar problems
2. Open a new issue if you find a bug
3. Join the community discussions for migration-related questions
