import json
import pathlib
import unittest

from recipe_scrapers import get_supported_urls, scrape_html


TARGETED_DOMAINS = (
    "imbibemagazine.com",
    "marionskitchen.com",
    "edition.theage.com.au",
    "kaleforniakravings.com",
    "betterhomebase.com",
    "instructables.com",
    "thebigtastybite.com",
    "dancyu.jp",
    "kikkoman.co.jp",
    "tiffycooks.com",
    "justapinch.com",
    "olivetomato.com",
    "wandercapetown.com",
    "yummylittlebelly.com",
)


class TestSouschefTargetedScrapers(unittest.TestCase):
    def setUp(self):
        fixture_dir = pathlib.Path("tests/test_data/souschef_targeted")
        self.html = (fixture_dir / "generic_recipe.testhtml").read_text()
        self.expected = json.loads((fixture_dir / "generic_recipe.json").read_text())

    def test_targeted_domains_are_registered(self):
        supported_urls = get_supported_urls()

        for domain in TARGETED_DOMAINS:
            with self.subTest(domain=domain):
                self.assertIn(domain, supported_urls)

    def test_targeted_domains_use_common_recipe_card_fallbacks(self):
        for domain in TARGETED_DOMAINS:
            with self.subTest(domain=domain):
                scraper = scrape_html(
                    html=self.html,
                    org_url=f"https://{domain}/recipes/fallback-recipe",
                    online=False,
                )

                self.assertEqual(self.expected["title"], scraper.title())
                self.assertEqual(self.expected["ingredients"], scraper.ingredients())
                self.assertEqual(self.expected["instructions"], scraper.instructions())
                self.assertEqual(self.expected["image"], scraper.image())
                self.assertEqual(self.expected["yields"], scraper.yields())
