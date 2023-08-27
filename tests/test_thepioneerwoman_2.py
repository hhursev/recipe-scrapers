# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.thepioneerwoman import ThePioneerWoman
from tests import ScraperTest


class TestThePioneerWomanScraper(ScraperTest):

    scraper_class = ThePioneerWoman
    test_file_name = "thepioneerwoman_2"

    def test_host(self):
        self.assertEqual("thepioneerwoman.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Ree Drummond", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Pumpkin Sheet Cake With Cream Cheese Frosting",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual(
            "Thanksgiving,baking,comfort food,dessert,main dish,snack",
            self.harvester_class.category(),
        )

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("18 servings", self.harvester_class.yields())

    def test_image(self):
        expected_image = "https://hips.hearstapps.com/hmg-prod/images/pumpkin-sheet-cake-recipe-1626966058.jpg?crop=0.670xw:1.00xh;0.0337xw,0&resize=1200:*"
        self.assertEqual(expected_image, self.harvester_class.image())

    def test_ingredients(self):
        expected_ingredients = [
            "2 sticks salted butter",
            "2 c. pumpkin puree (not pumpkin pie filling!)",
            "2 tsp. pumpkin pie spice",
            "1/2 c. boiling water",
            "2 c. all-purpose flour",
            "2 c. granulated sugar",
            "1/4 tsp. salt",
            "1/2 c. buttermilk",
            "2 eggs",
            "2 tsp. baking soda",
            "2 tsp. vanilla extract",
            "1/2 tsp. maple extract (optional)",
            "8 oz. cream cheese, softened",
            "1 stick unsalted butter, softened",
            "1 lb. powdered sugar",
            "Dash of salt",
            "1 tbsp. half and half or whole milk, plus more if needed for thinning",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "2 sticks salted butter",
                        "2 c. pumpkin puree (not pumpkin pie filling!)",
                        "2 tsp. pumpkin pie spice",
                        "1/2 c. boiling water",
                        "2 c. all-purpose flour",
                        "2 c. granulated sugar",
                        "1/4 tsp. salt",
                        "1/2 c. buttermilk",
                        "2 eggs",
                        "2 tsp. baking soda",
                        "2 tsp. vanilla extract",
                        "1/2 tsp. maple extract (optional)",
                    ],
                    purpose="For the cake:",
                ),
                IngredientGroup(
                    ingredients=[
                        "8 oz. cream cheese, softened",
                        "1 stick unsalted butter, softened",
                        "1 lb. powdered sugar",
                        "Dash of salt",
                        "1 tbsp. half and half or whole milk, plus more if needed for thinning",
                    ],
                    purpose="For the frosting:",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = (
            "For the cake: Preheat the oven to 350 degrees. Spray a sheet pan (11-inches by 17-inches) with baking spray and set aside.\n"
            "In a medium saucepan, melt the butter. Whisk in the pumpkin puree and pumpkin pie spice until it's totally combined. Whisk in the boiling water until the mixture is smooth and combined. Set aside.\n"
            "In a large bowl, combine the flour, sugar and salt. Whisk and set aside.\n"
            "In a liquid measuring cup, combine the buttermilk, eggs, baking soda, vanilla and maple extract, if using. Whisk and set aside.\n"
            "Pour the pumpkin mixture into the flour mixture and stir until halfway combined. Pour in the buttermilk mixture and stir until combined. Pour into the sheet pan and bake the cake for 20 minutes. Remove and allow to cool.\n"
            "For the frosting: In the bowl of an electric mixer, mix together the cream cheese, butter, powdered sugar, and salt until smooth. Add the half and half or milk and check the consistency. It should be somewhat thick but thin enough to spread in a thin layer.\n"
            "Spread the frosting all over the surface of the cake. Cut into squares and serve. Keep leftovers in the fridge, as frosting will get soft."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(4.17, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American,Comfort Food", self.harvester_class.cuisine())

    def test_description(self):
        expected_description = "Pumpkin sheet cake is moist, heavenly, and the perfect fall recipe. It’s perfect for Thanksgiving—and it’s also perfect for the other 364 days of the year."
        self.assertEqual(expected_description, self.harvester_class.description())
