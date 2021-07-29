from recipe_scrapers.koket import Koket
from tests import ScraperTest


class TestKoketScraper(ScraperTest):

    scraper_class = Koket

    def test_host(self):
        self.assertEqual("koket.se", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Agnes Fredriksson", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Blommande äpple med salt kolasås", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://img.koket.se/standard-mega/blommande-apple-med-salt-kolasas.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "4 äpplen (fast sort)",
                "4 gräddkolor (Werthers)",
                "50 g smör",
                "ca 1 krm salt",
                "2 tsk malen kanel",
                "4 msk rörsocker",
                "ca 10 valnötter",
                "vaniljglass",
                "2,5 dl vispgrädde",
                "3 msk strösocker",
                "0,5 dl sirap",
                "1 tsk salt",
                "1 msk smör",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            [
                "\nSätt ugnen på 220 grader.",
                "Skär av toppen på äpplena och gröp ur kärnhuset uppifrån, utan att göra hål i botten. Skär två cirklar runt hålet.",
                "Lägg äpplet upp och ner och skär snitt uppifrån och ner. ",
                "Lägg äpplena i en ugnsfast form med botten neråt.",
                "Lägg i en kola i varje äpple.",
                "Smält smöret och blanda ihop med salt, kanel och rörsocker.",
                "Pensla äpplena med smörblandningen och sätt in i ugnen. Efter ca 20 minuter är de klara och har slagit ut som en blomma.",
                "Under tiden så grovhacka nötterna och rosta i en torr panna tillsammans med salt. Det går fort så ha koll! ",
                "Servera de varma äpplena med en kula vaniljglass, kolasås (se recept nedan) och strö över de rostade nötterna.",
                "Blanda alla ingredienser i en kastrull.",
                "Låt koka under omrörning tills den har en gyllene färg.",
                "Låt den svalna lite och servera!\xa0Förvara inte i kylen. Då stelnar den.",
            ],
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.7, self.harvester_class.ratings())
