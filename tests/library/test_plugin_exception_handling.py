import logging
import unittest
from unittest import mock

from recipe_scrapers import scrape_html
from recipe_scrapers._exceptions import SchemaOrgException

HTML = """
<html><head><script type="application/ld+json">
{"@context": "https://schema.org", "@type": "Recipe", "name": "Soup",
 "recipeIngredient": ["water"]}
</script></head></html>
"""


class TestExceptionHandlingPlugin(unittest.TestCase):
    def setUp(self):
        self.scraper = scrape_html(
            HTML, org_url="https://example.com/soup", supported_only=False
        )

    def _suppressing(self, return_values=None):
        settings = mock.patch(
            "recipe_scrapers.plugins.exception_handling.settings"
        ).start()
        self.addCleanup(mock.patch.stopall)
        settings.SUPPRESS_EXCEPTIONS = True
        settings.LOG_LEVEL = logging.CRITICAL
        settings.ON_EXCEPTION_RETURN_VALUES = return_values or {}

    def test_missing_fields_raise_by_default(self):
        with self.assertRaises(SchemaOrgException):
            self.scraper.cuisine()

    def test_every_schema_field_is_silenced(self):
        self._suppressing()
        for method in (
            "cooking_method",
            "cook_time",
            "cuisine",
            "description",
            "dietary_restrictions",
            "keywords",
            "prep_time",
            "ratings_count",
            "site_name",
        ):
            with self.subTest(method=method):
                self.assertIsNone(getattr(self.scraper, method)())

    def test_configured_return_value_is_used(self):
        self._suppressing({"cuisine": "unknown"})

        self.assertEqual("unknown", self.scraper.cuisine())
