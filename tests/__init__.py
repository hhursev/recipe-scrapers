import json
import pathlib
import unittest
from typing import Callable

from recipe_scrapers import SCRAPERS, scrape_html
from recipe_scrapers._exceptions import StaticValueException
from recipe_scrapers._grouping_utils import IngredientGroup

MANDATORY_TESTS = [
    "author",
    "canonical_url",
    "host",
    "image",
    "ingredients",
    "instructions_list",
    "language",
    "site_name",
    "title",
    "total_time",
    "yields",
]

OPTIONAL_TESTS = [
    "ingredient_groups",
    "instructions",
    "category",
    "description",
    "cook_time",
    "cuisine",
    "nutrients",
    "prep_time",
    "cooking_method",
    "keywords",
    "ratings",
    "reviews",
    "equipment",
    "ratings_count",
    "dietary_restrictions",
]


class RecipeTestCase(unittest.TestCase):
    maxDiff = None
    been_wild = False


def test_func_factory(
    host: str, testhtml: pathlib.Path, testjson: pathlib.Path
) -> Callable:
    """
    Factory function to create a test function that asserts the actual output from
    the scraper matches the expected output.

    Parameters
    ----------
    host : str
        Host of the site, used to identify the correct scraper to use*
    testhtml : pathlib.Path
        Path to testhtml file that the scraper will parse..
    testjson : pathlib.Path
        Path to testjson file that contains the expected output from the scraper
        for the testhtml file.


    * We can't use the canonical url from the expected output to determine the scraper
    that should be used because some website that aggregate recipes from others site will
    set the canonical url to the site the recipe came from. tastykitchen.com is an example
    of this.


    Returns
    -------
    Callable
        Function that asserts the expected output from the scraper matches the
        actual output.
    """

    def test_func(self):
        with open(testjson, encoding="utf-8") as f:
            expect = json.load(f)
            expect["ingredient_groups"] = (
                [
                    IngredientGroup(**group)
                    for group in expect.get("ingredient_groups", [])
                ]
                if "ingredient_groups" in expect
                else [IngredientGroup(expect["ingredients"], purpose=None)]
            )
        supported_only = host in SCRAPERS
        actual = scrape_html(
            html=testhtml.read_text(encoding="utf-8"),
            org_url=host,
            online=False,
            supported_only=supported_only,
        )
        if not supported_only:
            self.assertFalse(self.been_wild, "Only one wild mode test should occur.")
            type(self).been_wild = True

        # Mandatory tests
        # If the key isn't present, check an assertion is raised
        for key in MANDATORY_TESTS:
            with self.subTest(key):
                scraper_func = getattr(actual, key)
                if key in expect.keys():
                    try:
                        return_value = scraper_func()
                    except StaticValueException as e:
                        return_value = e.return_value

                    self.assertEqual(
                        expect[key],
                        return_value,
                        msg=f"The actual value for .{key}() did not match the expected value.",
                    )
                else:
                    with self.assertRaises(
                        Exception,
                        msg=f".{key}() was expected to raise an exception but it did not.",
                    ):
                        scraper_func()

        # Optional tests
        for key in OPTIONAL_TESTS:
            if key not in expect:
                continue  # If the key isn't present, skip
            with self.subTest(key):
                scraper_func = getattr(actual, key)
                try:
                    return_value = scraper_func()
                except StaticValueException as e:
                    return_value = e.return_value

                self.assertEqual(
                    expect[key],
                    return_value,
                    msg=f"The actual value for .{key}() did not match the expected value.",
                )

        grouped = []
        for group in actual.ingredient_groups():
            grouped.extend(group.ingredients)

        with self.subTest("ingredient_groups"):
            self.assertEqual(sorted(actual.ingredients()), sorted(grouped))

        if "instructions_list" in expect:
            list_instructions_normalized = [
                line.strip() for line in expect["instructions_list"] if line.strip()
            ]

            string_instructions_normalized = [
                instruction.strip()
                for instruction in actual.instructions().split("\n")
                if instruction.strip()
            ]

            with self.subTest("instructions_list vs instructions comparison"):
                self.assertEqual(
                    string_instructions_normalized,
                    list_instructions_normalized,
                    msg="The actual value for .instructions() did not match the value from instructions_list.",
                )

    return test_func


def load_tests(
    loader: unittest.TestLoader, standard_tests: unittest.TestSuite, pattern: str
) -> unittest.TestSuite:
    """
    Customise the loading of tests. This function is automatically picked up by the
    unittest test loader.

    This function dynamically generates the class definition for RecipeTestCase by adding
    a test function for each pair of testhtml and testjson files found in the
    tests/test_data directory.

    This also includes the library tests from the tests/library folder as well.


    Parameters
    ----------
    loader : unittest.TestLoader
        The instance of TestLoader loading the tests when unittest is run
    standard_tests : unittest.TestSuite
        The tests found by loader by loading the tests from the tests module.
        This is empty and unused.
    pattern : str
        Pattern used to identify tests to load.
        This is unused.

    Returns
    -------
    unittest.TestSuite
        A TestSuite object populated with tests from the pairs of testhtml and testjson
        files, and the library tests.
    """
    test_dir = pathlib.Path("tests/test_data")
    for host in test_dir.iterdir():
        if not host.is_dir():
            continue

        for testhtml in host.glob("*.testhtml"):
            testjson = testhtml.with_suffix(".json")
            if not testjson.is_file():
                continue

            # Add a new function to RecipeTestCase class to test this scraper
            # The name of this function the path to the testjson file.
            setattr(
                RecipeTestCase,
                str(testjson),
                test_func_factory(host.name, testhtml, testjson),
            )

    # Create a test suite and load all tests from the RecipeTestClass definition
    suite = unittest.TestSuite()
    tests = loader.loadTestsFromTestCase(RecipeTestCase)
    suite.addTest(tests)

    # Add library tests to test suite
    library_tests = loader.discover("tests/library")
    suite.addTests(library_tests)

    return suite
