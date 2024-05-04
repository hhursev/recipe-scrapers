import json
import pathlib

from recipe_scrapers import scrape_html
from recipe_scrapers._grouping_utils import IngredientGroup

MANDATORY_TESTS = [
    "author",
    "canonical_url",
    "host",
    "description",
    "image",
    "ingredients",
    "ingredient_groups",
    "instructions",
    "instructions_list",
    "language",
    "site_name",
    "title",
    "total_time",
    "yields",
]

OPTIONAL_TESTS = [
    "category",
    "cook_time",
    "cuisine",
    "nutrients",
    "prep_time",
    "cooking_method",
    "ratings",
    "reviews",
    "equipment",
]


def load_test(host: str, testhtml: pathlib.Path, testjson: pathlib.Path):
    with open(testjson, encoding="utf-8") as f:
        expect = json.load(f)
        expect["ingredient_groups"] = [
            IngredientGroup(**group) for group in expect.get("ingredient_groups", [])
        ]
    actual = scrape_html(testhtml.read_text(encoding="utf-8"), host)
    return expect, actual


def run_mandatory_tests(self, expect, actual, tests=MANDATORY_TESTS):
    # Mandatory tests
    # If the key isn't present, check an assertion is raised
    for key in tests:
        with self.subTest(key):
            scraper_func = getattr(actual, key)
            if key in expect.keys():
                self.assertEqual(
                    expect[key],
                    scraper_func(),
                    msg=f"The actual value for .{key}() did not match the expected value.",
                )
            else:
                with self.assertRaises(
                    Exception,
                    msg=f".{key}() was expected to raise an exception but it did not.",
                ):
                    scraper_func()


def run_optional_test(self, expect, actual, tests=OPTIONAL_TESTS):
    # Optional tests
    # If the key isn't present, skip
    for key in tests:
        with self.subTest(key):
            scraper_func = getattr(actual, key)
            if key in expect.keys():
                self.assertEqual(
                    expect[key],
                    scraper_func(),
                    msg=f"The actual value for .{key}() did not match the expected value.",
                )
