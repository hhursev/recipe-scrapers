from recipe_scrapers.coop import Coop
from tests import ScraperTest


class TestCoopScraper(ScraperTest):

    scraper_class = Coop

    def test_host(self):
        self.assertEqual("coop.se", self.harvester_class.host())

    def test_author(self):
        self.assertEqual(
            "Sara Begner och Ulrika Brydling", self.harvester_class.author()
        )

    def test_title(self):
        self.assertEqual(
            "Grillat kött med lime- och chilismör", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Huvudrätt", self.harvester_class.category())

    def test_cook_time(self):
        self.assertEqual(15, self.harvester_class.cook_time())

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://res.cloudinary.com/coopsverige/image/upload/w_1200,h_1200/v1651049395/cloud/251336.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "600.0 g flapsteak, flankstek, entrecôte eller mörad högrev",
                "1.0 tsk flingsalt",
                "100.0 g rumsvarmt smör",
                "1.0 röd chili, skivad",
                "2.0 lime",
                "4.0 hjärtsalladshuvud",
                "0.0 flingsalt",
                "0.0 grovmalen svartpeppar",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Tänd grillen med kol/briketter på ena sidan. Salta köttet. Vispa smöret fluffigt och smaksätt med chili och finrivet skal av 1 lime.\nVid fin glöd, grilla köttet direkt över värmen ca 1–2 min på varje sida. Köttet ska få fin yta och en innertemp på 52–55°. Låt vila 5 min.\nDela lime och hjärtsallad och grilla ca 5 min. Skär köttet i skivor, strö över flingsalt och svartpeppar och servera med hjärtsallad, smör och pressad lime.""",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.71, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Mer Smak", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Grillat kött som toppas med ett smakrikt smör på chili och pressad lime. Servera med grillad hjärtsallad.",
            self.harvester_class.description(),
        )
