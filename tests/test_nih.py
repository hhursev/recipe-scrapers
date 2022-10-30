from recipe_scrapers.nihhealthyeating import IngredientGroup, NIHHealthyEating
from tests import ScraperTest

# test recipe's URL
# https://healthyeating.nhlbi.nih.gov/recipedetail.aspx?cId=0&rId=188


class TestNIHHealthyEatingRecipesScraper(ScraperTest):

    scraper_class = NIHHealthyEating
    test_file_name = "nihhealthyeating_1"

    def test_host(self):
        self.assertEqual("healthyeating.nhlbi.nih.gov", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Baked Tilapia With Tomatoes")

    def test_description(self):
        self.assertEqual(
            "This dish is easy to prepare, low in calories, and economical.",
            self.harvester_class.description(),
        )

    def test_recipe_source(self):
        self.assertEqual(
            "Delicious Heart Healthy Latino Recipes",
            self.harvester_class.recipe_source(),
        )

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_prep_time(self):
        self.assertEqual(10, self.harvester_class.prep_time())

    def test_cook_time(self):
        self.assertEqual(25, self.harvester_class.cook_time())

    def test_serving_size(self):
        self.assertEqual("1 fillet", self.harvester_class.serving_size())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_nutrients(self):
        self.assertEqual(
            {
                "calories": "265",
                "Total fat": "16 g",
                "Saturated fat": "2 g",
                "Cholesterol": "58 mg",
                "Sodium": "172 mg",
                "Total fiber": "3 g",
                "Protein": "22 g",
                "Carbohydrates": "9 g",
                "Potassium": "635 mg",
            },
            self.harvester_class.nutrients(),
        )

    def test_image(self):
        self.assertEqual(
            "https://healthyeating.nhlbi.nih.gov/images/food/Baked_Tilapia_With_Tomatoes.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "Cooking spray",
                "4 tilapia fillets",
                "4 medium tomatoes, peeled and chopped",
                "2 Tbsp olive oil",
                "1½ tsp thyme",
                "¼ C pitted black olives, diced",
                "¼ tsp red pepper flakes",
                "2 cloves garlic, minced",
                "½ C red onion, diced",
                "1 Tbsp lime juice",
                "Parsley and lemon wedges for garnish",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat oven to 400 °F.\nSpray baking dish with cooking spray.\nArrange fillets in the baking dish. The dish should be large enough so the fillets do not overlap.\nMix remaining ingredients, except parsley and lemon wedges, in a bowl.\nSpoon the tomato mixture evenly over the fillets.\nBake uncovered 15 to 20 minutes or until the fish flakes easily with a fork.\nGarnish with parsley and a lemon wedge, and serve.",
            self.harvester_class.instructions(),
        )

    def test_recipe_cards(self):
        self.assertEqual(
            [
                {
                    "size": '4" x 6" (353 KB)',
                    "url": "http://www.nhlbi.nih.gov/health/public/heart/obesity/wecan/downloads/baked-tilapia-4x6.pdf",
                },
                {
                    "size": '8.5" x 11" (403 KB)',
                    "url": "http://www.nhlbi.nih.gov/health/public/heart/obesity/wecan/downloads/baked-tilapia-letter.pdf",
                },
            ],
            self.harvester_class.recipe_cards(),
        )


# test recipe's URL
# https://healthyeating.nhlbi.nih.gov/recipedetail.aspx?linkId=11&cId=1&rId=5


class TestNIHHealthyEatingRecipesVariationScraper(ScraperTest):

    scraper_class = NIHHealthyEating
    test_file_name = "nihhealthyeating_2"

    def test_host(self):
        self.assertEqual("healthyeating.nhlbi.nih.gov", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Broiled Sirloin With Spicy Mustard and Apple Chutney",
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 Granny Smith apple, rinsed, peeled, cored, and diced (about 1 C)",
                        "2 Tbsp shallots, minced",
                        "1 Tbsp garlic, minced (about 2–3 cloves)",
                        "½ C canned no-salt-added diced tomatoes",
                        "2 oz golden seedless raisins (about ½ C)",
                        "¼ C apple cider vinegar",
                        "2 Tbsp maple syrup",
                    ],
                    purpose="For chutney:",
                ),
                IngredientGroup(
                    ingredients=[
                        "4 beef top sirloin steaks, lean\xa0(3 oz each)",
                        "¼ tsp salt",
                        "¼ tsp ground black pepper",
                        "1 Tbsp olive oil",
                    ],
                    purpose="For steak:",
                ),
                IngredientGroup(
                    ingredients=[
                        "2 C low-sodium beef broth",
                        "2 Tbsp Dijon mustard",
                        "2 Tbsp cornstarch",
                    ],
                    purpose="For mustard dressing:",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 Granny Smith apple, rinsed, peeled, cored, and diced (about 1 C)",
                "2 Tbsp shallots, minced",
                "1 Tbsp garlic, minced (about 2–3 cloves)",
                "½ C canned no-salt-added diced tomatoes",
                "2 oz golden seedless raisins (about ½ C)",
                "¼ C apple cider vinegar",
                "2 Tbsp maple syrup",
                "4 beef top sirloin steaks, lean\xa0(3 oz each)",
                "¼ tsp salt",
                "¼ tsp ground black pepper",
                "1 Tbsp olive oil",
                "2 C low-sodium beef broth",
                "2 Tbsp Dijon mustard",
                "2 Tbsp cornstarch",
            ],
            self.harvester_class.ingredients(),
        )
        # check length of ingredients() === sum of lengths of ingredient_groups()
        self.assertEqual(
            len(self.harvester_class.ingredients()),
            sum(
                [len(ig.ingredients) for ig in self.harvester_class.ingredient_groups()]
            ),
        )

    def test_recipe_cards(self):
        self.assertEqual(None, self.harvester_class.recipe_cards())


