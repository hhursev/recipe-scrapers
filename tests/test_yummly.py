from recipe_scrapers.yummly import Yummly
from tests import ScraperTest


class TestYummlyScraper(ScraperTest):

    scraper_class = Yummly

    def test_host(self):
        self.assertEqual("yummly.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.yummly.com/recipe/Easy-White-Cheese-_-Garlic-Pizzas-9351327",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Easy White Cheese & Garlic Pizzas"
        )

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "4 pieces naan",
                "2 tablespoons extra-virgin olive oil",
                "3 cloves garlic",
                "1 cup shredded mozzarella cheese (or shredded pizza blend cheese, 1 cup is 4 oz.)",
                "4 ounces ricotta cheese (4 oz. is 1 scant cup)",
                "1 1/2 teaspoons Italian seasoning",
                "2 tablespoons shaved Parmesan cheese (for serving)",
                "basil leaves (for garnish, optional)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Preheat oven to 425°F.",
                    "Line a baking sheet with parchment paper.",
                    "Arrange the naan on the baking sheet. Drizzle an equal amount of olive oil over the surface of each piece.",
                ]
            ),
            self.harvester_class.instructions(),
        )
