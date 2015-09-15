import os
import unittest

from recipe_scrapers.tasty_kitchen import TastyKitchen


class TestTastyKitchenScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'tasty_kitchen.html'
        )) as file_opened:
            self.harvester_class = TastyKitchen(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'tastykitchen.com/',
            self.harvester_class.host()
        )

    def test_publisher_site(self):
        self.assertEqual(
            'http://tastykitchen.com/',
            self.harvester_class.publisher_site()
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

    def test_ingredients(self):
        self.assertListEqual(
            [
                '2 cupsAll-purpose Flour',
                '1 teaspoonKosher Salt',
                '1 TablespoonBaking Powder',
                '1 teaspoonBaking Soda',
                '5 TablespoonsCold Unsalted Butter',
                '1 cupButtermilk',
                '4Garlic Scapes, Finely Chopped',
                '2 TablespoonsFresh Chives',
                '½ cupsShredded Cheddar Cheese, Sharp'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Preheat oven to 450ºF.\nCombine dry ingredients together in bowl. Cut butter into small \npea-sized pieces and fold into dry ingredients. Combine thoroughly, \nsmashing butter into mixture until blended. Stir in buttermilk and stir \nby hand until roughly blended.\nAdd scapes, chives and cheddar cheese, setting aside a small amount \nof cheese and chives to top biscuits with before baking. Combine to form\n a ball.\nTurn dough out onto floured surface and knead lightly (dough should \nhave slightly sticky consistency). Roll out dough so that it is 3/4 inch\n thick. Using a glass or a biscuit cutter, cut out 2-inch round shapes. \nPlace the rounds on an ungreased baking sheet. Gather dough scraps, and \ngently roll out again and repeat.\nSprinkle top of rounds with a pinch of cheddar cheese and chives. \nBake biscuits for 8–10 minutes until golden brown. Serve warm with a pat\n of butter.\n',
            self.harvester_class.instructions()
        )

    def test_social_rating(self):
        self.assertEqual(
            self.harvester_class.social_rating(),
            0
        )
