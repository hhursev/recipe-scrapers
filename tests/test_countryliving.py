from recipe_scrapers.countryliving import CountryLiving
from tests import ScraperTest


class TestCountryLivingScraper(ScraperTest):

    scraper_class = CountryLiving

    def test_host(self):
        self.assertEqual("countryliving.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.countryliving.com/food-drinks/a32042602/roasted-mushroom-and-bacon-dutch-baby/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Roasted Mushroom and Bacon Dutch Baby"
        )

    def test_total_time(self):
        self.assertEqual(70, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 lb. mixed mushrooms (such as cremini, beech, or shiitake), roughly chopped 4 slices bacon, sliced",
                "3 large eggs",
                "1 clove garlic, chopped",
                "3/4 c. whole milk",
                "3 tbsp. unsalted butter, melted, divided",
                "1/2 c. all-purpose flour, spooned and leveled",
                "2 tbsp. cornstarch",
                "Kosher salt",
                "1 tbsp. fresh thyme",
                "2 oz. fontina or Cheddar cheese, grated (about 1/2 cup)",
                "1 scallion, thinly sliced",
                "2 tbsp. chopped flat-leaf parsley",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Set oven racks in middle and upper positions. Preheat oven to 450°F. Place mushrooms and bacon on a rimmed baking sheet. Place on top rack in oven while preheating, and roast, stirring once, until mushrooms are golden brown, 25 to 30 minutes. Place a 10-inch cast-iron skillet on middle rack and heat 15 minutes.\nPlace eggs and garlic in a blender. Process on high until frothy, 45 seconds. With blender running, gradually add milk and 2 tablespoons butter; stop blender. Add flour, cornstarch, and 1/4 teaspoon salt; process 1 minute. Fold in thyme.\nCarefully add remaining tablespoon butter to heated skillet and swirl to coat. Immediately add batter. Bake until golden brown and puffed, 14 to 16 minutes. Sprinkle with cheese and bake until melted, 3 to 5 minutes.\nTop with mushroom mixture, scallions, and parsley.",
            self.harvester_class.instructions(),
        )
