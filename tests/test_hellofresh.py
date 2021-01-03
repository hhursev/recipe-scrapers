from tests import ScraperTest

from recipe_scrapers.hellofresh import HelloFresh


class TestHelloFreshScraper(ScraperTest):

    scraper_class = HelloFresh

    def test_host(self):
        self.assertEqual("hellofresh.com", self.harvester_class.host())

    def test_host_domain(self):
        self.assertEqual("hellofresh.co.uk", self.harvester_class.host(domain="co.uk"))

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.hellofresh.co.uk/recipes/thai-style-pork-stir-fry-wk-49-5a01c742450cfa39e02c5642",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Thai Style Pork Stir-Fry", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "150 grams Basmati Rice",
                "2 unit(s) Spring Onion",
                "1 pack(s) Green Beans",
                "300 grams Pork Mince",
                "3 tbsp Ketjap Manis",
                "1.5 tbsp Soy Sauce",
                "½ bunch(es) Fresh Thai Basil",
                "2 clove Garlic",
                "Salted Peanuts",
                "300 milliliter(s) Water",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """1) a) Pour the boiling water into a large saucepan and bring back to the boil on high heat. b) When boiling, add the rice and cook for 8-10 mins, then drain in a sieve and set aside.\n2) a) Meanwhile, trim the carrot then grate on the coarse side of your grater (no need to peel). b) Trim the spring onion then finely slice. Roughly chop the peanuts. Zest the lime then chop into wedges. c) Chop the pork into 2cm chunks. iIMPORTANT: Remember to wash your hands after handling raw meat.\n3) a) In a small bowl, stir together the easy ginger, ketjap manis, soy sauce, honey and the juice of half the lime. Set aside.\n4) a) Heat a splash of oil in a large frying pan on high heat. b) When hot, add the pork and stir-fry until browned all over, 4-5 mins.\n5) a) Lower the heat to medium then pour the sauce into the pan. b) Cook, coating the pork in the sticky sauce, for 2-3 mins.iIMPORTANT: The pork is cooked when it is no longer pink in the middle. c) Meanwhile, in a large bowl gently toss together the rice, lime zest, carrot, half the spring onion and half the peanuts. Season to taste with salt and pepper if needed.\n6) a) Serve the sticky pork on top of the veggie rice. b) Finish by pouring any sauce left in the pan over the top and scattering over the remaining peanuts and spring onion. c) Top with the remaining lime wedges. ENJOY!""",
            self.harvester_class.instructions(),
        )
