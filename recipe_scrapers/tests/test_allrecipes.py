import os
import unittest

from recipe_scrapers.allrecipes import AllRecipes


class TestAllRecipesScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'allrecipes.testhtml'
        )) as file_opened:
            self.harvester_class = AllRecipes(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'allrecipes.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Four Cheese Margherita Pizza'
        )

    def test_total_time(self):
        self.assertEqual(
            40,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        self.assertEqual("8 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '1/4 cup olive oil',
                '1 tablespoon minced garlic',
                '1/2 teaspoon sea salt',
                '8 Roma tomatoes, sliced',
                '2 (12 inch) pre-baked pizza crusts',
                '8 ounces shredded Mozzarella cheese',
                '4 ounces shredded Fontina cheese',
                '10 fresh basil leaves, washed, dried',
                '1/2 cup freshly grated Parmesan cheese',
                '1/2 cup crumbled feta cheese'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Stir together olive oil, garlic, and salt; toss with tomatoes, and allow to stand for 15 minutes. Preheat oven to 400 degrees F (200 degrees C).\nBrush each pizza crust with some of the tomato marinade. Sprinkle the pizzas evenly with Mozzarella and Fontina cheeses. Arrange tomatoes overtop, then sprinkle with shredded basil, Parmesan, and feta cheese.\nBake in preheated oven until the cheese is bubbly and golden brown, about 10 minutes.\n',
            self.harvester_class.instructions()
        )

    def test_ratings(self):
        self.assertEqual(
            4.81,
            self.harvester_class.ratings()
        )
