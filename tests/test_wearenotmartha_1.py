# mypy: allow-untyped-defs

from recipe_scrapers.wearenotmartha import WeAreNotMartha
from tests import ScraperTest


class TestWeAreNotMarthaScraper(ScraperTest):

    scraper_class = WeAreNotMartha
    test_file_name = "wearenotmartha_1"

    def test_host(self):
        self.assertEqual("wearenotmartha.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Sues", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Starbucks Grilled Cheese {Copycat Recipe}", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("lunch", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        expected_image_url = "https://wearenotmartha.com/wp-content/uploads/starbucks-grilled-cheese-featured.jpg"
        self.assertEqual(expected_image_url, self.harvester_class.image())

    def test_ingredients(self):
        expected_ingredients = [
            "1 1/2 Tbsp salted or unsalted butter, (softened)",
            "1 Tbsp finely grated parmesan cheese",
            "1/8 tsp garlic powder",
            "Pinch salt, (if butter is unsalted)",
            "4 slices sourdough bread",
            "2 oz sliced white cheddar cheese",
            "2 oz sliced mozzarella cheese",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = (
            "In a small bowl, mix together softened butter, parmesan, garlic powder, and salt (if using unsalted butter) until combined.\n"
            "Preheat a griddle or large skillet over medium-low heat.\n"
            "Spread butter mixture onto one side of all four slices of bread. Top the non-buttered sides of two of the bread slices with cheese. Press remaining bread slices, butter-side up, on top.\n"
            "Transfer sandwiches to griddle or skillet and cook until golden on bottom, about 5 minutes. Flip and cook until sandwiches are golden on second side and cheese is melted.\n"
            "Slice and serve."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        expected_description = "Are you obsessed with the grilled cheese sandwich at Starbucks? It's made with a blend of white cheddar, mozzarella, and garlic parmesan butter and is so easy to recreate at home with this Starbucks Grilled Cheese copycat recipe!"
        self.assertEqual(expected_description, self.harvester_class.description())
