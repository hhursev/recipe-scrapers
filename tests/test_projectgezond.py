# mypy: allow-untyped-defs

from recipe_scrapers.projectgezond import ProjectGezond
from tests import ScraperTest


class TestProjectGezondScraper(ScraperTest):

    scraper_class = ProjectGezond

    def test_host(self):
        self.assertEqual("projectgezond.nl", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Project Gezond", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Boeuf bourguignon", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Diner, Kerstrecepten", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual("30 minuten + 2 uur stoven", self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("twee personen", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.projectgezond.nl/wp-content/uploads/2021/11/BoeufBourguignon-768x1024.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "40 gr ontbijtspek",
                "250 gr runderriblappen",
                "10 gr bloem",
                "1 ui",
                "150 gr winterpeen",
                "1 teentje knoflook",
                "35 gr tomatenpuree",
                "100 ml rode wijn",
                "200 ml runderbouillon",
                "1 laurierblaadje",
                "1 takje tijm",
                "1 kruidnagel",
                "150 gr champignons",
                "50 gr zilveruitjes",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Bak de plakken ontbijtspek bruin en licht krokant in een droge (stoof)pan. Haal uit de pan en zorg dat het bakvet achterblijft.\nSnijd de runderriblappen in blokjes van 2 bij 2 centimeter. Bestrooi met peper, zout en de bloem. Schep om tot alles goed verdeeld is. \nSnijd de ui in halve ringen en de winterpeen in plakken.\nHak de knoflook fijn. \nVerwarm de pan waar het ontbijtspek in gebakken is opnieuw. Bak de riblappen op hoog vuur rondom bruin. \nGebruik indien nodig een klein beetje boter of olijfolie. \nVoeg de ui en winterpeen toe en bak enkele minuten mee met de blokjes vlees.\nZet het vuur lager en voeg de knoflook toe. Bak 1 à 2 minuten mee. Voeg de tomatenpuree toe. Roer los en bak 2 à 3 minuten mee.\nBlus af met de rode wijn. Roer eventuele aanbaksels los van de bodem. Laat de wijn grotendeels verdampen.\nVoeg de runderbouillon, het laurierblaadje, het takje tijm en de kruidnagel toe.\nSnijd de plakken ontbijtspek in stukjes en voeg toe.\nLaat het gerecht ongeveer 2 uur stoven met de deksel op de pan. \nBoen de champignons schoon en snijd ze in kwarten. \nSnijd de zilveruitjes doormidden. \nVoeg de champignons en de zilveruitjes toe.\nLaat alles nog minimaal 30 minuten stoven. Doe dit eventueel zonder deksel op de pan, zodat de boeuf bourguignon wat verder inkookt. \nHaal het laurierblaadje, het takje tijm en de kruidnagel uit de pan.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Deze klassieker vindt zijn oorsprong in de Franse keuken. ‘Rund op bourgondische wijze’ is een vertaling van ‘Boeuf bourguignon’ die niets aan de verbeelding overlaat.\nDit recept is dan ook het perfecte antwoord als het weer tijd is voor een potje stoof!\nWant het is verre van moeilijk om deze ultieme stoofpot te bereiden. Je hebt enkel wat (wacht)tijd en dus geduld nodig. Het is helemaal geen gek idee dat je dit recept al de dag van tevoren klaarmaakt trouwens. De smaken kunnen dan zelfs nog beter intrekken.\nAls dat geen ‘Boeuf bourguignon’ wordt…",
            self.harvester_class.description(),
        )
