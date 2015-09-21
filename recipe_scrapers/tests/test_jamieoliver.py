import os
import unittest

from recipe_scrapers.jamieoliver import JamieOliver


class TestJamieOliverScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'jamieoliver.html'
        )) as file_opened:
            self.harvester_class = JamieOliver(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'jamieoliver.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Meatballs & pasta'
        )

    def test_total_time(self):
        self.assertEqual(
            45,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                '4 sprigs fresh rosemary',
                "12 Jacob's cream crackers",
                '2 heaped teaspoons Dijon mustard',
                '500 g quality minced beef, higher-welfare pork, or a mixture of the two',
                '1 heaped tablespoon dried oregano',
                '1 large free-range egg',
                'sea salt',
                'freshly ground black pepper',
                'olive oil',
                '1 bunch fresh basil',
                '1 medium onion',
                '2 cloves garlic',
                '½ fresh or dried red chilli',
                '2x400 g tinned chopped tomatoes',
                '2 tablespoons balsamic vinegar',
                '400 g dried spaghetti or penne',
                'Parmesan cheese, for grating'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        self.assertEqual(
            "Meatballs are fantastic! They're perfect like this, with a one-minute homemade tomato sauce and spaghetti, but you could also try polenta or simple chunks of fresh crust bread. I like to make meatballs with a mixture of beef and pork, as I think it gives a really wonderful flavour and texture. Pick the rosemary leaves off the woody stalks and finely chop them. Wrap the crackers in a tea towel and smash up until fine, breaking up any big bits with your hands. Add to a mixing bowl with the mustard, minced meat, chopped rosemary and oregano. Crack in the egg and add a good pinch of salt and pepper. With clean hands scrunch and mix up well. Divide into 4 large balls. With wet hands, divide each ball into 6 and roll into little meatballs – you should end up with 24. Drizzle them with olive oil and jiggle them about so they all get coated. Put them on a plate, cover and place in the fridge until needed. Pick the basil leaves, keeping any smaller ones to one side for later. Peel and finely chop the onion and the garlic. Finely slice the chilli. Put a large pan of salted water on to boil. Next, heat a large frying pan on a medium heat and add 2 lugs of olive oil. Add your onion to the frying pan and stir for around 7 minutes or until softened and lightly golden. Then add your garlic and chilli, and as soon as they start to get some colour add the large basil leaves. Add the tomatoes and the balsamic vinegar. Bring to the boil and season to taste. Meanwhile, heat another large frying pan and add a lug of olive oil and your meatballs. Stir them around and cook for 8–10 minutes until golden (check they're cooked by opening one up – there should be no sign of pink). Add the meatballs to the sauce and simmer until the pasta is ready, then remove from the heat. Add the pasta to the boiling water and cook according to the packet instructions. Saving some of the cooking water, drain the pasta in a colander. Return the pasta to the pan. Spoon half the tomato sauce into the pasta, adding a little splash of your reserved water to loosen. Serve on a large platter, or in separate bowls, with the rest of the sauce and meatballs on top. Sprinkle over the small basil leaves and some grated Parmesan.",
            self.harvester_class.instructions()
        )
