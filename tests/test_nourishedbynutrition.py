from recipe_scrapers.nourishedbynutrition import NourishedByNutrition
from tests import ScraperTest


class TestNourishedByNutritionScraper(ScraperTest):

    scraper_class = NourishedByNutrition

    def test_host(self):
        self.assertEqual("nourishedbynutrition.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://nourishedbynutrition.com/healthy-salsa-verde-chicken-enchiladas-dairy-free/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Salsa Verde Chicken Enchiladas")

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://nourishedbynutrition.com/wp-content/uploads/2020/08/Salsa-Verde-Chicken-Enchiladas-8.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 cups shredded cooked chicken breast",
                "2 cups salsa verde, divided",
                "5 ounces spinach",
                "½ teaspoon garlic powder",
                "½ teaspoon ground cumin",
                "salt and pepper to taste",
                "8 tortillas (cassava flour or corn, flour, wheat, etc)",
                "½ cup Siete queso blanco (see notes for substitutions)",
                "½ avocado, thinly sliced",
                "¼ cilantro leaves",
                "2 tablespoons finely diced red onion",
                "1 lime, cut into wedges",
                "2-3 thinly sliced radishes",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat oven to 375F degrees.\nHeat a medium skillet over medium heat. Add the spinach and cover with a lid. Let spinach wilt. This should only take about 2-3 minutes. Remove from the heat and set aside.\nIn a bowl, combine the shredded chicken with the garlic powder, cumin, ½ cup of the salsa verde, and wilted spinach. Toss to coat.\nWrap them in a damp paper towel and microwave for 20-40 seconds to loosen them up so that they are easier to roll. You can also heat them directly the gas burner or in a saute pan one at a time. Pour ½ cup of the salsa verde on the bottom of a 9×13 baking dish, spread to coat the bottom.\nTo assemble the enchiladas, place about ¼ cup of chicken mixture on a tortilla. Gently roll the tortilla and place it seam side down into the prepared baking dish. Repeat with the remaining tortillas and chicken.\nPour the remaining 1 cup of salsa over the top of the enchiladas so they’re completely covered. Add the vegan queso blanco or shredded cheese of choice on top, if desired. Cover with foil. Bake for 25 minutes. Remove from oven and let sit for 5-10 minutes before topping with garnishes. Enjoy warm.",
            self.harvester_class.instructions(),
        )
