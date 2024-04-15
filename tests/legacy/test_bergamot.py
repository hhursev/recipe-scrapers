from responses import GET

from recipe_scrapers.bergamot import Bergamot
from tests.legacy import ScraperTest


class TestBergamotScraper(ScraperTest):
    scraper_class = Bergamot

    @classmethod
    def expected_requests(cls):
        yield GET, "https://dashboard.bergamot.app/shared/mIB4jYQtZU1A97", "tests/legacy/test_data/bergamot.testhtml"
        yield GET, "https://api.bergamot.app/recipes/shared?r=mIB4jYQtZU1A97", "tests/legacy/test_data/bergamot.testjson"

    def test_canonical_url(self):
        self.assertEqual(
            self.harvester_class.canonical_url(),
            "https://www.elle.fr/Elle-a-Table/Recettes-de-cuisine/Soupe-miso-aux-oignons-nouveaux-tofu-et-saumon-emiette-4188650",
        )

    def test_host(self):
        self.assertEqual("dashboard.bergamot.app", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            "Soupe miso aux oignons nouveaux, tofu et saumon émietté",
            self.harvester_class.title(),
        )

    def test_author(self):
        self.assertEqual(None, self.harvester_class.author())

    def test_total_time(self):
        self.assertEqual(50, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "100 g de saumon frais",
                "6 oignons nouveaux",
                "30 g d'algues wakame séchées",
                "70 g de pâte de miso blanc",
                "quelques cives",
                "300 g de tofu soyeux",
                "1 cuillère(s) à soupe d'huile de sésame",
                "1 cuillère(s) à soupe de graines de sésame",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Dans une poêle bien chaude, faites cuire le saumon côté peau pendant 5 mn, puis laissez-le refroidir avant de l’émietter.\nDans une casserole, versez 1,5l d’eau, la moitié des oignons lavés et coupés en deux dans la hauteur, et les algues, puis portez à ébullition, réduisez ensuite le feu et laissez mijoter pendant 20 mn. Filtrez et ajoutez le miso, mélangez soigneusement.\nAjoutez le reste des oignons coupés en quatre, les cives lavées et émincées, le tofu coupé en dés et les miettes de saumon. Arrosez d’huile de sésame et parsemez de graines de sésame. Dégustez bien chaud.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())
