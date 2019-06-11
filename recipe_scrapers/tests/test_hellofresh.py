import os
import unittest

from recipe_scrapers.hellofresh import HelloFresh


class TestHelloFreshScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'hellofresh.testhtml'
        )) as file_opened:
            self.harvester_class = HelloFresh(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'hellofresh.com',
            self.harvester_class.host()
        )

    def test_host_domain(self):
        self.assertEqual(
            'hellofresh.co.uk',
            self.harvester_class.host(domain='co.uk')
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

    def test_yields(self):
        self.assertEqual(
            0,
            self.harvester_class.yields()
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                '150 grams Basmati Rice',
                '1 unit(s) Carrot',
                '2 unit(s) Spring Onion',
                '1 bag(s) Salted Peanuts',
                '1 unit(s) Lime',
                '2 unit(s) Pork Steak',
                '1 sachet Ginger puree',
                '1 sachet Ketjap Manis',
                '1 sachet Soy Sauce',
                '1 sachet Honey'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        self.assertEqual(
            """1) Fill and boil your kettle. Pour the boiling water from your kettle into a large saucepan and bring back to the boil on high heat. When boiling, add the rice and cook for 8-10 mins, then drain in a sieve and set aside.\n2) Meanwhile, trim the carrot (no need to peel) then grate on a coarse grater. Trim the spring onion then finely slice. Roughly chop the peanuts. Roughly chop the coriander (stalks and all). Zest the lime then chop into wedges. Peel and grate the garlic (or use a garlic press). Chop the pork into 2cm chunks. IMPORTANT: Remember to wash your hands and equipment after handling raw meat.\n3) In a small bowl, stir together the garlic, easy ginger, ketjap manis, soy sauce, honey and the juice of half the lime. Set aside.\n4) Heat a splash of oil in a large frying pan on high heat. When hot, add the pork and stir- fry untill browned all over, 4-5 mins.\n5) Lower the heat to medium then pour the sauce into the pan. Cook, coating the pork in the sticky sauce, for 2-3 mins. iIMPORTANT: The pork is cooked when it is no longer pink in the middle. Meanwhile, in a large bowl gently toss together the cooked rice, lime zest, carrot, coriander, half the spring onion and half the peanuts. Season to taste with salt and pepperif needed.\n6) Serve the sticky pork on top of the veggie rice. Finish by pouring any sauce left in the pan over the top and scattering on the remaining peanuts and spring onion. Top with the remaining lime wedges. Enjoy!""",
            self.harvester_class.instructions()
        )
