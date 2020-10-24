import pytest
import unittest


class ScraperTest(unittest.TestCase):

    online = False

    def setUp(self):
        options = {"exception_handling": False}
        options.update(getattr(self, "scraper_options", {}))

        with open(
            "tests/test_data/{}.testhtml".format(self.scraper_class.__name__.lower()),
            encoding="utf-8",
        ) as testfile:
            self.harvester_class = self.scraper_class(testfile, test=True, **options)
            canonical_url = self.harvester_class.soup.find('link', {'rel': 'canonical'})
            if self.online:
                if not canonical_url:
                    pytest.skip(f"could not find canonical url for online test of scraper '{self.scraper_class.__name__}'")
                self.harvester_class = self.scraper_class(url=canonical_url['href'])
