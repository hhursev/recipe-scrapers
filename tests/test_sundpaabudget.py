from recipe_scrapers.sundpaabudget import SundPaaBudget
from tests import ScraperTest


class TestSundPaaBudgetScraper(ScraperTest):

    scraper_class = SundPaaBudget

    def test_host(self):
        self.assertEqual("sundpaabudget.dk", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            "One pot pasta med kyllingekebab",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual(
            "Kylling,One pot",
            self.harvester_class.category(),
        )

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_cook_time(self):
        self.assertEqual(20, self.harvester_class.cook_time())

    def test_prep_time(self):
        self.assertEqual(10, self.harvester_class.prep_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://sundpaabudget.dk/wp-content/uploads/2021/08/20210803123311_IMG_0714.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "300 g kyllingekebab",
                "1 spsk olie",
                "2 alm. løg",
                "2 tomater",
                "2 peberfrugter",
                "300 g fuldkornsspaghetti (el. pasta)",
                "125 g flødeost m. hvidløg (el. chili)",
                "7 dl vand",
                "1 bouillonterning",
                "0,5 tsk spidskommen",
                "0,5 tsk paprika (evt. røget)",
                "chili eller cayennepeber efter smag",
                "salt og peber",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Rengør og hak løg, peberfrugt og tomater i tern.
Opvarm olie i en stor gryde og svits kyllingekebaben et par minutter. Tilsæt grøntsagerne og lad det svitse med yderligere 2 minutter.
Tilsæt spaghetti, flødeost, vand, bouillonterning og krydderier.
Lad retten simre ved middelvarme til spaghettien er aldente og vandet er kogt næsten ind til en cremet sauce.
Smag til med salt og peber.""",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(3.9, self.harvester_class.ratings())

    def test_author(self):
        self.assertEqual("Britt // Sund på budget", self.harvester_class.author())

    def test_description(self):
        self.assertEqual(
            "Nem og lækker one pot med kyllingekebab (du kan også bruge okse/lam, hvis du hellere vil det).",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("da-DK", self.harvester_class.language())

    def test_site_name(self):
        self.assertEqual("Sund på budget", self.harvester_class.site_name())
