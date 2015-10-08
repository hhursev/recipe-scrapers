import os
import unittest

from recipe_scrapers.closetcooking import ClosetCooking


class TestClosetCooking(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'closetcooking.html'
        )) as file_opened:
            self.harvester_class = ClosetCooking(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'closetcooking.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Bacon Wrapped Jalapeno Popper Stuffed Chicken'
        )

    def test_total_time(self):
        self.assertEqual(
            40,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                '4 (6 ounce) chicken breasts, pounded thin',
                'salt and pepper to taste',
                '4 jalapenos, diced',
                '4 ounces cream cheese, room temperature',
                '1 cup cheddar cheese, shredded',
                '8 slices bacon'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Lay the chicken flat, season both sides with salt and pepper, place 1/4 of the mixture of the jalapenos, cream cheese and cheddar on the chicken and roll them up.\nWrap each chicken breast up in 2 slices of bacon and place them in a baking dish on a wire rack.\nBake in a pre-heated 400F/200C oven until cooked, about 25-35 minutes.',
            self.harvester_class.instructions()
        )
