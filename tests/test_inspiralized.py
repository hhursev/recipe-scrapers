from recipe_scrapers.inspiralized import Inspiralized
from tests import ScraperTest


class TestInspiralizedScraper(ScraperTest):

    scraper_class = Inspiralized

    def test_host(self):
        self.assertEqual("inspiralized.com", self.harvester_class.host())

    def test_language(self):
        self.assertEqual("en-US", self.harvester_class.language())

    def test_canonical_url(self):
        self.assertEqual(
            "https://inspiralized.com/brussels-sprouts-and-apple-salad-with-parmesan/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Brussels Sprouts and Apple Salad with Parmesan",
        )

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "3 tablespoons extra virgin olive oil",
                "3 tablespoons apple cider vinegar",
                "2.5 teaspoons honey",
                "salt and pepper",
                "4 cups shredded brussels sprouts",
                "1 medium apple, Blade D",
                "1/4 cup chopped raw almonds (for extra flavor, toast these first)",
                "1/3 cup shaved Parmesan",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "In a large bowl, whisk together the olive oil, apple cider vinegar, honey, and season with salt and pepper. Add the brussels sprouts and apples and toss well. Let sit in the refrigerator for at least 15-20 minutes and then take out and fold in the almonds and half of the Parmesan cheese. Transfer to a serving bowl or plate and top with remaining Parmesan.",
            self.harvester_class.instructions(),
        )
