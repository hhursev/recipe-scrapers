# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.plowingthroughlife import PlowingThroughLife
from tests import ScraperTest


class TestPlowingThroughLifeScraper(ScraperTest):
    scraper_class = PlowingThroughLife
    test_file_name = "plowingthroughlife_2"

    def test_host(self):
        self.assertEqual("plowingthroughlife.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual(
            "Jennifer @ Plowing Through Life", self.harvester_class.author()
        )

    def test_title(self):
        self.assertEqual(
            "Canned Cinnamon Rolls with Cream", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Breakfast,brunch", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("10 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://plowingthroughlife.com/wp-content/uploads/2022/08/Can-Cinnamon-Rolls-Heavy-Cream-FI.jpeg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 cans jumbo cinnamon rolls",
                "1 cup heavy whipping cream",
                "1 cup brown sugar",
                "1/2 cup butter (melted)",
                "1 tablespoon cinnamon",
                "1 cup powdered sugar",
                "1 tablespoon butter (softened)",
                "2 teaspoons vanilla",
                "3 - 6 tableaspoons milk",
                "2 packets prepared icing",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "2 cans jumbo cinnamon rolls",
                        "1 cup heavy whipping cream",
                        "1 cup brown sugar",
                        "1/2 cup butter (melted)",
                        "1 tablespoon cinnamon",
                    ],
                    purpose="Cinnamon Rolls",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 cup powdered sugar",
                        "1 tablespoon butter (softened)",
                        "2 teaspoons vanilla",
                        "3 - 6 tableaspoons milk",
                        "2 packets prepared icing",
                    ],
                    purpose="Icing",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        self.assertEqual(
            'Place cinnamon rolls in a single layer in the bottom of a lightly greased 9 x 13" baking pan. Pour heavy cream around the rolls to make an even layer in the pan.\nStir brown sugar, cinnamon and melted butter together and spread over top of cinnamon rolls.\nCover with foil and bake at 350°F for 25 - 30 minutes.\nIcing\nIn a small mixing bowl squeeze store bought icing add butter, powdered sugar, splash of vanilla and 1 tablespoon of milk.\nMix together and add 1 tablespoon of milk at a time until it reaches your preferred consistency.\nAllow the rolls to cool slightly and pour icing over top. Enjoy!',
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "A few extra ingredients are easy to add to these Canned Cinnamon Rolls with Heavy Cream to make a delightful breakfast recipe.",
            self.harvester_class.description(),
        )
