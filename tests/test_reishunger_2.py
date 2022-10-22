from recipe_scrapers.reishunger import Reishunger
from tests import ScraperTest


class TestReishungerScraper(ScraperTest):
    scraper_class = Reishunger
    test_file_name = "reishunger_2"

    def test_host(self):
        self.assertEqual("reishunger.de", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("snackicat", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Süßkartoffel-Kichererbsen-Curry", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("3 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cdn.reishunger.com/img7830bearbeitetklein.jpg?quality=85",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "240g Basmati Reis Pusa",
                "1 TL Kokosöl",
                "1 Dose Bio Kichererbsen",
                "200ml Kokosmilch",
                "1 Zwiebel",
                "1 Knoblauchzehe",
                "1 mittelgroße Süßkartoffel (hier: 300g)",
                "1 Paprika",
                "150ml Wasser",
                "20g Ingwer",
                "3 TL Curry",
                "Salz, Cayenne Pfeffer, Paprika edelsüß",
                "Kräuter nach Belieben (hier: Petersilie)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Zubereitung im Kochtopf Reis waschen. Den Reis mit kaltem Wasser bedecken. Mit den Händen den Reis in kreisenden Bewegungen waschen. Durch die überschüssige Stärke wird das Wasser trüb. Nun das Wasser abgießen und den Vorgang wiederholen bis das Wasser klar bleibt. Reis in einen Kochtopf geben. Wasser dazugeben. Nach Belieben salzen. Reis 10 Minuten einweichen lassen. Herd auf die höchste Hitzestufe stellen und Reis aufkochen lassen. Sobald das Wasser kocht, den Herd auf die mittlere Hitzestufe stellen und den Reis ca. 15 Minuten bei geschlossenem Deckel köcheln lassen bis das Wasser komplett aufgesogen wurde. Nach Belieben ein Stück Butter hinzufügen.",
                    'Zubereitung im Reiskocher Reis waschen. Den Reis mit kaltem Wasser bedecken. Mit den Händen den Reis in kreisenden Bewegungen waschen. Durch die überschüssige Stärke wird das Wasser trüb. Nun das Wasser abgießen und den Vorgang wiederholen bis das Wasser klar bleibt. Anschließend den Reis in den Innentopf geben. Reis in den Reiskocher geben. Wasser dazugeben. Nach Belieben salzen. Deckel schließen und den Kochvorgang im Modus "Weiß" starten. Sobald der Reiskocher in den Warmhaltemodus schaltet, ist der Reis fertig. Nach Belieben ein Stück Butter hinzufügen.',
                    "Zubereitung im Mikrowellen-Reiskocher Reis waschen. Den Reis mit kaltem Wasser bedecken. Mit den Händen den Reis in kreisenden Bewegungen waschen. Durch die überschüssige Stärke wird das Wasser trüb. Nun das Wasser abgießen und den Vorgang wiederholen bis das Wasser klar bleibt. Reis in den Mikrowellen Reiskocher geben. Wasser dazugeben. Nach Belieben salzen. Deckel aufsetzen und bei höchster Stufe (600-800 Watt) für 11 Minuten in die Mikrowelle stellen. Nach Belieben ein Stück Butter hinzufügen.",
                    "Zubereitung im Dämpfer Reis waschen. Du bedeckst den Reis mit kaltem Wasser. Mit den Händen bearbeitest du den Reis in kreisenden Bewegungen. Durch die überschüssige Stärke wird das Wasser trüb. Nun gießt du das Wasser ab und wiederholst den Vorgang solange bis das Wasser klar bleibt. Bambuskorb mit einem Baumwolltuch auslegen und den Reis darauf geben. Mit Stäbchen oder Gabel Löcher in die Masse drücken durch die Dampf entweichen kann. Bambuskorb mit Korbdeckel schließen. Topfboden mit ca. 1 cm Wasser bedecken und Bambuskorb reinstellen. Bei niedriger bis mittlerer Hitze ca. 20 Minuten dämpfen lassen. Zwischenzeitlich Wasser nachkippen, sodass der Korb stetig in ca. 1 cm hohem Wasser steht. Reis entnehmen und nach Belieben ein Stück Butter hinzufügen.",
                    "Zwiebeln und Knoblauch klein schneiden und in Kokosöl in einer Pfanne kurz anbraten.",
                    "Kokosmilch und Wasser vorsichtig in die Pfanne schütten.",
                    "Süßkartoffel und Paprika klein schneiden und in die Pfanne geben.",
                    "Kichererbsen abtropfen, Ingwer schälen und kleinschneiden, ebenfalls in die Pfanne geben.",
                    "Curry und Salz hinzugeben und bei geschlossenem Deckel kurz zum Kochen bringen, dann auf leichter Stufe circa 10 Minuten köcheln lassen.",
                    "Paprika edelsüß und Cayennepfeffer hinzugeben, verrühren und ca. weitere 5 Minuten köcheln lassen, bis die Soße schön eingekocht ist.",
                    "Mit Reis und Kräutern servieren, fertig. Guten Reishunger!",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4, self.harvester_class.ratings())
