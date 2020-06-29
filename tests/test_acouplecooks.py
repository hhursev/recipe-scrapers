import os
import unittest

from recipe_scrapers.acouplecooks import ACoupleCooks

# test recipe's URL
# https://www.acouplecooks.com/garlic-butter-shrimp/

class TestPrzepisyScraper(unittest.TestCase):
     def setUp(self):
         # tests are run from tests.py
         with open(os.path.join(
             os.path.dirname(os.path.realpath(__file__)),
             'test_data',
             'acouplecooks.testhtml'
         )) as file_opened:
             self.harvester_class = ACoupleCooks(file_opened, test=True)

     def test_host(self):
         self.assertEqual(
             'acouplecooks.com',
             self.harvester_class.host()
         )

     def test_title(self):
         self.assertEqual(
             'Garlic Butter Shrimp (Fast & Easy Dinner!)',
             self.harvester_class.title()
         )

     def test_total_time(self):
         self.assertEqual(
             3,
             self.harvester_class.total_time()
         )

     def test_yields(self):
         self.assertEqual(
             '4 serving(s)',
             self.harvester_class.yields()
         )

     def test_ingredients(self):
         self.assertEqual(
             [
                 '1 pound large shrimp, deveined (peeled or unpeeled)',
                 '3 garlic cloves',
                 '1/2 teaspoon kosher salt',
                 '3 tablespoons butter',
                 '2 lemon wedges',
                 'Fresh cilantro or parsley, for garnish'
             ],
             self.harvester_class.ingredients()
         )

     def test_instructions(self):
        self.assertEqual(
             'If frozen, thaw the shrimp (see the notes above).\nMince the garlic.\nPat the shrimp dry. In a medium bowl, mix the shrimp with the garlic and salt.\nIn a large skillet, heat the butter on medium high heat. Cook the shrimp for 1 to 2 minutes per side until opaque and cooked through, turning them with tongs.\nSpritz with juice of the lemon wedges and serve immediately.',
             self.harvester_class.instructions()
        )


