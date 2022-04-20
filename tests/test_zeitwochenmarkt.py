from recipe_scrapers.zeitwochenmarkt import ZeitWochenmarkt
from tests import ScraperTest

# test recipe's URL
# https://www.zeit.de/zeit-magazin/wochenmarkt/2021-08/kohlrabi-fenchel-carpaccio-fior-di-latte-rezept


class TestZeitWochenmarktScraper(ScraperTest):

    scraper_class = ZeitWochenmarkt

    def test_host(self):
        self.assertEqual("zeit.de", self.harvester_class.host())

    def test_title(self):
        self.assertEqual("Kohlrabi-Fenchel-Carpaccio", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_language(self):
        self.assertEqual("de", self.harvester_class.language())

    def test_image(self):
        self.assertEqual(
            "https://img.zeit.de/zeit-magazin/wochenmarkt/2021-08/kohlrabi-fenchel-carpaccio/wide__1300x731",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                '1 Kugel "Fior di Latte" (oder eine Burrata)',
                "1 Kohlrabi (klein)",
                "1 Fenchelknolle",
                "1/2 Bund Basilikum",
                "2 EL Pistazienkerne",
                "4 EL Olivenöl",
                "2 EL Zitronensaft",
                "1 TL Honig",
                "Salz",
                "Pfeffer",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        instructions = """Den Kohlrabi schälen, den Fenchel waschen. Beide vom unteren Strunk befreien. Den Kohlrabi einmal von der Spitze zum Boden in der Mitte durchschneiden. Nun beide Gemüse mit einem scharfen und stabilen Messer hauchdünn schneiden, bessere Ergebnisse erzielt man auf einer Mandoline. Idealerweise sind die Scheiben so dünn, dass man fast hindurchschauen kann.
Nun aus dem Olivenöl, dem Zitronensaft und Honig ein Dressing zusammenrühren, mit Salz und Pfeffer abschmecken. Die dünnen Gemüsescheiben fächerartig auf einen großen Teller legen, den Käse zerreißen und darauf verteilen. Das Dressing darübergeben und mit Basilikum und Pistazien servieren."""
        self.assertEqual(instructions, self.harvester_class.instructions())
