# mypy: allow-untyped-defs

from recipe_scrapers.keukenliefdenl import KeukenLiefdeNL
from tests import ScraperTest


class TestKeukenLiefdeNL1Scraper(ScraperTest):
    scraper_class = KeukenLiefdeNL
    test_file_name = "keukenliefdenl_1"

    def test_host(self):
        self.assertEqual("keukenliefde.nl", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.keukenliefde.nl/macaroni-stroganoff/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Annemiek", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Macaroni stroganoff", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Hoofdgerecht", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.keukenliefde.nl/wp-content/uploads/2017/11/Macaroni-stroganoff-4568.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "300 g macaroni",
                "1 ui, fijngesnipperd",
                "1 teen knoflook, uitgeperst",
                "2 paprika’s",
                "250 g champignons",
                "300 g rundergehakt",
                "1 blikje tomatenpuree",
                "1 el paprikapoeder",
                "1 tl chilipoeder (optioneel)",
                "1 runderbouillontablet",
                "Scheut kookroom of crème fraîche",
                "Olijfolie om in te bakken",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Verhit een hapjespan met een scheut olie en fruit de ui en knoflook op laag vuur, totdat ze zacht zijn. Was ondertussen de paprika’s en verwijder de zaadlijsten. Snijd de paprika’s in blokjes. Borstel de champignons schoon en snijd in plakken. Voeg de paprika’s, champignons, paprikapoeder (en chilipoeder) toe aan de ui en zet het vuur wat hoger. Bak kort verder, totdat de groenten iets geslinkt zijn. Voeg het gehakt, de tomatenpuree en verkruimelde bouillontablet toe. Roer het gehakt los. Doe de deksel op de pan en laat op laag tot middelhoog vuur zachtjes pruttelen. Roer — als het gehakt en de groenten gaar zijn — een scheut room door de saus en warm nog even door.\nKook ondertussen de macaroni gaar volgens de omschrijving op het pak. Giet de macaroni af en roer door het gehakt.\nGarneer eventueel met wat vers gehakte peterselie.",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "Een keer wat anders dan macaroni bolognese? Maak deze macaroni met stroganoffsaus: een goedgevulde saus met gehakt, paprika's en champignons.",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("nl-NL", self.harvester_class.language())
