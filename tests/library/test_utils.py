import unittest

from recipe_scrapers._utils import (
    _extract_fractional,
    format_diet_name,
    get_abstract_methods,
    get_minutes,
    get_nutrition_keys,
    get_url_slug,
    get_yields,
    url_path_to_dict,
)


class TestUtils(unittest.TestCase):
    iso8601_fixtures = {
        "PT1H": 60,
        "PT20M": 20,
        "PT2H10M": 130,
        "PT0H9M30S": 10,
    }
    minutes_fixtures = [
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
            "dietary_restrictions",
            "equipment",
            "host",
            "image",
            "ingredient_groups",
            "ingredients",
            "instructions",
            "instructions_list",
            "keywords",
            "language",
            "nutrients",
            "prep_time",
            "ratings",
            "ratings_count",
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

    def test_get_abstract_methods(self):
        abstract_methods = get_abstract_methods()
        expected_methods = [
            "author",
            "canonical_url",
            "site_name",
            "host",
            "language",
            "title",
            "ingredients",
            "ingredient_groups",
            "instructions",
            "instructions_list",
            "category",
            "yields",
            "description",
            "total_time",
            "cook_time",
            "prep_time",
            "cuisine",
            "cooking_method",
            "ratings",
            "ratings_count",
            "equipment",
            "nutrients",
            "dietary_restrictions",
            "image",
            "keywords",
        ]
        self.assertEqual((expected_methods), (abstract_methods))

    def test_get_nutrition_keys(self):
        nutrition_keys = get_nutrition_keys()
        expected_order = [
            "servingSize",
            "calories",
            "fatContent",
            "saturatedFatContent",
            "unsaturatedFatContent",
            "transFatContent",
            "carbohydrateContent",
            "sugarContent",
            "proteinContent",
            "sodiumContent",
            "fiberContent",
            "cholesterolContent",
        ]
        self.assertEqual((expected_order), (nutrition_keys))

    def test_get_yields(self):
        self.assertEqual("5 servings", get_yields("5"))

    def test_get_yields_empty_string(self):
        with self.assertRaises(ValueError):
            get_yields("")

    def test_get_yields_leading_zeros(self):
        test_cases = [
            ("02 servings", "2 servings"),
            ("02 dozen", "2 dozen"),
            ("02 items", "2 items"),
        ]
        for input_text, expected in test_cases:
            with self.subTest(input_text=input_text):
                self.assertEqual(expected, get_yields(input_text))

    def test_format_diet_name_from_restricted_diet_url(self):
        self.assertEqual("Vegan Diet", format_diet_name("https://schema.org/VeganDiet"))
        self.assertEqual(
            "Low Fat Diet", format_diet_name("http://schema.org/LowFatDiet")
        )

    def test_format_diet_name_from_restricted_diet_label(self):
        self.assertEqual("Vegetarian Diet", format_diet_name("VegetarianDiet"))
        self.assertEqual("Gluten Free Diet", format_diet_name("GlutenFreeDiet"))

    def test_format_diet_name_from_diet_object(self):
        mediterranean = {
            "@type": "Diet",
            "name": "Mediterranean",
        }
        vegan = {
            "@type": "Diet",
            "name": "Vegan",
        }

        self.assertEqual("Mediterranean", format_diet_name(mediterranean))
        self.assertEqual("Vegan", format_diet_name(vegan))

    def test_format_diet_name_from_diet_object_with_restricted_diet_name(self):
        diet = {"@type": "Diet", "name": "https://schema.org/VeganDiet"}
        self.assertEqual("Vegan Diet", format_diet_name(diet))

    def test_format_diet_name_returns_none_when_unusable(self):
        self.assertIsNone(format_diet_name({"@type": "Diet"}))
        self.assertIsNone(format_diet_name(None))
        self.assertIsNone(format_diet_name(42))
        self.assertIsNone(format_diet_name("https://schema.org/"))

    def test_get_yields_metric_weight_abbreviations(self):
        test_cases = [
            ("750g", "750 grams"),
            ("750 g di crema pasticcera", "750 grams"),
            ("1 kg dough", "1 kilogram"),
            ("2kg dough", "2 kilograms"),
        ]
        for input_text, expected in test_cases:
            with self.subTest(input_text=input_text):
                self.assertEqual(expected, get_yields(input_text))
