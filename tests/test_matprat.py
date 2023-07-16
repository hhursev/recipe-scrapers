from recipe_scrapers.matprat import Matprat
from tests import ScraperTest


class TestMatprat(ScraperTest):

    scraper_class = Matprat

    def test_host(self):
        self.assertEqual("matprat.no", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.matprat.no/oppskrifter/gjester/butter-chicken---indisk-smorkylling/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Butter chicken - indisk smørkylling"
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "MatPrat")

    def test_total_time(self):
        self.assertEqual(160, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://images.matprat.no/dxgehtetqy",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 stk. kylling (ca. 1300 g)",
                "4 båter hvitløk",
                "0,5 ss revet frisk ingefær",
                "2 ss sitronsaft",
                "1 dl gresk yoghurt",
                "0,5 ss chilipulver (helst indisk)",
                "1 ss garam masala",
                "1 ss rapsolje eller sennepsolje",
                "100 g cashewnøtter",
                "8 stk. tomat",
                "2 ss olje",
                "4 båter finhakket hvitløk",
                "0,5 ss revet frisk ingefær",
                "0,5 ss chilipulver (helst indisk)",
                "2 stk. hel kardemomme",
                "2 ts hel bukkehornkløver",
                "2 ss flytende honning",
                "1 stk. grønn chili",
                "2 ss smør",
                "1 dl fløte",
                "0,5 potte frisk koriander",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            """Fjern skinnet på kyllingen og tørk den godt. Kutt dype snitt i kjøttet på hele kyllingen. Finhakk hvitløk og bland med revet ingefær og sitronsaft, og gni kyllingen godt inn med blandingen. Dryss over litt salt. Sett kaldt i 20 minutter.\nBland sammen chilipulver, garam masala, olje og yoghurt. Tørk kyllingen med litt kjøkkenpapir og gni den godt inn med yoghurtblandingen. Plasser kyllingen på et fat og sett den kaldt i minst 4-6 timer, helst over natten.\nStek kyllingen midt i stekeovnen ved 200 °C, eller grill den til den er gyllenbrun og gjennomstekt, ca. 50 min. - 1 time.\nAvkjøl og plukk kjøttet av beina i store biter.\nLag smør- og tomatcurry: Bløtlegg cashewnøtter i litt lunkent vann i minst 30 minutter. Hell av vannet og mos nøttene i hurtigmikser eller med stavmikser. Sett til side.\nDel tomater i biter. Varm en sauteringspanne med olje og fres tomater, hvitløk, ingefær, chilipulver, Kardemomme og bukkehornkløver på middels varme til tomatene er helt myke.\nTilsett cashewpuré og bruk stavmikser eller hurtigmikser til å finmose sausen. Sil gjerne sausen gjennom en grov sikt for å få ut rester av skall, hvis du vil ha den ekstra fin.\nHa sausen tilbake i kjelen og la den småkoke i i noen minutter. Smak til med honning, finhakket grønn chili, salt og pepper. Visp inn fløte og romtemperert smør i den varme sausen.\nLegg kyllingbitene i sausen og la alt bli gjennomvarmt. Pynt med koriander.""",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())
