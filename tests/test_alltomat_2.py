from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.alltomat import AllTomat
from tests import ScraperTest


class TestAllTomatScraper(ScraperTest):

    scraper_class = AllTomat
    test_file_name = "alltomat_2"

    def test_host(self):
        self.assertEqual("alltommat.se", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://alltommat.expressen.se/recept/kottbullar-med-potatismos-graddsas-gurka-och-lingon/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("cecilia lundin", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Köttbullar med potatismos, gräddsås, gurka och lingon",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual("Husmanskost", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(50, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://static.cdn-expressen.se/images/aa/eb/aaeb4b38c3994b3ab57625533ca3e9b7/16x9/1920@80.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "500 g nötfärs",
                "1.5 dl vatten",
                "0.75 dl ströbröd",
                "0.5 gul lök",
                "1 ägg",
                "2 msk konc kalvfond",
                "1 tsk salt",
                "2 krm nymald svartpeppar",
                "2 msk smör",
                "1 kg potatis",
                "2 msk smör",
                "2.5 dl mjölk",
                "1.5 tsk salt",
                "2 dl vatten",
                "1 dl vispgrädde",
                "2 msk konc kalvfond",
                "1 tsk kinesisk soja",
                "2 krm strösocker",
                "1 krm nymald svartpeppar",
                "2 msk majsstärkelse (Maizena)",
                "0.5 gurka",
                "1 msk ättiksprit (12 %)",
                "2 msk strösocker",
                "3 msk vatten",
                "1 krm nymald svartpeppar",
                "2 msk persilja",
                "1.5 dl lingon",
                "0.5 dl strösocker",
                "persilja",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "500 g nötfärs",
                        "1.5 dl vatten",
                        "0.75 dl ströbröd",
                        "0.5 gul lök",
                        "1 ägg",
                        "2 msk konc kalvfond",
                        "1 tsk salt",
                        "2 krm nymald svartpeppar",
                        "2 msk smör",
                    ],
                    purpose="Ingredienser",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 kg potatis",
                        "2 msk smör",
                        "2.5 dl mjölk",
                        "1.5 tsk salt",
                    ],
                    purpose="Potatismos",
                ),
                IngredientGroup(
                    ingredients=[
                        "2 dl vatten",
                        "1 dl vispgrädde",
                        "2 msk konc kalvfond",
                        "1 tsk kinesisk soja",
                        "2 krm strösocker",
                        "1 krm nymald svartpeppar",
                        "2 msk majsstärkelse (Maizena)",
                    ],
                    purpose="Sås",
                ),
                IngredientGroup(
                    ingredients=[
                        "0.5 gurka",
                        "1 msk ättiksprit (12 %)",
                        "2 msk strösocker",
                        "3 msk vatten",
                        "1 krm nymald svartpeppar",
                        "2 msk persilja",
                    ],
                    purpose="Gurka",
                ),
                IngredientGroup(
                    ingredients=[
                        "1.5 dl lingon",
                        "0.5 dl strösocker",
                    ],
                    purpose="Rårörda lingon",
                ),
                IngredientGroup(
                    ingredients=[
                        "persilja",
                    ],
                    purpose="Garnering",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = """Gurka: Blanda ättika, socker, vatten och peppar och rör tills sockret har lösts upp. Hyvla gurkan tunt, t ex med en osthyvel och lägg i lagen. Låt stå i. kylen ca 1 timme. Blanda ner persilja precis före servering.\nLingon: Blanda de frysta lingonen med socker. Låt stå i rumstemperatur ca 1 timme. Rör då och då.\nSås: Blanda vatten, grädde, fond och soja i en kastrull. Låt koka upp och sjud ca 5 min. Krydda med socker och peppar. Rör ut majsstärkelsen i lite kallt vatten och blanda ner i såsen. Låt koka upp.\nBlanda vatten och ströbröd och låt stå ca 5 min. Skala och finriv löken. Blanda färsen med ströbrödsblandning, lök, ägg och fon. Krydda med salt och peppar. Forma färsen till stora köttbullar. Stek köttbullarna runtom i smör tills de fått fin färg och är genomstekta, 8–10 min.\nMos: Skala och skär potatisen i mindre bitar. Koka den mjuk i lättsaltat vatten. Låt potatisen rinna och ånga av. Mosa den tillsammans med smör med en elvisp. Koka up mjölken. Häll mjölken över potatisen och vispa kraftigt till ett luftigt mos. Krydda med salt.\nServera köttbullarna med mos, sås, gurka och lingon. Garnera med hackad persilja."""
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(3.8, self.harvester_class.ratings())
