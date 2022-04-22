from recipe_scrapers.innit import Innit
from tests import ScraperTest


class TestInnitScraper(ScraperTest):

    scraper_class = Innit

    def test_host(self):
        self.assertEqual("innit.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            "Tofu Mixed Greens Salad with Broccoli Beet Mix & Carrot Ginger Dressing",
            self.harvester_class.title(),
        )

    def test_total_time(self):
        self.assertEqual(51, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 Carrots",
                "1 piece Fresh Ginger",
                "1/2 Orange",
                "1 Tbsp Fresh Chives",
                "2 cups Broccoli",
                "1 lb Precooked Beets",
                "2 Tbsp Italian Parsley",
                "4 cups Fresh Spring Mix",
                "2 packages Extra Firm Tofu",
                "1 Tbsp Miso Paste",
                "1/2 tsp Sesame Seed Oil",
                "1/2 Tbsp Honey",
                "1 1/3 tsp Kosher Salt",
                "2/3 cup Olive Oil",
                "2 pinches Black Pepper",
                "1/4 cup Rice Wine Vinegar",
                "1 cup Sunflower Seeds",
            ],
            self.harvester_class.ingredients(),
        )

    def test_nutrients(self):
        self.assertEqual(
            {
                "sugarContent": "18 g",
                "proteinContent": "32 g",
                "fiberContent": "11 g",
                "unsaturatedFatContent": "55 g",
                "fatContent": "64 g",
                "cholesterolContent": "0 mg",
                "calories": "830 kcal",
                "carbohydrateContent": "34 g",
                "saturatedFatContent": "9 g",
                "sodiumContent": "1060 mg",
            },
            self.harvester_class.nutrients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Preheat
Preheat the oven to 425F.
Line sheet pan with foil.
Sear Tofu
Drain, pat dry & prepare tofu.
Heat pan on high heat for 2 minutes.
Cook for 7 min or until golden brown on all sides, seasoning half way.
Remove from pan.
Bake Broccoli
Toss broccoli with oil & salt.
Bake for 22 minutes.
Simmer Carrots & Ginger
Prepare ingredients.
Pre-heat pan. Add all ingredients; cover with water.
Cook until soft, about 5 minutes.
Blend Dressing Ingredients
Transfer carrot-ginger mixture to blender.
Add orange juice/zest, miso, sesame oil, honey, rice vinegar.
Blend until smooth.
Let cool in fridge for 10 minutes. Fold in chives & season.
Flavor Beets
Toss beets in oil. Season with salt, pepper & parsley.
Toast Sunflower Seeds
Combine ingredients.
Toast in oven for 5 - 7 min or until golden brown.
Mixed Greens
Wash greens & dry.
Serve and Enjoy!
Pair with your favorite music!""",
            self.harvester_class.instructions(),
        )

    def test_image(self):
        self.assertEqual(
            "https://www.innit.com/meal-service/en-US/images/Meal-Salads%3A%20Blended-Carrot_Ginger_Dressing%2BAssembled-Broccoli_Beet_Mix%2BSeared-Tofu-Diced%2BOlive_Oil%2BPrepared-Mixed_Greens_480x480.png",
            self.harvester_class.image(),
        )
