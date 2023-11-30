# mypy: allow-untyped-defs
import responses

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.coopse import CoopSE
from tests.legacy import ScraperTest


class TestCoopSEScraperGroups(ScraperTest):
    scraper_class = CoopSE

    @classmethod
    def expected_requests(cls):
        yield responses.GET, "https://www.coop.se/recept/champinjonsoppa/", "tests/legacy/test_data/coopse_groups.testhtml"
        yield responses.GET, "https://proxy.api.coop.se/external/recipe/recipes/159412?api-version=v1", "tests/legacy/test_data/coopse_groups.testjson"

    def test_host(self):
        self.assertEqual("coop.se", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Coop Sverige", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Champinjonsoppa", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Soppa", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 portioner", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "http://res.cloudinary.com/coopsverige/image/upload/v1432633965/30404.jpg",
            self.harvester_class.image(),
        )

    def test_ingredient_groups(self):
        groups = self.harvester_class.ingredient_groups()
        expected_groups = [
            IngredientGroup(
                ingredients=[
                    "300 g skivade champinjoner",
                    "1 finhackad gul lök",
                    "2 msk smör",
                    "2 hönsbuljongtärningar",
                    "3 msk vetemjöl",
                    "1 liter vatten",
                    "4 msk ädelost",
                    "1 dl vispgrädde",
                    "1 krm örtsalt",
                    "0.5 krm vitpeppar",
                    "0.5 dl hackade färska örter",
                ],
                purpose=None,
            ),
            IngredientGroup(
                ingredients=["0.5 dl hackade färska örter", "2 rostade brödkrutonger"],
                purpose="Till servering:",
            ),
        ]
        self.assertEqual(expected_groups, groups)

    def test_instructions(self):
        self.assertEqual(
            "Stek svamp och lök i smör i en gryta tills svampen får lite färg. Strö över mjöl och späd med vatten. Lägg i buljongtärningarna.\nKoka upp och låt koka under lock ca 20 minuter. Smula i osten och häll därefter i grädden. Smaka av med salt och peppar.\nGarnera soppan med färska örter och servera med rostade brödkrutonger.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(3.619718309859155, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(None, self.harvester_class.description())
