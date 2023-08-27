# mypy: allow-untyped-defs

from recipe_scrapers.thespruceeats import TheSpruceEats
from tests import ScraperTest


class TestTheSpruceEatsScraper(ScraperTest):

    scraper_class = TheSpruceEats
    test_file_name = "thespruceeats_1"

    def test_host(self):
        self.assertEqual("thespruceeats.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Diana Rattray", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Bell Pepper Sandwich Recipe", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Lunch,Dinner,Sandwich", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("1 serving", self.harvester_class.yields())

    def test_image(self):
        expected_image_url = "https://www.thespruceeats.com/thmb/jgDiDqHCg2AfmWiuTuc5yZbyuSw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/bell-pepper-sandwich-recipe-5216751-hero-01-bc8d5210259d4674872c92ce5377fc7d.jpg"
        self.assertEqual(expected_image_url, self.harvester_class.image())

    def test_ingredients(self):
        expected_ingredients = [
            "1 medium bell pepper",
            "1 1/2 ounces cream cheese, about 2 to 3 tablespoons",
            "1 teaspoon whole-grain mustard",
            "2 ounces thinly sliced ham",
            "1 1/2 ounces thinly sliced swiss cheese",
            "1/2 small cucumber, about 6 to 8 thin slices",
            "2 tablespoons guacamole, or a few slices of avocado",
            "1 dash salt, or seasoned salt, to taste",
            "1 dash ground black pepper, to taste",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = (
            "Gather the ingredients.\n"
            "With a sharp knife, remove the stem end of the pepper. Cut the pepper in half lengthwise and remove the ribs and seeds.\n"
            "Lay the pepper halves on a cutting board, cut-side up, and spread cream cheese on each half. Spread some whole-grain mustard on the cream cheese.\n"
            "Layer ham, cheese, cucumbers, and guacamole or avocado slices on each half.\n"
            "Put the halves together to form a sandwich and enjoy."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())
