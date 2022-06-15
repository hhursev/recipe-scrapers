from recipe_scrapers.finedininglovers import FineDiningLovers
from tests import ScraperTest


class TestFineDiningLoversScraper(ScraperTest):

    scraper_class = FineDiningLovers

    @property
    def test_file_name(self):
        return "{}_2".format(self.scraper_class.__name__.lower())

    def test_host(self):
        self.assertEqual("finedininglovers.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.finedininglovers.com/recipes/appetizer/avocado-and-blue-cheese-dip",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Avocado and Blue Cheese Dip")

    def test_total_time(self):
        self.assertEqual(15.0, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "Blue Cheese 150 g, crumbled",
                "Cream 2 tbsp, at least 30% fat",
                "Shallots 1, finely chopped",
                "Avocado 2, flesh scraped out",
                "Lemon Juice 2 tbsp",
                "Nutmeg",
                "Breadsticks 20 sticks",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "To prepare the avocado dip with blue cheese start squashing the cheese with a fork whilst adding the cream.\nStir in the shallot.\nDrizzle the avocado fruit with lemon juice.\nSquash with a fork and mix in with the cheese mixture.\nSeason with salt, ground white pepper and a pinch of nutmeg, then fill in small cups or glasses.\nServe the avocado and blue cheese dip with 5 grissini sticks.",
            self.harvester_class.instructions(),
        )

    def test_image(self):
        return self.assertEqual(
            "https://www.finedininglovers.com/sites/g/files/xknfdk626/files/styles/recipes_1200_800_fallback/public/Original_14003_avocado-blue-cheese.jpg",
            self.harvester_class.image(),
        )
