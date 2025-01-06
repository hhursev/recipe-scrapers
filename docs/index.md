# Recipe Scrapers

[![Github](https://img.shields.io/github/stars/hhursev/recipe-scrapers?style=social)](https://github.com/hhursev/recipe-scrapers/)
[![Version](https://img.shields.io/pypi/v/recipe-scrapers.svg)](https://pypi.org/project/recipe-scrapers/)
[![Python Version](https://img.shields.io/pypi/pyversions/recipe-scrapers)](https://pypi.org/project/recipe-scrapers/)
[![Downloads](https://pepy.tech/badge/recipe-scrapers)](https://pepy.tech/project/recipe-scrapers)
[![GitHub Actions Unittests](https://github.com/hhursev/recipe-scrapers/workflows/unittests/badge.svg?branch=main)](https://github.com/hhursev/recipe-scrapers/actions/)
[![Coveralls](https://coveralls.io/repos/hhursev/recipe-scraper/badge.svg?branch=main&service=github)](https://coveralls.io/github/hhursev/recipe-scraper?branch=main)
[![License](https://img.shields.io/github/license/hhursev/recipe-scrapers)](https://github.com/hhursev/recipe-scrapers/blob/main/LICENSE)

---

`recipe-scrapers` is a Python package designed to extract recipe data from HTM content of
cooking websites. It parses the HTML structure of recipe pages to provide a simple and consistent
API for retrieving structured data like ingredients, instructions, cooking time, and more.
Works with the python versions listed above.

## Installation

You can install `recipe-scrapers` using pip or your preferred Python package manager:

!!! tip "Install"
    ``` console
    pip install recipe-scrapers
    ```

!!! note

    This should produce output about the installation process, with the final line reading:
    `Successfully installed recipe-scrapers-<version-number>`.


## Overview

```python exec="on"
import sys
sys.path.insert(0, ".")
from recipe_scrapers import SCRAPERS

print(f"There are **{len(SCRAPERS.keys())}** cooking websites currently supported.")
```

For a full list check our [Supported Sites](./getting-started/supported-sites.md) section.

With `recipe-scrapers`, you should easily extract structured recipe data such as:

- title
- ingredients
- instructions
- cooking and preparation times
- yields
- image
- and many more...

Check out our [Examples](./getting-started/examples.md) section to see how to get started with the library.

## Core Functionality

`recipe-scrapers` long term aim is to focus **solely on HTML parsing** and not to handle
networking operations. This design choice provides flexibility in how you retrieve HTML content
and allows you to:

- Implement your own networking logic
- Handle rate limiting
- Manage caching
- Control error handling
- Use your preferred HTTP client


## Getting Started

👋 We suspect you've missed a few key links, such as us mentioning the [Examples](./getting-started/examples.md) and
the [Supported Sites](./getting-started/supported-sites.md) section.

Thus, we drop this tiny Python snippet for you (using Python's built-in `urllib`) to showcase how
you can use this package:

```python
from urllib.request import urlopen

from recipe_scrapers import scrape_html

url = "https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/"
html = urlopen(url).read().decode("utf-8")  # retrieves the recipe webpage HTML
scraper = scrape_html(html, org_url=url)
scraper.title()
scraper.instructions()
scraper.to_json()
# for a complete list of methods:
# help(scraper)
```

## Why recipe-scrapers Exists

Born from late-night coding sessions and a love for both food and programming, `recipe-scrapers`
evolved from a personal project into a community tool. It's open-sourced and under
the [MIT license](https://github.com/hhursev/recipe-scrapers/blob/main/LICENSE)
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

!!! tip "Happy cooking with code!"
    While building awesome stuff, remember to be mindful of websites' terms and fair usage -
    our [Copyright and Usage Guidelines](copyright-and-usage.md) will help you stay on track.
