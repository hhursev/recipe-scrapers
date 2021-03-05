from recipe_scrapers.geniuskitchen import GeniusKitchen
from tests import ScraperTest


class TestGeniusKitchenScraper(ScraperTest):

    scraper_class = GeniusKitchen

    def test_host(self):
        self.assertEqual("geniuskitchen.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.geniuskitchen.com/recipe/quiche-lorraine-cups-19170",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Quiche Lorraine Cups")

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "12 cooked crepes (, see All Purpose Dinner Crepes Batter)",
                "4 slices bacon, cooked crisp &,crumbled",
                "1 cup swiss cheese, grated",
                "2 tablespoons flour",
                "1⁄4 teaspoon salt",
                "2 eggs",
                "1 cup milk",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Lightly grease a 12 muffin pan or 12 custard cups.\nLine each with a crepe, fluting them.\nSprinkle bacon into the crepes.\nDivide the cheese between the crepes.\nMix together the flour, salt.\nMix the beaten eggs and milk, add to the flour.\nBlend well and pour into the crepes on top of the cheese.\nBake in 350F oven for 15-20 minutes or until firm.\nCool 5 minutes before removing from pan.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
