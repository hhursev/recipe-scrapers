# How To: Developer a New Scraper

## 1. Find the website and check if it supports recipe schema

Easiest way to check is to use `wild_mode=True`

If the site supports Recipe Schema, this will make things easier.

## 2: Identify a recipe and generate the scraper and test file

```python
>>> python generate.py <name> <url>
```

This will generate a file for the scraper with basic code that you will need to modify.

This will also download the recipe at the URL and create a test case (which we'll complete later)

## 3: Add the functionality to the scraper

If the website supports Recipe Schema, then this is mostly done for you.

If the website supports Recipe Schema, but not all fields then we will have to do some scraping of the html.

+more detail

## 4: Create the test

In the test file replace `None` with the result from scraping the recipe.

Don't do any processing in the test file.
