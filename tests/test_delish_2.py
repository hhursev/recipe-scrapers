# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.delish import Delish
from tests import ScraperTest


class TestDelishScraper(ScraperTest):

    scraper_class = Delish
    test_file_name = "delish_2"

    def test_host(self):
        self.assertEqual("delish.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            self.harvester_class.canonical_url(),
            "https://www.delish.com/cooking/recipe-ideas/a40272839/apple-cookie-recipe/",
        )

    def test_author(self):
        self.assertEqual("Riley Wofford", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Apple Cookies", self.harvester_class.title())

    def test_category(self):
        self.assertEqual(
            "nut-free,vegetarian,autumn,baking,dessert", self.harvester_class.category()
        )

    def test_total_time(self):
        self.assertEqual(100, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("20 servings", self.harvester_class.yields())

    def test_image(self):
        expected_image = "https://hips.hearstapps.com/hmg-prod/images/apple-cookies1-1656349038.jpg?crop=0.681xw:1.00xh;0.0696xw,0&resize=1200:*"
        self.assertEqual(expected_image, self.harvester_class.image())

    def test_ingredients(self):
        expected_ingredients = [
            "1 1/2 c. (180 g.) all-purpose flour",
            "1 tsp. apple pie spice",
            "3/4 tsp. baking soda",
            "1/2 tsp. kosher salt",
            "6 tbsp. (3/4 stick) butter, softened",
            "1/2 c. (100 g.) granulated sugar",
            "1/2 c. (107 g.) packed light brown sugar",
            "1 large egg",
            "1/2 tsp. pure vanilla extract",
            "1 medium tart apple (about 8 oz.; such as Granny Smith), cored, peeled, and grated (about 1 c.)",
            "3/4 c. powdered sugar",
            "4 tsp. fresh lemon juice",
            "Pinch of apple pie spice",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 1/2 c. (180 g.) all-purpose flour",
                        "1 tsp. apple pie spice",
                        "3/4 tsp. baking soda",
                        "1/2 tsp. kosher salt",
                        "6 tbsp. (3/4 stick) butter, softened",
                        "1/2 c. (100 g.) granulated sugar",
                        "1/2 c. (107 g.) packed light brown sugar",
                        "1 large egg",
                        "1/2 tsp. pure vanilla extract",
                        "1 medium tart apple (about 8 oz.; such as Granny Smith), cored, peeled, and grated (about 1 c.)",
                    ],
                    purpose="Cookie Dough",
                ),
                IngredientGroup(
                    ingredients=[
                        "3/4 c. powdered sugar",
                        "4 tsp. fresh lemon juice",
                        "Pinch of apple pie spice",
                    ],
                    purpose="Icing",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = (
            "Cookie Dough\n"
            "Preheat oven to 350°. Line 2 large baking sheets with parchment paper.\n"
            "In a medium bowl, whisk flour, apple pie spice, baking soda, and salt.\n"
            "In the bowl of a stand mixer fitted with the whisk attachment, beat butter, granulated sugar, and brown sugar on medium speed until light and fluffy, about 2 minutes. Add egg and mix until incorporated, then mix in vanilla. Add dry ingredients to butter mixture and beat until well combined. Stir in apples until just combined. Cover and chill dough until cold, about 30 minutes.\n"
            'Scoop 2-tablespoon balls of dough (about 20 balls) and arrange 2" apart on prepared sheets. Bake until cookies are just set and light golden brown, 14 to 18 minutes. Let cool completely.\n'
            "Icing\n"
            "In a small bowl, whisk powdered sugar and lemon juice. Add water, 1 teaspoon at a time, until icing is thick but pourable.\n"
            "Spoon icing over cooled cookies. Let stand until icing sets, about 15 minutes.\n"
            "Make Ahead: Cookies can be made 2 days ahead. Store in an airtight container at room temperature."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(3.0, self.harvester_class.ratings())
