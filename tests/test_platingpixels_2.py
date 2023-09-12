# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.platingpixels import PlatingPixels
from tests import ScraperTest


class TestPlatingPixelsScraper(ScraperTest):
    scraper_class = PlatingPixels
    test_file_name = "platingpixels_2"

    def test_host(self):
        self.assertEqual("platingpixels.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Matt Ivan", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Chicken Fried Chicken", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Chicken,Dinner,Entree", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.platingpixels.com/wp-content/uploads/2022/09/Chicken-Fried-Chicken-recipe-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 pounds Foster Farms Free Range Simply Raised Chicken Breast Fillets (cut in half)",
                "2 cups all-purpose flour",
                "2 teaspoons baking powder",
                "1 ½ teaspoons baking soda",
                "1 ½ teaspoons salt",
                "1 teaspoon garlic powder",
                "1 teaspoon paprika",
                "½ teaspoon ground black pepper",
                "1 ½ cups buttermilk",
                "1 large egg",
                "Frying oil (such as avocado, grapeseed, peanut, canola, or corn oil)",
                "⅓ cup of the used frying oil (or butter)",
                "½ cup flour",
                "2 ½ cups whole milk",
                "Salt and pepper to taste",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        return self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "2 pounds Foster Farms Free Range Simply Raised Chicken Breast Fillets (cut in half)",
                        "2 cups all-purpose flour",
                        "2 teaspoons baking powder",
                        "1 ½ teaspoons baking soda",
                        "1 ½ teaspoons salt",
                        "1 teaspoon garlic powder",
                        "1 teaspoon paprika",
                        "½ teaspoon ground black pepper",
                        "1 ½ cups buttermilk",
                        "1 large egg",
                        "Frying oil (such as avocado, grapeseed, peanut, canola, or corn oil)",
                    ],
                    purpose="Fried Chicken",
                ),
                IngredientGroup(
                    ingredients=[
                        "⅓ cup of the used frying oil (or butter)",
                        "½ cup flour",
                        "2 ½ cups whole milk",
                        "Salt and pepper to taste",
                    ],
                    purpose="Country Gravy Sauce",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        self.assertEqual(
            "To Fry the Chicken Breasts\nIn a large bowl, whisk together flour, baking powder, baking soda, salt, garlic powder, paprika, and pepper. Set aside.\nIn a separate bowl stir together the buttermilk and egg.\nOne at a time, dip the chicken breasts into the flour mixture and press to evenly coat both sides. Next, dip into the buttermilk mixture, then dip into the flour mixture again to coat well. Repeat for remaining chicken pieces.\nPreheat about 2 inches of frying oil in a skillet or frying pan on medium to 325° F.\nAdd some of the breaded chicken breast pieces, leaving space between each. Fry for 3 to 5 minutes until browned. Rotate to brown the other sides and cook to an internal temp of at least 165° F.\nRemove the chicken breasts and place them onto a paper-towel line plate to drain. Repeat for remaining chicken pieces. Reserve some of the frying oil to make the country gravy.\nServe with country gravy or desired sauce and sides.\nTo Make the Country Gravy\nIn a medium saucepan over medium heat, stir together the reserved frying oil and flour until it forms a thick past-like consistency. If using butter, melt the butter first, then add the flour.\nSlowly add the milk while and whisk until smooth. Cook 3 to 5 minutes, stirring often, to heat and thicken the sauce.\nPour over the fried chicken and serve.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Chicken Fried Chicken is a simple recipe of breaded chicken breasts fried to crispy, extra crunchy goodness for an easy weeknight dinner the family will love.",
            self.harvester_class.description(),
        )
