from recipe_scrapers.madensverden import MadensVerden
from tests import ScraperTest


class TestMadensVerdenScraper(ScraperTest):

    scraper_class = MadensVerden

    def test_host(self):
        self.assertEqual("madensverden.dk", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            "Rabarbertrifli - nem trifli med rabarber og makron",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual(
            "Dessert",
            self.harvester_class.category(),
        )

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_cook_time(self):
        self.assertEqual(15, self.harvester_class.cook_time())

    def test_prep_time(self):
        self.assertEqual(15, self.harvester_class.prep_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://madensverden.dk/wp-content/uploads/2017/08/billederesultat-for-rabarbertrifli.jpg",
            self.harvester_class.image(),
        )

    def test_nutrients(self):
        self.assertEqual(
            {"calories": "270 kcal", "servingSize": "1 person"},
            self.harvester_class.nutrients(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "400 gram rabarber",
                "75 gram sukker",
                "10 gram vaniljesukker",
                "2 pasteuriserede æggeblommer (1 bæger)",
                "40 gram sukker",
                "10 gram majsstivelse",
                "2,5 deciliter sødmælk",
                "2,5 deciliter piskefløde",
                "100 gram makroner",
                "40 gram mandelflager",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Start med at lave rabarberkompot. Rabarber snittes i tynde skiver, som koges i en kasserolle sammen med sukker og vaniljesukker. Kogetiden er cirka 10 minutter, og du skal ikke tilsætte vand, da rabarberne kaster rigeligt med væske af sig. Lad kompotten køle af.
Cremen laves ved at piske æggeblommer sammen med sukker og majsstivelse i en kasserolle. Koges op med sødmælken indtil den har den rette konsistens, og du skal piske i den undervejs så cremen ikke brænder på. Lad den køle lidt af.
Fløden piskes til en let flødeskum.
Anret nu trifli med rabarber i portionsglas.
Først med et lag creme nederst, så knuste makroner og ovenpå det den lækre rabarberkompot.
Slut af med flødeskum og pynt med mandelflager.
Stil rabarbertriflierne i køleskabet, og lad dem trække i mindst en time før servering.""",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.69, self.harvester_class.ratings())

    def test_author(self):
        self.assertEqual("Holger Rørby Madsen", self.harvester_class.author())

    def test_cuisine(self):
        self.assertEqual("Dansk", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Rabarbertrifli er en populær dessert, der også laves med knuste makroner og letpisket flødeskum. Den lækre trifli med rabarber kan laves god tid i forvejen.",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("da-DK", self.harvester_class.language())

    def test_site_name(self):
        self.assertEqual("Madens Verden", self.harvester_class.site_name())
