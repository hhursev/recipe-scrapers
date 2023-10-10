# mypy: allow-untyped-defs

from recipe_scrapers.foodnetwork import FoodNetwork
from tests import ScraperTest


class TestFoodNetworkScraper(ScraperTest):

    scraper_class = FoodNetwork

    def test_host(self):
        self.assertEqual("foodnetwork.co.uk", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://foodnetwork.co.uk/recipes/tuscan-mushrooms-5389",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Food Network UK", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Tuscan mushrooms", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://d2vsf1hynzxim7.cloudfront.net/production/media/21503/conversions/foodnetwork-image-9b081a76-feaf-4b63-baea-077714959bc7-default.webp",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "50g diced jarred roasted sweet red peppers",
            "50g diced pitted green olives",
            "30g grated Pecorino Romano",
            "2 spring onions, diced",
            "2 tbsp extra-virgin olive oil",
            "1/2 tsp salt",
            "1/4 tsp freshly ground black pepper",
            "450g white button mushrooms, cleaned and stemmed",
            "10g finely chopped fresh basil leaves",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        pass

    def test_multiple_instructions(self):
        pass

    def test_cuisine(self):
        self.assertEqual("Italian", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Stuff these mushrooms with roasted red peppers and olives.",
            self.harvester_class.description(),
        )
