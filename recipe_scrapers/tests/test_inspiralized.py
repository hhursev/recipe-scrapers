import os
import unittest

from recipe_scrapers.inspiralized import Inspiralized


class TestInspiralizedScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'inspiralized.testhtml'
        )) as file_opened:
            self.harvester_class = Inspiralized(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'inspiralized.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Spiralized Pasta Carbonara, Two Ways"
        )

    def test_total_time(self):
        self.assertEqual(
            20,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        self.assertEqual(
            "2 serving(s)",
            self.harvester_class.yields()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '1 tbsp olive oil',
                '1 large garlic clove, minced',
                '1/4 tsp red pepper flakes',
                '1/4 cup diced red onion',
                '1/2 cup cubed pancetta',
                '2 whole large eggs',
                '3 medium zucchinis, Blade C',
                'pepper, to taste',
                '1/3 cup grated parmesan cheese'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        self.assertEqual(
            'Place a large skillet over medium heat and add in the olive oil. Once the oil heats, add in the garlic and red pepper flakes. Cook the garlic for 30 seconds, add in the onion and cook for 2-3 minutes or until the onion softens. Then, add in the pancetta cubes. Cook, stirring often, until cooked through, about 5 minutes.\nOnce the pancetta is done cooking, add a medium skillet over medium heat and crack over two eggs. Let them cook until the egg whites set.\nWhile your eggs are cooking, add the zucchini noodles to the pancetta, season with pepper and toss to combine. Stirring frequently, let cook for about 2-3 minutes and then add in the parmesan cheese. Toss the noodles with the cheese and then plate into bowls. Top each bowl with one of the eggs. Enjoy!',
            self.harvester_class.instructions()
        )
