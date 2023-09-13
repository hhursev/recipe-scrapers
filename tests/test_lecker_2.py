from recipe_scrapers.lecker import Lecker
from tests import ScraperTest


class TestLeckerScraper2(ScraperTest):

    scraper_class = Lecker
    test_file_name = "lecker_2"

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

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Den Backofen auf ca. 50 °C vorheizen. 75 ml Milch lauwarm erwärmen und mit 1 TL Zucker sowie 1 TL Trockenhefe verrühren. Anschließend 25 Minuten ruhen lassen. 250 g Mehl und 1/2 TL Salz mischen. Hefemilch, 1 EL Öl, 75 g Joghurt und 1 Ei zugeben.\xa0Die Teigzutaten\xa0mit einem Kochlöffel verrühren. Dann mit den Händen zu einem geschmeidigen, glatten Teig verkneten.",
                    "Den Teig für das Naan-Brot mit einem Küchentuch abdecken und im warmen Ofen ca. 1 Stunde gehen lassen, bis sich das Volumen verdoppelt hat.\xa0Den Teig nach dem Gehen auf einer bemehlten Arbeitsfläche noch einmal kräftig durchkneten. Dadurch wird er elastischer und besser formbar. Anschließend\xa0zu 6 Kugeln formen und diese nochmals 15 Minuten ruhen lassen.",
                    "Die Kugeln mit der Teigrolle jeweils zu ca. 1/2 cm dünnen ovalen Fladen à ca. 18 x 10 cm ausrollen.\xa0Eine Pfanne* ohne Fett erhitzen. Die Brotfladen darin bei starker Hitze nacheinander von jeder Seite 1-2 Minuten golbraun braten. Wenn das Brot blasen wirft, wenden und von der anderen Seite braten.",
                    "Tipps: Ein Pfanne aus Gusseisen ist aufgrund ihrer natürlichen Beschichtung am besten zum Braten von Naan-Brot\xa0geeignet.\xa0Mit frischem Koriander, Knoblauch oder Kümmel im Grundteig sorgst du je nach Gusto im Handumdrehen für geschmackliche Vielfalt.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [],
            self.harvester_class.ingredients(),
        )
