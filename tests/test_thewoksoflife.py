from recipe_scrapers.thewoksoflife import Thewoksoflife
from tests import ScraperTest


class TestThewoksoflifeScraper(ScraperTest):

    scraper_class = Thewoksoflife

    def test_host(self):
        self.assertEqual("thewoksoflife.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://thewoksoflife.com/whole-wheat-mantou/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "The Perfect Whole Wheat Mantou Recipe"
        )

    def test_yields(self):
        self.assertEqual("12 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://thewoksoflife.com/wp-content/uploads/2018/01/whole-wheat-mantou-9-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 \u2154 cups warm milk ((400 ml))",
                "1 teaspoon active dry yeast ((3 grams))",
                "1 tablespoon sugar ((12 grams))",
                "2 \u00be cups all-purpose flour ((400 grams))",
                "1\u00bc to 1\u00bd cups whole wheat flour ((about 170-200 grams; how much you\u2019ll need is dependent on the humidity in your kitchen))",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertTrue(
            self.harvester_class.instructions().startswith(
                "Heat the milk until warm to the touch (not hot). Then "
            )
        )
        self.assertEqual(len(self.harvester_class.instructions()), 1786)
