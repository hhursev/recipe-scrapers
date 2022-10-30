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
            "Was ist eigentlich Naan-Brot?Als Naan-Brot bezeichnet man dünne Teigfladen aus mit Joghurt gesäuertem Hefeteig, die traditionell über dem offenen Feuer gebacken werden. In unserem Rezept übernimmt diesen Part eine heiße Pfanne. Einfaches Naan-Brot wird ausschließlich mit Salz gewürzt und typischerweise als Beilage zu heißen Gerichten wie Currys und Fleischgerichten gereicht werden. Naan-Brot Rezept - Zutaten für 6 Stück:75 ml Milch1 TL Zucker1 TL Trockenhefe1/2 TL Salz250 g + etwas Mehl1 EL Öl75 g Vollmilchjoghurt1 Ei (Gr. M) Naan-Brot Rezept - Schritt 1:Erst kommt der Löffel - dann die Hände zum EinsatzDen Backofen auf ca. 50 °C vorheizen. 75 ml Milch lauwarm erwärmen und mit 1 TL Zucker sowie 1 TL Trockenhefe verrühren. Anschließend 25 Minuten ruhen lassen. 250 g Mehl und 1/2 TL Salz mischen. Hefemilch, 1 EL Öl, 75 g Joghurt und 1 Ei zugeben. Die Teigzutaten mit einem Kochlöffel verrühren. Dann mit den Händen zu einem geschmeidigen, glatten Teig verkneten. Naan-Brot Rezept - Schritt 2:Den Teig für das Naan-Brot mit einem Küchentuch abdecken und im warmen Ofen ca. 1 Stunde gehen lassen, bis sich das Volumen verdoppelt hat. Den Teig nach dem Gehen auf einer bemehlten Arbeitsfläche noch einmal kräftig durchkneten. Dadurch wird er elastischer und besser formbar. Anschließend zu 6 Kugeln formen und diese nochmals 15 Minuten ruhen lassen.Naan-Brot Rezept- Schritt 3:Das Brot lässt sich am besten mit dem Pfannenwender drehenDie Kugeln mit der Teigrolle jeweils zu ca. 1/2 cm dünnen ovalen Fladen à ca. 18 x 10 cm ausrollen. Eine Pfanne* ohne Fett erhitzen. Die Brotfladen darin bei starker Hitze nacheinander von jeder Seite 1-2 Minuten golbraun braten. Wenn das Brot blasen wirft, wenden und von der anderen Seite braten.Tipps: Ein Pfanne aus Gusseisen ist aufgrund ihrer natürlichen Beschichtung am besten zum Braten von Naan-Brot geeignet. Mit frischem Koriander, Knoblauch oder Kümmel im Grundteig sorgst du je nach Gusto im Handumdrehen für geschmackliche Vielfalt. Schnelle Teig-Variante mit BackpulverFür die Zubereitung des Hefeteigs muss man etwas Zeit einplanen. Wenn es mal schnell gehen soll, kann man auch eine Naan-Brot-Variante mit Backpulver backen. Für das Rezept 250 g Mehl, 1 TL Zucker, 1 TL Backpulver sowie einen 1/2 TL Salz in einer Schüssel mischen. 75 g Vollmilchjoghurt zugeben und alles zunächst mit einem Kochlöffel verrühren und anschließen mit den Händen zu einem geschmeidigen Teig verkneten.Aus dem Teig 6 gleich große Kugeln formen und diese auf bemehlter Arbeitsfläche mit der Teigrolle zu dünnen Fladen à ca. 18 x 10 cm ausrollen. Eine Pfanne erhitzen und die Brotfladen darin bei starker Hitze von jeder Seite 1-2 Minuten braten. Sobald das Brot blasen wirft, wenden und weiterbraten.Tipp: Für echte Brotliebhaber empfehlen wir einen Brotbackautomaten Und dazu schmeckt Naan-Brot besonders gut: Indisches Essen weiterlesen Curry-Rezepte weiterlesen",
            self.harvester_class.instructions(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [],
            self.harvester_class.ingredients(),
        )
