# mypy: allow-untyped-defs

from recipe_scrapers.platingpixels import PlatingPixels
from tests import ScraperTest


class TestPlatingPixelsScraper1(ScraperTest):

    scraper_class = PlatingPixels
    test_file_name = "platingpixels_1"

    def test_host(self):
        self.assertEqual("platingpixels.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Matt Ivan", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Instant Pot Korean Short Ribs (Kalbi)", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Entree", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.platingpixels.com/wp-content/uploads/2021/01/Instant-Pot-Beef-Short-Ribs-recipe-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "4 pounds flanken beef short ribs",
                "1 cup soy sauce",
                "¼ cup honey",
                "2 tablespoons sesame oil",
                "2 tablespoons garlic chili paste",
                "1 tablespoon rice vinegar",
                "½ teaspoon black pepper",
                "½ teaspoon crushed red chili flakes",
                "3 cloves garlic (minced)",
                "1 tablespoon fresh grated ginger",
                "Sesame seeds and sliced green onions (as garnishes)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "In a large bowl, whisk together all ingredients except ribs and sesame seeds. Add beef short ribs and toss to coat. Let rest for 15 minutes for flavors to soak in.\nPlace the prepared ribs on a wire rack in the Instant Pot. Pour remaining liquid over the ribs. Close the lid and cook on manual HIGH pressure for 30 minutes.\nOnce cooked, allow steam to release manually. Or open the release valve after 5 minutes with tongs. Remove the ribs carefully, set aside, and cover with foil to keep warm.\nSet the Instant Pot to high saute and simmer sauce with the lid open until thickened, about 5-10 minutes.\nCoat both sides of the ribs with the sauce, sprinkle with sesame seeds and green onions before serving.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Asian", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Instant Pot Korean Short Ribs (Kalbi) coated in a thick homemade glaze that's bursting with umami, sweet and spicy flavors.",
            self.harvester_class.description(),
        )
