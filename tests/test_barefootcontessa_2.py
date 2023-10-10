# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.barefootcontessa import BareFootContessa
from tests import ScraperTest


class TestBareFootContessaScraper(ScraperTest):

    scraper_class = BareFootContessa
    test_file_name = "barefootcontessa_2"

    def test_host(self):
        self.assertEqual("barefootcontessa.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://barefootcontessa.com/recipes/parmesan-chicken",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Ina Garten", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Parmesan Chicken | Recipes", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Dinner", self.harvester_class.category())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://d14iv1hjmfkv57.cloudfront.net/assets/recipes/parmesan-chicken/_1200x630_crop_center-center_82_none/chicken.jpg?v=1696019468",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "6 boneless, skinless chicken breasts",
            "1 cup all-purpose flour",
            "Kosher salt and freshly ground black pepper",
            "2 extra-large eggs",
            "1¼ cups seasoned dry bread crumbs",
            "½ cup finely grated Parmesan cheese, plus extra for serving",
            "Unsalted butter",
            "Good olive oil",
            "Baby salad greens for 6, washed and spun dry",
            "Lemon Vinaigrette (recipe follows)",
            "¼ cup freshly squeezed lemon juice (2 lemons)",
            "½ cup good olive oil",
            "Kosher salt and freshly ground black pepper",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "6 boneless, skinless chicken breasts",
                        "1 cup all-purpose flour",
                        "Kosher salt and freshly ground black pepper",
                        "2 extra-large eggs",
                        "1¼ cups seasoned dry bread crumbs",
                        "½ cup finely grated Parmesan cheese, plus extra for serving",
                        "Unsalted butter",
                        "Good olive oil",
                        "Baby salad greens for 6, washed and spun dry",
                        "Lemon Vinaigrette (recipe follows)",
                    ],
                    purpose=None,
                ),
                IngredientGroup(
                    ingredients=[
                        "¼ cup freshly squeezed lemon juice (2 lemons)",
                        "½ cup good olive oil",
                        "Kosher salt and freshly ground black pepper",
                    ],
                    purpose="Lemon Vinaigrette (Makes 3/4 Cup)",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = (
            "Pound the chicken breasts until they are ¼-inch thick. You can use either a meat mallet or a rolling pin.\n"
            "Combine the flour, 2 teaspoons salt, and 1 teaspoon pepper on a dinner plate. Beat the eggs with 1 tablespoon of water in a large shallow bowl. On a second dinner plate, combine the bread crumbs and the ½ cup grated Parmesan cheese. Coat the chicken breasts on both sides with the flour mixture, dusting off the excess, then dip both sides into the egg mixture and finally dredge both sides in the breadcrumb mixture, pressing lightly.\n"
            "Heat 1 tablespoon of butter and 1 tablespoon of olive oil in a large (12-inch) sauté pan over medium-low heat and cook 2 chicken breasts at a time for 2 to 3 minutes on each side, until just cooked through. Remove the cooked chicken to a plate (or keep warm in the oven; see below). Add more butter and oil and cook the rest of the chicken breasts.\n"
            "Toss the salad greens with the lemon vinaigrette. Place each chicken breast on a plate and pile mound of salad on top. Serve hot with shaved or grated Parmesan on top.\n"
            "Notes: You can pound the meat between two sheets of wax paper, plastic wrap, or directly on a board.\n"
            "To keep the cooked chicken breasts warm, place on a sheet pan in a 200-degree oven for up to 15 minutes.\n"
            "Measure the lemon juice in a 1-cup glass measuring cup. Add the olive oil, 1 teaspoon salt and ½ teaspoon pepper and whisk together."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())
