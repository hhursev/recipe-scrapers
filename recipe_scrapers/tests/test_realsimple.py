import os
import unittest

from recipe_scrapers.realsimple import RealSimple


class TestRealSimpleScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'realsimple.html'
        )) as file_opened:
            self.harvester_class = RealSimple(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'realsimple.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Pan-Roasted Chicken With Lemon-Garlic Green Beans'
        )

    def test_total_time(self):
        self.assertEqual(
            75,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                'tablespoons olive oil',
                '2 lemons, 1 thinly sliced, 1 juiced',
                '4 cloves garlic, minced',
                'teaspoon kosher salt',
                'teaspoon freshly ground black pepper',
                'pound trimmed green beans',
                '8 small red potatoes, quartered',
                '4 chicken breasts (bones left in, with skin, about 3 1/4 pounds)'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        self.assertEqual(
            'Preheat oven to 450°F. Coat a large baking dish or cast-iron skillet with 1 tablespoon of the olive oil. Arrange the lemon slices in a single layer in the bottom of the dish or skillet.\nIn a large bowl, combine the remaining oil, lemon juice, garlic, salt, and pepper; add the green beans and toss to coat. Using a slotted spoon or tongs, remove the green beans and arrange them on top of the lemon slices. Add the potatoes to the same olive-oil mixture and toss to coat. Using a slotted spoon or tongs, arrange the potatoes along the inside edge of the dish or skillet on top of the green beans. Place the chicken in the same bowl with the olive-oil mixture and coat thoroughly. Place the chicken, skin-side up, in the dish or skillet. Pour any of the remaining olive-oil mixture over the chicken.\nRoast for 50 minutes. Remove the chicken from the dish or skillet. Place the beans and potatoes back in oven for 10 minutes more or until the potatoes are tender. Place a chicken breast on each of 4 serving plates; divide the green beans and potatoes equally. Serve warm.',
            self.harvester_class.instructions()
        )
