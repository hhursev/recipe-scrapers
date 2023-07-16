# mypy: allow-untyped-defs

from recipe_scrapers.rutgerbakt import RutgerBakt
from tests import ScraperTest


class TestRutgerBaktScraper(ScraperTest):
    scraper_class = RutgerBakt
    test_file_name = "rutgerbakt_2"

    def test_host(self):
        self.assertEqual("rutgerbakt.nl", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Rutger van den Broek", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Abrikozenvlaai", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(120, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual(None, self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://rutgerbakt.nl/wp-content/uploads/2020/04/abrikozenvlaai-scaled-1920x1080-c-default.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 recept vlaaideeg",
                "1 kilo verse rijpe abrikozen of 750 gr abrikozenhelften, uitgelekt uit blik",
                "¾ recept banketbakkersroom",
                "suiker, optioneel, om te bestrooien",
                "boter, om in te vetten",
                "bloem, voor het werkblad",
                "150 gr abrikozenjam",
                "20 gr amandelschaafsel",
                "poedersuiker, om te bestuiven",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Maak eerst de banketbakkersroom en het vlaaideeg.\nAls je verse abrikozen gebruikt moeten deze eerst nog voorbereid worden, om de schil te verwijderen. Snijd de abrikozen kruislings in en leg ze 1 à 2 minuten in kokend water. Leg ze vervolgens in ijskoud water om het kookproces te stoppen. Verwijder de schil van de abrikozen, halveer ze en verwijder de pit.\nVet een vlaaivorm met een doorsnede van 28 centimeter en een hoogte van 3 centimeter in met boter. Kneed het deeg nog kort door en rol het dan op een bebloemd werkblad uit tot een ronde lap, die ruim over de vlaaivorm past. Bekleed de vorm met het deeg en zorg dat het overal goed aansluit. Verwijder het overhangende deeg door met een deegroller over de vorm te rollen of met behulp van een mes.\nVerwarm de oven voor op 220 °C. Klop de afgekoelde banketbakkersroom los met (hand)mixer met garde(s) en verdeel deze over de met deeg beklede vlaaivorm. Rangschik de abrikozenhelften met de bolle kanten omhoog op de banketbakkersroom, zodat de hele vlaai bedekt is. Als je wilt kun je nog wat suiker over de abrikozen strooien.\nAbrikozenvlaai bakken\nLaat de vlaai nog 15 minuten rusten en bak deze vervolgens in 25 tot 35 minuten goudbruin en gaar. Laat de vlaai na het bakken een halfuur afkoelen in de vorm en plaats hem daarna op een rooster om verder af te koelen.\nVerlaag de oventemperatuur naar 160 °C en spreid het amandelschaafsel uit over een met bakpapier beklede bakplaat. Rooster het schaafsel 6-8 minuten tot het goudbruin is.\nVerwarm de abrikozenjam en bestrijk daarmee de afgekoelde abrikozen vlaai. Strooi het amandelschaafsel over de vlaai en bestuif de rand licht met poedersuiker.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.0, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "Met dit recept kun je zelf een heerlijke abrikozenvlaai bakken! Deze vlaai is het lekkerst met verse abrikozen, maar buiten het seizoen kun je die ook vervangen door abrikozen uit blik. Ik gebruik voor deze vlaai een vulling van banketbakkersroom. Dat in combinatie met de frisse abrikozen en vlaaibodem levert een heerlijke abrikozentaart op! Wil je een abrikozenvlaai met slagroom maken? Garneer de afgekoelde vlaai dan met opgeklopte slagroom. Van dit abrikozenvlaai recept kun je 10-12 punten snijden. ",
            self.harvester_class.description(),
        )
