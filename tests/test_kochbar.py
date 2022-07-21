from recipe_scrapers.kochbar import Kochbar
from tests import ScraperTest


class TestKochbarScraper(ScraperTest):

    scraper_class = Kochbar

    def test_host(self):
        self.assertEqual("kochbar.de", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.kochbar.de/rezept/549118/Ligurisches-Huehnerragout-mit-Zucchini-Spezzatino-con-zucchine.html",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Ligurisches Hühnerragout mit Zucchini – Spezzatino con zucchine",
        )

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://ais.kochbar.de/kbrezept/549118_1087108/1200x1200/ligurisches-huehnerragout-mit-zucchini-spezzatino-con-zucchine-rezept-bild-nr-2.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "250 g Hühnerbrust, ohne Knochen",
                "3 mittelgross Knoblauchzehen, frisch",
                "2 TL Zitronensaft",
                "2 EL Olivenöl, extra vergine",
                "1 TL Oregano, frisch oder TK",
                "4 kleine Zwiebelchen, rot",
                "2 mittelgross Knoblauchzehen, frisch",
                "200 g Zucchini, grün",
                "1 mittelgross Kartoffel, festkochend",
                "40 g Karotte",
                "4 mit Tomaten, rot, vollreif",
                "2 EL Schnittsellerie-Stängel, frisch oder TK",
                "1 kleine Peperoni, rot, mittelscharf",
                "3 EL Olivenöl",
                "2 TL Rosmarin, frisch oder TK",
                "6 Oliven, grün, kernlos",
                "2 Prise Pfeffer, schwarz, frisch aus der Mühle",
                "2 EL Schnittsellerie-Blätter, frisch oder TK",
                "50 g Tomatensaft",
                "50 g Weißwein, trocken",
                "1 TL Zucker",
                "2 TL (gestrichen) Hühnerbrühe, Kraftbouillon",
                "Blüten und Blätter",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Die Hühnerbrust in ca. 2 x 3 cm große Stücke schneiden. Die Knoblauchzehen in eine Schale auspressen und die restlichen Zutaten zur Marinade zufügen. Die Hühnerstücke in der Marinade für ca. 1 Stunde marinieren.\nIn der Zwischenzeit für das Gemüse die Zwiebelchen und die Knoblauchzehen an beide Enden kappen, schälen und in kleine Stücke schneiden. Den Zucchino waschen, an beiden Enden kappen und längs halbieren. Die Hälften quer in ca. 8 mm dicke Scheiben schneiden. Die Kartoffel waschen, schälen, längs halbieren, die Hälften längs halbieren und quer vierteln. In Salzwasser in 15 Minuten gar kochen, das Wasser abgießen und die Kartoffeln bereit halten.\nDie Karotte waschen, an beiden Enden kappen und schälen. Mit einer groben Raspel die entsprechende Menge von unten her abraspeln. Bei den Tomaten die Stiele entfernen, häuten, vierteln und entkernen. Die Viertel längs und quer halbieren.\nDie frische Schnittsellerie waschen, trocken schütteln und die makellosen Blätter abzupfen, zerkleinern, 2 EL bereit halten und den Rest tieffrieren. Die makellosen Stiele quer in ca. 3 mm breite Röllchen schneiden und 2 EL davon bereithalten. Die restlichen Röllchen tieffrieren. TK-Ware abwiegen und auftauen lassen. Die frischen, roten Peperoni waschen, die Stiele entfernen, diagonal in ca. 6 mm breite Stücke schneiden und die Körner belassen.\nFür die Würze die Oliven längs vierteln und mit den restlichen Zutaten bereit halten. Die Zutaten für die Sauce mischen und rühren, bis der Zucker gelöst ist. Die Hühnerstücke abseihen und die Marinadenreste in die Sauce mischen.\nIn einer tiefen Pfanne oder Wok das Olivenöl erhitzen bis es duftet. Die Zwiebelchen und die Knoblauchzehen zugeben und 30 Sekunden braten, dann die Hühnerstücke zufügen und 3 Minuten scharf braten. Zucchini, Karotte, Schnittsellerie-Stängel und Peperoni dazugeben und 1 Minute pfannenrühren. Die Kartoffel- und Tomatenstücke zusammen mit der Würze untermischen. Noch 1 Minute pfannenrühren und dann mit der Sauce ablöschen. Mit Deckel 3 Minuten köcheln lassen.\nMit Salz und Pfeffer abschmecken, auf die angewärmten Servierteller verteilen, garnieren, sofort gut warm servieren und genießen.",
            self.harvester_class.instructions(),
        )
