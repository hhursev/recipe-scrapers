from recipe_scrapers.acouplecooks import ACoupleCooks
from tests import ScraperTest


# test recipe's URL
# https://www.acouplecooks.com/garlic-butter-shrimp/
class TestACoupleCooks(ScraperTest):

    scraper_class = ACoupleCooks

    def test_host(self):
        self.assertEqual("acouplecooks.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.acouplecooks.com/garlic-butter-shrimp/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            "Garlic Butter Shrimp (Fast & Easy Dinner!)", self.harvester_class.title()
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Sonja Overhiser")

    def test_total_time(self):
        self.assertEqual(8, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                {
                    "name": "large shrimp, deveined (peeled or unpeeled)",
                    "quantity": 1.0,
                    "unit": "pound sterling",
                },
                {"name": "garlic cloves", "quantity": 3.0, "unit": "dimensionless"},
                {"name": "kosher salt", "quantity": 0.5, "unit": "teaspoon"},
                {"name": "butter", "quantity": 3.0, "unit": "tablespoon"},
                {"name": "lemon wedges", "quantity": 2.0, "unit": "dimensionless"},
                {
                    "name": "Fresh cilantro or parsley, for garnish",
                    "quantity": None,
                    "unit": None,
                },
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "If frozen, thaw the shrimp (see the notes above).\nMince the garlic.\nPat the shrimp dry. In a medium bowl, mix the shrimp with the garlic and salt.\nIn a large skillet, heat the butter on medium high heat. Cook the shrimp for 1 to 2 minutes per side until opaque and cooked through, turning them with tongs.\nSpritz with juice of the lemon wedges and serve immediately.",
            self.harvester_class.instructions(),
        )
