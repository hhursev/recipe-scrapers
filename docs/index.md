# Recipe Scrapers

[![Github](https://img.shields.io/github/stars/hhursev/recipe-scrapers?style=social)](https://github.com/hhursev/recipe-scrapers/)
[![Version](https://img.shields.io/pypi/v/recipe-scrapers.svg)](https://pypi.org/project/recipe-scrapers/)
[![Python Version](https://img.shields.io/pypi/pyversions/recipe-scrapers)](https://pypi.org/project/recipe-scrapers/)
[![GitHub Actions Unittests](https://github.com/hhursev/recipe-scrapers/actions/workflows/unittests.yaml/badge.svg?branch=main)](https://github.com/hhursev/recipe-scrapers/actions/)
[![Coveralls](https://coveralls.io/repos/hhursev/recipe-scraper/badge.svg?branch=main&service=github)](https://coveralls.io/github/hhursev/recipe-scraper?branch=main)
[![License](https://img.shields.io/github/license/hhursev/recipe-scrapers)](https://github.com/hhursev/recipe-scrapers/blob/main/LICENSE)

---

`recipe-scrapers` is a [Python](https://www.python.org/) package for extracting recipe data from
cooking websites. It parses recipe information from standard
[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) structure, [Schema](https://schema.org/)
markup (including JSON-LD, Microdata, and RDFa formats), or [OpenGraph](https://ogp.me/) metadata.

The package provides a simple and consistent API for retrieving data such as ingredients, instructions,
cooking times, and more.

Compatible with the Python versions listed above. This package does not circumvent or bypass any
bot protection measures implemented by websites.


!!! tip "Install"
``` console
    pip install recipe-scrapers
```

```python exec="on"
import sys
sys.path.insert(0, ".")
from recipe_scrapers import SCRAPERS

print(f"There are **{len(SCRAPERS.keys())}** cooking websites currently supported.")
```

For a full list check our [Supported Sites](./getting-started/supported-sites.md) section.


## Getting Started

Parsing recipe information can be as simple as:

```python
from recipe_scrapers import scrape_me

scraper = scrape_me("https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/")
scraper.title()
scraper.instructions()
scraper.to_json()
# for a complete list of methods:
# help(scraper)
```

!!! warning
    `recipe-scrapers` is designed to focus **exclusively on HTML parsing**.

    This core principle guides our development and support. You'll need to implement your own solution
    for fetching recipe HTMLs and managing network requests. The library works best when you
    provide both the HTML content and its source domain.

    For more advanced implementations, we recommend using:

```python
    from recipe_scrapers import scrape_html
```

    Check out our [Examples](./getting-started/examples.md) section.


## Overview

With `recipe-scrapers`, you can easily extract structured recipe data such as:

- title
- ingredients
- instructions
- cooking and preparation times
- yields
- image
- and many more...

Check out our [Examples](./getting-started/examples.md) section to see how to get started with the library.


## Why recipe-scrapers Exists

Born from late-night coding sessions and a love for both food and programming, `recipe-scrapers`
evolved from a personal project into a community tool. It's opensource under the
[MIT license](https://github.com/hhursev/recipe-scrapers/blob/main/LICENSE)
with a simple goal: let developers focus on building amazing food-related applications without
reinventing the recipe-parsing wheel.

Today, our library helps power diverse projects across the cooking landscape:

- Meal prep and planning applications
- Smart shopping list generators
- Recipe collection managers
- Cooking time estimators
- Diet and nutrition trackers
- Food blogs and recipe aggregators

We're excited to see what you'll create! Feel free to share your project in our
[community showcase](https://github.com/hhursev/recipe-scrapers/issues/9) - we love seeing what others build with the library.


While building awesome stuff, remember to be mindful of websites' terms and fair use.
Our [Copyright and Usage](copyright-and-usage.md) will help you stay on track.
