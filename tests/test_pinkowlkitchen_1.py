# mypy: allow-untyped-defs

from recipe_scrapers.pinkowlkitchen import PinkOwlKitchen
from tests import ScraperTest


class TestPinkOwlKitchenScraper(ScraperTest):

    scraper_class = PinkOwlKitchen
    test_file_name = "pinkowlkitchen_1"

    def test_host(self):
        self.assertEqual("pinkowlkitchen.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Ashley", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Chocolate Chess Pie", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("10 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://pinkowlkitchen.com/wp-content/uploads/2023/08/chocolate-chess-pie-featured-image.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1, 9-inch pie crust (homemade, refrigerated, or frozen, my homemade pie crust from my sweet potato pie recipe is linked)",
            "1 1/2 cups granulated sugar",
            "1/4 cup unsweetened cocoa powder (regular or Dutch-processed)",
            "1/4 teaspoon salt",
            "1/4 cup melted butter (unsalted)",
            "3 large eggs (beaten)",
            "1/2 cup evaporated milk (see note)",
            "1 1/2 teaspoons pure vanilla extract",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        self.assertEqual(
            "Preheat your oven to 350°F. Prepare your pie crust by gently pressing your homemade or refrigerated pie crust into your pie plate and crimping the edges, or by setting your frozen pie crust out on the counter while you prepare the filling.\n"
            "In a large mixing bowl, whisk together the sugar, cocoa powder, and salt until combined. Add the melted butter, beaten eggs, evaporated milk, and vanilla extract to the bowl and whisk until the filling is smooth and lump free.\n"
            "Pour the filling into your prepared pie crust and bake the pie in the preheated oven for 50 to 55 minutes, until the pie has puffed up and the center is just barely jiggly.\n"
            "Allow the pie to cool to room temperature on a wire rack. Enjoy chilled or room temperature with a dollop of fresh whipped cream!",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Chocolate chess pie is a decadent, fudgy custard pie baked in a buttery homemade pie crust. This tasty pie is a chocolate lover's dream and makes the perfect Thanksgiving dessert!",
            self.harvester_class.description(),
        )
