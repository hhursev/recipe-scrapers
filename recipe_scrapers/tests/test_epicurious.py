import os
import unittest

from recipe_scrapers.epicurious import Epicurious


class TestEpicurious(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
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

    def test_yields(self):
        self.assertEqual(
            0,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertCountEqual(
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

    def test_ratings(self):
        return self.assertGreaterEqual(self.harvester_class.ratings(), 0.99)

    def test_reviews(self):
        self.assertCountEqual(
            "This was yummy, the tofu especially.  The sauce for the tofu really made the dish.  In light of that, I'd like to try this again with rice noodles instead of ramen and chicken instead of tofu.  I didn't really dig the fresh ramen as much as I thought I would (too eggy).  I'm not sure chicken will work quite so well as the tofu but it's worth a shot. lisamichellek from Seattle, WA",
            self.harvester_class.reviews()[0]['review_text'])

        self.assertEqual(self.harvester_class.reviews()[0]['rating'], 4)
