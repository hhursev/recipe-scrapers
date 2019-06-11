import os
import unittest

from recipe_scrapers.tastykitchen import TastyKitchen


class TestTastyKitchenScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'tasty_kitchen.testhtml'
        )) as file_opened:
            self.harvester_class = TastyKitchen(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'tastykitchen.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Cheddar and Garlic Scape Biscuits'
        )

    def test_total_time(self):
        self.assertEqual(
            30,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        self.assertEqual(
            "12 serving(s)",
            self.harvester_class.yields()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '2 cups All-purpose Flour',
                '1 teaspoon Kosher Salt',
                '1 Tablespoon Baking Powder',
                '1 teaspoon Baking Soda',
                '5 Tablespoons Cold Unsalted Butter',
                '1 cup Buttermilk',
                '4 Garlic Scapes, Finely Chopped',
                '2 Tablespoons Fresh Chives',
                '½ cups Shredded Cheddar Cheese, Sharp'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
           'Preheat oven to 450ºF.\nCombine dry ingredients together in bowl. Cut butter into small pea-sized pieces and fold into dry ingredients. Combine thoroughly, smashing butter into mixture until blended. Stir in buttermilk and stir by hand until roughly blended.\nAdd scapes, chives and cheddar cheese, setting aside a small amount of cheese and chives to top biscuits with before baking. Combine to form a ball.\nTurn dough out onto floured surface and knead lightly (dough should have slightly sticky consistency). Roll out dough so that it is 3/4 inch thick. Using a glass or a biscuit cutter, cut out 2-inch round shapes. Place the rounds on an ungreased baking sheet. Gather dough scraps, and gently roll out again and repeat.\nSprinkle top of rounds with a pinch of cheddar cheese and chives. Bake biscuits for 8–10 minutes until golden brown. Serve warm with a pat of butter.',
            self.harvester_class.instructions()
        )
