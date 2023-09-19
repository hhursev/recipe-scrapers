# mypy: allow-untyped-defs

from recipe_scrapers.plowingthroughlife import PlowingThroughLife
from tests import ScraperTest


class TestPlowingThroughLifeScraper(ScraperTest):

    scraper_class = PlowingThroughLife
    test_file_name = "plowingthroughlife_1"

    def test_host(self):
        self.assertEqual("plowingthroughlife.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual(
            "Jennifer @ Plowing Through Life", self.harvester_class.author()
        )

    def test_title(self):
        self.assertEqual("Crock Pot Mac and Cheese", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Side Dish", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(160, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://plowingthroughlife.com/wp-content/uploads/2020/05/Farmhouse-Mac-and-cheese-FI.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "8 ounces macaroni (cooked)",
                "2 tablespoons vegetable oil",
                "12 ounces evaporated milk",
                "1 1/2 cups milk",
                "1 teaspoon salt",
                "1/2 teaspoon pepper (optional)",
                "1 tablespoon dried onion flakes (use up to 2 T. for maximum flavor)",
                "1 1/2 cups Velveeta cheese (12 ounces)",
                "1 1/2 cups shredded cheddar cheese",
                "4 tablespoons butter (melted)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "In a crock pot toss cooked macaroni with vegetable oil.\nStir in remaining ingredients.\nCover and cook on low for 2 - 3 hours. Stir a couple times and enjoy!",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Creamy macaroni and cheese is super easy to make in a crock pot. Cooked pasta, Velveeta and cheddar cheese along with evaporated milk make a rich and delicious side dish for any occasion! Our Farmhouse Style Crock Pot Mac and Cheese is a family favorite!",
            self.harvester_class.description(),
        )
