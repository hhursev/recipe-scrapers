import os
import unittest

from recipe_scrapers.bonappetit import BonAppetit


class TestBonAppetitScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'bonappetit.html'
        )) as file_opened:
            self.harvester_class = BonAppetit(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'bonappetit.com',
            self.harvester_class.host()
        )

    def test_publisher_site(self):
        self.assertEqual(
            'http://bonappetit.com/',
            self.harvester_class.publisher_site()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Red Wine-Braised Short Ribs'
        )

    def test_total_time(self):
        self.assertEqual(
            0,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                '5 pounds bone-in beef short ribs, cut crosswise into 2-inch pieces',
                'Kosher salt and freshly ground black pepper',
                '3 tablespoons vegetable oil',
                '3 medium onions, chopped',
                '3 medium carrots, peeled, chopped',
                '2 celery stalks, chopped',
                '3 tablespoons all-purpose flour',
                '1 tablespoon tomato paste',
                '1 750 ml bottle dry red wine (preferably Cabernet Sauvignon)',
                '10 sprigs flat-leaf parsley',
                '8 sprigs thyme',
                '4 sprigs oregano',
                '2 sprigs rosemary',
                '2 fresh or dried bay leaves',
                '1 head of garlic, halved crosswise',
                '4 cups low-salt beef stock'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Preheat oven to \n350°. Season short ribs with salt and pepper. Heat oil in a large Dutch \noven over medium-high. Working in 2 batches, brown short ribs on all \nsides, about 8 minutes per batch. Transfer short ribs to a plate. Pour \noff all but 3 Tbsp. drippings from pot.\nAdd onions, \ncarrots, and celery to pot and cook over medium-high heat, stirring \noften, until onions are browned, about 5 minutes. Add flour and tomato \npaste; cook, stirring constantly, until well combined and deep red, 2-3 \nminutes. Stir in wine, then add short ribs with any accumulated juices. \nBring to a boil; lower heat to medium and simmer until wine is reduced \nby half, about 25 minutes. Add all herbs to pot along with garlic. Stir \nin stock. Bring to a boil, cover, and transfer to oven.\nCook until short\n ribs are tender, 2–2½ hours. Transfer short ribs to a platter. Strain \nsauce from pot into a measuring cup. Spoon fat from surface of sauce and\n discard; season sauce to taste with salt and pepper. Serve in shallow \nbowls over mashed potatoes with sauce spooned over.',
            self.harvester_class.instructions()
        )
