# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.nutritionfacts import NutritionFacts
from tests import ScraperTest


class TestNutritionFactsScraper(ScraperTest):
    scraper_class = NutritionFacts
    test_file_name = "nutritionfacts_2"

    def test_host(self):
        self.assertEqual("nutritionfacts.org", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://nutritionfacts.org/recipe/cinnamon-roll-oatmeal/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual(
            "Jill Dalton from the Whole Food Plant Based Cooking Show",
            self.harvester_class.author(),
        )

    def test_title(self):
        self.assertEqual("Cinnamon Roll Oatmeal", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Breakfast", self.harvester_class.category())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://nutritionfacts.org/app/uploads/2023/08/jill-wfpb-cooking-cinnamon-roll-oats-scaled.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "4 cups water",
            "8 pitted dates",
            "2 teaspoons cinnamon",
            "2 teaspoons vanilla extract or powder",
            "2 cups rolled oats",
            "Raw pecans (optional garnish, as desired)",
            "½ cup raw cashews",
            "½ teaspoon vanilla extract",
            "2 pitted dates",
            "¾-1 cup water",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "4 cups water",
                        "8 pitted dates",
                        "2 teaspoons cinnamon",
                        "2 teaspoons vanilla extract or powder",
                        "2 cups rolled oats",
                        "Raw pecans (optional garnish, as desired)",
                    ],
                    purpose="For the Oatmeal",
                ),
                IngredientGroup(
                    ingredients=[
                        "½ cup raw cashews",
                        "½ teaspoon vanilla extract",
                        "2 pitted dates",
                        "¾-1 cup water",
                    ],
                    purpose="For the Drizzle",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "To make the oatmeal, in a high-speed blender, combine the water, dates, cinnamon, and vanilla. Blend until smooth and pour into a saucepan with the rolled oats. Cook until the oats reach your desired consistency.",
                    "To make the drizzle, combine all of the ingredients into a high-speed blender. Blend until smooth and creamy.",
                    "Divide the oatmeal into bowls, top with the drizzle, and garnish with pecans, as desired.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "This Cinnamon Roll Oatmeal is a naturally sweet and delicious way to start your day. It’s a date-sweetened oatmeal paired with a creamy cashew drizzle that makes for a fancy, yet simple breakfast. Less than 3 percent of Americans meet the daily recommended fiber intake, despite research suggesting that high-fiber foods, such as whole grains, can affect the progression of coronary heart disease. The soluble fiber of oatmeal forms a gel in the stomach, delaying stomach emptying, making one feel full for a longer period.",
            self.harvester_class.description(),
        )
