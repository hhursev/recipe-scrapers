from recipe_scrapers.koket import Koket
from tests import ScraperTest


class TestKoketScraper(ScraperTest):

    scraper_class = Koket

    def test_host(self):
        self.assertEqual("koket.se", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Tommy Myllymäki", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Myllymäkis toast skagen", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://img.koket.se/standard-mega/myllymakis-toast-skagen-2.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 kg räkor med skal (gärna färska av fin kvalitet)",
                "2 äggulor",
                "2 tsk senap",
                "1 msk vitvinsvinäger",
                "6 dl matolja",
                "1 kruka dill",
                "10 cm färsk pepparrot, skalad",
                "4 skiva vitt bröd (ej levain)",
                "smör, till stekning",
                "50 g löjrom",
                "1 citron",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Skala alla räkor och ställ åt sidan.\nGör en majonnäs genom att lägga ner äggulor, senapen och vinägern i en bunke. Tillsätt matoljan i en tunn stråle medan du vispar hela tiden. Använd elvisp eller handvisp. När majonnäsen är tjock och du ser dragen/spåren av vispen i majonnäsen är den klar.\nLägg alla räkor i en bunke, tillsätt fint plockad dill och blanda ner lite majonnäs i taget.\nTillsätt lite riven pepparrot och smaka av. Slå på mer majonnäs för en rinnigare röra eller mer pepparrot för mer sting.\nTa fram brödet och skär ut önskad form utan att ta med kanterna, använd en skål eller ett glas som mall om ni vill ha runda bröd. Stek sedan gyllene i smör.\nLägg upp bröden på tallrik, toppa med skagenröra och en rejäl klick löjrom. Avsluta med en dillkvist och en citronskiva.""",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(3.6, self.harvester_class.ratings())
