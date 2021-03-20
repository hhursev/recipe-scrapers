from recipe_scrapers.template import Template
from tests import ScraperTest


class TestTemplateScraper(ScraperTest):

    scraper_class = Template

    def test_host(self):
        self.assertEqual("example.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual(None, self.harvester_class.author())

    def test_title(self):
        self.assertEqual(None, self.harvester_class.title())

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
