from recipe_scrapers.akispetretzikis import AkisPetretzikis
from tests import ScraperTest


class TestAkisPetretzikisScraper(ScraperTest):

    scraper_class = AkisPetretzikis

    def test_host(self):
        self.assertEqual("akispetretzikis.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Akis Petretzikis", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Lemon chicken with artichokes", self.harvester_class.title())

    def test_category(self):
        self.assertEqual(None, self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8-10", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://d3fch0cwivr6nf.cloudfront.net/system/uploads/medium/data/15973/aginares-lemonates-me-kotopoulo.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 1/2 kilo chicken breast fillet",
                "4-5 tablespoon(s) olive oil",
                "salt",
                "pepper",
                "50 g all-purpose flour",
                "2 onions",
                "2 clove(s) of garlic",
                "750 g artichokes",
                "80 g white wine",
                "lemon juice",
                "400 g water",
                "1 tablespoon(s) chicken stock pot",
                "2 tablespoon(s) tarragon",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Place a frying pan over high heat and add 2-3 tablespoons olive oil.",
                    "Cut the chicken into 2-3 cm pieces and add them into a bowl. Add salt, pepper, the flour, and mix.",
                    "Transfer the chicken to the hot pan and sauté for 3-4 minutes until golden.",
                    "Place a pot over high heat and add 2 tablespoons olive oil.",
                    "Finely chop the onions and the garlic, add them to the pot, and sauté.",
                    "Add the artichokes, the chicken, and deglaze the pot with the wine.",
                    "Add the lemon juice, the water, the chicken stock pot, the tarragon, and mix.",
                    "Cover with the lid and simmer over medium heat for 20-25 minutes.",
                    "Serve with pepper, olive oil, lemon slices, and parsley.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.91, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Lemon chicken with artichokes by the Greek chef Akis Petretzikis. A quick and easy recipe for a hearty lemon chicken with tender artichokes!",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("en", self.harvester_class.language())
