from recipe_scrapers.spendwithpennies import SpendWithPennies
from tests import ScraperTest


class TestSpendWithPenniesScraper(ScraperTest):

    scraper_class = SpendWithPennies

    def test_host(self):
        self.assertEqual("spendwithpennies.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.spendwithpennies.com/gooey-chocolate-pudding-cake/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Chocolate Pudding Cake")

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.spendwithpennies.com/wp-content/uploads/2013/10/Chocolate-Pudding-Cake-SpendWithPennies-B-4.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "3/4 cup all-purpose flour",
                "1/2 cup sugar",
                "1/2 cup unsweetened cocoa powder",
                "1 1/2 teaspoons baking powder",
                "2/3 cup milk",
                "2 tablespoons vegetable oil",
                "1 teaspoon vanilla",
                "2/3 cup brown sugar (packed)",
                "1/4 cup cocoa powder",
                "1/4 cup miniature semisweet chocolate chips",
                "1 1/4 cups very hot water",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat oven to 350°F.\nIn a 2 qt casserole dish, combine flour, white sugar, cocoa powder, and baking powder.\nAdd milk and oil, and vanilla. Stir until well mixed.\nIn a small bowl, combine brown sugar, cocoa powder and chocolate chips. Sprinkle over cake batter. DO NOT STIR. Pour hot water over top.\nBake for 30-35 minutes or until the top looks cooked. Serve warm (with ice cream if desired).",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
