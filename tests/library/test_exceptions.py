import unittest

from recipe_scrapers import NoSchemaFoundInWildMode


class TestExceptions(unittest.TestCase):
    def test_no_schema_found_in_wild_mode_error(self):
        exception = NoSchemaFoundInWildMode("example.com")

        self.assertEqual(exception.url, "example.com")
        self.assertEqual(exception.message, "No Recipe Schema found at example.com.")
