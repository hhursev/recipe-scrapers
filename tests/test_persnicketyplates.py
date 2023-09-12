# mypy: allow-untyped-defs

from recipe_scrapers.persnicketyplates import PersnicketyPlates
from tests import ScraperTest


class TestPersnicketyPlatesScraper(ScraperTest):

    scraper_class = PersnicketyPlates

    def test_host(self):
        self.assertEqual("persnicketyplates.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Melissa Williams", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Easy Slow Cooker Hawaiian Meatballs", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Appetizer,Main Course", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(125, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.persnicketyplates.com/wp-content/uploads/2023/06/slow-cooker-hawaiian-meatballs-10-SQUARE.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "3 pounds frozen meatballs (beef, pork, turkey, plant based)",
                "20 ounces pineapple chunks (drained)",
                "2 cups frozen peppers & onions",
                "18 ounces bbq sauce (2 cups)",
                "¼ cup low sodium soy sauce",
                "¼ cup white vinegar",
                "¼ cup brown sugar",
                "3 cloves garlic (minced)",
                "2 Tablespoons chopped scallions (for garnish)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Pour the frozen meatballs, pineapple chunks, peppers and onions into the basin of a 6-8 quart slow cooker.\nIn a medium mixing bowl, whisk together the barbecue sauce, soy sauce, vinegar, brown sugar, and minced garlic.\nPour the sauce over the meatballs and gently stir to evenly distribute.\nCover and cook on HIGH for 2-3 hours.\nGarnish with chopped scallions.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Slow cooker Hawaiian meatballs are made with frozen meatballs, canned pineapple, peppers, onions, and a sweet and tangy sauce. This dump-and-go crockpot recipe makes the perfect appetizer or a main dish that the whole family will love!",
            self.harvester_class.description(),
        )
