import os
import unittest

from recipe_scrapers.thepioneerwoman import ThePioneerWoman


class TestThePioneerWomanScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'thepioneerwoman.html'
        )) as file_opened:
            self.harvester_class = ThePioneerWoman(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'thepioneerwoman.com',
            self.harvester_class.host()
        )

    def test_publisher_site(self):
        self.assertEqual(
            'http://thepioneerwoman.com/',
            self.harvester_class.publisher_site()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Patty Melts'
        )

    def test_total_time(self):
        self.assertEqual(
            35,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                '1 stickButter',
                '1 wholeLarge Onion, Halved And Sliced',
                '1-1/2 poundGround Beef',
                'Salt And Pepper, to taste',
                '5 dashesWorcestershire Sauce',
                '8 slicesSwiss Cheese',
                '8 slicesRye Bread'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'In a medium skillet, melt 2 tablespoons of butter over medium-low \nheat. Throw in the sliced onions and cook slowly for 20 to 25 minutes, \nstirring occasionally, until the onions are golden brown and soft.In a medium bowl, mix together the ground beef, salt & pepper, and Worcestershire. Form into 4 patties.Melt\n 2 tablespoons butter in a separate skillet over medium heat. Cook the \npatties on both sides until totally done in the middle.Assemble\n patty melts this way: Slice of bread, slice of cheese, hamburger patty,\n 1/4 of the cooked onions, another slice of cheese, and another slice of\n bread. On a clean griddle or in a skillet, melt 2 tablespoons butter \nand grill the sandwiches over medium heat until golden brown. Remove the\n sandwiches and add the remaining 2 tablespoons of butter to the \nskillet. Turn the sandwiches to the skillet, flipping them to the other \nside. Cook until golden brown and crisp, and until cheese is melted.Slice in half and serve immediately!',
            self.harvester_class.instructions()
        )
