from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.bakingmischief import BakingMischief
from tests import ScraperTest


class TestBakingMischiefScraper(ScraperTest):

    scraper_class = BakingMischief
    test_file_name = "bakingmischief_2"

    def test_host(self):
        self.assertEqual("bakingmischief.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://bakingmischief.com/small-carrot-cake-with-cream-cheese-frosting/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Tracy", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Small Carrot Cake", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(90, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://bakingmischief.com/wp-content/uploads/2017/03/small-carrot-cake-with-cream-cheese-frosting-image-square.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "7x5-inch Baking Dish",
            "½ cup (60g) all-purpose flour",
            "½ teaspoon baking powder",
            "½ teaspoon cinnamon",
            "½ teaspoon allspice",
            "¼ teaspoon salt",
            "½ cup (100g) granulated sugar",
            "¼ cup vegetable oil",
            "1 large egg",
            "⅔ cup loosely packed grated peeled carrots",
            "2 ounces cream cheese (softened)",
            "4 tablespoons (2oz) unsalted butter (softened)",
            "¼ teaspoon vanilla extract",
            "⅔ cup (80g) powdered sugar (sifted)",
            "Pinch of salt",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "7x5-inch Baking Dish",
                    ],
                    purpose="Special Equipment",
                ),
                IngredientGroup(
                    ingredients=[
                        "½ cup (60g) all-purpose flour",
                        "½ teaspoon baking powder",
                        "½ teaspoon cinnamon",
                        "½ teaspoon allspice",
                        "¼ teaspoon salt",
                        "½ cup (100g) granulated sugar",
                        "¼ cup vegetable oil",
                        "1 large egg",
                        "⅔ cup loosely packed grated peeled carrots",
                    ],
                    purpose="Carrot Cake",
                ),
                IngredientGroup(
                    ingredients=[
                        "2 ounces cream cheese (softened)",
                        "4 tablespoons (2oz) unsalted butter (softened)",
                        "¼ teaspoon vanilla extract",
                        "⅔ cup (80g) powdered sugar (sifted)",
                        "Pinch of salt",
                    ],
                    purpose="Frosting",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = (
            "Preheat your oven to 350°F. Lightly grease your baking dish.\n"
            "In a small bowl, whisk together flour, baking powder, cinnamon, allspice, and salt.\n"
            "In a medium bowl, whisk together sugar, vegetable oil, and egg until well combined. Stir in flour mixture and use a rubber spatula to fold in grated carrots. Transfer batter to prepared baking dish.\n"
            "Bake for 25 to 30 minutes, until a toothpick inserted into the center of the cake comes out clean. Place cake (in pan) on a cooling rack, and cool completely before frosting, about 45 minutes.\n"
            "Frosting\n"
            "Whisk together cream cheese, butter, and vanilla until smooth. Add sifted powdered sugar and salt and whisk until well-combined and fluffy. Spread frosting over the cake. Chilling before serving is optional but recommended.\n"
            "Serve cake in the baking dish and enjoy!"
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(4.88, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        expected_description = "This incredibly easy Small Carrot Cake With Cream Cheese Frosting is a perfect replica of my mom's potluck favorite!"
        self.assertEqual(expected_description, self.harvester_class.description())
