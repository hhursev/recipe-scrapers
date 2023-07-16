# mypy: allow-untyped-defs

from recipe_scrapers.leanandgreenrecipes import LeanAndGreenRecipes
from tests import ScraperTest


class TestLeanAndGreenRecipesScraper(ScraperTest):

    scraper_class = LeanAndGreenRecipes

    def test_host(self):
        self.assertEqual("leanandgreenrecipes.net", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("lean.green", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Yellow Squash Taco Casserole", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(40.0, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("5 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://leanandgreenrecipes.net/sites/default/files/2021-08/Yellow%20Squash%20Taco%20Casserole.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1.25 lbs Lean Ground Beef",
                "2 cup Yellow Squash",
                "1.5 tsp Cumin",
                "1.5 tsp Paprika",
                "1.5 tsp Chili Powder",
                "1/8 tsp Cayenne Pepper",
                "1/2 tsp Salt",
                "3/4 tsp Garlic Powder",
                "2 cup Low Fat Cheddar Cheese",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Preheat oven to 350*F.\nCook the ground beef. After browning the meat, add the canned Diced tomatoes and seasonings to the ground beef and simmer for 5 minutes.\nPlace the sliced squash to the bottom of a 9 x 13 inch baking pan.\nPlace meat mixture on top of squash, sprinkle grated cheese on top.\nBake in preheated oven for about 25 minutes.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(3.8, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Mexican", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Tip: Recipe makes 5 servings, but casserole can be divided into individual 1 serving portions and freezing for later.",
            self.harvester_class.description(),
        )
