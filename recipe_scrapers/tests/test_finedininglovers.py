import os
import unittest

from recipe_scrapers.finedininglovers import FineDiningLovers


class TestFineDiningLoversScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'finedininglovers.testhtml'
        )) as file_opened:
            self.harvester_class = FineDiningLovers(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'finedininglovers.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Zucchini Raw Vegan Lasagna'
        )

    def test_total_time(self):
        self.assertEqual(
            50,
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
                'Zucchini',
                'Basil',
                'Pine nuts',
                'Extra-virgin olive oil',
                'Yeast flakes',
                'Garlic',
                'Salt',
                'Tomato',
                'Sundried tomato',
                'Extra-virgin olive oil',
                'Salt',
                'Pepper',
                'Brown sugar',
                'Dried oregano',
                'Macadamia nuts',
                'Yeast flakes',
                'Salt',
                'Lime',
                'Water'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'For the macadamia cheese Pour all ingredients in a blender and mix until a thick cream. Set aside. For the tomato cream Pour all ingredients into a blender and mix until creamy. Set aside. For the basil pesto Pour all ingredients into a blender and mix until creamy. Set aside. Wash zucchini and cut them into very thin slices. Make the raw vegan lasagna alternating a layer of zucchini, a layer of macadamia cheese, a layer of zucchini, a layer of tomato sauce, a layer of zucchini, a layer of basil pesto. Keep the lasagna in the fridge and serve decorated with fresh basil and pine nuts.',
            self.harvester_class.instructions()
        )
