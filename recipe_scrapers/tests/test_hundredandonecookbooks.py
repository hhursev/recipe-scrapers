import os
import unittest

from recipe_scrapers.hundredandonecookbooks import HundredAndOneCookbooks


class TestHundredAndOneCookbooksScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            '101cookbooks.testhtml'
        )) as file_opened:
            self.harvester_class = HundredAndOneCookbooks(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            '101cookbooks.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Nikki's Healthy Cookies Recipe"
        )

    def test_total_time(self):
        self.assertEqual(
            0,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        self.assertEqual(
            0,
            self.harvester_class.yields()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '3 large, ripe bananas,  well mashed (about 1 1/2 cups)',
                '1 teaspoon vanilla extract',
                "1/4 cup coconut oil, barely warm - so it isn't solid (or alternately, olive oil)",
                '2 cups rolled oats',
                '2/3 cup almond meal',
                '1/3 cup coconut, finely shredded & unsweetened',
                '1/2 teaspoon cinnamon',
                '1/2 teaspoon fine grain sea salt',
                '1 teaspoon baking powder',
                '6 - 7 ounces chocolate chips or dark chocolate bar chopped'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat oven to 350 degrees, racks in the top third.\nIn a large bowl combine the bananas, vanilla extract, and coconut oil. Set aside. In another bowl whisk together the oats, almond meal, shredded coconut, cinnamon, salt, and baking powder. Add the dry ingredients to the wet ingredients and stir until combined. Fold in the chocolate chunks/chips.The dough is a bit looser than a standard cookie dough, don't worry about it. Drop dollops of the dough, each about 2 teaspoons in size, an inch apart, onto a parchment (or Silpat) lined baking sheet. Bake for 12 - 14 minutes. I baked these as long as possible without burning the bottoms and they were perfect - just shy of 15 minutes seems to be about right in my oven.\nMakes about 3 dozen bite-sized cookies.\nPrint Recipe",
            self.harvester_class.instructions()
        )
