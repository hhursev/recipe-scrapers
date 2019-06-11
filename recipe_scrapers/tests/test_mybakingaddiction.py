import os
import unittest

from recipe_scrapers.mybakingaddiction import MyBakingAddiction


class TestMyBakingAddictionScraper(unittest.TestCase):

    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'mybakingaddiction.testhtml'
        )) as file_opened:
            self.harvester_class = MyBakingAddiction(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'mybakingaddiction.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Pumpkin Roll'
        )

    def test_total_time(self):
        self.assertEqual(
            40,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        self.assertEqual(
            "10 serving(s)",
            self.harvester_class.yields()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '2/3 cup pure pumpkin puree',
                '3 large eggs',
                '1 cup powdered sugar, sifted',
                '1/2 teaspoon baking soda',
                '1/4 teaspoon salt',
                'For the Filling',
                '1/4 cup powdered sugar (to sprinkle on towel)',
                '1 (8 ounce) package cream cheese, softened',
                '1 tablespoon pumpkin pie spice',
                '1/2 teaspoon baking powder',
                '1 teaspoon vanilla extract',
                '6 tablespoons butter, softened',
                '1 cup granulated sugar',
                '3/4 cup all-purpose flour',
                '1 teaspoon pure vanilla extract',
                'For the Cake'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Preheat oven to 375°F. Line a 15 x 10-inch jelly-roll pan with parchment paper and spray with non-stick cooking spray. Sprinkle a clean tea towel with powdered sugar. Set pan and towel aside.\nIn a medium bowl, combine flour, baking powder, baking soda, pumpkin pie spice and salt.\nIn a large bowl with an electric mixer, beat eggs, vanilla and sugar until thick.\nAdd in pumpkin and mix to combine.\nStir in flour mixture.\nSpread batter evenly into prepared pan.\nBake for 13 to 15 minutes or until top of cake springs back when touched.\nImmediately loosen and turn cake onto prepared towel. Carefully peel off paper. Roll up cake and towel together, starting with narrow end. Cool on wire rack.\nIn a medium bowl, beat cream cheese, powdered sugar, butter and vanilla extract until smooth.\nCarefully unroll cake; remove towel.\nSpread cream cheese mixture over cake. Reroll cake.\nWrap in plastic wrap and refrigerate at least one hour.',
            self.harvester_class.instructions()
        )
