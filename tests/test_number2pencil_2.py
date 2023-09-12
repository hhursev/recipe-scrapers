# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.number2pencil import Number2Pencil
from tests import ScraperTest


class TestNumber2PencilScraper(ScraperTest):

    scraper_class = Number2Pencil
    test_file_name = "number2pencil_2"

    def test_host(self):
        self.assertEqual("number-2-pencil.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Melissa", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Sheet Pan Strawberry Shortcake Recipe", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.number-2-pencil.com/wp-content/uploads/2023/05/Sheet-Pan-Strawberry-Shortcake-7.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "3 1/2 cups all-purpose flour",
                "3/4 cup sugar (granulated)",
                "5 teaspoons baking powder",
                "1/2 teaspoon table salt",
                "1 cup unsalted butter (cold, 2 sticks)",
                "2 eggs (lightly beaten)",
                "2 cups heavy whipping cream",
                "1 teaspoon pure vanilla extract",
                "2 cups heavy whipping cream",
                "1/3 cup powdered sugar",
                "2 pounds strawberries (washed and sliced)",
                "1/4 cup sugar (granulated, more or less depending on berry sweetness)",
                "1 teaspoon fresh lemon juice",
                "chamomile flowers (optional)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "3 1/2 cups all-purpose flour",
                        "3/4 cup sugar (granulated)",
                        "5 teaspoons baking powder",
                        "1/2 teaspoon table salt",
                        "1 cup unsalted butter (cold, 2 sticks)",
                        "2 eggs (lightly beaten)",
                        "2 cups heavy whipping cream",
                        "1 teaspoon pure vanilla extract",
                    ],
                    purpose="Shortcake",
                ),
                IngredientGroup(
                    ingredients=[
                        "2 cups heavy whipping cream",
                        "1/3 cup powdered sugar",
                    ],
                    purpose="Whipped Cream",
                ),
                IngredientGroup(
                    ingredients=[
                        "2 pounds strawberries (washed and sliced)",
                        "1/4 cup sugar (granulated, more or less depending on berry sweetness)",
                        "1 teaspoon fresh lemon juice",
                        "chamomile flowers (optional)",
                    ],
                    purpose="Strawberry Topping",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Shortcake\nPreheat oven to 400℉ and set aside a non stick 13x10 sheet pan.\nIf using a food processor, add flour, sugar, baking powder, and salt in food processor. Pulse briefly to combine. Add cold butter to food processor and pulse briefly several times until butter is combined with flour and mixture resembles coarse sand. Transfer mixture to mixing bowl and stir in eggs, heavy whipping cream, and vanilla extract. Stir just until combined.\nTransfer shortcake dough to sheet pan and use slightly damp hand to spread dough evenly on sheet pan. Use a spoor or spatula to smooth dough.\nBake for 20-25 minutes until shortcake is golden brown. Remove and let cool completely.\nWhipped Cream\nIn a large bowl, use an electric mixer to beat heavy whipping cream and powdered sugar together until soft peaks form. Do not over beat. You can also use a stand mixer with a whisk attachment.\nStrawberry Topping\nSlice strawberries and mix with sugar and lemon juice.\nTo Assemble Strawberry Shortcake\nLet shortcake cool, then top with whipped cream, followed by strawberries. Serve immediately for best results.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Sheet Pan Strawberry Shortcake Recipe – buttery homemade shortcake with whipped cream and fresh strawberries. It’s the ultimate summer dessert for a crowd!",
            self.harvester_class.description(),
        )
