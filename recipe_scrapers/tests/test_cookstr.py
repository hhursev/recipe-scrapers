import os
import unittest

from recipe_scrapers.cookstr import Cookstr


class TestCookstrScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'cookstr.testhtml'
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
            'Chocolate Cake'
        )

    def test_total_time(self):
        self.assertEqual(
            60,
            self.harvester_class.total_time()
        )

    def test_total_time(self):
        self.assertEqual(
            0,
            self.harvester_class.yields()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '1 recipe Chocolate Cake Mix',
                '1/2 cup coffee or water',
                '1/2 cup almond or soy milk (vanilla flavor preferred)',
                '1/2 cup canola oil',
                '1/2 cup pure maple syrup',
                '2 tablespoons apple cider vinegar'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Preheat the oven to 350°F. Lightly grease a 9-inch cake pan with coconut oil or line a 12-cup muffin tin with paper liners.\nIn a large bowl, sift the dry cake mix ingredients using a fine-mesh sieve.\nIn a medium bowl, mix together the coffee, almond milk, oil, maple syrup, and vinegar.\nAdd the liquid ingredients to the bowl with the cake mix and whisk gently until there are no large clumps remaining.\nPour the batter into the prepared pan. Bake for 22 to 27 minutes in the cake pan or 20 to 25 minutes in the muffin tin. The cake/cupcakes can be stored in an airtight container in the fridge for up to 5 days or frozen for 2 to 3 months.',
            self.harvester_class.instructions()
        )
