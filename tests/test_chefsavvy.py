# mypy: allow-untyped-defs

from recipe_scrapers.chefsavvy import ChefSavvy
from tests import ScraperTest


class TestChefSavvyScraper(ScraperTest):

    scraper_class = ChefSavvy

    def test_host(self):
        self.assertEqual("chefsavvy.com", self.harvester_class.host())

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
        self.assertEqual(expected_yields, self.harvester_class.yields())

    def test_instructions(self):
        expected_instructions = """Add steak, broth, soy sauce, garlic, oyster sauce, brown sugar, and sesame oil to a slow cooker. Stir to combine.
        Cook on low for 4-5 hours or until steak is tender.
        Reserve 1/4 cup of the cooking liquid and whisk in the cornstarch to the reserved liquid.
        Slowly stir the cornstarch mixture into the slow cooker along with the broccoli and continue cooking on low for an additional 30 minutes or until sauce has thickened and broccoli is tender.
        Serve immediately with rice and enjoy!"""

        # Normalize the line endings and remove leading/trailing whitespaces
        actual_instructions = (
            self.harvester_class.instructions().strip().replace("\r\n", "\n")
        )

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
