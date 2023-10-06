# mypy: allow-untyped-defs

from recipe_scrapers.uitpaulineskeukennl import UitPaulinesKeukenNl
from tests import ScraperTest


class TestUitPaulinesKeukenNlScraper(ScraperTest):
    scraper_class = UitPaulinesKeukenNl
    test_file_name = "uitpaulineskeukennl_2"

    def test_host(self):
        self.assertEqual("uitpaulineskeuken.nl", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Monique van Loon", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Crispy sushi bites", self.harvester_class.title())

    def test_category(self):
        self.assertEqual(
            "Gezonde tussendoortjes, Avocado, Rijst, Zalm, Aziatische recepten, Gezonde recepten, "
            "Lactosevrije recepten, Notenvrije recepten, Oud en nieuw, Vis recepten, Herfst recepten, Lente "
            "recepten, Winter recepten, Zomer recepten, Borrelhapjes, Lunch, Voorgerecht",
            self.harvester_class.category(),
        )

    def test_total_time(self):
        self.assertEqual(50, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("10 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://uitpaulineskeuken.nl/wp-content/uploads/2023/07/Crispy-sushi-bites2.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "200 gr sushirijst",
                "350 ml water",
                "4 el sushi-azijn (voor de rijst)",
                "zonnebloemolie",
                "250 gr verse zalmfilet (zonder huid)",
                "2 avocado's (in dunne plakjes)",
                "0,5 komkommer (in kleine blokjes)",
                "2 el sojasaus",
                "1+1 el sushi-azijn",
                "1/2 limoen (alleen het sap)",
                "1 el sesamolie",
                "0,5 tl chilivlokken",
                "1 el (zwart) sesamzaadjes",
                "sriracha mayonaise",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Maak de sushirijst zoals op de verpakking vermeld staat. Breng de rijst op smaak met sushi-azijn. Neem een ronde uitsteker van ca 5 cm. Verdeel 3 el sushirijst over het vormpje en druk het aan. Ga door totdat alle rijst verwerkt is. Je kan de rondjes eventueel een dag van tevoren maken en bewaren in de koelkast.",
                    "Laat wat zonnebloemolie heet worden in een koekenpan. Bak de sushi rondjes aan weerszijden goudbruin en krokant. Leg apart.",
                    "Snijd de zalm in blokjes en doe dit in een bakje. Voeg 2 el sojasaus, 1 el sushi-azijn, 1 el sesamolie, het sap van een halve limoen en een 0,5 tl chili vlokken en het sesamzaad toe en leg apart.",
                    "Snijd de avocado in hele dunne plakjes. Snijd de komkommer in blokjes en breng deze op smaak met 1 el sushi-azijn.",
                    "Verdeel over ieder stukje gebakken sushi een paar plakjes avocado, een lepel gemarineerde zalm, wat zoetzure komkommer en garneer met sriracha mayo.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Aziatische recepten", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Zin in sushi, maar wil je eens wat anders aan je gezin, jezelf of gasten serveren? Dan zijn "
            "deze crispy sushi bites met zalm, avocado & komkommer het perfecte hapje voor jou! Lekker "
            "om te dippen in sojasaus. Deze bites zijn eenvoudig te maken en perfect voor een feestje. "
            "Bak de sushirijst goudbruin en krokant in zonnebloemolie, en voeg vervolgens de "
            "gemarineerde zalm, avocado en zoetzure komkommer toe. Garneer met een vleugje sriracha mayo "
            "voor extra pit. Geniet van deze kleurrijke crispy sushi!",
            self.harvester_class.description(),
        )
