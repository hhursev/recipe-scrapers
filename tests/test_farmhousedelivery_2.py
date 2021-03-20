from recipe_scrapers.farmhousedelivery import FarmhouseDelivery
from tests import ScraperTest


class TestFarmhouseDeliveryScraper(ScraperTest):

    scraper_class = FarmhouseDelivery

    def setUp(self):
        with open(
            "tests/test_data/{}_2.testhtml".format(self.scraper_class.__name__.lower()),
            encoding="utf-8",
        ) as testfile:
            self.harvester_class = self.scraper_class(testfile)

    def test_host(self):
        self.assertEqual("recipes.farmhousedelivery.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://recipes.farmhousedelivery.com/one-pan-crispy-rosemary-chicken-thighs-roasted-radishes/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            "One Pan Crispy Rosemary Chicken Thighs + Roasted Radishes",
            self.harvester_class.title(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1/2 lemon, juiced",
                "1/4 c olive oil",
                "1 tsp spicy mustard",
                "1 head of garlic, minced",
                "2 tsp pink Himalayan salt",
                "1 tsp black pepper",
                "4 sprigs fresh rosemary, de-stemmed",
                "4 bone-in chicken thighs (Find them here.)",
                "3 red potatoes, diced",
                "1 bunch radishes, quartered",
                "1 red onion, sliced",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "❶ Preheat your oven to 400°F.",
                    "❷ In a medium sized mixing bowl, whisk together olive oil, lemon juice, mustard, garlic, salt , pepper and rosemary.",
                    "❸ Layer potatoes, radishes and onions on a baking sheet. Lightly drizzle with the tinest bit of olive oil. The chicken thighs will drip fat for cooking, so we don’t want to overdo it with the oil.",
                    "❹ Pat chicken thighs dry and rub with seasoning mixture. Be sure to get in under the skin too.",
                    "❺ Place chicken thighs over your vegetable layer.",
                    "❻ Roast for 55 minutes, then broil for 3 minutes for an extra crisp factor! Enjoy!",
                    "– For more lifestyle tips and recipes from Rebecca, you can find her on Instagram at @xxrlilly",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_image(self):
        self.assertEqual(
            "http://recipes.farmhousedelivery.com/wp-content/uploads/2019/05/FHD-Chic-Thigh-Recipe-225x300.jpeg",
            self.harvester_class.image(),
        )
