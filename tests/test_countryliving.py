# mypy: allow-untyped-defs

from recipe_scrapers.countryliving import CountryLiving
from tests import ScraperTest


class TestCountryLivingScraper(ScraperTest):

    scraper_class = CountryLiving

    def test_host(self):
        self.assertEqual("countryliving.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Christopher Michel", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Honey-Apple Baked Brie with Fried Sage", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual(
            "autumn,cocktail party,appetizers", self.harvester_class.category()
        )

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://hips.hearstapps.com/hmg-prod/images/honey-apple-baked-brie-with-fried-sage-1663854012.jpg?crop=1.00xw:0.803xh;0,0.177xh&resize=1200:*",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1 (8-ounce) wheel Brie",
            "1/2 sheet all-butter puff pastry (such as Dufour), thawed",
            "2 tbsp. apple butter",
            "1 tbsp. pure honey",
            "1 large egg, beaten",
            "2 tbsp. unsalted butter",
            "4 tsp. pure maple syrup",
            "1 Honeycrisp apple, sliced",
            "Canola oil, for frying",
            "12 fresh sage leaves",
            "Kosher salt",
            "Crackers, for serving",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = "Preheat oven to 425°F. Line a rimmed baking sheet with parchment paper. Place cheese on puff pastry and cut off top rind. Top with apple butter and honey. Fold pastry up around cheese, pinching to seal. Place on prepared baking sheet; brush with egg. Bake until golden brown, 20 to 25 minutes.\nMeanwhile, melt butter and syrup in a large skillet over medium heat. Add apples and cook, stirring occasionally, until soft, 9 to 11 minutes. Transfer to a bowl; clean out skillet.\nLine a plate with paper towels. Heat 1/8 inch oil in skillet over medium-high heat. Add sage and press into oil to fully coat. Fry just until leaves are crisp, 10 to 20 seconds. Transfer to prepared plate. Season with salt."
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
