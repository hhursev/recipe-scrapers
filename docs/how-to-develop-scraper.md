# How To: Develop a New Scraper

## 1. Find a website

If you have found a website you want to scrape the recipes from, first of all check to see if the website is already supported.

The project [README](https://github.com/hhursev/recipe-scrapers/blob/main/README.rst) has a list of the hundreds of websites already supported.

You can also check from within Python:

```python
>>> from recipe_scrapers import SCRAPERS
```

`SCRAPERS` is a dict where the keys are the hostnames of the supported websites and the values are the scraper classes for each supported website.

```python
>>> from recipe_scrapers import SCRAPERS
>>> SCRAPERS.get("bbcgoodfood.com")
recipe_scrapers.bbcgoodfood.BBCGoodFood
```

It's a good idea to file an [issue](https://github.com/hhursev/recipe-scrapers/issues/new/choose) on GitHub to track support for the website, and to indicate whether you are working on it.

## 2. Fork the recipe-scrapers repository and clone

If this is your first time contributing to this repository then you will need to create a fork of the repository and clone it to your computer.

To create a fork, click the Fork button near the top of page on the project GitHub page. This will create a copy of the repository under your GitHub user.

You can then clone the fork to your computer and set it up for development.

**Clone the repository**, replacing \<username> with your username

```shell
$ git clone git@github.com:<username>/recipe-scrapers.git
$ cd recipe-scrapers
```

**Create a virtual environment, activate and install dependencies**
```shell
$ python -m venv .venv --upgrade-deps
$ source .venv/bin/activate
$ pip install -r requirements-dev.txt
$ pip install pre-commit
$ pre-commit install
```

**Check that everything is working by running the tests**
```shell
$ python -m unittest
```
This will run all the tests for all the scrapers. You should not see any errors or failures.

## 3. Identify a recipe and generate the scraper and test file

To develop the scraper for the website, first identify a recipe. This will be used to create the test case that will validate that the scraper is working correctly.

> [!NOTE]
> Try to pick a recipe that involves more than one instruction, if you can.  The test suite considers single-instruction recipes to indicate possible human error.  If you need to, though, you can [indicate that that's expected](https://github.com/hhursev/recipe-scrapers/blob/98ead6fc6e9653805b01539a3f46fbfb4e096136/tests/test_allrecipes.py#L147-L150).

Next, find out if the website supports [Recipe Schema](https://schema.org/Recipe). If the website does support Recipe Schema, this will make creating the scraper straightforward. If not, supporting the site will be more complex but still possible.

```python
>>> from recipe_scrapers import scrape_me
>>> scraper = scrape_me(URL, wild_mode=True)
>>> scraper.schema.data
{'@context': 'https://schema.org',
 '@type': 'Recipe',
 ...
}
```

If Recipe Schema is available, then `scraper.schema.data` will return a dict containing information about the recipe.

If Recipe Schema is not available, then `scraper.schema.data` will return an empty dict.

Next, generate the scraper class and test files by running this command:

```shell
$ python generate.py <ClassName> <URL>
```

This will generate a file for the scraper with name \<ClassName> with basic code that you will need to modify. This will also download the recipe at \<URL> and create a test case.

You can find the generated scraper class in the `recipe_scrapers/` directory in a file the same as \<ClassName> but all lower case. The generated scraper class will look something like this:

```python
from ._abstract import AbstractScraper

class ScraperName(AbstractScraper):
    @classmethod
    def host(cls):
        return "websitehost.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
```

The generated scraper class will automatically be populated with functions that assume the Recipe Schema is available, regardless of whether it is or not.

## 4. Add functionality to the scraper

If the website supports Recipe Schema, then this is mostly done for you already. You can check if the output from each function is what you would expect from the recipe by using the scraper.

```python
>>> from recipe_scrapers import scrape_me
>>> scraper = scrape_me(URL)
>>> scraper.title()
"..."
>>> scraper.ingredients()
[
    "...",
    "..."
]
# etc.
```

Some additional functionality may be required in the scraper functions to make the output match the recipe on the website.

An in-depth guide on all the functions a scraper can support and what their output should be can be found [here](in-depth-guide-scraper-functions.md). The automatically generated scraper does not include all of these functions be default, so you may wish to add some of the additional functions listed if the website can support them.

If the website does not support Recipe Schema, or the schema does not include all of the recipe information, then you can scrape the information out of the website HTML. Each scraper has a `bs4.BeautifulSoup` object made available in `self.soup` which contains the parsed HTML. This can be used to extract the recipe information needed.

An example of a scraper that uses this approach is [Przepisy](https://github.com/hhursev/recipe-scrapers/blob/main/recipe_scrapers/przepisy.py).

The [BeautifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html) is a good resource for getting started with extracting information from HTML. An guide of common patterns and best practice used in this library can be found [here](in-depth-guide-html-scraping).

Some helper functions are available in the `_utils.py` file. These are functions that are commonly needed when extracting information from HTML, such as `normalize_string()`.

## 5. Create the test

A test case was automatically created when the scraper class was created. It can be found in the `tests/` directory with the name `test_lowercaseclassname.py`. The HTML from the URL used to generate the scraper is also downloaded to the `tests/test_data/` directory.

The generated test case will look something like this:

```python
from recipe_scrapers.newscraperclass import NewScraperClass
from tests import ScraperTest

class TestNewScraperScraper(ScraperTest):

    scraper_class = NewScraperClass

    def test_host(self):
        self.assertEqual("websitehost.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual(None, self.harvester_class.author())

    def test_title(self):
        self.assertEqual(None, self.harvester_class.title())

    def test_category(self):
        self.assertEqual(None, self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(None, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual(None, self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(None, self.harvester_class.image())

    def test_ingredients(self):
        self.assertEqual(None, self.harvester_class.ingredients())

    def test_instructions(self):
        self.assertEqual(None, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(None, self.harvester_class.description())
```

You will need to modify each of these functions to replace `None` with the correct output from the scraper for the recipe in the URL you used to generate the test. You should not do any processing of the scraper output in the test case, this would belong in the scraper itself.

This test case should only have tests for the functions that the scraper implements. You may need to add or remove tests depending on the implementation of the scraper.

You can check whether your scraper is passing the tests by running

```shell
$ python -m unittest tests.test_myscraper
```

> [!NOTE]
> It is also recommended that you manually test the scraper with a couple of different recipes from the website, to check that there aren't any special cases the scraper will need to handle. You don't need to create test cases for each of these.

## 6. Open a pull request

Once you have finished developing the scraper and test case, you can commit the files to git and push them to GitHub. You should also update the README.rst to list the site, alphabetically, under the [Scrapers available for:](https://github.com/hhursev/recipe-scrapers#scrapers-available-for) header.

After you have pushed the changes to GitHub, you can open a pull request in the [recipe-scrapers project](https://github.com/hhursev/recipe-scrapers/pulls). Your changes will undergo some automatic tests (no different to running the all the tests in the project, but this time on all supported platforms and using all supported Python versions) and be reviewed by other project contributors.
