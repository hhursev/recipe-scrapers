# mypy: allow-untyped-defs

from recipe_scrapers.smulweb import Smulweb
from tests import ScraperTest


class TestSmulwebScraper(ScraperTest):

    scraper_class = Smulweb

    def test_host(self):
        self.assertEqual("smulweb.nl", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("pwiggers", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Lekker! Ovenschotel spitskool champignons spekreepjes en prei",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual("Ovenschotel", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://d1mlbwr23caxox.cloudfront.net/public/sites/default/files/styles/recipe_teaser/public/recipe-images/IMG_1442.JPG_16.jpg?VersionId=HiJx912VlnCnUKiAYHKDqDsZLjsSy9zI",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "Plm. 750 gram spitskool",
                "1 prei",
                "250 gram champignons",
                "150 gram mager gerookte spekreepjes of baconreepjes",
                "1 eetlepel neutrale olie",
                "peper, zout",
                "1/2 theelepel gemalen nootmuskaat",
                "cayennepeper naar smaak",
                "1 + 1 eetlepel mosterd",
                "200 ml crème fraîche",
                "750 gram kruimige aardappelen",
                "50 geraspte belegen kaas",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertCountEqual(
            [
                "Verwarm de oven voor op 200 graden.",
                "Verhit de olie in de wok.",
                "Bak hierin de spekreepjes knapperig.",
                "Voeg de plakjes champignons toe en bak deze mee tot al het vocht is verdwenen.",
                "Voeg de prei toe en bak deze plm. 2 minuten mee.",
                "Doe dan de spitskool erbij en roerbak alles nog plm. 5 - 10 minuten, afhankelijk van de dikte van de spitskool. (De spitskool moet nog knapperig blijven!)",
                "Maak de spitskool op smaak met peper, zout, nootmuskaat en wat cayennepeper.",
                "Roer 2 eetlepels crème fraîche en 1 eetlepel mosterd door de kool.",
                "Doe de kool in een vuurvaste ovenschool.",
                "Laat de gare aardappels goed droog stomen.",
                "Stamp de aardappels met een stamper grof en roer de rest van de crème fraîche en 1 eetlepel mosterd door de aardappelen.",
                "Strijk de aardappelen uit over de spitkool en bestrooi met wat geraspte kaas.",
                "Zet de schaal in de voorverwarmde oven tot de kaas een goudbruine kleur heeft gekregen.",
                "Als de ingrediënten nog warm zijn kun je de schaal ook even onder de grill zetten tot de kaas goudbruin is.",
            ],
            self.harvester_class.instructions_list(),
        )

    def test_ratings(self):
        self.assertEqual(3.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Nederlands", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Lekker pittige ovenschotel. Door het gebruik van de mosterd en crème fraîche krijgt de kool een lekkere romige smaak. Geen aardappelpuree bovenop, maar aardappelen gestampt met wat crème fraîche en mosterd erdoor geroerd. Hierdoor krijg je een wat grovere laag, die heerlijk is bij de spitskool.Ook lekker met plakjes ontbijtspek op de schotel. Ze worden lekker knapperig in de oven. (zie foto)",
            self.harvester_class.description(),
        )
