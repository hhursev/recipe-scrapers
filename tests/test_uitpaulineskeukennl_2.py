# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.uitpaulineskeukennl import UitPaulinesKeukenNL
from tests import ScraperTest


class TestuitPaulinesKeukenNL(ScraperTest):
    scraper_class = UitPaulinesKeukenNL
    test_file_name = "uitpaulineskeukennl_2"

    def test_host(self):
        self.assertEqual("uitpaulineskeuken.nl", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://uitpaulineskeuken.nl/recept/blondies-met-citroen",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Marianne Snel", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Blondies met citroen", self.harvester_class.title())

    def test_category(self):
        self.assertEqual(
            "Cake recepten, High tea, Koekjes recepten, Chocolade, Verjaardag, Bakrecepten",
            self.harvester_class.category(),
        )

    def test_total_time(self):
        self.assertEqual(55, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://uitpaulineskeuken.nl/wp-content/uploads/2022/07/Citroen-blondies-UPK-22-11-JUL-BLOGPOST-258.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "150 gr witte chocolade",
                "200 gr bloem",
                "125 gr roomboter",
                "2 eieren",
                "150 gr suiker",
                "1,5 tl vanille-extract",
                "130 gr garneer amandelen",
                "4 tl citroenrasp",
                "4 el citroensap",
                "snufje zout",
                "2 eiwitten",
                "250 gr poedersuiker",
                "2 tl citroenrasp",
                "3 el citroensap",
                "1 citroen (garnering )",
                "Bakvorm 20x20cm",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "150 gr witte chocolade",
                        "200 gr bloem",
                        "125 gr roomboter",
                        "2 eieren",
                        "150 gr suiker",
                        "1,5 tl vanille-extract",
                        "130 gr garneer amandelen",
                        "4 tl citroenrasp",
                        "4 el citroensap",
                        "snufje zout",
                    ],
                    purpose="Ingrediënten 9-12 blondies",
                ),
                IngredientGroup(
                    ingredients=[
                        "2 eiwitten",
                        "250 gr poedersuiker",
                        "2 tl citroenrasp",
                        "3 el citroensap",
                        "1 citroen (garnering )",
                    ],
                    purpose="Ingrediënten topping",
                ),
                IngredientGroup(
                    ingredients=[
                        "Bakvorm 20x20cm",
                    ],
                    purpose="Materiaal",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Verwarm de oven voor op 175 graden (boven- en onderwarmte), 160 graden (hetelucht). Bekleed de "
                    "bakvorm met bakpapier.",
                    "Hak de amandelen met een scherp mes in kleine stukjes.",
                    "Breek de chocolade in stukjes en laat samen met de boter in een steelpannetje op laag vuur "
                    "smelten tot een gladde massa. Neem de pan van het vuur en roer de suiker, snufje zout, "
                    "vanille-extract en citroenrasp er door. Voeg 1 voor 1 de eieren toe en klop goed door, "
                    "blijf kloppen zodat de eieren niet stollen. Schep de bloem en gehakte amandelen door het beslag.",
                    "Verdeel het beslag over de bakvorm en strijk de bovenkant glad. Bak de blondies 35-40 minuten in "
                    "de voorverwarmde oven tot de bovenkant goudbruin is. Haal uit de oven, prik verspreid over de "
                    "koek met een vork gaatjes en schenk de citroensap er over en laat helemaal afkoelen.",
                    "Maak ondertussen het glazuur. Klop de eiwitten, citroensap en rasp in een mengkom en roer de "
                    "poedersuiker er door. Meng tot een mooi glad glazuur. Strijk het glazuur over de bovenkant van "
                    "de blondies. Snijd in 9-12 blokjes. Snijd de citroen in dunne plakjes en leg op elk blokje een "
                    "citroentje.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(3.7, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Zin in iets lekkers? Probeer dan eens deze heerlijke\xa0blondies met citroen. Blondies zijn "
            "brownies maar dan van witte chocolade. Om ze lekker fris en zomers te maken hebben we in "
            "dit blondie recept veel citroen verwerkt. Zo bestrijk je de koek na het bakken direct met "
            "citroensap, dan kan de citroensmaak er goed in trekken. En daarna besmeer je het met "
            "citroenglazuur. Op en top zomer! Met dit recept maak je een koek die je in 9 tot 12 stukjes "
            "kunt snijden. Lekker voor bij de thee of koffie, ze staan geweldig op een high tea tafel en "
            "zijn een superleuke afsluiter voor een gezellige picknick! Zin in?",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("nl-NL", self.harvester_class.language())
