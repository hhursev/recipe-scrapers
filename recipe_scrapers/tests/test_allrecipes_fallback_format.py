import os
import unittest

from recipe_scrapers.allrecipes import AllRecipes


class TestAllRecipesFallbackFormatScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'allrecipes_fallback_format.testhtml'
        )) as file_opened:
            self.harvester_class = AllRecipes(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'allrecipes.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Smothered Chicken Breasts'
        )

    def test_total_time(self):
        self.assertEqual(
            35,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            'https://images.media-allrecipes.com/userphotos/4488475.jpg',
            self.harvester_class.image()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '4 (6 ounce) skinless, boneless chicken breast halves',
                '¼ teaspoon salt',
                '¼ teaspoon lemon pepper seasoning',
                '1 tablespoon vegetable oil',
                '8 strips bacon',
                '1 onion, sliced',
                '¼ cup packed brown sugar',
                '½ cup shredded Colby-Monterey Jack cheese',
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Sprinkle chicken with salt and lemon-pepper.\nHeat oil in a large skillet over medium heat; cook the chicken breasts in hot oil until no longer pink in the center and the juices run clear, 13 to 15 minutes. An instant-read thermometer inserted into the center should read at least 165 degrees F (74 degrees C). Remove and keep warm.\nPlace bacon in large skillet and cook over medium-high heat, turning occasionally, until evenly browned, about 10 minutes. Drain bacon slices on paper towels; reserve 2 tablespoons drippings. Cook and stir onion and brown sugar in reserved drippings until onion is golden, about 5 minutes.\nPlace two bacon strips on each chicken breast half; top with caramelized onions and sprinkle with Colby-Monterey Jack cheese.',
            self.harvester_class.instructions()
        )

    def test_ratings(self):
        self.assertEqual(
            4.70,
            self.harvester_class.ratings()
        )
