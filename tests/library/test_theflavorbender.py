import json
import pathlib
import unittest

from recipe_scrapers import (
    SCRAPERS,
    get_supported_urls,
    scrape_html,
    scraper_exists_for,
)
from recipe_scrapers._grouping_utils import IngredientGroup


class TestTheFlavorBender(unittest.TestCase):
    def setUp(self):
        fixture = pathlib.Path(
            "tests/test_data/theflavorbender.com/theflavorbender_1.testhtml"
        )
        self.html = fixture.read_text(encoding="utf-8")
        self.expected = json.loads(
            fixture.with_suffix(".json").read_text(encoding="utf-8")
        )
        self.url = self.expected["canonical_url"]

    def test_registration_and_public_dispatch(self):
        self.assertIn("theflavorbender.com", get_supported_urls())
        for url in (self.url, self.url.replace("www.", "")):
            self.assertTrue(scraper_exists_for(url))
            for options in ({}, {"supported_only": True}, {"supported_only": False}):
                with self.subTest(url=url, options=options):
                    scraper = scrape_html(self.html, url, **options)
                    self.assertIs(type(scraper), SCRAPERS["theflavorbender.com"])
                    self.assertEqual(scraper.host(), "theflavorbender.com")
                    self.assertEqual(scraper.title(), self.expected["title"])

    def test_schema_only(self):
        html = (
            '<script type="application/ld+json">'
            + json.dumps(
                {
                    "@context": "https://schema.org",
                    "@type": "Recipe",
                    "name": "Synthetic beans",
                    "recipeIngredient": ["1 cup beans"],
                    "recipeInstructions": [
                        {"@type": "HowToStep", "text": "Warm the beans."}
                    ],
                }
            )
            + "</script>"
        )
        for options in ({}, {"supported_only": True}):
            with self.subTest(options=options):
                scraper = scrape_html(html, self.url, **options)
                self.assertEqual(scraper.title(), "Synthetic beans")
                self.assertEqual(scraper.instructions_list(), ["Warm the beans."])
                self.assertEqual(
                    scraper.ingredient_groups(), [IngredientGroup(["1 cup beans"])]
                )

    def test_ingredient_order_and_duplicates(self):
        scraper = scrape_html(self.html, self.url)
        groups = scraper.ingredient_groups()
        self.assertEqual(
            groups,
            [IngredientGroup(**group) for group in self.expected["ingredient_groups"]],
        )
        self.assertEqual(
            [ingredient for group in groups for ingredient in group.ingredients],
            scraper.ingredients(),
        )
        self.assertEqual(scraper.ingredients().count("1 tsp oil"), 3)

    def test_repeated_group_headings(self):
        scraper = scrape_html(self.html, self.url)
        for heading in scraper.soup.select(".wprm-recipe-ingredient-group-name"):
            heading.string = "  Shared heading  "
        groups = scraper.ingredient_groups()
        self.assertEqual([group.purpose for group in groups], ["Shared heading"] * 3)
        self.assertEqual(
            [group.ingredients for group in groups],
            [group["ingredients"] for group in self.expected["ingredient_groups"]],
        )

    def test_missing_group_headings(self):
        scraper = scrape_html(self.html, self.url)
        for heading in scraper.soup.select(".wprm-recipe-ingredient-group-name"):
            heading.decompose()
        groups = scraper.ingredient_groups()
        self.assertEqual([group.purpose for group in groups], [None] * 3)
        self.assertEqual(
            [ingredient for group in groups for ingredient in group.ingredients],
            scraper.ingredients(),
        )

    def test_mismatched_ingredient_counts(self):
        for count in (6, 8):
            with self.subTest(count=count):
                scraper = scrape_html(self.html, self.url)
                if count == 6:
                    scraper.soup.select_one(".wprm-recipe-ingredient").decompose()
                else:
                    extra = scraper.soup.new_tag(
                        "li", attrs={"class": "wprm-recipe-ingredient"}
                    )
                    scraper.soup.select_one(".wprm-recipe-ingredients").append(extra)
                with self.assertRaisesRegex(
                    ValueError,
                    f"Found {count} grouped ingredients but was expecting to find 7",
                ):
                    scraper.ingredient_groups()

    def test_image_selection(self):
        for options in ({}, {"best_image": True}, {"best_image": False}):
            with self.subTest(options=options):
                scraper = scrape_html(self.html, self.url, **options)
                expected = (
                    "https://images.example/grain-bowl.jpg"
                    if options.get("best_image") is False
                    else self.expected["image"]
                )
                self.assertEqual(scraper.image(), expected)

    def test_wprm_equipment(self):
        scraper = scrape_html(self.html, self.url)
        self.assertEqual(scraper.equipment(), [])
        equipment = scraper.soup.new_tag(
            "div", attrs={"class": "wprm-recipe-equipment-name"}
        )
        equipment.string = "  Mixing bowl*"
        scraper.soup.select_one(".wprm-recipe-container").append(equipment)
        self.assertEqual(scraper.equipment(), ["Mixing bowl"])
