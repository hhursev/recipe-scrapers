# mypy: allow-untyped-defs

from recipe_scrapers.forktospoon import ForkToSpoon
from tests import ScraperTest

# Based on https://forktospoon.com/air-fryer-parmesan-tomatoes/


class TestForkToSpoonScraper(ScraperTest):

    scraper_class = ForkToSpoon

    def test_host(self):
        self.assertEqual("forktospoon.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://forktospoon.com/air-fryer-parmesan-tomatoes/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Fork To Spoon", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Air Fryer Parmesan Tomatoes", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Side Dish", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://forktospoon.com/wp-content/uploads/2023/06/air-fryer-parmesan-tomatoes.png",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "3 large tomatoes (Cut in half)",
                "1 cup bread crumbs",
                "1/4 cup parmesan cheese (grated)",
                "1 teaspoon garlic (minced)",
                "1 tablespoon olive oil",
                "1/2 teaspoon dried basil",
                "1/2 teaspoon dried parsley",
                "1/2 teaspoon dried oregano",
                "1/2 teaspoon dried dill",
                "1 teaspoon salt",
                "1/2 teaspoon black pepper",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "In a small mixing bowl, mix the bread crumbs, parmesan cheese, minced garlic, olive oil, basil, parsley, oregano, dill, salt, and black pepper. Mix well.\nSlice your tomatoes in half, and top with the breadcrumb mixture. Set into the air fryer at 330 degrees F, air fryer sitting for 6 to 10 minutes, or until the tomatoes are perfectly roasted.\nPlate, serve, and enjoy!",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Air Fryer Parmesan Tomatoes are amazing! If you are looking for the perfect summer-baked tomato recipe, this one is the one, and it's so easy to make and so flavorful!",
            self.harvester_class.description(),
        )
