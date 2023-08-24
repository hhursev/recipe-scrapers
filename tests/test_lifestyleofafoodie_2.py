# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.lifestyleofafoodie import LifestyleOfAFoodie
from tests import ScraperTest


class TestLifestyleOfAFoodieScraper(ScraperTest):

    scraper_class = LifestyleOfAFoodie
    test_file_name = "lifestyleofafoodie_2"

    def test_host(self):
        self.assertEqual("lifestyleofafoodie.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Chahinez", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Crispy air fryer frozen french fries", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Side Dish", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(13, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        expected_image = "https://lifestyleofafoodie.com/wp-content/uploads/2021/01/Air-fryer-frozen-French-fries-18-of-18-scaled.jpg"
        self.assertEqual(expected_image, self.harvester_class.image())

    def test_ingredients(self):
        expected_ingredients = [
            "2 lbs Bag of frozen French fries",
            "6 tbsp ketchup",
            "2 tsp horse radish",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = "Place your french fries of crinkle fries in the air fryer and air fry at 400F for 12 minutes. Make sure to shake the basket halfway through to bake everything more evenly.\nMake the spicy ketchup\nin a small bowl mix the ketchup and horse radish together until well incorporated. Dip your french fries in it and enjoy!"
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        expected_description = "This is the best air fryer frozen french fries recipe ever. Make it as a snack or as a side dish for your burger days."
        self.assertEqual(expected_description, self.harvester_class.description())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "2 lbs Bag of frozen French fries",
                    ],
                    purpose=None,
                ),
                IngredientGroup(
                    ingredients=[
                        "6 tbsp ketchup",
                        "2 tsp horse radish",
                    ],
                    purpose="Spicy ketchup",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )
