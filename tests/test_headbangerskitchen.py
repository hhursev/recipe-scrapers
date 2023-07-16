from recipe_scrapers.headbangerskitchen import HeadbangersKitchen
from tests import ScraperTest


class TestHeadbangersKitchenScraper(ScraperTest):

    scraper_class = HeadbangersKitchen

    def test_host(self):
        self.assertEqual("headbangerskitchen.com", self.harvester_class.host())

    # def test_canonical_url(self):
    #     self.assertEqual(
    #         'https://headbangerskitchen.com/recipe/keto-omelet-indian-style/',
    #         self.harvester_class.canonical_url(),
    #     )

    def test_author(self):
        self.assertEqual("Sahil Makhija", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Keto Omelet (Indian Style)", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(10, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("1 serving", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://headbangerskitchen.com/wp-content/uploads/2020/11/KETOMASALAOMELET-Vertical.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "3 Eggs",
                "20 grams Cheese",
                "20 grams Red onion",
                "1 Tbsp Heavy Whipping Cream ( Order online )",
                "1/2 Tsp Tumeric ( Order online )",
                "1/2 Tsp Kashmiri Red Chilli Powder ( Order online )",
                "1 Tbsp Ghee",
                "salt and pepper to taste",
                "1 Tsp Coriander",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Crack the 3 eggs into a bowl and add in the chopped onion, coriander, salt, pepper, tumeric, chilli powder and heavy cream and beat well.\nHeat the ghee in a frying pan and once melted add in the beaten eggs. Grate in the cheese and cover and cook for about 4 minutes. Fold the egg and finish cooking.\nServe with a side of salad.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.33, self.harvester_class.ratings())
