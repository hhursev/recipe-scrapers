# mypy: allow-untyped-defs

from recipe_scrapers.keukenliefdenl import KeukenLiefdeNL
from tests import ScraperTest


class TestKeukenLiefdeNL2Scraper(ScraperTest):

    scraper_class = KeukenLiefdeNL
    test_file_name = "keukenliefdenl_2"

    def test_host(self):
        self.assertEqual("keukenliefde.nl", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Johan", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Sticky kippenvleugels (van de kamado)", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Hapje", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(5, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual(None, self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.keukenliefde.nl/wp-content/uploads/2023/09/Sticky-kippenvleugels-van-de-kamado-1675.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "Kippenvleugels",
                "Kipkruiden",
                "Teriyakisaus (zelfgemaakt of kant-en-klaar)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Stook de kamado indirect op tot 150 graden.\nLeg de kippenvleugels als de temperatuur stabiel op 150 graden blijft op het rooster en sluit de klep voor een half uur.\nDoe de teriyaki saus alvast in een vuurvaste pan en zet die na zo’n 20 minuten bij de kippenvleugels op het rooster.\nDe saus kan zo lekker opwarmen en iets dunner worden waardoor de vleugels zometeen lekker door de saus gehaald kunnen worden en goed veel saus aan de vleugels blijft plakken.\nNa 30 minuten open je de klep en haal je de vleugels met een tang door de saus. Zorg dat de kippenvleugels goed omhult zijn met saus. Leg de vleugels daarna weer terug op het rooster en laat ze met gesloten klep nog zo’n 10 minuten liggen.",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "In dit recept laten we je zien hoe je deze smakelijke sticky kippenvleugels van de kamado (of in de oven) kunt maken. Ze zijn verslavend lekker!",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("nl-NL", self.harvester_class.language())
