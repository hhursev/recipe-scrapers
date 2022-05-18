from recipe_scrapers.lecker import Lecker
from tests import ScraperTest


class TestLeckerScraper(ScraperTest):

    scraper_class = Lecker

    def test_host(self):
        self.assertEqual("lecker.de", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("lecker.de", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Gemüsepfanne mit Hähnchen, Zuckerschoten und Brokkoli",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual("Hauptgericht", self.harvester_class.category())

    def test_prep_time(self):
        self.assertEqual(0, self.harvester_class.prep_time())

    def test_cook_time(self):
        self.assertEqual(25, self.harvester_class.cook_time())

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://images.lecker.de/,id=7e976162,b=lecker,w=610,cg=c.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 Brokkoli",
                "150 g Zuckerschoten",
                "2 Lauchzwiebeln",
                "4 kleine Hähnchenbrustfilets (à ca. 140 g)",
                "2 EL Sonnenblumenöl",
                "4 EL Sojasoße",
                "50 ml Gemüsebrühe",
                "6 Stiele Koriander",
                "1 EL Sesamsaat",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Schritt 1\nBrokkoli putzen und in kleinen Röschen vom Strunk schneiden. Zuckerschoten putzen. Lauchzwiebeln putzen und in ca. 10 cm lange Stücke schneiden.\nSchritt 2\nBrokkoli, Zuckerschoten und Lauchzwiebeln in reichlich kochendem Salzwasser 2–3 Minuten garen. Herausnehmen und mit kaltem Wasser abspülen. Auf ein Sieb gießen und gut abtropfen lassen.\nSchritt 3\nFleisch trocken tupfen und in Würfel (ca. 1,5 x 1,5 cm) schneiden. Öl in einer weiten Pfanne oder einem Wok erhitzen. Fleisch darin, unter Wenden, ca. 3 Minuten kräftig anbraten. Hitze reduzieren und weitere ca. 2 Minuten braten. Gemüse, Sojasoße und Brühe zufügen und 3–4 Minuten dünsten. Dabei gelegentlich wenden.\nSchritt 4\nKoriander waschen und trocken schütteln und, bis auf einige Blätter zum Garnieren, samt Stiel grob hacken. Sesam und Koriander zur Gemüsepfanne geben und untermischen. Mit Salz und Pfeffer abschmecken und mit Koriander garnieren.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.1, self.harvester_class.ratings())

    def test_nutrients(self):
        self.assertEqual(
            {
                "calories": "260",
                "carbohydrateContent": "7",
                "fatContent": "7",
                "proteinContent": "38",
                "servingSize": "1 Portion",
            },
            self.harvester_class.nutrients(),
        )

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Unser beliebtes Rezept für Gemüsepfanne mit Hähnchen, Zuckerschoten und Brokkoli und mehr als 65.000 weitere kostenlose Rezepte auf LECKER.de.",
            self.harvester_class.description(),
        )
