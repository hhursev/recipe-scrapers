import unittest
from typing import Any, Iterator, Optional, Tuple

import responses


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
        if cls == ScraperTest:
            # Only modify setUpClass if subclass of ScraperTest
            return super().setUpClass()

        with responses.RequestsMock() as rsps:
            start_url = None
            for method, url, path in cls.expected_requests():
                start_url = start_url or url
                with open(path, encoding="utf-8") as f:
                    rsps.add(method, url, body=f.read())

            cls.harvester_class = cls.scraper_class(url=start_url)

    def run(self, result=None):
        """
        Python's unittest (default) test runner will want to run tests
        from a class/module if there are test_* methods in it.

        We don't want this to be the case with ScraperTest though.
        We also don't want to flood our logs with loads of "skips".

        Overwrite the default built-in runner in this case
        and make it not attempting a run at all.
        """
        if self.__class__ == ScraperTest:
            return None

        super().run(result)

    def test_consistent_ingredients_lists(self):
        # Assert that the ingredients returned by the ingredient_groups() function
        # are the same as the ingredients return by the ingredients() function.
        grouped = []
        for group in self.harvester_class.ingredient_groups():
            grouped.extend(group.ingredients)

        self.assertEqual(sorted(self.harvester_class.ingredients()), sorted(grouped))

    def test_multiple_instructions(self):
        # Assert that the instructions_list() method returns more than one item;
        # this implicitly also confirms that instructions() returns a newline-separated
        # value of type 'str'
        instructions = self.harvester_class.instructions_list()
        message = (
            "Most recipes contain more than one instruction, but this recipe test "
            "did not.  Please check the implementation (and source HTML) and either "
            "fix the code, or override this method in your test module if you are sure "
            "this is the expected behaviour."
        )
        self.assertGreater(len(instructions), 1, message)
