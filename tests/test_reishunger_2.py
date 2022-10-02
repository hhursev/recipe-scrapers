from recipe_scrapers.reishunger import Reishunger
from tests import ScraperTest


class TestReishungerScraper(ScraperTest):
    scraper_class = Reishunger

    @property
    def test_file_name(self):
        return "{}_2".format(self.scraper_class.__name__.lower())

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
            '\n\n\nZubereitung\n\n\n\n\n\n\n\n\n\n1. Schritt\n\n\n\n\n\nAusgewählte Sorte:\n\nBasmati Reis Pusa\n\n\n\n\n\n\n\n\n\n\n\n\n\nKochtopf\n\n\n\n\n\n\n\n\n\n\n\n\n \n\nReiskocher\n\n\n\n\n\n\n\n \n\nMikrowelle\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDämpfer\n\n\n\n\n\n\n\nZubereitung im\nKochtopf\n\n\n\n\nReis waschen. Den Reis mit kaltem Wasser bedecken. Mit den Händen den Reis in kreisenden Bewegungen waschen. Durch die überschüssige Stärke wird das Wasser trüb. Nun das Wasser abgießen und den Vorgang wiederholen bis das Wasser klar bleibt.\n\n\nReis in einen Kochtopf geben.\n\n\nWasser dazugeben. Nach Belieben salzen.\n\n\nReis 10 Minuten einweichen lassen.\n\n\nHerd auf die höchste Hitzestufe stellen und Reis aufkochen lassen.\n\n\nSobald das Wasser kocht, den Herd auf die mittlere Hitzestufe stellen und den Reis ca. 15 Minuten bei geschlossenem Deckel köcheln lassen bis das Wasser komplett aufgesogen wurde.\n\n\nNach Belieben ein Stück Butter hinzufügen.\n\n\n\n\n\n\n\n\nZubereitung im\n\nReiskocher\n\n\n\n\n\nReis waschen. Den Reis mit kaltem Wasser bedecken. Mit den Händen den Reis in kreisenden Bewegungen waschen. Durch die überschüssige Stärke wird das Wasser trüb. Nun das Wasser abgießen und den Vorgang wiederholen bis das Wasser klar bleibt. Anschließend den Reis in den Innentopf geben.\n\n\nReis in den Reiskocher geben.\n\n\nWasser dazugeben. Nach Belieben salzen.\n\n\nDeckel schließen und den Kochvorgang im Modus "Weiß" starten.\n\n\nSobald der Reiskocher in den Warmhaltemodus schaltet, ist der Reis fertig.\n\n\nNach Belieben ein Stück Butter hinzufügen.\n\n\n\n\n\n\n\n\nZubereitung im\n\nMikrowellen-Reiskocher\n\n\n\n\n\nReis waschen. Den Reis mit kaltem Wasser bedecken. Mit den Händen den Reis in kreisenden Bewegungen waschen. Durch die überschüssige Stärke wird das Wasser trüb. Nun das Wasser abgießen und den Vorgang wiederholen bis das Wasser klar bleibt.\n\n\nReis in den Mikrowellen Reiskocher geben.\n\n\nWasser dazugeben. Nach Belieben salzen.\n\n\nDeckel aufsetzen und bei höchster Stufe (600-800 Watt) für 11 Minuten in die Mikrowelle stellen.\n\n\nNach Belieben ein Stück Butter hinzufügen.\n\n\n\n\n\n\n\n\nZubereitung im\n\nDämpfer\n\n\n\n\n\nReis waschen. Du bedeckst den Reis mit kaltem Wasser. Mit den Händen bearbeitest du den Reis in kreisenden Bewegungen. Durch die überschüssige Stärke wird das Wasser trüb. Nun gießt du das Wasser ab und wiederholst den Vorgang solange bis das Wasser klar bleibt.\n\n\nBambuskorb mit einem Baumwolltuch auslegen und den Reis darauf geben.\n\n\nMit Stäbchen oder Gabel Löcher in die Masse drücken durch die Dampf entweichen kann.\n\n\nBambuskorb mit Korbdeckel schließen. Topfboden mit ca. 1 cm Wasser bedecken und Bambuskorb reinstellen.\n\n\nBei niedriger bis mittlerer Hitze ca. 20 Minuten dämpfen lassen. Zwischenzeitlich Wasser nachkippen, sodass der Korb stetig in ca. 1 cm hohem Wasser steht.\n\n\nReis entnehmen und nach Belieben ein Stück Butter hinzufügen.\n\n\n\n\n\n\n\n\n\n\n2. Schritt\n\n\n\n\nZwiebeln und Knoblauch klein schneiden und in Kokosöl in einer Pfanne kurz anbraten.\n\n\n\n3. Schritt\n\n\n\n\nKokosmilch und Wasser vorsichtig in die Pfanne schütten.\n\n\n\n4. Schritt\n\n\n\n\nSüßkartoffel und Paprika klein schneiden und in die Pfanne geben.\n\n\n\n5. Schritt\n\n\n\n\nKichererbsen abtropfen, Ingwer schälen und kleinschneiden, ebenfalls in die Pfanne geben.\n\n\n\n6. Schritt\n\n\n\n\nCurry und Salz hinzugeben und bei geschlossenem Deckel kurz zum Kochen bringen, dann auf leichter Stufe circa 10 Minuten köcheln lassen.\n\n\n\n7. Schritt\n\n\n\n\nPaprika edelsüß und Cayennepfeffer hinzugeben, verrühren und ca. weitere 5 Minuten köcheln lassen, bis die Soße schön eingekocht ist.\n\n\n\n8. Schritt\n\n\n\n\nMit Reis und Kräutern servieren, fertig. Guten Reishunger!\n\n\n\n\n',
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4, self.harvester_class.ratings())
