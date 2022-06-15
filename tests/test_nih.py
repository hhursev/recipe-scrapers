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

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

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
