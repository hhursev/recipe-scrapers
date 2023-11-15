from recipe_scrapers.hellofresh import HelloFresh
from tests import ScraperTest


class TestHelloFreshScraper(ScraperTest):
    scraper_class = HelloFresh

    def test_host(self):
        self.assertEqual("hellofresh.com", self.harvester_class.host())

    def test_host_domain(self):
        self.assertEqual("hellofresh.co.uk", self.harvester_class.host(domain="co.uk"))

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.hellofresh.co.uk/recipes/thai-style-pork-rice-bowl-5feb63f527c560013957dd24",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            "Thai Style Pork Rice Bowl with Green Beans, Coriander and Rice",
            self.harvester_class.title(),
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "HelloFresh")

    def test_total_time(self):
        self.assertEqual(50, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 unit(s) Echalion Shallot",
                "150 grams Green Beans",
                "150 grams Basmati Rice",
                "25 milliliter(s) Soy Sauce",
                "2 unit(s) Garlic Clove",
                "½ unit(s) Red Chilli",
                "2 unit(s) Spring Onion",
                "240 grams Pork Mince",
                "50 grams Ketjap Manis",
                "300 milliliter(s) Water for the Rice",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        expected_instructions = "\n".join(
            [
                "Pour the water for the rice (see ingredients for amount) into a saucepan and bring to the boil. When boiling, add 0.25 tsp of salt, stir in the rice, lower the heat to medium and pop a lid on the pan. Leave to cook for 10 mins, then remove the pan from the heat (still covered) and leave to the side for another 10 mins or until ready to serve (the rice will continue to cook in its own steam).",
                "Meanwhile, halve, peel and chop the shallot into small pieces. Peel and grate the garlic (or use a garlic press). Halve the red chilli lengthways, de-seed and finely chop. Trim the spring onion and thinly slice. Trim the green beans then chop into thirds.",
                "Heat a splash of oil in a frying pan on high heat. Once hot, add the green beans and stir-fry until tender, about 5-6 mins. When cooked, transfer to a plate.",
                "Keep the pan on high heat and add another splash of oil if the pan is dry. Add the pork mince and stir-fry until browned, 6-8 mins, breaking it up with a wooden spoon as it cooks. When the pork is cooked, drain off any excess oil, add the shallot, garlic, spring onion and as much chilli as you dare. Cook until the veggies are softened, another 2-3 mins.",
                "Return the green beans to the pan. Add the ketjap manis and soy sauce and stir everything together. Tip: If the mixture is a little dry, add a splash of water.",
                "Remove the pan from the heat. Fluff up the rice with a fork and share between your bowls. Top with the pork stir-fry and get stuck in. Super tasty! Or, as they say in Thailand, Aloy mak!",
            ]
        )

        self.assertEqual(
            expected_instructions,
            self.harvester_class.instructions(),
        )

    def test_nutrients(self):
        self.assertEqual(
            {"servingSize": "368"},
            self.harvester_class.nutrients(),
        )

    def test_cuisine(self):
        self.assertEqual("Thai", self.harvester_class.cuisine())

    def test_category(self):
        self.assertEqual("main course", self.harvester_class.category())
