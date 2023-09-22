# mypy: allow-untyped-defs

from recipe_scrapers.themagicalslowcooker import TheMagicalSlowCooker
from tests import ScraperTest


class TestTheMagicalSlowCookerScraper(ScraperTest):

    scraper_class = TheMagicalSlowCooker
    test_file_name = "themagicalslowcooker_1"

    def test_host(self):
        self.assertEqual("themagicalslowcooker.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Sarah Olson", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Slow Cooker Ground Beef", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Main Course", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(245, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.themagicalslowcooker.com/wp-content/uploads/2023/08/crockpot-ground-beef-8.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 lbs. ground beef ((7-20 % fat))",
                "1 ½ tsp. salt",
                "½ tsp. garlic powder",
                "½ tsp. onion powder",
                "1 small white onion (diced)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Crumble the beef slightly with your fingers and add to the slow cooker.\nSprinkle over the salt, pepper, onion powder and garlic powder.\nAdd the diced white onion. Stir.\nCook on low for 5 hours or on high for 3 hours. Stirring occasionally, when stirring break up the meat with the spatula.\nServe and enjoy.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Whip up the best-tasting ground beef using just 5 ingredients. This Slow Cooker Ground Beef can be used in just about every recipe!",
            self.harvester_class.description(),
        )
