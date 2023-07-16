# mypy: allow-untyped-defs

from recipe_scrapers.rutgerbakt import RutgerBakt
from tests import ScraperTest


class TestRutgerBaktScraper(ScraperTest):
    scraper_class = RutgerBakt
    test_file_name = "rutgerbakt_1"

    def test_host(self):
        self.assertEqual("rutgerbakt.nl", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Rutger van den Broek", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Arretjescake", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(180, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual(None, self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://rutgerbakt.nl/wp-content/uploads/2020/10/arretjescake-scaled-1920x1080-c-default.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "75 ml slagroom",
                "2 eidooiers",
                "50 +150 gr witte basterdsuiker",
                "50 gr cacaopoeder",
                "225 gr boter, gesmolten",
                "225 gr biscuits (Maria biscuits)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Begin met het maken van de custard. Doe de slagroom in een steelpannetje en breng dit aan de kook. Doe de eidooiers met de 50 gram basterdsuiker in een kom en klop deze door elkaar. Schenk de kokende slagroom al roerende op het eidooiermengsel en klop alles goed door. Giet het mengsel terug in de pan. Verwarm het op laag vuur en blijf roeren tot het mengsel dikker begint te worden. De custard mag niet koken, verwarm deze tot ongeveer 85 °C. Haal de pan dan van het vuur.\nDoe de rest van de basterdsuiker met het cacaopoeder en de custard in een kom en klop dit met een (hand)mixer met garde(s) door elkaar. Voeg de gesmolten boter toe en klop alles door tot de suiker opgelost is. Dit kun je testen door wat van het mengsel tussen duim en wijsvinger te pakken. Voel je nog korrels van de suiker, dan moet je nog wat langer kloppen.\nDoe de biscuitjes in een schone theedoek en vouw deze dicht. Sla met een deegroller (of een ander hard voorwerp) op de doek zodat de koekjes in stukjes breken. Voeg de biscuitstukjes toe aan het mengsel en roer door elkaar. Bekleed de binnenkant van een cakevorm van 25 centimeter met plasticfolie en laat het folie aan de bovenkant overhangen. Schep het mengsel in de vorm, druk het goed aan en dek het af met het overhangende plasticfolie. Laat de arretjescake 2-3 uur opstijven in de koelkast. Haal de cake met behulp van het folie uit de vorm en snijd ‘m in plakken.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.0, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "Maak zelf de lekkerste arretjescake met dit recept! Serveer plakjes of kleine stukjes arretjescake tijdens de koffie of als onderdeel van een high tea. Deze traktatie van cacao, koekjes en boter is helemaal niet moeilijk om te maken en perfect als je op zoek bent naar iets lekkers om van te voren te maken of een no-bake lekkernij. Voor deze arretjescake heb je namelijk geen oven nodig, maar je laat hem opstijven in de koelkast.\xa0",
            self.harvester_class.description(),
        )
