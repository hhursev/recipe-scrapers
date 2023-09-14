# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.tofoo import Tofoo
from tests import ScraperTest


class TestTofooScraper(ScraperTest):

    scraper_class = Tofoo
    test_file_name = "tofoo_2"

    def test_host(self):
        self.assertEqual("tofoo.co.uk", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("The Tofoo co.", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Sticky Sriracha Tofoo", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Vegans", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual(2, self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://tofoo.co.uk/wp-content/uploads/2023/07/StickySriracha-scaled.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1 pack of Naked Tofoo, cut into cubes",
            "2 tbsp cornflour",
            "2 tbsp veg oil",
            "Black pepper",
            "2 tbsp Sriracha",
            "2 tbsp soy sauce",
            "2 tbsp honey (or vegan alternative)",
            "1 tbsp rice vinegar",
            "280g microwave rice",
            "Sesame seeds",
            "Sliced spring onion",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 pack of Naked Tofoo, cut into cubes",
                        "2 tbsp cornflour",
                        "2 tbsp veg oil",
                        "Black pepper",
                    ],
                    purpose="For the Tofoo",
                ),
                IngredientGroup(
                    ingredients=[
                        "2 tbsp Sriracha",
                        "2 tbsp soy sauce",
                        "2 tbsp honey (or vegan alternative)",
                        "1 tbsp rice vinegar",
                    ],
                    purpose="For the sauce",
                ),
                IngredientGroup(
                    ingredients=[
                        "280g microwave rice",
                        "Sesame seeds",
                        "Sliced spring onion",
                    ],
                    purpose="To serve (optional)",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = [
            "In a bowl, mix the cornflour with a pinch of pepper and toss your Tofoo cubes through until evenly covered.",
            "Heat your veg oil in a large frying pan over a medium heat. Once hot, add your Tofoo cubes and cook for 5 mins, turning them over until golden on all sides.",
            "Whisk all sauce ingredients in a small bowl and add to your Tofoo. Stir and cook for a few mins until all your Tofoo is evenly covered in sticky sauce.",
            "Meanwhile, cook your microwave rice as per the pack instructions and add into bowls before topping with your sticky Sriracha Tofoo. Scatter with spring onion and sesame seeds for the ultimate fakeaway, ready in only 20 mins!",
        ]
        expected_instructions = "\n".join(expected_instructions)
        self.assertEqual(expected_instructions, self.harvester_class.instructions())
