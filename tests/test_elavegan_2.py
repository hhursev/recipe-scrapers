# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.elavegan import ElaVegan
from tests import ScraperTest


class TestElaVeganScraper(ScraperTest):
    scraper_class = ElaVegan
    test_file_name = "elavegan_2"

    def test_host(self):
        self.assertEqual("elavegan.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://elavegan.com/vegan-coffee-cake/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Ela", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Vegan Coffee Cake", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Breakfast,Cake,Dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(55, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("9 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://elavegan.com/wp-content/uploads/2022/11/a-piece-of-vegan-coffee-cake-on-a-small-plate.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1 cup oat flour ((gluten-free if needed))",
            "1/2 cup rice flour ((see notes))",
            "2 Tbsp cornstarch (or potato starch)",
            "1/3 cup Erythritol (or sugar)",
            "1 1/2 tsp baking powder",
            "1/4 tsp baking soda",
            "1/2 tsp sea salt",
            "3/4 cup almond milk (or any other dairy-free milk)",
            "2/3 cup applesauce (unsweetened)",
            "2 Tbsp oil ((see notes))",
            "1 Tbsp apple cider vinegar",
            "1 tsp vanilla extract",
            "1/2 cup rice flour (or regular flour, if you're not gluten-free)",
            "1/2 cup almond flour (or shredded unsweetened coconut)",
            "1/4 cup coconut sugar (or brown sugar)",
            "2 Tbsp oil",
            "2 Tbsp maple syrup (or any other liquid sweetener)",
            "2 tsp cinnamon",
            "1/4 tsp sea salt",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 cup oat flour ((gluten-free if needed))",
                        "1/2 cup rice flour ((see notes))",
                        "2 Tbsp cornstarch (or potato starch)",
                        "1/3 cup Erythritol (or sugar)",
                        "1 1/2 tsp baking powder",
                        "1/4 tsp baking soda",
                        "1/2 tsp sea salt",
                    ],
                    purpose="Dry Cake Ingredients",
                ),
                IngredientGroup(
                    ingredients=[
                        "3/4 cup almond milk (or any other dairy-free milk)",
                        "2/3 cup applesauce (unsweetened)",
                        "2 Tbsp oil ((see notes))",
                        "1 Tbsp apple cider vinegar",
                        "1 tsp vanilla extract",
                    ],
                    purpose="Wet Cake Ingredients",
                ),
                IngredientGroup(
                    ingredients=[
                        "1/2 cup rice flour (or regular flour, if you're not gluten-free)",
                        "1/2 cup almond flour (or shredded unsweetened coconut)",
                        "1/4 cup coconut sugar (or brown sugar)",
                        "2 Tbsp oil",
                        "2 Tbsp maple syrup (or any other liquid sweetener)",
                        "2 tsp cinnamon",
                        "1/4 tsp sea salt",
                    ],
                    purpose="Streusel",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = [
            "I recommend measuring the ingredients in grams on a kitchen scale. Check the video in the post for visual instructions.",
            "Start by lining a baking dish with parchment paper with an overhang on all sides (for easy removal). My pan measures 6×9 inches (ca. 15x23 cm).",
            "Make the streusel topping: Add all dry ingredients for the streusel to a bowl, stir with a whisk, then add the wet ingredients. Use your fingers to combine everything until the mixture is slightly crumbly. Set aside and preheat your oven to 350 degrees Fahrenheit (ca. 180 °C).",
            "Add all dry cake ingredients into a large mixing bowl and stir with a whisk. You could also add the dry ingredients to a food processor and blend for a couple of seconds.",
            "Next, add the wet cake ingredients and stir with a whisk. You can also use a hand mixer.",
            "Assemble: Pour about half of the batter into the lined baking dish. Then add half of the cinnamon streusel. Pour the remaining batter on top of the streusel and finally add the remaining streusel.",
            "Bake for about 35-40 minutes, or until a toothpick inserted into the center of the crumb cake comes out almost clean (it can be crumbly but shouldn't be wet). The baking time can be a few minutes less or more, depending on your oven and the size of the pan. Let cool completely, then drizzle with icing (optional). Check the recipe notes below for the icing. Enjoy!",
        ]
        expected_instructions = "\n".join(expected_instructions)
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(4.95, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American,German", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            'A soft and tender vegan coffee cake with cinnamon crumble topping! This delicious and easy-to-make crumb cake will satisfy your cravings for a "buttery" cake. It\'s perfect for breakfast or dessert and the recipe is plant-based (dairy-free, egg-free), gluten-free, and can be made refined sugar-free.',
            self.harvester_class.description(),
        )
