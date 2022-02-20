from recipe_scrapers.kptncook import KptnCook
from tests import ScraperTest


class TestKptnCookScraper(ScraperTest):

    scraper_class = KptnCook

    def test_host(self):
        self.assertEqual("mobile.kptncook.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual(None, self.harvester_class.author())

    def test_title(self):
        self.assertEqual(None, self.harvester_class.title())

    def test_category(self):
        self.assertEqual(None, self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(None, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual(None, self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(None, self.harvester_class.image())

    def test_ingredients(self):
        self.assertEqual(None, self.harvester_class.ingredients())

    def test_instructions(self):
        self.assertEqual(None, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(None, self.harvester_class.description())
