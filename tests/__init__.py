import unittest
from typing import Any, Iterator, Optional, Tuple

import responses


class AbstractTest:
    """
    The addition of a test function to the ScraperTest class, to be inherited by all
    derived classes, means that the unittest test runner will try to run
    ScraperTest.test_*.
    However this will cause an error due to the setUpClass function failing when run
    on ScraperTest directly instead of on a class derived from ScraperTest.

    By nesting the ScraperTest class inside another class, the test functions of Scraper
    class are hidden from the unittest test runner. This means they will only run in the
    context of a class derived from AbstractTest.ScraperTest, which is what we want.
    """

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

            self.assertEqual(
                sorted(self.harvester_class.ingredients()), sorted(grouped)
            )
