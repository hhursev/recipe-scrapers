from recipe_scrapers.finedininglovers import FineDiningLovers
from tests import ScraperTest


class TestFineDiningLoversScraper(ScraperTest):

    scraper_class = FineDiningLovers

    @property
    def test_file_name(self):
        return "{}_3".format(self.scraper_class.__name__.lower())

    def test_host(self):
        self.assertEqual("finedininglovers.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.finedininglovers.com/article/black-forest-cake-recipe",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "The Ultimate Black Forest Cake Recipe"
        )

    def test_total_time(self):
        self.assertEqual(0, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual(0, self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertIn(
            "The black forest cake or gateau, a classic German cake synonymous with the 1980s",
            self.harvester_class.instructions(),
        )

    def test_image(self):
        return self.assertEqual(
            "https://www.finedininglovers.com/sites/g/files/xknfdk626/files/styles/open_graph_image/public/2021-03/german_dark_forest_cake_%C2%A9iStock.jpg?itok=afnz-p6c",
            self.harvester_class.image(),
        )
