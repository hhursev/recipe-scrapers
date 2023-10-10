from recipe_scrapers.emmikochteinfach import EmmiKochtEinfach
from tests import ScraperTest


class TestEmmiKochtEinfachScraper(ScraperTest):
    scraper_class = EmmiKochtEinfach

    def test_host(self):
        self.assertEqual("emmikochteinfach.de", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://emmikochteinfach.de/klassisches-rindergulasch/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Emmi", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Klassisches Rindergulasch ganz einfach", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual(None, self.harvester_class.category())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://emmikochteinfach.de/wp-content/uploads/2022/02/seo_Gulasch-Nah-200.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "600 g Rindergulasch (ca. 3x3 cm große Stücke, gegebenenfalls selbst kleiner schneiden)",
                "400 ml Rinderfond (selbstgemacht oder aus dem Glas)",
                "300 g Schalotten (geschält und halbiert)",
                "200 ml trockener Rotwein, einen den Du gerne trinkst (alternativ roter 100% Traubendirektsaft )",
                "40 g Tomatenmark",
                "3 EL Butterschmalz (z.B. Buttaris; Alternativ Pflanzenöl )",
                "1 Knoblauchzehe (geschält, klein geschnitten)",
                "1-2 TL Zitronenabrieb (unbehandelt bzw. Bio) (kannst Du auch weggelassen )",
                "2 TL Paprikapulver, edelsüß",
                "1/2 TL Majoran, getrocknet",
                "1 Msp. Cayennepfeffer",
                "1 Prise Salz",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """
Das Gulasch-Fleisch bitte ca. eine halbe Stunde vor der Zubereitung aus dem Kühlschrank nehmen, damit es Zimmertemperatur annehmen kann und nicht eiskalt gebraten wird. Wenn Du das Fleisch selbst schneidest, erst Scheiben quer zur Fleischfaser und daraus wiederum Würfel schneiden. Eine ideale Größe ist ca. 3x3 cm (Walnussgröße). Die 600 g Fleisch nur mäßig salzen, wenn überhaupt nur mit 1 Prise Salz kurz vor dem Anbraten.
Jetzt schälst Du die 300 g Schalotten und halbierst sie, besonders große Exemplare kannst Du auch vierteln. 1 EL Butterschmalz in einem Bräter / Schmortopf erhitzen und darin die Schalotten goldgelb anbraten. Herausnehmen und zur Seite stellen.
Im Anschluss wieder 1 EL Butterschmalz im Bräter erhitzen und bei sehr hoher Temperatur das Fleisch portionsweise anbraten. Erst nach ca. 1 Minute das erste Mal wenden, damit nicht zu viel Hitze vom Boden entweicht, das Fleisch eine schöne Bräune annimmt und sich Röstaromen bilden. Die Fleischportionen entsprechend zur Seite stellen. HINWEIS: Meine Empfehlung ist das Fleisch auf jeden Fall portionsweise anzubraten, auch wenn es etwas Geduld erfordert. Wenn das gesamte Gulaschfleisch auf einmal in den Topf kommt, kann der Boden in der Regel die Hitze nicht halten und das Fleisch köchelt mehr als zu braten.
Nun kommt das gesamte Fleisch zurück in den Bräter zur letzten Fleischportion zurück, ebenfalls die Schalotten sowie 40 g Tomatenmark. Das Tomatenmark gut unterrühren damit es kurz mit rösten kann.
Mit 200 ml trockenem Rotwein ablöschen und den Rotwein zu 2/3 verkochen lassen, sprich auf ungefähr 1/3 reduzieren.
In der Zwischenzeit 1 Knoblauchzehe schälen und in feine Würfel schneiden. Die Zitrone heiß abwaschen, abtrocknen und die Schale mit einer feinen Reibe abreiben für ca. 1 bis 2 TL Zitronenabrieb. Wenn der Rotwein reduziert ist, den Knoblauch, 1-2 TL Zitronenabrieb, 2 TL Paprikapulver, 1/2 TL Majoran und 1 Messerspitze Cayennepfeffer hinzufügen und kurz unterrühren.TIPP: Das Gulasch erhält durch den Zitronenabrieb ein feines Zitronenaroma. Wenn Du das nicht möchtest, kannst Du den Abrieb auch einfach weglassen.
Das Fleisch und die Schalotten nun mit 400 ml Rinderfond ablöschen und mit Deckel für ca. 1,5 Stunden bei geringer Hitze auf der Herdplatte garen. Nach einer Stunde mal nachsehen, ob Dir die Soße zu flüssig erscheint. Falls ja, kannst Du das Gulasch die letzten 30 Minuten ohne Deckel weiter garen. Am Ende der Garzeit das Gulasch nach Belieben abschmecken und gegebenenfalls eindicken.
Ich wünsche Dir einen guten Appetit! Lass Dir mein klassisches Rindergulasch Rezept gut schmecken.
        """.strip(),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.99, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "Mein Familienrezept ist ein echter Klassiker. Gulasch kochen geht einfacher als man denkt. Mit zartem Fleisch, leckeren Röstaromen und einer sämigen Soße wird es auch Dir gelingen.",
            self.harvester_class.description(),
        )

    def test_total_time(self):
        return self.assertEqual(120.0, self.harvester_class.total_time())

    def test_cook_time(self):
        return self.assertEqual(90.0, self.harvester_class.cook_time())

    def test_prep_time(self):
        return self.assertEqual(30.0, self.harvester_class.prep_time())
