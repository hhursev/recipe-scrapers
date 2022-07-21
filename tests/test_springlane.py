from recipe_scrapers.springlane import Springlane
from tests import ScraperTest


class TestSpringlaneScraper(ScraperTest):

    scraper_class = Springlane

    def test_host(self):
        self.assertEqual("springlane.de", self.harvester_class.host())

    def test_site_name(self):
        self.assertEqual("Springlane", self.harvester_class.site_name())

    def test_language(self):
        self.assertEqual("de-DE", self.harvester_class.language())

    def test_author(self):
        self.assertEqual("Springlane", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Tiramisu ohne Ei und ohne Alkohol – Dolci für alle!",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual(
            "Awareness,Dessert,Espressomaschinen,Recipe,Sweet Treats",
            self.harvester_class.category(),
        )

    def test_cuisine(self):
        self.assertEqual("Italien", self.harvester_class.cuisine())

    def test_total_time(self):
        self.assertEqual(260, self.harvester_class.total_time())

    def test_cook_time(self):
        self.assertEqual(240, self.harvester_class.cook_time())

    def test_prep_time(self):
        self.assertEqual(20, self.harvester_class.prep_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.springlane.de/magazin/wp-content/uploads/2017/01/Tiramisu-ohne-Ei-und-ohne-Amaretto_15.jpg",
            self.harvester_class.image(),
        )

    def test_nutrients(self):
        self.assertEqual({}, self.harvester_class.nutrients())

    def test_ingredients(self):
        self.assertEqual(
            [
                "500 g Mascarpone",
                "400 ml Sahne",
                "100 g Puderzucker",
                "150 ml Espresso",
                "280 g Löffelbiskuit",
                "Kakaopulver",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Sahne steif schlagen und mit Mascarpone und Puderzucker verr\u00fchren. Espresso kochen und abk\u00fchlen lassen.\n"
            + "H\u00e4lfte der L\u00f6ffelbiskuits in die Auflaufform geben. 75 ml Espresso dar\u00fcbertr\u00e4ufeln. "
            + "H\u00e4lfte der Creme auf den L\u00f6ffelbiskuits verstreichen. "
            + "Restliche L\u00f6ffelbiskuits, Espresso und Creme daraufgeben, mindestens 4 Stunden kaltstellen. Vor dem Servieren mit Kakaopulver best\u00e4uben.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())
