# mypy: allow-untyped-defs

from recipe_scrapers.weightwatchers import WeightWatchers
from tests import ScraperTest


class TestWeightwatchersScraper(ScraperTest):

    # Test-Url:
    # https://cmx.weightwatchers.de/details/WWRECIPE:5667ab72a29713e4335bb342

    scraper_class = WeightWatchers

    def test_host(self):
        self.assertEqual("www.weightwatchers.com", self.harvester_class.host())

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
                "2 Stück Geflügelwürstchen",
                "1 Stück, klein Zwiebel/n",
                "200 g Champignons, frisch; braun",
                "120 g Nudeln, trocken, jede Sorte; Spiralnudeln",
                "1 Prise(n) Salz/Jodsalz",
                "2 TL Pflanzenöl, Rapsöl/Sonnenblumenöl",
                "400 g Tomaten, passiert",
                "1 Prise(n) Pfeffer",
                "1⁄2 TL Paprikapulver",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredientsCount(self):
        self.assertEqual(9, len(self.harvester_class.ingredients()))

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

    def test_nutrients(self):
        expected_nutrients = {
            "personal points": "earn 12 personal points",
            "positive points": "+2 Punkte von 2 Portion(en) Gemüse",
        }
        self.assertEqual(self.harvester_class.nutrients(), expected_nutrients)
