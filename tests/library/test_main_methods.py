import json
import pathlib
import unittest
from unittest import mock
from warnings import catch_warnings, simplefilter

from recipe_scrapers import (
    NoSchemaFoundInWildMode,
    WebsiteNotImplementedError,
    get_supported_urls,
    scrape_html,
    scrape_me,
    scraper_exists_for,
)
from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers._utils import get_host_name
from recipe_scrapers.budapestcookingclass import BudapestCookingClass


class TestMainMethods(unittest.TestCase):

    def test_valid_call_formats(self):
        test_html = "<!-- load this variable with the HTML from the URL below -->"
        test_url = "https://en.wikibooks.org/wiki/Cookbook:B%C3%A9chamel_Sauce_(Beeton)"

        # These calls should all be equivalent and valid.
        scrape_html(test_html, test_url)
        scrape_html(test_html, org_url=test_url)
        scrape_html(test_html, org_url=test_url)  # short for 'original url'
        # scrape_html(html=test_html, url=test_url)  # TODO

    def test_invalid_call_formats(self):
        invalid_combinations = (
            (True, True),
            (True, False),
            (False, True),
            (False, False),
        )
        for supported_only, wild_mode in invalid_combinations:
            with self.subTest():
                with catch_warnings(record=True) as ws:
                    with self.assertRaises(ValueError):
                        scrape_html(
                            html="<html></html>",
                            org_url="https://recipe-scrapers.example/",
                            supported_only=supported_only,
                            wild_mode=wild_mode,
                        )
                        self.assertTrue(
                            any(isinstance(w.category, DeprecationWarning) for w in ws)
                        )

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

    def test_budapestcookingclass_supported(self):
        for name in ("budapestcookingclass_1", "budapestcookingclass_2"):
            fixture = pathlib.Path(
                "tests", "test_data", "budapestcookingclass.com", name
            )
            html = fixture.with_suffix(".testhtml").read_text(encoding="utf-8")
            expected = json.loads(
                fixture.with_suffix(".json").read_text(encoding="utf-8")
            )
            url = expected["canonical_url"]
            for org_url in (url, url.replace("https://", "https://www.")):
                for options in ({}, {"supported_only": True}):
                    with self.subTest(fixture=name, url=org_url, options=options):
                        scraper = scrape_html(html, org_url, **options)
                        self.assertIs(type(scraper), BudapestCookingClass)
                        self.assertTrue(scraper_exists_for(org_url))
                        self.assertIn(scraper.host(), get_supported_urls())
                        self.assertEqual(expected["title"], scraper.title())

    def test_budapestcookingclass_image_selection(self):
        fixture = pathlib.Path(
            "tests", "test_data", "budapestcookingclass.com", "budapestcookingclass_1"
        )
        html = fixture.with_suffix(".testhtml").read_text(encoding="utf-8")
        expected = json.loads(fixture.with_suffix(".json").read_text(encoding="utf-8"))
        for best_image, expected_image in (
            (None, expected["image"]),
            (False, expected["image"]),
            (True, "https://images.example/synthetic-soup-alternate.jpg"),
        ):
            with self.subTest(best_image=best_image):
                scraper = scrape_html(
                    html, expected["canonical_url"], best_image=best_image
                )
                self.assertEqual(expected_image, scraper.image())

    def test_budapestcookingclass_grouping_cardinality(self):
        fixture = pathlib.Path(
            "tests", "test_data", "budapestcookingclass.com", "budapestcookingclass_2"
        )
        html = fixture.with_suffix(".testhtml").read_text(encoding="utf-8")
        expected = json.loads(fixture.with_suffix(".json").read_text(encoding="utf-8"))
        ingredient = '<li class="wprm-recipe-ingredient">1 egg yolk</li>'
        for replacement, count in (("", 7), (ingredient * 2, 9)):
            with self.subTest(count=count):
                scraper = scrape_html(
                    html.replace(ingredient, replacement, 1), expected["canonical_url"]
                )
                with self.assertRaisesRegex(
                    ValueError,
                    f"Found {count} grouped ingredients but was expecting to find 8",
                ):
                    scraper.ingredient_groups()

    def test_budapestcookingclass_multiple_recipe_cards(self):
        fixture = pathlib.Path(
            "tests", "test_data", "budapestcookingclass.com", "budapestcookingclass_2"
        )
        html = fixture.with_suffix(".testhtml").read_text(encoding="utf-8")
        expected = json.loads(fixture.with_suffix(".json").read_text(encoding="utf-8"))
        html = html.replace(
            "</body>", '<div class="wprm-recipe-container"></div></body>'
        )

        scraper = scrape_html(html, expected["canonical_url"])

        with self.assertRaisesRegex(
            ValueError, "Expected one WP Recipe Maker recipe card"
        ):
            scraper.ingredient_groups()

    def test_budapestcookingclass_without_recipe_card(self):
        fixture = pathlib.Path(
            "tests", "test_data", "budapestcookingclass.com", "budapestcookingclass_2"
        )
        html = fixture.with_suffix(".testhtml").read_text(encoding="utf-8")
        expected = json.loads(fixture.with_suffix(".json").read_text(encoding="utf-8"))
        html = html.split("<body>", 1)[0] + "<body></body></html>"

        scraper = scrape_html(html, expected["canonical_url"])

        self.assertEqual(
            [IngredientGroup(expected["ingredients"])], scraper.ingredient_groups()
        )

    @mock.patch("recipe_scrapers.urlopen")
    def test_budapestcookingclass_scrape_me(self, mock_urlopen):
        fixture = pathlib.Path(
            "tests", "test_data", "budapestcookingclass.com", "budapestcookingclass_1"
        )
        mock_urlopen.return_value.read.return_value = fixture.with_suffix(
            ".testhtml"
        ).read_bytes()
        expected = json.loads(fixture.with_suffix(".json").read_text(encoding="utf-8"))

        scraper = scrape_me(expected["canonical_url"])

        self.assertIs(type(scraper), BudapestCookingClass)
        for method in (
            "title",
            "total_time",
            "yields",
            "ingredients",
            "instructions",
            "image",
        ):
            with self.subTest(method=method):
                self.assertEqual(expected[method], getattr(scraper, method)())
        mock_urlopen.assert_called_once()
        self.assertEqual(
            expected["canonical_url"], mock_urlopen.call_args.args[0].full_url
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

        with catch_warnings(record=True) as ws:
            simplefilter("always", category=DeprecationWarning)
            scrape_html(
                html=None,
                org_url="https://recipe-scrapers.example/algorithmic-cupcakes.html",
                online=True,
                supported_only=False,
            )
            self.assertTrue(any(w.category is DeprecationWarning for w in ws))

        assert mock_get.called

    def test_unsupported_website(self):
        html, url = (
            "<!DOCTYPE html><html><body>arbitrary</body></html>",
            "https://unsupported.recipe-scrapers.example/unavailable.html",
        )

        with self.assertRaises(WebsiteNotImplementedError):
            scrape_html(html=html, org_url=url, online=False)

        with self.assertRaises(WebsiteNotImplementedError):
            scrape_html(html=html, org_url=url, online=False, supported_only=True)

        with self.assertRaises(NoSchemaFoundInWildMode):
            with catch_warnings(record=True) as ws:
                simplefilter("always", category=DeprecationWarning)
                scrape_html(html=html, org_url=url, online=False, wild_mode=True)

        self.assertTrue(any(w.category is DeprecationWarning for w in ws))
