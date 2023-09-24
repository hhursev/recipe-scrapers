# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.norecipes import NoRecipes
from tests import ScraperTest


class TestNoRecipesScraper(ScraperTest):

    scraper_class = NoRecipes
    test_file_name = "norecipes_2"

    def test_host(self):
        self.assertEqual("norecipes.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Marc", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Best Orange Chicken", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Entree", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://norecipes.com/wp-content/uploads/2017/06/orange-chicken-005.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "450 grams boneless skin-on chicken thighs (cut into 1.5-inch pieces)",
            "1 tablespoon soy sauce",
            "1 tablespoon sake",
            "1 teaspoon fresh ginger (grated)",
            "1/2 cup potato starch",
            "vegetable oil (for frying)",
            "3/4 cup orange juice",
            "1/3 cup orange marmalade",
            "1/2 tablespoon orange zest (zest of 1/2 orange)",
            "1/2 teaspoon potato starch",
            "1/2 teaspoon salt",
            "1/4 red bell pepper (minced, for garnish)",
            "1/2 teaspoon toasted sesame seeds (for garnish)",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = [
            "Add the chicken, soy sauce, sake and fresh ginger to a bowl and mix together. Let the chicken marinate for at least 15 minutes, or preferably up to 8 hours.",
            "Add all the ingredients for the orange sauce into a skillet and whisk together.",
            "When you're ready to make the orange chicken, preheat a heavy pot filled with 2-inches of vegetable oil to 340 degrees F (170 C). Prepare a paper towel lined rack.",
            "Add 1/2 cup potato starch to another bowl, and dust the chicken with the potato starch. You want an even coating, but it should not be caked on.",
            "Fry the chicken in batches until golden brown and cooked through, flipping a few times to ensure it browns evenly.",
            "Drain the chicken on the prepared rack.",
            "When all the chicken is done, heat the skillet with the orange sauce over medium-high heat, stirring constantly until it starts to thicken.",
            "Add the fried chicken to the orange sauce and toss to coat evenly. The orange chicken is done when the sauce forms a thick glaze around the pieces of the chicken. Garnish with red pepper and sesame seeds.",
        ]
        self.assertEqual(
            "\n".join(expected_instructions), self.harvester_class.instructions()
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "450 grams boneless skin-on chicken thighs (cut into 1.5-inch pieces)",
                        "1 tablespoon soy sauce",
                        "1 tablespoon sake",
                        "1 teaspoon fresh ginger (grated)",
                        "1/2 cup potato starch",
                        "vegetable oil (for frying)",
                    ],
                    purpose="for chicken",
                ),
                IngredientGroup(
                    ingredients=[
                        "3/4 cup orange juice",
                        "1/3 cup orange marmalade",
                        "1/2 tablespoon orange zest (zest of 1/2 orange)",
                        "1/2 teaspoon potato starch",
                        "1/2 teaspoon salt",
                    ],
                    purpose="for orange sauce",
                ),
                IngredientGroup(
                    ingredients=[
                        "1/4 red bell pepper (minced, for garnish)",
                        "1/2 teaspoon toasted sesame seeds (for garnish)",
                    ],
                    purpose="to serve",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_ratings(self):
        self.assertEqual(4.39, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Best,Chinese-American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Orange Chicken is a classic Chinese-American take-out dish popularized by Panda Express. My version is loaded with juicy chunks of gingery marinated chicken, and the all-natural glaze is made with a triple dose orange which makes it super fragrant.",
            self.harvester_class.description(),
        )
