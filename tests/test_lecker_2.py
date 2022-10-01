from recipe_scrapers.lecker import Lecker
from tests import ScraperTest


class TestLeckerScraper(ScraperTest):

    scraper_class = Lecker

    @property
    def test_file_name(self):
        return "{}_2".format(self.scraper_class.__name__.lower())

    def test_host(self):
        self.assertEqual("lecker.de", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            "Naan-Brot backen - so geht das Rezept",
            self.harvester_class.title(),
        )

    def test_image(self):
        self.assertEqual(
            "https://www.lecker.de/assets/field/image/naan-brot-b_0.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertIn(
            "Als Naan-Brot bezeichnet man dünne Teigfladen aus m",
            self.harvester_class.instructions(),
        )
