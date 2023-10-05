from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.bigoven import BigOven
from tests import ScraperTest


class TestBigOven(ScraperTest):

    scraper_class = BigOven
    test_file_name = "bigoven_2"

    def test_host(self):
        self.assertEqual("bigoven.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.bigoven.com/recipe/white-chocolate-raspberry-cupcakes/165783",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Kimography", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "White Chocolate Raspberry Cupcakes", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Desserts", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://bigoven-res.cloudinary.com/image/upload/h_320,w_320,c_fill/white-chocolate-raspberry-cupc-bd2bf9.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "8 tablespoons Butter ; at room temp",
            "3/4 cup Sugar",
            "1 1/4 cups Flour",
            "1/4 teaspoon Baking soda",
            "1 teaspoon Baking Powder",
            "1/4 teaspoon Kosher salt",
            "2 Eggs ; at room temp",
            "1/4 cup Sour cream",
            "1/2 teaspoon Raspberry extract",
            "1/3 cup White chocolate chips",
            "1/2 cup cream cheese",
            "1 cup sifted powdered sugar",
            "1/2 teaspoon vanilla extract",
            "1/4 cup butter ; room temp.",
            "1/2 pint fresh raspberries",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "8 tablespoons Butter ; at room temp",
                        "3/4 cup Sugar",
                        "1 1/4 cups Flour",
                        "1/4 teaspoon Baking soda",
                        "1 teaspoon Baking Powder",
                        "1/4 teaspoon Kosher salt",
                        "2 Eggs ; at room temp",
                        "1/4 cup Sour cream",
                        "1/2 teaspoon Raspberry extract",
                        "1/3 cup White chocolate chips",
                    ],
                    purpose=None,
                ),
                IngredientGroup(
                    ingredients=[
                        "1/2 cup cream cheese",
                        "1 cup sifted powdered sugar",
                        "1/2 teaspoon vanilla extract",
                        "1/4 cup butter ; room temp.",
                        "1/2 pint fresh raspberries",
                    ],
                    purpose="Icing:",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "1.Preheat the oven to 350F degrees. Line a muffin pan with 8 liners. Sift the flour, baking soda, baking powder, and salt.",
                    "2.Cream the butter & sugar until light and fluffy. Add the eggs one at a time. Slowly add the flour to the butter mixture. Add the sour cream & raspberry extract. Then stir in the chocolate chunks.",
                    "3.Divide the batter evenly among the liners and bake for 15-20 minutes, until done. For mini cupcakes, bake 12-14 minutes.",
                    "For the icing:",
                    "1/2 cup of cream cheese",
                    "1 cup of sifted powder sugar",
                    "1/2 tsp. of vanilla extract",
                    "1/4 cup of butter ~~at; room temp.",
                    "A half pint of fresh raspberries",
                    "Beat cream cheese, powdered sugar, vanilla, butter and raspberries until smooth. Top each cupcake with frosting and 1 raspberry, if desired.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        expected_ratings = {"count": 24, "rating": 4.0}
        self.assertEqual(expected_ratings, self.harvester_class.ratings())
