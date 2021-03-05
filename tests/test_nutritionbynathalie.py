from recipe_scrapers.nutritionbynathalie import NutritionByNathalie
from tests import ScraperTest


class TestNutritionByNathalieScraper(ScraperTest):

    scraper_class = NutritionByNathalie

    def test_host(self):
        self.assertEqual("nutritionbynathalie.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.nutritionbynathalie.com/single-post/2020/07/30/Mexican-Cauliflower-Rice",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Mexican Cauliflower Rice")

    def test_yields(self):
        self.assertEqual(None, self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://static.wixstatic.com/media/d3b5ba_7ae468273837425aa869486557b06bac~mv2.jpg/v1/fill/w_473,h_565,al_c,q_80,usm_0.66_1.00_0.01/d3b5ba_7ae468273837425aa869486557b06bac~mv2.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 bag fresh or frozen cauliflower rice (if using fresh cauliflower rice, add olive oil, avocado oil or coconut oil to pan)",
                "1-2 Tbsp olive oil",
                "1/4 teaspoon turmeric",
                "1/4 teaspoon cayenne pepper (optional)",
                "1/2 teaspoon garlic powder",
                "3/4 cup salsa",
                "vegan chive or scallion cream cheese",
                "fresh cilantro, chopped",
                "sea salt and pepper to taste",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Heat a pan on medium heat with oil.\nAdd the cauliflower and allow it to cook for about 5 minutes (should be nearly fully cooked).\nTurn heat down to low and add turmeric, cayenne, garlic powder, salsa, salt and pepper and continue to cook until done (about 2-3 more minutes).\nStir in vegan cream cheese and cilantro. Serve immediately and enjoy!",
            self.harvester_class.instructions(),
        )
