from recipe_scrapers.przepisy import Przepisy
from tests import ScraperTest

# test recipe's URL
# https://www.przepisy.pl/przepis/placki-ziemniaczane


class TestPrzepisyScraper(ScraperTest):

    scraper_class = Przepisy

    def test_host(self):
        self.assertEqual("przepisy.pl", self.harvester_class.host())

    def test_language(self):
        self.assertEqual("pl", self.harvester_class.language())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.przepisy.pl/przepis/placki-ziemniaczane",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Placki ziemniaczane", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "ziemniaki 1 kilogram",
                "cebula 1 sztuka",
                "jajka 2 sztuki",
                "Przyprawa w Mini kostkach Czosnek Knorr 1 sztuka",
                "Gałka muszkatołowa z Indonezji Knorr 1 szczypta",
                "sól 1 szczypta",
                "mąka 3 łyżki",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Obierz ziemniaki, zetrzyj na tarce. Odsącz masę przez sito. Zetrzyj cebulę na tarce.\nDodaj do ziemniaków cebulę, jajka, gałkę muszkatołową oraz mini kostkę Knorr.\nWymieszaj wszystko dobrze, dodaj mąkę, aby nadać masie odpowiednią konsystencję.\nRozgrzej na patelni olej, nakładaj masę łyżką. Smaż placki z obu stron na złoty brąz i od razu podawaj.",
            self.harvester_class.instructions(),
        )
