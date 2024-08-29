import unittest

from recipe_scrapers import (
    AbstractScraper,
    NoSchemaFoundInWildMode,
    RecipeSchemaNotFound,
    WebsiteNotImplementedError,
    scrape_html,
)


class TestExceptions(unittest.TestCase):
    def test_website_not_implemented_error(self):
        with self.assertRaises(WebsiteNotImplementedError):
            scrape_html(html="<html></html>", org_url="http://example.com/recipe")

    def test_no_schema_found_in_wild_mode_error(self):
        exception = NoSchemaFoundInWildMode("example.com")

        self.assertEqual(exception.url, "example.com")
        self.assertEqual(exception.message, "No Recipe Schema found at example.com.")

    def test_no_schema_found_for_fill_plugin(self):
        class TestScraper(AbstractScraper):
            @classmethod
            def host(cls):
                return "example.com"

        scraper = TestScraper(html="<html></html>", url="http://example.com/recipe")
        with self.assertRaises(RecipeSchemaNotFound):
            scraper.category()
