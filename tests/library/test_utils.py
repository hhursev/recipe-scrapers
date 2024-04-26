import unittest

from recipe_scrapers._utils import (
    _extract_fractional,
    get_minutes,
    get_url_slug,
    url_path_to_dict,
)


class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.iso8601_fixtures = {
            "PT1H": 60,
            "PT20M": 20,
            "PT2H10M": 130,
            "PT0H9M30S": 10,
        }
        cls.minutes_fixtures = [
            ("1 hour 15 mins", 75),
            ("1h and 15mins", 75),
            ("3h10m", 190),
            ("PT2H30M", 150),
            ("P0DT1H10M", 70),
            ("90", 90),
            ("1.5 hours", 90),
            ("2 days", 2880),
            ("1½ hours", 90),
            ("1¾ hours", 105),
            ("1¼ hours", 75),
            ("1⅔ hours", 100),
            ("1 1/2 hours", 90),
            ("1 3/4 hours", 105),
            ("1 1/4 hours", 75),
            ("1 2/3 hours", 100),
            ("15 - 20 minutes", 20),
            ("15 to 20 minutes", 20),
            ("Pá-Pum", None),
            ("PT0M", None),
        ]

    def test_minutes_fixtures(self):
        # Tests for minute related output formats.
        for text, expected in self.minutes_fixtures:
            with self.subTest(text=text):
                self.assertEqual(expected, get_minutes(text))

    def test_iso8601_fixtures(self):
        # Tests for ISO 8601 formatted outputs formats.
        for text, expected in self.iso8601_fixtures.items():
            with self.subTest(text=text):
                self.assertEqual(expected, get_minutes(text))

    def test_split_fractions(self):
        input_string = "3 1 / 2"
        expected_result = 3.5
        self.assertEqual(expected_result, _extract_fractional(input_string))

    def test_url_path_to_dict(self):
        input_path = (
            "https://recipes:scraper@www.example.com:8080/path/to/resource?key=value"
        )
        expected_result = {
            "schema": "https",
            "user": "recipes",
            "password": "scraper",
            "host": "www.example.com",
            "port": "8080",
            "path": "/path/to/resource",
            "query": "?key=value",
        }
        self.assertEqual(expected_result, url_path_to_dict(input_path))

    def test_list_public_methods(self):
        from recipe_scrapers import AbstractScraper

        expected_methods = [
            "author",
            "canonical_url",
            "category",
            "cook_time",
            "cooking_method",
            "cuisine",
            "description",
            "equipment",
            "host",
            "image",
            "ingredient_groups",
            "ingredients",
            "instructions",
            "instructions_list",
            "language",
            "nutrients",
            "prep_time",
            "ratings",
            "ratings_count",
            "reviews",
            "site_name",
            "title",
            "total_time",
            "yields",
        ]
        public_methods = [
            method
            for method in dir(AbstractScraper)
            if callable(getattr(AbstractScraper, method))
            and not method.startswith("_")
            and method not in ["soup", "links", "to_json"]
        ]
        self.assertEqual((expected_methods), (public_methods))

    def test_get_url_slug(self):
        input_url = "https://example.com/first/second/last"
        url_slug = get_url_slug(input_url)
        self.assertEqual("last", url_slug)
