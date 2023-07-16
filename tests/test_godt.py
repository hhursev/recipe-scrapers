from recipe_scrapers.godt import Godt
from tests import ScraperTest


class TestGodtScraper(ScraperTest):

    scraper_class = Godt

    def test_host(self):
        self.assertEqual("godt.no", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Grove pannekaker",
        )

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cdn-yams.godt.no/api/v1/godt-recipe/images/42/425b83de-49b1-4807-973d-a0fe0cb3a818?rule=w2000_auto",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "4 stk egg",
                "2 ss sukker",
                "2 ss smør",
                "1 l lettmelk",
                "2.5 dl fint sammalt hvetemel",
                "3.5 dl hvetemel",
                "1 dl havregryn",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            """Pisk sammen egg, sukker, smeltet smør og halvparten av melken. Rør inn fin sammalt hvete. Bland inn hvetemelet og spe med resten av melken. Vend inn havregryn til slutt. La deigen stå og svelle i en halvtime.\nStek tynne pannekaker i stekepanne på middels varme. Bruk litt smør eller formfett til stekingen dersom du ikke har en god teflonpanne. Serveres nystekte!""",
            self.harvester_class.instructions(),
        )
