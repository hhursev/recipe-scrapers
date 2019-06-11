import os
import unittest

from recipe_scrapers.simplyrecipes import SimplyRecipes


class TestSimplyRecipesScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'simpyrecipes.testhtml'
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
            'One-Pot Chicken and Rice Soup'
        )

    def test_total_time(self):
        self.assertEqual(
            45,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        # 6 to 8 servings (makes about 3 quarts), debatable it should be 8 servings.
        self.assertEqual(
            "8 item(s)",
            self.harvester_class.yields()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '2 bone-in chicken breasts, skin removed (1 to 1 1/2 pounds)',
                '1 cup long-grain white rice, like basmati',
                '2 celery ribs, diced small',
                '2 medium carrots, peeled and diced small',
                '1 onion, diced small',
                '2 cloves garlic, left whole',
                '1 teaspoon salt, plus more to taste (see Recipe Note)',
                '1/2 teaspoon ground black pepper',
                '2 quarts unsalted or low-sodium chicken stock',
                'Juice of 1/2 lemon (about 3 tablespoons)',
                'Chopped fresh parsley, for serving'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            '1 Assemble the soup and bring to a simmer: Combine the chicken, white rice, celery, carrots, onions, garlic, salt, and pepper in a large pot. Add the chicken stock and bring to a boil over high heat.\nOnce the soup is boiling, reduce the heat to keep the soup at a gentle simmer.\n\n2 Simmer for about 25 minutes: As the soup simmers, skim off any foam that collects on the surface with a spoon. Continue to simmer until the rice and vegetables are tender, about 25 minutes. Remove the soup from heat.\n3 Shred the chicken and make the garlic paste: Remove the chicken and garlic cloves using a slotted spoon or tongs. Transfer the chicken breasts to a bowl and shred with two forks. Discard the bones. Return the shredded chicken to the pot.\nSmash the garlic cloves into a paste against a cutting board using a fork or the flat of your knife. Stir the paste back into the soup.\n\n4 Season and serve: Stir the lemon juice into to the soup, and taste. The soup should taste rich, barely salty, and with just a hint of lemon. Add more salt or lemon juice as needed until it tastes good to you.\nDivide among bowls and sprinkle with some parsley for serving.\nLeftovers will keep for about a week refrigerated, or up to 3 months frozen.',
            self.harvester_class.instructions()
        )
