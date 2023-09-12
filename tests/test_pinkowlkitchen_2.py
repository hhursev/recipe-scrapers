# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.pinkowlkitchen import PinkOwlKitchen
from tests import ScraperTest


class TestPinkOwlKitchenScraper(ScraperTest):

    scraper_class = PinkOwlKitchen
    test_file_name = "pinkowlkitchen_2"

    def test_host(self):
        self.assertEqual("pinkowlkitchen.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Ashley", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Chocolate Cream Cold Brew (Starbucks Copycat)",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual("Beverage", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(5, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("1 serving", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://pinkowlkitchen.com/wp-content/uploads/2022/06/chocolate-cream-cold-brew-featured-image.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "2 tablespoons heavy cream",
            "2 tablespoons 2% milk",
            "1 tablespoon malted milk powder",
            "1 teaspoon vanilla syrup (homemade or store-bought, my recipe linked)",
            "1 teaspoon cocoa powder",
            "8 ounces cold brew coffee",
            "1 tablespoon vanilla syrup (homemade or store-bought)",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "2 tablespoons heavy cream",
                        "2 tablespoons 2% milk",
                        "1 tablespoon malted milk powder",
                        "1 teaspoon vanilla syrup (homemade or store-bought, my recipe linked)",
                        "1 teaspoon cocoa powder",
                    ],
                    purpose="Chocolate Cold Foam",
                ),
                IngredientGroup(
                    ingredients=[
                        "8 ounces cold brew coffee",
                        "1 tablespoon vanilla syrup (homemade or store-bought)",
                    ],
                    purpose="Coffee",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = (
            "Add the cream, milk, malted milk powder, vanilla syrup, and cocoa powder to a large cup or glass. Use a handheld milk frother to beat the mixture until it doubles in volume and becomes light and frothy. Set aside.\n"
            "Fill a tall glass with ice and pour the cold brew over the ice. Add the vanilla syrup, being careful to leave about an inch or so at the top of the glass to accommodate the cold foam.\n"
            "Pour the chocolate cold foam over the coffee and enjoy!"
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(4.8, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        expected_description = "Chocolate Cream Cold Brew is a delicious coffee drink sweetened with homemade vanilla syrup and topped off with a smooth and frothy chocolate cold foam. This Starbucks dupe tastes even better than the original and makes the perfect summer beverage!"
        self.assertEqual(expected_description, self.harvester_class.description())
