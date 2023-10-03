# mypy: allow-untyped-defs

from recipe_scrapers.keukenliefdenl import KeukenLiefdeNL
from tests import ScraperTest


class TestKeukenLiefdeNL3Scraper(ScraperTest):

    scraper_class = KeukenLiefdeNL
    test_file_name = "keukenliefdenl_3"

    def test_host(self):
        self.assertEqual("keukenliefde.nl", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Annemiek", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Stroganoff-gehaktschotel", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Hoofdgerecht", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(None, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.keukenliefde.nl/wp-content/uploads/2014/11/Stroganoff-gehaktschotel-27.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1,5 kilo aardappels, geschild",
                "Melk",
                "Roomboter",
                "2 uien, gepeld en in ringen",
                "2 tenen knoflook, gepeld en fijngehakt",
                "3 paprika’s, in repen gesneden",
                "250 g champignons, in plakjes gesneden",
                "1 el paprikapoeder",
                "1 blikje tomatenpuree",
                "1 runderbouillonblokje",
                "500 g rundergehakt",
                "2 el crème fraîche",
                "Worchestersaus",
                "Tabasco",
                "75 g geraspte kaas",
                "Olie om in te bakken",
                "Eventueel scheutje Vodka",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Bereiding Verhit een grote koekenpan of braadpan met wat olie en bak de ui, knoflook, paprika’s en champignons op middelhoog vuur, totdat ze zacht zijn. Voeg de paprikapoeder en tomatenpuree toe en bak even mee.\nVerkruimel het bouillonblokje boven de pan en voeg het gehakt toe. Roer het gehakt met een vork goed rul. Blus het gehaktmengsel eventueel af met een scheut Vodka, laat inkoken en voeg dan 100 ml water toe.\nZet het vuur weer laag en laat 15 minuten zachtjes pruttelen, of totdat de saus is ingedikt. Roer de laatste 5 minuten van de kooktijd de crème fraîche door het gehakt. Proef de saus en breng indien nodig verder op smaak met wat Worchestersaus en tabasco.\nKook ondertussen de aardappels gaar en giet ze af. Stamp ze fijn en roer de puree glad met wat melk en een klont roomboter.\nDe puree moet niet te dik zijn, anders kun je hem zometeen moeilijk uitstrijken. Breng goed op smaak met zout en peper.\nVerwarm de oven voor op 200 graden. Vet de ovenschaal in. Verdeel het gehaktmengsel over de ovenschaal en dek af met de aardappelpuree. Bestrooi met de geraspte kaas.\nBak de ovenschotel circa 30 tot 40 minuten in de oven, of totdat de bovenkant goudbruin is.\nLaat de schotel voor serveren iets afkoelen.\nEnjoy!\nThema recepten, Wereldgerecht, Hongaarse recepten, Mannenvoer, Hoofdgerecht, Ovenrecepten, Vleesrecepten",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "Een heerlijk gerecht geïnspireerd op de Hongaarse keuken: stroganoff-gehaktschotel!",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("nl-NL", self.harvester_class.language())
