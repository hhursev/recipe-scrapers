# mypy: allow-untyped-defs

from recipe_scrapers.weightwatchers import Weightwatchers
from tests import ScraperTest


class TestWeightwatchersScraper(ScraperTest):

    # Test-Url:
    # https://cmx.weightwatchers.de/details/WWRECIPE:5667ab72a29713e4335bb342

    scraper_class = Weightwatchers

    def test_host(self):
        self.assertEqual("weightwatchers.de", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("WeightWatchers", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Würstchengulasch mit Nudeln")

    def test_category(self):
        self.assertEqual("WeightWatchers", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_cook_time(self):
        self.assertEqual(0, self.harvester_class.cook_time())

    def test_prep_time(self):
        self.assertEqual(25, self.harvester_class.prep_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cmx.weightwatchers.com/assets-proxy/weight-watchers/image/upload/t_WINE_EXTRALARGE/i34cskr1hxegmxqukawd.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2Stück Geflügelwürstchen",
                "1Stück, klein Zwiebel",
                "Champignons, frisch 200g, braun",
                "Nudeln, trocken, jede Sorte 120g, Spiralnudeln",
                "Salz/Jodsalz 1Prise(n)",
                "Pflanzenöl, Rapsöl/Sonnenblumenöl 2TL",
                "Tomaten, passiert 400g",
                "Pfeffer 1Prise(n)",
                "Paprikapulver 1⁄2TL",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Würstchen in Scheiben schneiden. Zwiebel schälen und würfeln. Champignons trocken abreiben und vierteln. Nudeln nach Packungsanweisung in Salzwasser garen.\nÖl in einem Topf erhitzen und Zwiebelwürfel darin andünsten. Würstchenscheiben und Champignonviertel zufügen und ca. 3 Minuten anbraten. Mit Tomaten ablöschen, aufkochen und ca. 5 Minuten köcheln lassen. Würstchengulasch mit Salz, Pfeffer und Paprikapulver würzen. Nudeln abgießen, untermischen und in einer Frischhaltedose transportieren. Würstchengulasch erwärmen und servieren.",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "18 Uhr und alle haben Hunger? Dann koche rasch das Würstchengulasch und alle sind happy.",
            self.harvester_class.description(),
        )

    def test_difficulty(self):
        self.assertEqual("Leicht", self.harvester_class.difficulty())
