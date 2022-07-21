import os

from recipe_scrapers.cookstr import Cookstr
from tests import ScraperTest


class TestCookstrScraper(ScraperTest):

    scraper_class = Cookstr

    def test_host(self):
        self.assertEqual("cookstr.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.Cookstr.com/recipes/chocolate-cake-nicole-axworthy",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Chocolate Cake")

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_total_yields(self):
        self.assertEqual(None, self.harvester_class.yields())

    def test_total_yields_raises_exception(self):
        os.environ["RECIPE_SCRAPERS_SETTINGS"] = "recipe_scrapers.settings.default"

        with self.assertRaises(Exception):
            self.assertEqual(None, self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 recipe Chocolate Cake Mix",
                "1/2 cup coffee or water",
                "1/2 cup almond or soy milk (vanilla flavor preferred)",
                "1/2 cup canola oil",
                "1/2 cup pure maple syrup",
                "2 tablespoons apple cider vinegar",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat the oven to 350°F. Lightly grease a 9-inch cake pan with coconut oil or line a 12-cup muffin tin with paper liners.\nIn a large bowl, sift the dry cake mix ingredients using a fine-mesh sieve.\nIn a medium bowl, mix together the coffee, almond milk, oil, maple syrup, and vinegar.\nAdd the liquid ingredients to the bowl with the cake mix and whisk gently until there are no large clumps remaining.\nPour the batter into the prepared pan. Bake for 22 to 27 minutes in the cake pan or 20 to 25 minutes in the muffin tin. The cake/cupcakes can be stored in an airtight container in the fridge for up to 5 days or frozen for 2 to 3 months.",
            self.harvester_class.instructions(),
        )
