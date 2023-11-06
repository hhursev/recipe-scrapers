# mypy: allow-untyped-defs

from recipe_scrapers.zaubertopf import ZauberTopf
from tests import ScraperTest


class TestZauberTopfScraper(ScraperTest):
    scraper_class = ZauberTopf

    def test_host(self):
        self.assertEqual("zaubertopf.de", self.harvester_class.host())

    def canonical_url(self):
        self.assertEqual(
            "https://www.zaubertopf.de/wikinger-auflauf-monsieur-cuisine/",
            self.harvester_class.host(),
        )

    def test_author(self):
        self.assertEqual("mein ZauberTopf", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Wikinger-Auflauf mit dem Monsieur Cuisine", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Monsieur Cuisine", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(46, self.harvester_class.total_time())

    def test_image(self):
        self.assertEqual(
            "https://www.zaubertopf.de/wp-content/uploads/2022/10/Wikinger-Auflauf-mit-dem-Monsieur-Cuisine_44778-640x640.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "250 g Schweinefleisch, in Stücken",
                "250 g Rindfleisch, in Stücken",
                "1 Ei",
                "1,5 TL mittelscharfer Senf",
                "1 TL edelsüßes Paprikapulver",
                "Salz",
                "frisch gemahlener schwarzer Pfeffer",
                "2 EL Sonnenblumenöl zum Braten",
                "40 g Butter, in Stücken, zzgl. etwas mehr zum Fetten",
                "40 g Weizenmehl Type 405",
                "350 g Sahne",
                "350 g Milch",
                "1 TL getrocknete Kräuter (Thymian, Oregano)",
                "1 Msp. frisch geriebene Muskatnuss",
                "600 g Kartoffeln, in kleinen Würfeln",
                "500 g Hokkaidokürbis, in kleinen Würfeln",
                "200 g Karotten, in kleinen Würfeln",
                "200 g Erbsen (TK)",
                "Petersilie zum Garnieren",
                "Auflaufform (Ø ca. 26 cm)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        expected_instructions = (
            "Das Fleisch flach in einen Gefrierbeutel geben und für etwa 45 Min. in das Gefrierfach legen.\n"
            "Den Backofen auf 200 °C Ober-/Unterhitze vorheizen. Das angefrorene Fleisch in den Mixbehälter geben und 12 Sek. | Stufe 7 zerkleinern. Je nach gewünschter Feinheit das Fleisch mit dem Spatel nach unten schieben und erneut 10 Sek. | Stufe 7 zerkleinern.\n"
            "Ei, Senf, Paprikapulver, 1,5 TL Salz und 0,5 TL Pfeffer hinzufügen und 25 Sek. | Linkslauf | Stufe 3 vermengen. Aus der Masse 12 Bällchen formen und in einer Pfanne mit dem Öl scharf anbraten. Den Mixtopf spülen.\n"
            "Butter in den Mixbehälter geben und 2 Min. | Stufe 2 | 100 °C erhitzen. Mehl zufügen und 1 Min. | Stufe 2 | 100 °C anschwitzen. Sahne, Milch, Kräuter, 1 TL Salz, 3 Prisen Pfeffer sowie Muskat in den Mixbehälter geben und alles 6 Min. | Stufe 3 | 90 °C aufkochen.\n"
            "Die Soße mit Gemüse und Hackbällchen in die Auflaufform geben und im heißen Ofen ca. 45–50 Min. backen. Anschließend aus dem Ofen nehmen und mit Petersilie garniert servieren."
        )

        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_description(self):
        self.assertEqual(
            "Dieser Wikinger-Auflauf vereint feine Hackbällchen mit Gemüse in einer köstlichen Sahnesoße. Kein Wunder, dass er bei Familien so beliebt ist. Die Zubereitung mit dem Monsieur Cuisine ist ganz einfach. Er zaubert dir sogar das Hackfleisch für die leckeren Bällchen. Hier unser Rezept, probiere es doch gleich mal aus!",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("de-DE", self.harvester_class.language())
