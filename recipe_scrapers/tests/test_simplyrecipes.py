import os
import unittest

from recipe_scrapers.simplyrecipes import SimplyRecipes


class TestSimplyRecipesScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'simpyrecipes.html'
        )) as file_opened:
            self.harvester_class = SimplyRecipes(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'simplyrecipes.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Cheesy Bread'
        )

    def test_total_time(self):
        self.assertEqual(
            20,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                '4 oz shredded Mozzarella cheese (1 cup)',
                '8 oz shredded sharp cheddar cheese (about 2 cups)',
                '1/4 to 1/2 cup chopped green onion (to taste)',
                '1/4 cup mayonnaise',
                '1 Tbsp sour cream (optional)',
                '1-2 cloves garlic, minced',
                '1/2 stick unsalted butter (1/4 cup, 2 ounces), softened to the point of being slightly melted',
                '1 loaf of French or Italian bread (I used Ciabatta)'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            '1 In a large bowl, mix together the cheeses and the green onion. Stir in the mayonnaise and sour cream. In a separate small bowl blend the butter and garlic until smooth. Add the butter mixture to the cheese mixture.\n\n2 Preheat broiler. Slice loaf of bread in half horizontally, lay crust side down on a foil-lined baking sheet. Spread cheese mixture over the bread.\n\n3 Place under the broiler until nicely browned, about 3 to 5 minutes.\n\n4 Remove from broiler and let sit for 5 minutes until cool enough to handle. Slice the bread with a bread knife. Serve.\nVariations:\nTry mixing in other ingredients with the topping mixture, such as chopped black olives, chopped canned artichoke hearts, minced shrimp, or crab meat.',
            self.harvester_class.instructions()
        )
