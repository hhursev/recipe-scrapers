# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.nrkmat import NRKMat
from tests import ScraperTest


class TestNRKMatScraper(ScraperTest):

    scraper_class = NRKMat
    test_file_name = "nrkmat_1"

    def test_host(self):
        self.assertEqual("nrk.no", self.harvester_class.host())

    def test_author(self):
        self.assertEqual(
            "Gino D'Acampo i TV-programmet «Ginos italienske fristelser»",
            self.harvester_class.author(),
        )

    def test_title(self):
        self.assertEqual(
            "Honningmarinert grillet kylling med rosmarinpoteter",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual("Middag", self.harvester_class.category())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://gfx.nrk.no/XuK_5Mw6V4wOrt3NLJh-VQLHcFhoLAp4dsSMmlCiEmaw.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1,3 kg hel kylling",
                "3 ss flytende honning",
                "1 ss ferske rosmarinblader",
                "2 hvitløkfedd",
                "3 ss tomatpure",
                "50 ml olivenolje, extra virgin",
                "1/2 sitron, juicen",
                "1 ss fersk persille, hakket (til pynt)",
                "salt og nykvernet pepper",
                "500 g nypoteter",
                "75 ml olivenolje, extra virgin",
                "4 hvitløkfedd",
                "3 kvister rosmarin",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1,3 kg hel kylling",
                        "3 ss flytende honning",
                        "1 ss ferske rosmarinblader",
                        "2 hvitløkfedd",
                        "3 ss tomatpure",
                        "50 ml olivenolje, extra virgin",
                        "1/2 sitron, juicen",
                        "1 ss fersk persille, hakket (til pynt)",
                        "salt og nykvernet pepper",
                    ],
                    purpose=None,
                ),
                IngredientGroup(
                    ingredients=[
                        "500 g nypoteter",
                        "75 ml olivenolje, extra virgin",
                        "4 hvitløkfedd",
                        "3 kvister rosmarin",
                    ],
                    purpose="Potetene",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Når kyllingen skal varmebehandles hardt må eventuell hyssing som holder skroget sammen fjernes. Legg fuglen med brystet ned på en skjærefjøl. Bruk en skarp kniv og kutt langs begge sidene av ryggraden, og kast den. Vend kyllingen og bruk håndflaten til å trykke godt langs brystbenet for å flate ut fuglen, slik at den blir liggende flat.\nDrypp honning over kyllingen, deretter spres rosmarinblader og knust hvitløk over den. Fordel tomatpuré og drypp olje over den. Salt og pepre. Gni blandingen godt over hele kyllingen for å få marinaden jevnt fordelt.\nForvarm en stor jernpanne med riller over høy varme i 5-10 minutter. Når den er varm, reduseres varmen til middels og kyllingbrystsiden legges på grillpannen. Klem over sitronsaften når du snur kyllingen. Stek i 15 minutter på hver side, eller til den er gyllen og gjennomstekt. Sett til side for å hvile, og hold den varm.\nI mellomtiden deles nypotetene opp i grove biter. Kok potetene i saltet vann i 4-5 minutter, eller til de er møre. Tøm av vannet.\nVarm olivenoljen i en stor stekepanne på middels varme. Tilsett hvitløk skåret i tynne skiver. Når den begynner å surre tilsettes rosmarin og poteter. Krydre med salt og pepper. Stek potetene i 4-5 minutter, eller til de er gyllenbrune. Vend potetene ofte.\nSkjær kyllingen i biter og legg på et serveringsfat sammen med potetene. Dryss over persille og ha et siste skvis med sitron over retten før den serveres.",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "Kyllingen skal stekes på så høy varme at honning\xadmarinaden svir seg. Den bitre smaken av brent og den søte honningen smaker fortreffelig sammen med rosmarin\xadpotetene.",
            self.harvester_class.description(),
        )
