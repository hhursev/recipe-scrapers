import os
import unittest

from recipe_scrapers.epicurious import Epicurious


class TestEpicurious(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'epicurious.testhtml'
        )) as file_opened:
            self.harvester_class = Epicurious(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'epicurious.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Ramen Noodle Bowl with Escarole and Spicy Tofu Crumbles '
        )

    def test_total_time(self):
        self.assertEqual(
            0,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                '2 (5.5-ounce) servings fresh or dried ramen noodles',
                '4 cups torn escarole',
                '3 tablespoons Roasted Garlic Chili Sauce',
                'Kosher salt',
                '4 Pickled Scallions',
                'Spicy Tofu Crumbles, thinly sliced radish, and chopped peanuts (for serving)'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Cook noodles according to package directions. During the last minute of cooking, add escarole. Drain and rinse under cold water.\nToss noodles, escarole, and chili sauce in a large bowl until coated; season with salt. Divide noodles between bowls. Slice scallions into 1" pieces and place on top of noodles along with some tofu crumbles, radishes, and peanuts.',
            self.harvester_class.instructions()
        )
