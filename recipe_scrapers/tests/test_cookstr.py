import os
import unittest

from recipe_scrapers.cookstr import Cookstr


class TestCookstrScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'cookstr.html'
        )) as file_opened:
            self.harvester_class = Cookstr(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'cookstr.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Mozzarella-Tomato-Basil Frittata'
        )

    def test_total_time(self):
        self.assertEqual(
            30,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                '12 large eggs',
                '½ cup whole milk',
                '2 tablespoons extra virgin olive oil',
                '4 large ripe tomatoes, peeled and sliced',
                '1 pound fresh or smoked mozzarella, diced',
                '2 tablespoons slivered basil leaves',
                'Salt and freshly ground black pepper'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Preheat the broiler.\nIn a large bowl, beat the eggs with the milk.\nPour 1 tablespoon of the oil into a very large ovenproof skillet, or use 2 skillets with half the ingredients in each. Place over medium heat on the stovetop and pour in the egg mixture. Scatter the tomatoes, cheese, and basil over the eggs. Season with salt and pepper to taste.\nWhen the bottom just begins to brown, place the skillet under the broiler just until the top is set, a minute or less. Remove from the oven and use a large spatula to transfer the frittata to a serving platter. Cool about 10 minutes, cut into wedges, and serve.\n',
            self.harvester_class.instructions()
        )
