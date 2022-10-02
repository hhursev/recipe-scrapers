from recipe_scrapers.reishunger import Reishunger
from tests import ScraperTest


class TestReishungerScraper(ScraperTest):

    scraper_class = Reishunger

    @property
    def test_file_name(self):
        return "{}_1".format(self.scraper_class.__name__.lower())

    def test_host(self):
        self.assertEqual("reishunger.de", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("pommesherz", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Crispy Tofu Bowl", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cdn.reishunger.com/crispy-tofu-bowl.jpg?quality=85",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "200 gr Bio Basmati Reis",
                "50 ml Erdnuss Sauce",
                "200 gr Tofu",
                "etwas Paniermehl",
                "etwas Mehl",
                "1 Ei",
                "100 gr Edamame",
                "1 Möhre",
                "1/4 Rotkohl",
                "50 gr Zuckerschoten",
                "5 Maiskölbchen",
                "30 gr Sprossen",
                "eine Handvoll Cashew Kerne",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n\n\nZubereitung\n\n\n\n\n\n\n\n\n\n1. Schritt\n\n\n\n\nReis nach Anleitung im Digitalen Reiskocher oder Kochtopf kochen.\n\n\n\n2. Schritt\n\n\n\n\nGemüse schneiden und ca. 5 min blanchieren.\n\n\n\n3. Schritt\n\n\n\n\nDen Tofu in Stücke schneiden und in Mehl Ei und Paniermehl wälzen und kurz von allen Seiten anbraten.\n\n\n\n4. Schritt\n\n\n\n\nCashew Kerne in einer Pfanne kurz anrösten.\n\n\n\n5. Schritt\n\n\n\n\nDie Sauce erwärmen und den Tofu auf einen Spieß ziehen (optimal).\n\n\n\n6. Schritt\n\n\n\n\nAlles schön anrichten und mit den Sprossen toppen. Guten Reishunger! :-)\n\n\n\n\n",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())
