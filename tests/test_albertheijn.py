from recipe_scrapers.albertheijn import AlbertHeijn
from tests import ScraperTest


class TestAlbertHeijnScraper(ScraperTest):

    scraper_class = AlbertHeijn

    def test_host(self):
        self.assertEqual("ah.nl", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Albert Heijn", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Kruidige groentecalzone", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("hoofdgerecht", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://static.ah.nl/static/recepten/img_001329_890x594_JPG.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 kleine rode ui",
                "1 courgette",
                "1 rode paprika",
                "0.5 eetlepel Italiaanse kruiden",
                "2 eetlepels olijfolie",
                "2 theelepels knoflookpuree",
                "1 pakje pizza & tomato",
                "1 pakje walnootkaas",
                "0.5 eetlepel olie om in te vetten",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Oven voorverwarmen op 200 °C of gasovenstand 4. Ui, courgette en paprika schoonmaken en in kleine blokjes snijden. In kom groenten, kruiden, olijfolie, knoflookpuree en inhoud van potje tomatensaus door elkaar scheppen.Op aanrecht pizzadeeg uitspreiden, iets uitrollen en in twee gelijke stukken snijden. Plakken kaas naast elkaar erop leggen, ca. 2 cm van randen vrijhouden. Op helft van elk stuk courgettemengsel scheppen. Andere helft over vulling klappen en randen van deeg tussen duim en wijsvinger tot mooie schulprand dichtknijpen. Bakplaat invetten. Calzones erop leggen en in midden van oven in ca. 25 minuten goudbruin en gaarbakken.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(3.08, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("italiaans", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual("", self.harvester_class.description())
