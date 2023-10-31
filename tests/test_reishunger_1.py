from recipe_scrapers.reishunger import Reishunger
from tests import ScraperTest


class TestReishungerScraper(ScraperTest):
    scraper_class = Reishunger
    test_file_name = "reishunger_1"

    def test_host(self):
        self.assertEqual("reishunger.de", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.reishunger.de/rezepte/rezept/2743/crispy-tofu-bowl",
            self.harvester_class.canonical_url(),
        )

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
            "\n".join(
                [
                    "Reis nach Anleitung im Digitalen Reiskocher oder Kochtopf kochen.",
                    "Gemüse schneiden und ca. 5 min blanchieren.",
                    "Den Tofu in Stücke schneiden und in Mehl Ei und Paniermehl wälzen und kurz von allen Seiten anbraten.",
                    "Cashew Kerne in einer Pfanne kurz anrösten.",
                    "Die Sauce erwärmen und den Tofu auf einen Spieß ziehen (optimal).",
                    "Alles schön anrichten und mit den Sprossen toppen. Guten Reishunger! :-)",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(3.67, self.harvester_class.ratings())
