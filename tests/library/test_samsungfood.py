import json
import unittest
from unittest.mock import patch

from recipe_scrapers import scrape_html
from recipe_scrapers._exceptions import FillPluginException


class TestSamsungFood(unittest.TestCase):
    url = "https://app.samsungfood.com/recipes/test-recipe"
    recipe_key = "whisk.x.recipe.v1.RecipeAPI/GetRecipe_test"

    def scraper(self, recipe=None, schema=None, script=None, hydrate=None):
        if script is None:
            if hydrate is None:
                hydrate = {self.recipe_key: {"recipe": recipe or {}}}
            script = "\n  var hydrate = " + json.dumps(hydrate) + ";\n"
        schema_script = (
            '<script type="application/ld+json">'
            + json.dumps(
                {"@context": "https://schema.org", "@type": "Recipe", **schema}
            )
            + "</script>"
            if schema is not None
            else ""
        )
        return scrape_html(
            f'<html lang="en"><head>{schema_script}</head>'
            f"<body><script>{script}</script></body></html>",
            self.url,
            online=False,
        )

    def test_samsungfood_hydration_fields(self):
        scraper = self.scraper(
            {
                "id": "test-recipe",
                "name": "Hydrated recipe",
                "description": "A recipe",
                "recipeAuthor": {
                    "author": {"value": {"firstName": "Test", "lastName": "Cook"}}
                },
                "ingredients": [{"text": "- 1 egg"}],
                "instructions": {"steps": [{"text": "1. Mix."}, {"text": "2. Bake."}]},
                "servings": 2,
                "durations": {"prepTime": 5, "cookTime": 10},
                "images": [{"url": "https://example.com/recipe.jpg"}],
                "labels": {
                    "mealType": [{"displayName": "Breakfast"}],
                    "cuisine": [{"displayName": "American"}],
                    "technique": [{"displayName": "Baking"}],
                },
            }
        )
        expected = {
            "title": "Hydrated recipe",
            "description": "A recipe",
            "author": "Test Cook",
            "ingredients": ["1 egg"],
            "instructions": "Mix.\nBake.",
            "yields": "2 servings",
            "total_time": 15,
            "prep_time": 5,
            "cook_time": 10,
            "image": "https://example.com/recipe.jpg",
            "category": "Breakfast",
            "cuisine": "American",
            "cooking_method": "Baking",
            "keywords": ["Hydrated recipe", "Breakfast", "American"],
            "canonical_url": self.url,
            "language": "en",
            "site_name": "Samsung Food",
        }
        for method, value in expected.items():
            with self.subTest(method=method):
                self.assertEqual(getattr(scraper, method)(), value)

    def test_samsungfood_schema_wins_over_hydration(self):
        scraper = self.scraper(
            {
                "id": "test-recipe",
                "name": "Hydrated title",
                "durations": {"totalTime": 40},
            },
            schema={"name": "Schema title", "totalTime": "PT20M"},
        )
        self.assertEqual(scraper.title(), "Schema title")
        self.assertEqual(scraper.total_time(), 20)

    def test_samsungfood_missing_schema_field_uses_hydration(self):
        scraper = self.scraper(
            {
                "id": "test-recipe",
                "name": "Hydrated title",
                "durations": {"prepTime": 5},
            },
            schema={"name": None},
        )
        self.assertEqual(scraper.title(), "Hydrated title")
        self.assertEqual(scraper.prep_time(), 5)

    def test_samsungfood_valid_schema_does_not_parse_broken_hydration(self):
        scraper = self.scraper(
            script="var hydrate = broken;", schema={"name": "Schema title"}
        )
        self.assertEqual(scraper.title(), "Schema title")

    def test_samsungfood_invalid_or_missing_hydration(self):
        scripts = (
            "",
            "var hydrate = {broken};",
            "var hydrate = null;",
            "var hydrate = [];",
            "var hydrate = {};",
            'var hydrate = {"whisk.x.recipe.v1.RecipeAPI/GetRecipe_test": null};',
            'var hydrate = {"whisk.x.recipe.v1.RecipeAPI/GetRecipe_test": {"recipe": []}};',
        )
        for script in scripts:
            with self.subTest(script=script):
                with self.assertRaises(FillPluginException):
                    self.scraper(script=script).title()

    def test_samsungfood_missing_optional_fields(self):
        scraper = self.scraper({"id": "test-recipe", "name": "Recipe"})
        for method in (
            "prep_time",
            "total_time",
            "nutrients",
            "category",
            "author",
            "ratings",
        ):
            with self.subTest(method=method):
                with self.assertRaises(FillPluginException):
                    getattr(scraper, method)()

    def test_samsungfood_empty_or_invalid_image_collection(self):
        for images in ([], None, {}, [None]):
            with self.subTest(images=images):
                scraper = self.scraper({"id": "test-recipe", "images": images})
                self.assertIsNone(scraper.image())

    def test_samsungfood_zero_and_partial_durations(self):
        for durations, expected in (
            ({"cookTime": 0}, 0),
            ({"prepTime": 5}, 5),
            ({"cookTime": 10}, 10),
            ({"totalTime": 30, "cookTime": 10}, 30),
        ):
            with self.subTest(durations=durations):
                scraper = self.scraper({"id": "test-recipe", "durations": durations})
                self.assertEqual(scraper.total_time(), expected)
        self.assertEqual(
            self.scraper(
                {"id": "test-recipe", "durations": {"cookTime": 0}}
            ).cook_time(),
            0,
        )

    def test_samsungfood_rating_counts_are_not_star_ratings(self):
        for rating, count in (
            ({}, 0),
            ({"likeCount": 3}, 3),
            ({"likeCount": 3, "dislikeCount": 1}, 4),
        ):
            with self.subTest(rating=rating):
                scraper = self.scraper(
                    {"id": "test-recipe", "reviews": {"rating": rating}}
                )
                self.assertEqual(scraper.ratings_count(), count)
                with self.assertRaises(FillPluginException):
                    scraper.ratings()

    def test_samsungfood_nutrients(self):
        def component(code, value, unit):
            return {
                "code": {"name": code},
                "value": value,
                "unit": {"displayName": unit},
            }

        scraper = self.scraper(
            {
                "id": "test-recipe",
                "nutrition": {
                    "components": [
                        component("ENERC_KCAL", 123.456, "kcal"),
                        component("FAT", 0, "g"),
                        component("PROCNT", 10, "g"),
                        component("NA", 12.345, "mg"),
                        component("UNKNOWN", 1, "g"),
                    ]
                },
            }
        )
        self.assertEqual(
            scraper.nutrients(),
            {
                "calories": "123.46",
                "fatContent": "0 g",
                "proteinContent": "10 g",
                "sodiumContent": "12.35 mg",
            },
        )

    def test_samsungfood_selects_current_recipe_not_recommendations(self):
        scraper = self.scraper(
            hydrate={
                self.recipe_key + "other": {"recipe": {"id": "other", "name": "Wrong"}},
                "recommendations": {"recipe": {"id": "test-recipe", "name": "Wrong"}},
                self.recipe_key: {"recipe": {"id": "test-recipe", "name": "Correct"}},
            }
        )
        self.assertEqual(scraper.title(), "Correct")
        scraper = self.scraper({"id": "other", "name": "Wrong"})
        with self.assertRaises(FillPluginException):
            scraper.title()

    def test_samsungfood_schema_only_ingredient_cleanup(self):
        scraper = self.scraper(
            script="",
            schema={
                "recipeIngredient": ["- 1 egg"],
                "recipeInstructions": "1. Mix.\n2. Bake.",
                "nutrition": {"calories": "unavailable", "proteinContent": "5 g"},
            },
        )
        self.assertEqual(scraper.ingredients(), ["1 egg"])
        self.assertEqual(scraper.instructions(), "Mix.\nBake.")
        self.assertEqual(scraper.nutrients(), {"proteinContent": "5 g"})

    def test_samsungfood_empty_fields_use_library_exceptions(self):
        for recipe, method in (
            ({"name": ""}, "title"),
            ({"description": None}, "description"),
            ({"durations": {}}, "total_time"),
            ({"labels": {"mealType": []}}, "category"),
            ({"ingredients": [{}]}, "ingredients"),
            ({"instructions": {"steps": [{}]}}, "instructions"),
            ({"nutrition": {"components": []}}, "nutrients"),
            ({"recipeAuthor": {"author": {"value": {}}}}, "author"),
        ):
            with self.subTest(method=method):
                scraper = self.scraper({"id": "test-recipe", **recipe})
                with self.assertRaises(FillPluginException):
                    getattr(scraper, method)()

    def test_samsungfood_unique_recipe_with_host_only_url(self):
        scraper = scrape_html(
            "<script>var hydrate = "
            + json.dumps({self.recipe_key: {"recipe": {"name": "Unique recipe"}}})
            + "</script>",
            "app.samsungfood.com",
        )
        self.assertEqual(scraper.title(), "Unique recipe")

    def test_samsungfood_ambiguous_recipes_with_host_only_url(self):
        scraper = scrape_html(
            "<script>var hydrate = "
            + json.dumps(
                {
                    self.recipe_key: {"recipe": {"name": "First recipe"}},
                    self.recipe_key + "other": {"recipe": {"name": "Other recipe"}},
                }
            )
            + "</script>",
            "app.samsungfood.com",
        )
        with self.assertRaises(FillPluginException):
            scraper.title()

    def test_samsungfood_hydration_is_parsed_once(self):
        scraper = self.scraper({"id": "test-recipe", "name": "Recipe", "servings": 1})
        with patch.object(
            scraper, "_parse_hydrate", wraps=scraper._parse_hydrate
        ) as parse:
            self.assertEqual(scraper.title(), "Recipe")
            self.assertEqual(scraper.yields(), "1 serving")
            self.assertEqual(scraper.title(), "Recipe")
            parse.assert_called_once()
