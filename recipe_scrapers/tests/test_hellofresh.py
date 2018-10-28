import os
import unittest

from recipe_scrapers.hellofresh import HelloFresh


class TestHelloFreshScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'hellofresh.testhtml'
        )) as file_opened:
            self.harvester_class = HelloFresh(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'hellofresh.co.uk',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            'Thai Style Pork Stir-Fry',
            self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(
            20,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                '150 grams Basmati Rice',
                '1 unit(s) Carrot',
                '2 unit(s) Spring Onion',
                '1 bag(s) Salted Peanuts (ContainsPeanuts)',
                '1 unit(s) Lime', '2 unit(s) Pork Steak',
                '1 sachet Ginger puree',
                '1 sachet Ketjap Manis (ContainsGluten,Soya)',
                '1 sachet Soy Sauce (ContainsGluten,Soya)',
                '1 sachet Honey'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        self.assertEqual(
            """a) Pour the boiling water into a large saucepan and bring back to the boil on high heat. b) When boiling, add the rice and cook for 8-10 mins, then drain in a sieve and set aside.\na) Meanwhile, trim the carrot then grate on the coarse side of your grater (no need to peel). b) Trim the spring onion then finely slice. Roughly chop the peanuts. Zest the lime then chop into wedges. c) Chop the pork into 2cm chunks. iIMPORTANT: Remember to wash your hands after handling raw meat.\na) In a small bowl, stir together the easy ginger, ketjap manis, soy sauce, honey and the juice of half the lime. Set aside.\na) Heat a splash of oil in a large frying pan on high heat. b) When hot, add the pork and stir-fry until browned all over, 4-5 mins.\na) Lower the heat to medium then pour the sauce into the pan. b) Cook, coating the pork in the sticky sauce, for 2-3 mins.iIMPORTANT: The pork is cooked when it is no longer pink in the middle. c) Meanwhile, in a large bowl gently toss together the rice, lime zest, carrot, half the spring onion and half the peanuts. Season to taste with salt and pepper if needed.\na) Serve the sticky pork on top of the veggie rice. b) Finish by pouring any sauce left in the pan over the top and scattering over the remaining peanuts and spring onion. c) Top with the remaining lime wedges. ENJOY!""",
            self.harvester_class.instructions()
        )
