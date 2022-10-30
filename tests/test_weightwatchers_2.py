# mypy: allow-untyped-defs

from recipe_scrapers.weightwatchers import WeightWatchers
from tests import ScraperTest


class TestWeightwatchersScraper(ScraperTest):

    # Test-Url:
    # https://cmx.weightwatchers.de/details/WWRECIPE:562a9bc8a43e6bde2cf369df

    scraper_class = WeightWatchers
    test_file_name = "weightwatchers_2"

    def test_host(self):
        self.assertEqual("www.weightwatchers.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("WeightWatchers", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Hackbraten Stroganoff")

    def test_category(self):
        self.assertEqual("WeightWatchers", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(65, self.harvester_class.total_time())

    def test_cook_time(self):
        self.assertEqual(25, self.harvester_class.cook_time())

    def test_prep_time(self):
        self.assertEqual(40, self.harvester_class.prep_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cmx.weightwatchers.com/assets-proxy/weight-watchers/image/upload/t_WINE_EXTRALARGE/vziguy9ale25vtx7spgl.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "125 g Champignons, frisch",
                "5 Stück Cornichons",
                "1 Bund Frühlingszwiebeln/Lauchzwiebeln",
                "600 g Tatar, roh",
                "2 EL Paniermehl/Semmelbrösel",
                "1 Stück, Gewichtsklasse M Eier, Hühnereier",
                "4 TL Senf, klassisch",
                "1 Prise(n) Salz/Jodsalz",
                "1 Prise(n) Pfeffer",
                "600 g Kartoffeln; festkochend",
                "2 TL Halbfettmargarine, 39 % Fett",
                "1 EL Weizenmehl",
                "300 ml Gemüsebouillon/Gemüsebrühe, zubereitet; (2 TL Instantpulver)",
                "3 EL Crème légère",
                "2 EL, gehackt Petersilie",
                "430 g Rote Bete (Konserve); entspricht 1 Glas",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredientsCount(self):
        self.assertEqual(16, len(self.harvester_class.ingredients()))

    def test_instructions(self):
        self.assertEqual(
            "Backofen auf 200° C (Gas: Stufe 3, Umluft: 180° C) vorheizen. Champignons trocken abreiben und mit Cornichons in feine Würfel schneiden. Frühlingszwiebeln waschen und in Ringe schneiden. Champignon-, Cornichonwürfel und Frühlingszwiebelringe mit Tatar, Paniermehl, Ei, 1 Teelöffel Senf, Salz und Pfeffer verkneten und zu einem Braten formen.\nHackbraten in eine Kastenform (Länge 30 cm) geben und im Backofen auf unterer Schiene ca. 45 Minuten garen. Kartoffeln schälen, halbieren und in Salzwasser ca. 20 Minuten garen. Für die Sauce Margarine in einem Topf schmelzen, Mehl darin hellgelb anschwitzen, unter Rühren mit Brühe ablöschen, ca. 4 Minuten köcheln lassen. Mit Créme légère verfeinern und mit Salz, Pfeffer, restlichem Senf und Petersilie würzen. Kartoffeln abgießen und Rote Bete abtropfen lassen. Hackbraten mit Senfsauce, Salzkartoffeln und Rote Bete servieren.",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "Wenn das mal keine mutige Abwandlung des beliebten Klassiker ist. Schmeckt übrigens ganz vorzüglich!",
            self.harvester_class.description(),
        )

    def test_difficulty(self):
        self.assertEqual("Mittel", self.harvester_class.difficulty())

    def test_nutrients(self):
        expected_nutrients = {"personal points": "10 personal points"}
        self.assertEqual(self.harvester_class.nutrients(), expected_nutrients)
