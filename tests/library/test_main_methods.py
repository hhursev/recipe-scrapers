import unittest

from recipe_scrapers import get_supported_urls, scraper_exists_for
from recipe_scrapers._utils import get_host_name


class TestMainMethods(unittest.TestCase):
    def test_get_supported_urls(self):
        urls = get_supported_urls()
        self.assertGreater(len(urls), 200)
        self.assertIn(get_host_name("https://www.hellofresh.nl/"), urls)
        self.assertIn(get_host_name("https://hellofresh.com/"), urls)

    def test_scraper_exists_for(self):
        self.assertFalse(scraper_exists_for("example.com"))
        self.assertTrue(scraper_exists_for("https://www.hellofresh.nl/"))
        self.assertTrue(
            scraper_exists_for("https://eatsmarter.de/rezepte/gruenkohl-kokos-suppe")
        )
