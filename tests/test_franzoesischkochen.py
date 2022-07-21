from recipe_scrapers.franzoesischkochen import FranzoesischKochen
from tests import ScraperTest


class TestFranzoesischKochenScraper(ScraperTest):

    scraper_class = FranzoesischKochen

    def test_host(self):
        self.assertEqual("franzoesischkochen.de", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Aurélie Bastian", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Tourte mit Feigen und Confit de canard", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(90, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual(None, self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.franzoesischkochen.de/wp-content/uploads/2020/09/Tourte-confit-de-canard.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "4-5 Feigen",
                "1 Confit de Canard (Brust bei mir oder 2 Keulen)",
                "3 Schalotten",
                "200-250 g Pfifferlingen",
                "1 Nelke",
                "1 Lorbeerblatt",
                "3 Kardamomkapseln",
                "1 TL Kastanien Honig",
                "150 ml Rotwein (optional)",
                "Rosmarin",
                "Thymian",
                "Salz und Pfeffer",
                "1 Rolle Blätterteig (Quadratisch",
                "oder 2 runde)",
                "50 g gehobelte Mandeln",
                "Milch zum Pinseln.",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "1- Die Schalotten schälen und in dünnen Scheiben schneiden....",
                    "2- In einer großen Pfanne 2-3 EL Entenfett (aus den Confit Dose) geben ... und erhitzen...",
                    "3- In einer kleinen Pfanne die gehobelten Mandeln kurz anbraten. Auf die Seite stellen.",
                    "4- Die Feigen in kleinen Scheiben schneiden und in einer Pfanne mit ein bisschen Rotwein (oder Wasser) und dem Kardamom köcheln lassen...",
                    "5- Den Blätterteig ausrollen, halbieren und in einen 20 cm Ring (oder eine Backform legen).",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())
