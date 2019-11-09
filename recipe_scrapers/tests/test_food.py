import os
import unittest

from recipe_scrapers.food import Food


class TestFoodScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'food.testhtml'
        )) as file_opened:
            self.harvester_class = Food(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'food.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Chicken Noodle Soup With Carrots, Parsnips and Dill'
        )

    def test_total_time(self):
        self.assertEqual(
            45,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        self.assertEqual(
            "4 serving(s)",
            self.harvester_class.yields()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '8 cups low sodium chicken broth',
                '1 onion, chopped',
                '4 carrots, halved lengthwise and cut crosswise into 1-inch pieces',
                '4 parsnips, halved lengthwise and cut crosswise into 1-inch pieces',
                '1 1⁄2 teaspoons salt',
                '1⁄4 teaspoon fresh ground black pepper',
                '1 split chicken breast',
                '1 cup noodles (about 2 ounces)',
                '1⁄4 cup chopped fresh dill',
                '1⁄4 cup chopped fresh parsley'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'In a large pot, combine the broth, onion, carrots, parsnips, salt, and pepper and bring to a simmer. Add the chicken breasts to the pot and simmer until jfor about 20 minutes, until cooked. Remove the chicken and let rest.  When cool enough to handle, remove skin and bones and chop or shred intobite-size pieces.\nWhile chicken is cooling, bring the soup back to a simmer and stir the noodles into the soup. Simmer until the vegetables are tender and the noodles are done, about 5 minutes. Return the chicken pieces to the pot and then stir in the dill and the parsley.',
            self.harvester_class.instructions()
        )

    def test_ratings(self):
        self.assertEqual(
            5.0,
            self.harvester_class.ratings()
        )
