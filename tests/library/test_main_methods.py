import pathlib
import unittest
from unittest import mock

from recipe_scrapers import (
    WebsiteNotImplementedError,
    get_supported_urls,
    scrape_html,
    scraper_exists_for,
)
from recipe_scrapers._utils import get_host_name


class TestMainMethods(unittest.TestCase):

    def test_valid_call_formats(self):
        test_html = "<!-- load this variable with the HTML from the URL below -->"
        test_url = "https://en.wikibooks.org/wiki/Cookbook:B%C3%A9chamel_Sauce_(Beeton)"

        # These calls should all be equivalent and valid.
        scrape_html(test_html, test_url)
        scrape_html(test_html, org_url=test_url)
        scrape_html(test_html, org_url=test_url)  # short for 'original url'
        # scrape_html(html=test_html, url=test_url)  # TODO

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

    @mock.patch("recipe_scrapers.requests.get")
    def test_offline_no_html_retrieval(self, mock_get):
        with self.assertRaises(ValueError):
            scrape_html(
                html=None,
                org_url="https://recipe-scrapers.example/algorithmic-cupcakes.html",
                online=False,
                supported_only=False,
            )

        assert not mock_get.called

    @mock.patch("recipe_scrapers.requests.get")
    def test_online_mode_html_retrieval(self, mock_get):
        recipe_html = pathlib.Path(
            "tests/test_data/recipe-scrapers.example/online.testhtml"
        )
        mock_get.return_value = mock.MagicMock()
        mock_get.return_value.text = recipe_html.read_text()

        scrape_html(
            html=None,
            org_url="https://recipe-scrapers.example/algorithmic-cupcakes.html",
            online=True,
            supported_only=False,
        )

        assert mock_get.called

    def test_unsupported_website(self):
        with self.assertRaises(WebsiteNotImplementedError):
            scrape_html(
                html="<!DOCTYPE html><html><body>arbitrary</body></html>",
                org_url="https://unsupported.recipe-scrapers.example/unavailable.html",
                online=False,
                supported_only=True,
            )
