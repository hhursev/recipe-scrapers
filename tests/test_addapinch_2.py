# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.addapinch import AddAPinch
from tests import ScraperTest


class TestAddAPinchScraper(ScraperTest):

    scraper_class = AddAPinch
    test_file_name = "addapinch_2"

    def test_host(self):
        self.assertEqual("addapinch.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://addapinch.com/citrus-scones-with-orange-glaze/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Robyn Stone", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Citrus Scones Recipe with Orange Glaze", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Breakfast", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://addapinch.com/wp-content/uploads/2015/03/citrus-scones-recipe-DSC_12521-2.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "2 cups all-purpose flour",
            "1/2 cup sugar (+ more for topping)",
            "3 teaspoons baking powder",
            "1/2 teaspoon kosher salt",
            "1/2 cup cold butter (+ more for topping)",
            "3/4 - 1 cup heavy cream",
            "1 teaspoon lemon juice",
            "2 teaspoons orange zest",
            "2 teaspoons lemon zest",
            "1 cup confectioner's sugar",
            "3-4 tablespoons orange juice",
            "1 tablespoon orange zest",
            "coarse sugar for topping (optional)",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "2 cups all-purpose flour",
                        "1/2 cup sugar (+ more for topping)",
                        "3 teaspoons baking powder",
                        "1/2 teaspoon kosher salt",
                        "1/2 cup cold butter (+ more for topping)",
                        "3/4 - 1 cup heavy cream",
                        "1 teaspoon lemon juice",
                        "2 teaspoons orange zest",
                        "2 teaspoons lemon zest",
                    ],
                    purpose="Citrus Scone Recipe:",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 cup confectioner's sugar",
                        "3-4 tablespoons orange juice",
                        "1 tablespoon orange zest",
                        "coarse sugar for topping (optional)",
                    ],
                    purpose="Orange Glaze:",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = [
            "Prep. Preheat oven to 400º F. Line a rimmed baking sheet pan with parchment paper or a nonstick baking sheet.",
            "For the scones:",
            "Make the Dough. Whisk together flour, sugar, baking powder, and salt in a large bowl. Add butter to the bowl and cut into the flour with a pastry blender until the largest pieces of butter are about the size of a pea and the flour mixture resembles coarse meal. Stir in 3/4 cup of heavy cream, lemon juice, and orange and lemon zests.. Press dough together between the palms of your hands. If it doesn't just hold together, add more heavy cream until is just holds together.",
            "Prepare the Dough. Pour dough onto a lightly floured countertop or a pastry board. Pat dough into a large round disc, about an inch thick. Cut dough into equal sized wedges and place onto prepared baking sheet pan. Melt about 2 tablespoons butter and brush on top of dough.",
            "Bake. Bake scones for 20-25 minutes or until they are just beginning to turn lightly brown. Remove from the oven.",
            "Orange Glaze:",
            "Make the Glaze. Whisk all of the glaze ingredients together in a medium sized bowl until smooth and then drizzle on top of each scone after it has cooled for a few five minutes. Sprinkle with coarse sugar, if desired.",
        ]
        expected_instructions_str = "\n".join(expected_instructions)
        self.assertEqual(expected_instructions_str, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Citrus Scones with Orange Glaze are wonderful for breakfast, brunch, or dessert. Bright and delicious, this scones recipe is like a slice of sunshine and is ready in 30 minutes!",
            self.harvester_class.description(),
        )
