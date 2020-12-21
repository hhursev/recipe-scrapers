from tests import ScraperTest

from recipe_scrapers.yummly import Yummly


class TestYummlyScraper(ScraperTest):

    scraper_class = Yummly

    def test_host(self):
        self.assertEqual("yummly.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.yummly.com/recipe/Carrot-Milk-shake-1099424",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Carrot Milk shake")

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertSetEqual(
            set(
                [
                    "3 teaspoons sugar",
                    "4 cashew",
                    "1 1/2 cups milk",
                    "100 grams carrot",
                    "1 cardamom",
                ]
            ),
            set(self.harvester_class.ingredients()),
        )

    def test_instructions(self):
        return self.assertEqual("", self.harvester_class.instructions())