# test recipe's URL
# https://healthyeating.nhlbi.nih.gov/recipedetail.aspx?linkId=0&cId=10&rId=163


class TestNIHHealthyEatingRecipesEdgeCaseScraper(ScraperTest):

    scraper_class = NIHHealthyEating
    test_file_name = "nihhealthyeating_3"

    def test_host(self):
        self.assertEqual("healthyeating.nhlbi.nih.gov", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Fruit Skewers With Yogurt Dip")

    def test_recipe_source(self):
        self.assertEqual(
            "Deliciously Healthy Family Meals",
            self.harvester_class.recipe_source(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 C strawberries, rinsed, stems removed, and cut in half",
                        "¼ C fat-free plain yogurt",
                        "1/8 tsp vanilla extract",
                        "1 Tbsp honey",
                    ],
                    purpose="For dip:",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 C strawberries, rinsed, stems removed, and cut in half",
                        "1 C fresh pineapple, diced (or canned pineapple chunks in juice, drained)",
                        "½ C blackberries",
                        "1 tangerine or Clementine, peeled and cut into 8 segments",
                        "8 6-inch wooden skewers",
                    ],
                    purpose=None,
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 C strawberries, rinsed, stems removed, and cut in half",
                "¼ C fat-free plain yogurt",
                "1/8 tsp vanilla extract",
                "1 Tbsp honey",
                "1 C strawberries, rinsed, stems removed, and cut in half",
                "1 C fresh pineapple, diced (or canned pineapple chunks in juice, drained)",
                "½ C blackberries",
                "1 tangerine or Clementine, peeled and cut into 8 segments",
                "8 6-inch wooden skewers",
            ],
            self.harvester_class.ingredients(),
        )
        # check length of ingredients() === sum of lengths of ingredient_groups()
        self.assertEqual(
            len(self.harvester_class.ingredients()),
            sum(
                [len(ig.ingredients) for ig in self.harvester_class.ingredient_groups()]
            ),
        )
