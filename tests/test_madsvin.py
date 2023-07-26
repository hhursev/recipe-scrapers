# mypy: allow-untyped-defs

from recipe_scrapers.madsvin import Madsvin
from tests import ScraperTest


class TestMadsvinScraper(ScraperTest):
    scraper_class = Madsvin

    def test_host(self):
        self.assertEqual("madsvin.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual("Pandekager", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("10 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://madsvin.com/wp-content/uploads/2020/08/Pandekager-opskrift.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "125 gram hvedemel",
                "3 æg mellemstore",
                "3 dl sødmælk ((anden mælk kan også fint bruges))",
                "2 spsk sukker ((både rørsukker og hvid sukker kan bruges))",
                "½ stang vanilje ((eller 1 spsk vaniljesukker))",
                "25 gram smør ((smeltet))",
                "½ tsk salt",
                "smør (til stegning - neutral olie kan også bruges)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ratings(self):
        self.assertEqual(4.67, self.harvester_class.ratings())

    def test_category(self):
        self.assertEqual("bagværk,Dessert,Kage", self.harvester_class.category())

    def test_description(self):
        self.assertEqual(
            "De lækreste hjemmelavede pandekager, der vækker glæde hos både børn og voksne",
            self.harvester_class.description(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Pandekager\n"
            "Hæld mel, salt, sukker og vanilje i en skål og slå æggene ud i den.\n"
            "Pisk sammen til en ensformet masse uden klumper.\n"
            "Smelt smør i en kasserolle eller i mikroovnen, og rør ud i pandekagedejen.\n"
            "Pisk til sidst mælk i i dejmassen, og sæt den på køl i 20-30 minutter, så den lige kan nå at sætte sig (det hjælper også pandekagen til at holde lidt bedre sammen).\n"
            "Put en klat smør på en middelvarm pande, hæld 0,5-0,75 dl pandekagedej på panden og lad det stege til pandekagen bliver fast - det tager 45-60 sekunder..\n"
            "Vend den herefter og lad den stege i 45-60 sekunders tid, så den er let gylden på begge sider.\n"
            "Læg pandekagen på en tallerken og dæk med staniol/alufolie så de holdes varme.\n"
            "Gentag ovenstående trin til alle pandekager er lavet.\n"
            "Servér med marmelade, sukker, is, sirup, honning, frugt - eller hvad du nu har lyst til.\n"
            "Her er det vitterligt kun fantasien, der sætter grænser.",
            self.harvester_class.instructions().replace(". ", ".\n"),
        )

    def test_language(self):
        self.assertEqual("da-DK", self.harvester_class.language())
