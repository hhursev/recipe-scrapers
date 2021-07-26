import unittest

from recipe_scrapers import (
    NoSchemaFoundInWildMode,
    WebsiteNotImplementedError,
    scrape_me,
)


class TestExceptions(unittest.TestCase):
    def test_WebsiteNotImplementedError(self):
        with self.assertRaises(WebsiteNotImplementedError):
            scrape_me("https://example.com/recipe")

    def test_NoSchemaFoundInWildMode(self):
        exception = NoSchemaFoundInWildMode("example.com")

        self.assertEquals(exception.url, "example.com")
        self.assertEquals(exception.message, "No Recipe Schema found at example.com.")
