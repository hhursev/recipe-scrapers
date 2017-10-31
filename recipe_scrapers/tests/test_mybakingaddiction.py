import os
import unittest

from recipe_scrapers.mybakingaddiction import MyBakingAddiction


class TestMyBakingAddictionScraper(unittest.TestCase):

    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
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
            'Cheesecake in a Jar'
        )

    def test_total_time(self):
        self.assertEqual(
            0,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '½ cup plus 2 tablespoons granulated sugar',
                'zest of one lemon',
                '2 packages cream cheese, 8 oz each; room temperature',
                '2 large eggs; room temperature',
                '¼ cup heavy cream',
                '1 ½ teaspoons pure vanilla extract',
                '1 cup fresh berries'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Preheat oven to 350°F.\nBegin to boil a large pot of water for the water bath.\nIn the bowl of your stand mixer fitted with your paddle attachment, combine the sugar and lemon zest and mix until the sugar is moistened and fragrant.\nAdd in the cream cheese and cream together until smooth.\nAdd eggs, one at a time, fully incorporating each before adding the next. Make sure to scrape down the bowl in between each egg.\nAdd heavy cream and vanilla and mix until smooth.\nPour batter into canning jars until about ¾ of the way full.\nPlace jars into a larger pan and pour boiling water into the larger pan until halfway up the sides of the jars.\nBake 25 to 30 minutes, the edges will appear to be set, but the center will still have a little jiggle to it.\nCarefully remove the cheesecake jars from the water bath and place on a cooling rack to cool completely.\nOnce the cheesecakes are completely cooled, place them into the refrigerator for at least 5 hours.\nTop will fresh berries and serve.',
            self.harvester_class.instructions()
        )
