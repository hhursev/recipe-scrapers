# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.nrkmat import NRKMat
from tests import ScraperTest


class TestNRKMatScraper(ScraperTest):

    scraper_class = NRKMat
    test_file_name = "nrkmat_2"

    def test_host(self):
        self.assertEqual("nrk.no", self.harvester_class.host())

    def test_author(self):
        self.assertEqual(
            "Rolf Tikkanen Øygarden i Sørlandssendinga/NRK P1",
            self.harvester_class.author(),
        )

    def test_title(self):
        self.assertEqual(
            "Kikertsuppe med eple og karri",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual("Middag", self.harvester_class.category())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://gfx.nrk.no/N4ehJVVfjwllrjaJIVPlEwDrxwjw_2UhedQNN4ad9Pxw.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 stor gul løk",
                "2 hvitløkfedd",
                "3 ts karripulver",
                "5 dl kyllingbuljong",
                "1,5 boks ferdig kokte kikerter",
                "1 grønt eple",
                "limejuice",
                "salt",
                "pepper",
                "2 ss finhakket bladpersille",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 stor gul løk",
                        "2 hvitløkfedd",
                        "3 ts karripulver",
                        "5 dl kyllingbuljong",
                        "1,5 boks ferdig kokte kikerter",
                        "1 grønt eple",
                        "limejuice",
                        "salt",
                        "pepper",
                        "2 ss finhakket bladpersille",
                    ],
                    purpose=None,
                )
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Sett på en kasserolle på medium temperatur og ha i litt olje.\nHakk løk og hvitløk grovt, la det surre i oljen. Tilsett karripulveret.\nHa i kikertene og bland godt.\nSlå over kyllingbuljong, og kok opp suppen.\nLa suppen koke i cirka 6–7 minutter.\nKjør suppen helt glatt med en stavmikser, ha den tilbake i kjelen og varm opp.\nKutt et eple i terninger.\nHa suppen i dype skåler, ringle over litt olivenolje, saften av en presset lime, salt og pepper. Topp suppen med finhakket grønt eple og bladpersille. Dersom du har litt røykt paprikapulver, kan du gjerne gi suppen et fint lite dryss.",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "Det er mange grunner til å nyte kikertsuppe med eple og karri. Suppen varmer godt i kroppen, den er stappfull av proteiner, kjernesunn og den koster ikke mer enn en tyggegummipakke!",
            self.harvester_class.description(),
        )
