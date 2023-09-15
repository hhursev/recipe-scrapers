from recipe_scrapers.nibbledish import NibbleDish
from tests import ScraperTest


class TestNibbleDishScraper(ScraperTest):

    scraper_class = NibbleDish

    def test_host(self):
        self.assertEqual("nibbledish.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Soon dubu Chigae")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "NibbleDish Contributor")

    def test_ingredients(self):
        self.assertEqual(
            [
                "3 tablespoons of red pepper powder",
                "2 tablespoons sesame oil",
                "2 small onions, chopped.",
                "3 cloves of garlic, minced.",
                "Shrimp, peeled, deveined, as much as you like.",
                "Red pepper flakes",
                "1 case of silken tofu, chopped into little cubes.",
                "1 beef bouillon cube",
                "2 1/2 cups of water",
                "2 tsp fish sauce",
                "A bunch of green onions/scallions",
                "Mussels, as much as you like, removed from shell",
                "Mushrooms, any kind you like. (Shiitake and enoki mushrooms recommended but I only had button.)",
                "1 tablespoon of gochuchang",
                "1 egg.",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "In your pot, heat up sesame oil and add onions and garlic. Fry them till cooked.",
                    "Add the shrimp and mussels next. Add the red pepper powder and fry.",
                    "Put the water in the pot, let it boil and add the beef bouillon cube. Add fish sauce.",
                    "Add the mushrooms, tofu and gochuchang.",
                    "Add the egg and with a fork, whisk it around to make strands.",
                    "Add scallions on top and serve on top of rice.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_image(self):
        self.assertEqual(
            "http://media.nibbledish.com/wp-content/legacy-recipe-images/b2d1d675269ccfed2f246a99b3c04cbc.jpg",
            self.harvester_class.image(),
        )
