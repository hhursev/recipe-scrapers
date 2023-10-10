# mypy: allow-untyped-defs

from recipe_scrapers.addapinch import AddAPinch
from tests import ScraperTest


class TestAddAPinchScraper(ScraperTest):

    scraper_class = AddAPinch
    test_file_name = "addapinch_1"

    def test_host(self):
        self.assertEqual("addapinch.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://addapinch.com/the-best-chocolate-cake-recipe-ever/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Robyn Stone", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "The Best Chocolate Cake Recipe {Ever}", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("24 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://addapinch.com/wp-content/uploads/2020/04/chocolate-cake-DSC_1768.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "2 cups all-purpose flour",
            "2 cups sugar",
            "3/4 cup unsweetened cocoa powder",
            "2 teaspoons baking powder",
            "1 1/2 teaspoons baking soda",
            "1 teaspoon kosher salt",
            "1 teaspoon espresso powder (homemade or store-bought)",
            "1 cup milk (or buttermilk, almond, or coconut milk)",
            "1/2 cup vegetable oil (or canola oil, or melted coconut oil)",
            "2 large eggs",
            "2 teaspoons vanilla extract",
            "1 cup boiling water",
            "Chocolate Buttercream Frosting Recipe",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = (
            "Preheat oven to 350º F. Prepare two 9-inch cake pans by spraying with baking spray or buttering and lightly flouring.\n"
            "For the chocolate cake:\n"
            "Add flour, sugar, cocoa, baking powder, baking soda, salt and espresso powder to a large bowl or the bowl of a stand mixer. Whisk through to combine or, using your paddle attachment, stir through flour mixture until combined well.\n"
            "Add milk, vegetable oil, eggs, and vanilla to flour mixture and mix together on medium speed until well combined. Reduce speed and carefully add boiling water to the cake batter until well combined.\n"
            "Distribute cake batter evenly between the two prepared cake pans. Bake for 30-35 minutes, until a toothpick or cake tester inserted in the center of the chocolate cake comes out clean.\n"
            "Remove from the oven and allow to cool for about 10 minutes, remove from the pan and cool completely.\n"
            "Frost the cake with Chocolate Buttercream Frosting."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "The Best Chocolate Cake Recipe - A one bowl chocolate cake recipe that is quick, easy, and delicious! Updated with gluten-free, dairy-free, and egg-free options!",
            self.harvester_class.description(),
        )
