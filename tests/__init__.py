import pytest
import unittest


class ScraperTest(unittest.TestCase):

    online = False
    test_file_name = None

    def setUp(self):
        options = {"exception_handling": False}
        options.update(getattr(self, "scraper_options", {}))

        test_file_name = (
            self.test_file_name
            if self.test_file_name
            else self.scraper_class.__name__.lower()
        )
        with open(
            "tests/test_data/{}.testhtml".format(test_file_name), encoding="utf-8"
        ) as testfile:
            self.harvester_class = self.scraper_class(testfile, test=True, **options)
            canonical_url = self.harvester_class.canonical_url()
            if self.online:
                if not canonical_url:
                    pytest.skip(
                        f"could not find canonical url for online test of scraper '{self.scraper_class.__name__}'"
                    )
                self.harvester_class = self.scraper_class(url=canonical_url)
