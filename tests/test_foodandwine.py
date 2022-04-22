from recipe_scrapers.foodandwine import FoodAndWine
from tests import ScraperTest


class TestFoodAndWineScraper(ScraperTest):

    scraper_class = FoodAndWine

    def test_host(self):
        self.assertEqual("foodandwine.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.foodandwine.com/recipes/kwames-pepper-shrimp",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Kwame’s Pepper Shrimp", self.harvester_class.title())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F9%2F2020%2F08%2F21%2Fpepper-shrimp-FT-RECIPE0920.jpg",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1/2 cup unsalted butter (4 ounces)",
                "5 large garlic cloves, minced",
                "1 fresh Scotch bonnet chile, stemmed, unseeded, and minced (about 1 tablespoon)",
                "1 1/2 teaspoons minced peeled fresh ginger",
                "1/2 cup fresh lime juice",
                "1/2 cup distilled white vinegar",
                "1 thyme sprig",
                "3 pounds unpeeled head-on raw large shrimp, deveined",
                "1 teaspoon kosher salt",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Melt butter in a large pot over medium. Add garlic, chile, and ginger; cook, stirring often, until aromatic and tender, about 5 minutes. Add lime juice, vinegar, and thyme; bring to a simmer over medium. Increase heat to medium-high; add shrimp, and cook, stirring often, until shrimp are opaque and cooked through, about 5 minutes. Remove from heat. Sprinkle with salt, and serve immediately.",
            self.harvester_class.instructions(),
        )
