# mypy: allow-untyped-defs

from recipe_scrapers.vegetarbloggen import Vegetarbloggen
from tests import ScraperTest


class TestVegetarbloggenScraper(ScraperTest):

    scraper_class = Vegetarbloggen

    def test_host(self):
        self.assertEqual("vegetarbloggen.no", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Mari Hult", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Pasta i gresskarsaus", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("hovedrett", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.vegetarbloggen.no/content/uploads/sites/7/2021/11/gresskarpasta-oppskriftsbilde.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "0,5 flaskegresskar (eller annen type gresskar)",
                "1 sjalottløk",
                "salt",
                "200 g tørka pasta (pass på at den er uten egg)",
                "olivenolje (til steking)",
                "10 blad salvie (sånn ca. )",
                "1,5 dl vegansk matfløte",
                "1 ts eplesidereddik (eventuelt sitronsaft)",
                "4 ss gresskarkjerner",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        expected_instructions = """
        Skjær skallet av gresskaret, del det i to på midten og fjern eventuelle kjerner (disse kan du steke i olje og ha på salt, blir godt!). Skjær fruktkjøttet i terninger med lengder på litt under 1 cm. Finhakk sjalottløk.
        Kok opp godt med vann i en gryte, ha i litt salt. Kok pasta etter anvisning på pakken.
        Varm opp litt olje til medium/høy varme i en stor gryte eller panne. Ha i gresskar, krydre med litt salt, og la det steke i noen minutter. Ha så i sjalottløk, og stek i et par minutter til.
        Dytt gresskaret til side slik at det tar ca. halvparten av bunnen gryten. Ha i litt mer olje i den tomme delen, og ha i salviebladene. Fres dem i et par minutter. Rør dem deretter sammen med gresskarterningene.
        Hell på vegansk fløte og eddik, og la gresskaret putre til pastaen er klar. Sil vannet av pastaen, ha den over i gryten med gresskarblandingen, rør sammen, smak eventuelt til med mer salt.
        Servér retten rykende varm, topp med gresskarkjerner.
        """
        expected_instructions = "\n".join(
            line.strip() for line in expected_instructions.split("\n")
        ).strip()

        actual_instructions = self.harvester_class.instructions().strip()
        self.assertEqual(expected_instructions, actual_instructions)

    def language(self):
        return "no"
