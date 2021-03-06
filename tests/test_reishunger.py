from recipe_scrapers.reishunger import Reishunger
from tests import ScraperTest


class TestReishungerScraper(ScraperTest):

    scraper_class = Reishunger

    def test_host(self):
        self.assertEqual("reishunger.de", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Luke", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Cremiges Erdnuss-Curry", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.reishunger.de/upload/123/19944/cremiges-erdnuss-curry.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "200g Basmati Reis",
                "2 TL Erdnussöl",
                "100g Brokkolli",
                "200g Tofu",
                "1 Dose Kichererbsen",
                "1 rote Zwiebel",
                "eine halbe Mango",
                "1 Stück Ingwer",
                "250ml Kokosmilch",
                "25g Rote Thai Curry Paste",
                "2 TL Bio Reissirup",
                "1-2 Kurkuma",
                "3 EL Wasser",
                "3 TL Erdnussmus",
                "1 Zitrone",
                "ein halber TL Salz",
                "2 TL Reisessig",
                "eine Prise Kreuzkümmel",
                "eine Prise Paprika",
                "eine Prise Limettenpulver",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Den Reis waschen und kochen.\nDas Öl in die Pfanne geben und erhitzen. Die Zwiebel, den Ingwer (ca. 1 cm großes Stück), den Tofu und den Brokkoli kleinschneiden. Die Kichererbsen abgießen.\nZwiebel, den Ingwer und den Tofu in die Pfanne geben und für 3-4 Minuten auf mittlerer Hitze anbraten. Den Brokkoli und die Kichererbsen hinzugeben, alles gut verrühren und alles weitere 4-5 Minuten anbraten.\nDie Mango in Würfel schneiden. Alle Zutaten für die Soße vermischen und zusammen mit der Mango in die Pfanne geben. Auf niedriger Hitze 3-4 Minuten köcheln lassen.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())
