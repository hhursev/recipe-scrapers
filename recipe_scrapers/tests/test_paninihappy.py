import os
import unittest

from recipe_scrapers.paninihappy import PaniniHappy


class TestPaniniHappyScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'paninihappy.testhtml'
        )) as file_opened:
            self.harvester_class = PaniniHappy(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'paninihappy.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Grilled Mac & Cheese with BBQ Pulled Pork'
        )

    def test_total_time(self):
        self.assertEqual(
            30,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        self.assertEqual(
            "4 item(s)",
            self.harvester_class.yields()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '4 tablespoons unsalted butter, divided',
                '4 cups prepared macaroni and cheese, warmed',
                '2 onions, thinly sliced',
                'Kosher salt and freshly ground pepper',
                '1 cup barbecue sauce',
                '2 cups prepared pulled pork',
                '8 slices sourdough bread',
                '12 slices sharp cheddar cheese (about 6 ounces)'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Spread the macaroni and cheese in an 8-inch-square baking dish to about 3/4 inch thick. Cover with plastic wrap and chill until firm, about 45 minutes. Cut the macaroni and cheese into squares that are slightly smaller than the bread slices.\nMeanwhile, melt 2 tablespoons butter in a skillet over medium heat. Add the onions and cook, stirring, until caramelized, about 20 minutes. Season with salt and pepper.\nCombine the barbecue sauce and pulled pork in a saucepan over low heat and cook until warmed through, about 5 minutes.\nPreheat the panini grill to medium-high heat.\nMelt the remaining 2 tablespoons butter and brush on one side of each bread slice. Flip over half of the bread slices; layer 1 slice of cheddar, 1 macaroni-and-cheese square and another slice of cheddar on each. Top each with one-quarter of the pulled pork and caramelized onions and another slice of cheddar. Top with the remaining bread slices, buttered-side up.\nWorking in batches, cook the sandwiches until the cheese melts and the bread is golden, about 5 minutes.',
            self.harvester_class.instructions()
        )
