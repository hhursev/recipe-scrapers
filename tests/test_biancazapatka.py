from recipe_scrapers.biancazapatka import BiancaZapatka
from tests import ScraperTest


class TestBiancaZapatkaScraper(ScraperTest):

    scraper_class = BiancaZapatka

    def test_host(self):
        self.assertEqual("biancazapatka.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual('Bianca Zapatka', self.harvester_class.author())

    def test_title(self):
        self.assertEqual('Rice Noodle Salad with Tempeh and Peanut Sauce', self.harvester_class.title())

    def test_category(self):
        self.assertEqual('Lunch &amp; Dinner,Main Course', self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual('4 servings', self.harvester_class.yields())

    def test_image(self):
        self.assertEqual('https://biancazapatka.com/wp-content/uploads/2022/07/buddha-bowl-sauce.jpg', self.harvester_class.image())

    def test_ingredients(self):
        self.assertEqual(['7 oz Tempeh (oder Tofu)', '2 garlic clo[654 chars]uts'], self.harvester_class.ingredients())

    def test_instructions(self):
        self.assertEqual('Marinated Tempeh\nFor the marinade, pour[1078 chars]joy!', self.harvester_class.instructions())

    def test_cuisine(self):
        self.assertEqual('Asian', self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual('This colorful Tempeh Rice Noodle Salad B[309 chars]nce!', self.harvester_class.description())
