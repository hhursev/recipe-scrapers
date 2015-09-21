import os
import unittest

from recipe_scrapers.thevintagemixer import TheVintageMixer


class TestTheVintageMixerScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'thevintagemixer.html'
        )) as file_opened:
            self.harvester_class = TheVintageMixer(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'thevintagemixer.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Cauliflower Pizza Crust Recipe'
        )

    def test_total_time(self):
        self.assertEqual(
            0,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                '1 small head of cauliflower, leaves and stems removed',
                '1 teaspoon basil',
                '1 teaspoon oregano',
                '1 teaspoon parsley',
                '1 teaspoon salt',
                '1/2 cup Manchengo sheep milk cheese (or Mozzarella)',
                '2 eggs', 'cornmeal, to dust the pizza stone',
                '1 jar marinara or pizza sauce',
                '1/2 cup sheep milk cheese',
                '5-8 basil leaves'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat oven to 350 degrees.\nChop cauliflower florets into chunks. Pulse the cauliflower in a food processor until it resembles a fine grain, like rice or couscous. Pour cauliflower into a large bowl. Add herbs, and salt, then cheese and eggs.\nSpread a tablespoon or so of cornmeal all over a pizza stone. Place the cauliflower mixture (note- this won't resemble a ball of dough) on the middle of the stone and use your hands to press it into a circle about 1/4 inch thick.\nBake for 20 minutes at 350 then an additional 10 minutes at 400 degrees. Crust will be done when it turns golden brown in color.\nRemove crust from oven. Change oven temperature to 450 degrees. Add pizza sauce, cheese and whatever toppings you would like, then bake again for about 5 minutes or until cheese on top is melted.",
            self.harvester_class.instructions()
        )
