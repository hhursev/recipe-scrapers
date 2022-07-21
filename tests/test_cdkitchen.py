from recipe_scrapers.cdkitchen import CdKitchen
from tests import ScraperTest


class TestCdKitchen(ScraperTest):

    scraper_class = CdKitchen

    def test_host(self):
        self.assertEqual("cdkitchen.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.cdkitchen.com/recipes/recs/473/Veal-Steak-Vesuvio92364.shtml",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Veal Steak Vesuvio", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 veal shoulder arm or blade steaks, cut 1 inch thick",
                "2 baking potatoes, cut lengthwise into 8 wedges",
                "1 lemon, cut lengthwise into 8 wedges",
                "1/2 cup frozen peas, cooked",
                "Seasoning",
                "2 tablespoons olive oil",
                "3 cloves garlic, minced",
                "1 teaspoon dried oregano",
                "1/2 teaspoon black pepper",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Combine seasoning ingredients. Brush 1/2 of seasoning on veal steaks. Toss remaining seasoning with potatoes.\nPlace steaks and potatoes on rack in broiler pan so surface of veal is 3 to 4 inches from heat. Squeeze juice from lemon wedges over steaks and potatoes; place wedges on rack. Broil 26 to 28 minutes for medium doneness, turning steaks, potatoes and lemon once. Remove steaks.\nContinue broiling potatoes and lemon 3 to 5 minutes or until lightly browned. Carve veal; season with salt. Serve with potatoes, lemon and peas.",
            self.harvester_class.instructions(),
        )

    def test_image(self):
        self.assertEqual(
            "https://cdn.cdkitchen.com/recipes/images/sharing/25/veal-steak-vesuvio-63237-small.png",
            self.harvester_class.image(),
        )
