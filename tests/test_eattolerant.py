from recipe_scrapers import EatTolerant
from tests import ScraperTest


class TestEatTolerant(ScraperTest):
    scraper_class = EatTolerant

    def test_host(self):
        self.assertEqual("eattolerant.de", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://eattolerant.de/suppe/vegane-rotkohlsuppe-mit-kokosmilch-histaminarm-glutenfrei-low-carb/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Vegane Rotkohlsuppe mit Kokosmilch"
        )

    def test_description(self):
        self.assertEqual(self.harvester_class.description(), "")

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://eattolerant.de/wp-content/uploads/2022/01/Vegane-Rotkohlsuppe-13-scaled.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "500 g Rotkohl (Nettogewicht)",
                "1 kleiner Apfel (z.B. Boskopp)",
                "200 g Kartoffeln",
                "1 Zwiebel",
                "1 kleines Stück Ingwer",
                "500 ml Gemüsebrühe",
                "200 ml Kokosmilch",
                "1 TL Zucker",
                "20 ml Verjus Sauer",
                "3 EL Kokosöl",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Die äußeren Blätter vom Rotkohl entfernen, anschließend halbieren, großzügig den Strunk entfernen und in kleine Stücke schneiden.\nDen Apfel sowie die Kartoffeln waschen und schälen, ebenfalls in kleine Stücke schneiden.\nDie Zwiebel in Würfel schneiden und den Ingwer fein reiben.\nDas Kokosöl in einem Top erhitzen, anschließend die Zwiebel und den Rotkohl kurz darin anbraten. Währenddessen mit Salz würzen.\nDie Apfel- und Kartoffelstücke zugeben, ebenfalls kurz anbraten.\nDie Gemüsebrühe, Kokosmilch und den Ingwer zugeben und die Suppe ca. 25 Minuten köcheln lassen. Kurz vor Ende der Garzeit den Verjus sowie Zucker zugeben. Anschließend fein pürieren und sofort servieren.",
            self.harvester_class.instructions(),
        )
