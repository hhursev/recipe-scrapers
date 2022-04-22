from recipe_scrapers.momswithcrockpots import MomsWithCrockPots
from tests import ScraperTest


class TestMomsWithCrockPotsScraper(ScraperTest):

    scraper_class = MomsWithCrockPots

    def test_host(self):
        self.assertEqual("momswithcrockpots.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://momswithcrockpots.com/slow-cooked-macaroni-cheese/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Crockpot Macaroni & Cheese")

    def test_total_time(self):
        self.assertEqual(225, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "8 ounces macaroni",
                "2 teaspoons olive oil",
                "1 cup evaporated milk",
                "1/2 cup milk",
                "1/2 teaspoon salt",
                "1/4 teaspoon ground black pepper",
                "2 cups Cheddar cheese (shredded, or a Cheddar blend)",
                "4 tablespoons butter (melted)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            'Cook the macaroni following package directions. Drain in a colander and rinse with hot water. Drain well.\nGenerously butter the sides and bottom of a 3 1/2- to 4-quart slow cooker (I use about 2 tablespoons of butter).\nCombine the macaroni with the remaining ingredients in the slow cooker and blend well. Cover the slow cooker and cook on LOW for 2 1/2 to 3 1/2 hours, stirring a few times.\nIf desired, spoon the cooked macaroni and cheese mixture into a baking dish, sprinkle with a little more cheese, and put under the broiler for a minute or 2, just until cheese is melted.\nWhen the macaroni and cheese is done, feel free to spoon into a baking dish, top with a little more cheese, and put under the broiler for a minute or two for that "fresh from the oven" look.\nUse a gluten free pasta',
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.0, self.harvester_class.ratings())
