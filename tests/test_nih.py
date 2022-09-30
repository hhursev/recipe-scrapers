from recipe_scrapers.nihhealthyeating import NIHHealthyEating
from tests import ScraperTest

# test recipe's URL
# https://healthyeating.nhlbi.nih.gov/recipedetail.aspx?cId=0&rId=188


class TestNIHHealthyEatingRecipesScraper(ScraperTest):

    scraper_class = NIHHealthyEating

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
        self.assertCountEqual(
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
        self.assertCountEqual(
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
