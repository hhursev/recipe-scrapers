# mypy: allow-untyped-defs
import responses

from recipe_scrapers.coopse import CoopSE
from tests.legacy import ScraperTest


class TestCoopSEScraper(ScraperTest):
    scraper_class = CoopSE

    @classmethod
    def expected_requests(cls):
        yield responses.GET, "https://www.coop.se/recept/fransk-appelkaka-med-mandel-och-citron/", "tests/legacy/test_data/coopse.testhtml"
        yield responses.GET, "https://proxy.api.coop.se/external/recipe/recipes/458836?api-version=v1", "tests/legacy/test_data/coopse.testjson"

    def test_host(self):
        self.assertEqual("coop.se", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Coop Sverige", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Fransk äppelkaka med mandel och citron", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Bakverk", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("1 portioner", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "http://res.cloudinary.com/coopsverige/image/upload/v1432635038/31469.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "3 dl vetemjöl",
                "2 msk socker",
                "150 g smör",
                "1 citron, finrivet skal och saft",
                "1 dl sötmandel",
                "2 krm riven bittermandel",
                "4 äpplen, i tunna skivor",
                "1 dl ljus aprikosmarmelad",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Sätt ugnen på 225 grader. Mixa mjöl, socker, smör, citronskal, citronsaft, sötmandel och bittermandel i en matberedare till en boll.\nTryck ut degen i en pajform, cirka 28 centimeter i diameter, nagga och ställ i frysen 10 minuter. Förgrädda skalet 10 minuter. Placera äppelskivorna tätt, lite omlott i cirklar i det förgräddade skalet. Grädda i mitten av ugnen i 225° tills skalet och äpplena blivit gyllenbruna, 10-15 minuter.\nVärm marmeladen i en kastrull och pensla på äppelkakan.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(2.8461538461538463, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual("Grann och god äppelpaj.", self.harvester_class.description())
