import os
import unittest

from recipe_scrapers.yummly import Yummly


class TestYummlyScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'yummly.testhtml'
        )) as file_opened:
            self.harvester_class = Yummly(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'yummly.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Carrot Milk shake'
        )

    def test_total_time(self):
        self.assertEqual(
            30,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        self.assertEqual(
            "4 serving(s)",
            self.harvester_class.yields()
        )

    def test_ingredients(self):
        self.assertSetEqual(
            set([
                '3 teaspoons sugar',
                '4 cashew',
                '1 1/2 cups milk',
                '100 grams carrot',
                '1 cardamom'
            ]),
            set(self.harvester_class.ingredients())
        )

    def test_instructions(self):
        return self.assertEqual(
            '',
            self.harvester_class.instructions()
        )
