import os
import unittest

from recipe_scrapers.steamykitchen import SteamyKitchen


class TestSteamyKitchenScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'streamykitchen.html'
        )) as file_opened:
            self.harvester_class = SteamyKitchen(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'steamykitchen.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Vietnamese Pho: Beef Noodle Soup Recipe'
        )

    def test_total_time(self):
        self.assertEqual(
            270,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                'THE BROTH',
                '2 onions, halved',
                '4" nub of ginger, halved lengthwise',
                '5-6 pounds of good beef bones, preferably leg and knuckle',
                '1 pound of beef meat - chuck, brisket, rump, cut into large slices [optional]',
                '6 quarts of water',
                '1 package of Pho Spices [1 cinnamon stick, 1 tbl coriander seeds, 1 tbl fennel seeds, 5 whole star anise, 1 cardamom pod, 6 whole cloves - in mesh bag]',
                '1 1/2 tablespoons kosher salt (halve if using regular table salt)',
                '1/4 cup fish sauce',
                '1 inch chunk of yellow rock sugar (about 1 oz) - or 1oz of regular sugar',
                '2 pounds rice noodles (dried or fresh)',
                'Cooked beef from the broth (shredded or thinly sliced)',
                '1/2 pound flank, london broil, sirloin or eye of round, sliced as thinly as possible.',
                'big handful of each: mint, cilantro, basil',
                '2 limes, cut into wedges',
                '2-3 chili peppers, sliced',
                '2 big handfuls of fresh bean sprouts',
                'Hoisin sauce', 'Sriracha hot sauce'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Char: Turn your broiler on high and move rack to the highest spot. Place ginger and onions on baking sheet. Brush just a bit of cooking oil on the cut side of each. Broil on high until ginger and onions begin to char. Turn over and continue to char. This should take a total of 10-15 minutes. Parboil the bones: Fill large pot (12-qt capacity) with cool water. Boil water, and then add the bones, keeping the heat on high. Boil vigorously for 10 minutes. Drain, rinse the bones and rinse out the pot. If you have a lot of marrow in the bones, use a small spoon to scoop out and discard some of the marrow. Refill pot with bones and 6 qts of cool water. Bring to boil over high heat and lower to simmer. Using a ladle or a fine mesh strainer, remove any scum that rises to the top. Boil broth: Add ginger, onion, spice packet, beef, sugar, fish sauce, salt and simmer uncovered for 1 1/2 hours. Remove the beef meat and set aside (you\'ll be eating this meat later in the bowls) Continue simmering for another 1 1/2 hours. Strain broth and return the broth to the pot. Taste broth and adjust seasoning - this is a crucial step. If the broth\'s flavor doesn\'t quite shine yet, add 2 teaspoons more of fish sauce, large pinch of salt and a small nugget of rock sugar (or 1 teaspoon of regular sugar). Keep doing this until the broth tastes perfect. Prepare noodles & meat: Slice your flank/london broil/sirloin as thin as possible - try freezing for 15 minutes prior to slicing to make it easier. Remember the cooked beef meat that was part of your broth? Cut or shred the meat and set aside. Arrange all other ingredients on a platter for the table. Your guests will "assemble" their own bowls. Follow the directions on your package of noodles - there are many different sizes and widths of rice noodles, so make sure you read the directions. For some fresh rice noodles, just a quick 5 second blanch in hot water is all that\'s needed. The package that I purchased (above) - needed about 45 seconds in boiling water. Ladling: Bring your broth back to a boil. Line up your soup bowls next to the stove. Fill each bowl with rice noodles, shredded cooked beef and raw meat slices. As soon as the broth comes back to a boil, ladle into each bowl. the hot broth will cook your raw beef slices. Serve immediately. Guests can garnish their own bowls as they wish.',
            self.harvester_class.instructions()
        )
