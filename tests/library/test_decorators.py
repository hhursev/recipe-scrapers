import unittest

from recipe_scrapers._abstract import AbstractScraper
from recipe_scrapers._decorators import opengraph_fallback


class DecoratorTest(unittest.TestCase):

    TEST_URL = "https://example.org"
    TEST_HTML = "<html><meta property='og:image' content='https://example.org/empty.png'></html>"

    class DecoratedScraper(AbstractScraper):
        @classmethod
        def host(self):
            return "example.org"

        @opengraph_fallback
        def image(self):
            pass

        @opengraph_fallback
        def ingredients(self):
            pass

    def test_extraction_not_implemented(self):
        # An attempt to access a field that has no implementation in the extractor
        scraper = self.DecoratedScraper(url=self.TEST_URL, html=self.TEST_HTML)
        self.assertRaises(NotImplementedError, scraper.ingredients)

    def test_extraction_successful(self):
        scraper = self.DecoratedScraper(url=self.TEST_URL, html=self.TEST_HTML)
        self.assertEqual(scraper.image(), "https://example.org/empty.png")
