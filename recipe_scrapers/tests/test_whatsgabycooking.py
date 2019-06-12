import os
import unittest

from recipe_scrapers.whatsgabycooking import WhatsGabyCooking


class TestWhatsGabyCookingScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'whatsgabycooking.testhtml'
        )) as file_opened:
            self.harvester_class = WhatsGabyCooking(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'whatsgabycooking.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Strawberry Basil Lemonade'
        )

    def test_total_time(self):
        self.assertEqual(
            0,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '10 lemons, juiced, about 1 cup of fresh lemon juice',
                '3/4 cup super fine sugar',
                '4 cups water',
                '8-10 strawberries, tops removed',
                '1/3 cup fresh basil',
                '1/2 cup gin or vodka (optional)'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Juice the lemons and transfer the juice into a large pitcher.\nAdd the sugar and the water and stir to combine and dissolve the sugar.\nAdd the strawberries and basil.\nUsing an immersion blender, blend the mixture for about 20 seconds just until the mixture turns pink and the basil is finely chopped.\nAdd alcohol if desired. Serve over crushed ice and enjoy!',
            self.harvester_class.instructions()
        )
