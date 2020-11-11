from tests import ScraperTest

from recipe_scrapers.nutritionbynathalie import NutritionByNathalie


class TestNutritionByNathalieScraper(ScraperTest):

    scraper_class = NutritionByNathalie

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
