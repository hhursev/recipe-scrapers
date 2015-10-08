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
            'epicurious.html'
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
            'Poached Eggs in Tomato Sauce with Chickpeas and Feta'
        )

    def test_total_time(self):
        self.assertEqual(
            35,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                '1/4 cup olive oil',
                '1 medium onion, finely chopped',
                '4 garlic cloves, coarsely chopped',
                '2 jalapeños, seeded, finely chopped',
                '1 15-ounce can chickpeas, drained',
                '2 teaspoons Hungarian sweet paprika',
                '1 teaspoon ground cumin',
                '1 28-ounce can whole peeled tomatoes, crushed by hand, juices reserved',
                'Kosher salt and freshly ground black pepper',
                '1 cup coarsely crumbled feta',
                '8 large eggs',
                '1 tablespoon chopped flat-leaf parsley',
                '1 tablespoon chopped fresh cilantro',
                'Warm pita bread'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Preheat oven to 425°F. Heat oil in a large ovenproof skillet over medium-high heat. Add onion, garlic, and jalapeños; cook, stirring occasionally, until onion is soft, about 8 minutes. Add chickpeas, paprika, and cumin and cook for 2 minutes longer.\nAdd crushed tomatoes and their juices. Bring to a boil, reduce heat to medium-low, and simmer, stirring occasionally, until sauce thickens slightly, about 15 minutes. Season to taste with salt and pepper. Sprinkle feta evenly over sauce. Crack eggs one at a time and place over sauce, spacing evenly apart. Transfer skillet to oven and bake until whites are just set but yolks are still runny, 5-8 minutes. Garnish with parsley and cilantro. Serve with pita for dipping.\nPer serving: 358 calories, 22 g fat, 22 g carbohydrates\nNutritional analysis provided by Bon Appétit',
            self.harvester_class.instructions()
        )
