# Recipe Scrapers

Welcome to Recipe Scrapers - a Python package that makes extracting recipes from websites a piece of cake! 🍰

This documentation is in **early** development and actively being improved. For now, please refer to the repository's [README](https://github.com/hhursev/recipe-scrapers/blob/main/README.rst).


[We support the following sites](supported-sites.md)

[Contributing to Our Documentation](contributing-to-our-documentation.md)


----


## Goal

This library has the goals of

* making recipe information **accessible**,
* ensuring the author is **attributed** correctly,
* representing the recipes **accurately** and **authentically**

Sometimes it is simple and straightforward to achieve all these goals, and sometimes it is more difficult (which is why this library exists). Where some interpretation or creativity is required to scrape a recipe, we should always keep those goals in mind. Occasionally, that might mean that we can't support a particular website.

## Contents:

- [Contributing to Our Documentation](contributing-to-our-documentation.md)
* [How To: Develop a New Scraper](contributing.md)
* In Depth Guides:
    * [HTML Scraping](in-depth-guide-html-scraping.md)
    * [Ingredient Groups](in-depth-guide-ingredient-groups.md)
    * [Scraper Functions](in-depth-guide-scraper-functions.md)
    * [Debugging](in-depth-guide-debugging.md) (coming soon)


## What is Recipe Scrapers?

Recipe Scrapers is a Python library that simplifies the process of extracting structured recipe data from cooking and recipe websites. It handles the complexities of web scraping while providing you with clean, structured recipe data.

```python
from urllib.request import urlopen

from recipe_scrapers import scrape_html

url = "https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/"
html = urlopen(url).read().decode("utf-8")  # retrieves the recipe webpage HTML
scraper = scrape_html(html, org_url=url)
scraper.title()
scraper.instructions()  # etc.
# for a complete list of methods:
# help(scraper)
```
