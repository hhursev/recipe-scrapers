# mypy: allow-untyped-defs

from recipe_scrapers.chefsavvy import ChefSavvy
from tests import ScraperTest


class TestChefSavvyScraper(ScraperTest):

    scraper_class = ChefSavvy

    def test_host(self):
        self.assertEqual("chefsavvy.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://chefsavvy.com/slow-cooker-broccoli-beef/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Kelley Simmons", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Slow Cooker Broccoli Beef", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Main Course", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(310, self.harvester_class.total_time())

    def test_yields(self):
        expected_yields = "4 servings"
        actual_yields = self.harvester_class.yields()
        self.assertEqual(expected_yields, actual_yields)

    def test_ingredients(self):
        expected_ingredients = [
            "2 pounds chuck steak (sliced thin (about 1-inch thick))",
            "1 cup low sodium beef broth",
            "1/2 cup low sodium soy sauce",
            "4 garlic cloves (minced)",
            "1/4 cup oyster sauce",
            "1/4 cup brown sugar",
            "2 teaspoons sesame oil",
            "2 tablespoons cornstarch",
            "2 heads broccoli (cut into florets)",
            "sesame seeds for garnish, if desired",
        ]
        actual_ingredients = self.harvester_class.ingredients()
        self.assertEqual(expected_ingredients, actual_ingredients)

    def test_instructions(self):
        expected_instructions = (
            "Add steak, broth, soy sauce, garlic, oyster sauce, brown sugar and sesame oil "
            "to a slow cooker. Stir to combine.Cook on low for 4-5 hours or until steak is "
            "tender.\nReserve 1/4 cup of the cooking liquid and whisk in the cornstarch to the "
            "reserved liquid.\nSlowly stir the cornstarch mixture into the slow cooker along with "
            "the broccoli and continue cooking on low for an additional 30 minutes or until sauce "
            "has thickened and broccoli is tender.\nServe immediately with rice and enjoy!"
        )
        actual_instructions = self.harvester_class.instructions()
        self.assertEqual(expected_instructions, actual_instructions)

    def test_ratings(self):
        self.assertEqual(4.67, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Chinese", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Slow Cooker Broccoli Beef. Super tender steak cooked low and slow for 5 hours! Serve over a bowl of rice or noodles!",
            self.harvester_class.description(),
        )

    def test_image(self):
        expected_image_url = "https://chefsavvy.com/wp-content/uploads/easy-slow-cooker-broccoli-beef.jpg"
        self.assertEqual(expected_image_url, self.harvester_class.image())
