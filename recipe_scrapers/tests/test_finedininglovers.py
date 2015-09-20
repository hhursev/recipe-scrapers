import os
import unittest

from recipe_scrapers.finedininglovers import FineDiningLovers


class TestFineDiningLoversScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'finedininglovers.html'
        )) as file_opened:
            self.harvester_class = FineDiningLovers(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'finedininglovers.com',
            self.harvester_class.host()
        )

    def test_publisher_site(self):
        self.assertEqual(
            'https://finedininglovers.com/',
            self.harvester_class.publisher_site()
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

    def test_ingredients(self):
        self.assertListEqual(
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
            'For the macadamia cheesePour all ingredients in a blender and mix until a thick cream. Set aside.For the tomato creamPour all ingredients into a blender and mix until creamy. Set aside.For the basil pestoPour all ingredients into a blender and mix until creamy. Set aside.Wash zucchini and cut them into very thin slices.Make theraw vegan lasagnaalternating a layer of \nzucchini, a layer of macadamia cheese, a layer of zucchini, a layer of \ntomato sauce, a layer of zucchini, a layer of basil pesto. Keep the \nlasagna in the fridge and serve decorated with fresh basil and pine \nnuts.',
            self.harvester_class.instructions()
        )
