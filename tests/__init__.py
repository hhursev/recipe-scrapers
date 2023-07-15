import os
import unittest
from typing import Any, Iterator, List, Optional, Tuple

import responses


def load_tests(
    loader: unittest.loader.TestLoader, _, pattern: str
) -> unittest.suite.TestSuite:
    """Override the default unittest test loader to remove any test class that have
    the type ScraperClass.
    See https://docs.python.org/3/library/unittest.html#load-tests-protocol

    This is necessary because we have added a test function to ScraperTest which we
    want to be inherited by all the scraper test classes. Unfortunately this means
    the default test loader finds this function and tried to execute it for the
    ScraperTest class, where we get errors because ScraperTest is not design to be
    a test class on its own.

    Parameters
    ----------
    loader : unittest.loader.TestLoader
        Unittest test loader object
    _ : unittest.suite.TestSuite
        Tests discovered in __init__.py of test package. Unused.
    pattern : str
        Test discovery pattern. The default is test*.py which we leave unchanged.

    Returns
    -------
    unittest.suite.TestSuite
        Unittest test suite with all tests with a type of ScraperTest removed
    """

    # Discover all tests in the current package using the default pattern
    test_dir = os.path.dirname(__file__)
    package_tests = loader.discover(start_dir=test_dir, pattern=pattern)

    # Iterate through all discovered tests.
    filtered_tests: List[Any] = []
    for test_suite in package_tests:  # type: ignore[union-attr]
        # The first level of iteration effectively iterates through each discovered file
        for test_cases in test_suite:  # type: ignore[union-attr]
            # If the file contains a class derived from ScraperTest, we will have two
            # sets of tests case. One for ScraperTest and one for the derived class
            # Check the type of the first test in each set of test cases and append to
            # the list of filtered tests if the type is not ScraperTest
            if type(test_cases._tests[0]) is not ScraperTest:  # type: ignore[union-attr]
                filtered_tests.append(test_cases)

    # Update loader to only use the list of filtered tests.
    return loader.suiteClass(filtered_tests)


class ScraperTest(unittest.TestCase):

    maxDiff = None
    test_file_name: Optional[str] = None
    test_file_extension = "testhtml"
    scraper_class: Any

    @classmethod
    def expected_requests(cls) -> Iterator[Tuple[str, str, str]]:
        """
        Descriptions of the expected requests that the scraper-under-test will make, as
        tuples of: HTTP method, URL, path-to-content-file
        """
        filename = cls.test_file_name or cls.scraper_class.__name__.lower()
        path = f"tests/test_data/{filename}.{cls.test_file_extension}"
        yield responses.GET, "https://test.example.com", path

    @classmethod
    def setUpClass(cls):
        with responses.RequestsMock() as rsps:
            start_url = None
            for method, url, path in cls.expected_requests():
                start_url = start_url or url
                with open(path, encoding="utf-8") as f:
                    rsps.add(method, url, body=f.read())

            cls.harvester_class = cls.scraper_class(url=start_url)

    def test_consistent_ingredients_lists(self):
        # Assert that the ingredients returned by the ingredient_groups() function
        # are the same as the ingredients return by the ingredients() function.
        grouped = []
        for group in self.harvester_class.ingredient_groups():
            grouped.extend(group.ingredients)

        self.assertEqual(sorted(self.harvester_class.ingredients()), sorted(grouped))
