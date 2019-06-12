import os
import unittest

from recipe_scrapers.foodrepublic import FoodRepublic


class TestFoodRepublicScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'foodrepublic.testhtml'
        )) as file_opened:
            self.harvester_class = FoodRepublic(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'foodrepublic.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Dutch White Asparagus Recipe'
        )

    def test_total_time(self):
        self.assertEqual(
            60,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        self.assertEqual(
            "4 serving(s)",
            self.harvester_class.yields()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '12 spears Dutch white asparagus',
                '1/2 each Meyer lemon, orange and grapefruit',
                '2 cups water, for steaming',
                '1 cup grated Parmesan cheese',
                '1/2 cup Chardonnay',
                '1/2 cup white wine vinegar',
                '2 sprigs fresh thyme',
                '1/2 cup shallots, minced',
                'small chunk of Parmesan rind',
                '4 tablespoons unsalted butter, chilled and cut into small cubes',
                '4 fresh eggs, poached (see instructions)',
                '4 slices prosciutto'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'After peeling and trimming the asparagus, steam it in citrus water — water with Meyer lemon, orange and grapefruit slices — until fork tender.\nIn a pot add the Chardonnay, white wine vinegar, thyme, shallots and chunk of Parmesan rind; reduce about a quarter.\nRemove from heat and slowly whisk in cubes of butter until sauce is thick and glossy.\nPour 2 tablespoons of beurre blanc on a plate, top it with a poached egg, steamed white asparagus, prosciutto and grated Parmesan.\nSpring Asparagus Soup Recipe\nGoat Cheese And Asparagus Macaroni Salad Recipe\nRoasted Asparagus & Scrambled Eggs Recipe',
            self.harvester_class.instructions()
        )
