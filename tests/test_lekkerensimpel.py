from recipe_scrapers.lekkerensimpel import LekkerEnSimpel
from tests import ScraperTest


class TestLekkerEnSimpelScraper(ScraperTest):

    scraper_class = LekkerEnSimpel

    def test_host(self):
        self.assertEqual("lekkerensimpel.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual("Poké bowl met kip", self.harvester_class.title())

    def test_image(self):
        self.assertEqual(
            "https://www.lekkerensimpel.com/wp-content/uploads/2022/03/588A2370-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "200 gr sushi rijst",
                "2 el sushi azijn (of 1,5 el rijstazijn, 1 tl suiker en een snuf zout)",
                "2 krokante kipschnitzels",
                "1 avocado",
                "100 gr peen julienne",
                "0.5 komkommer",
                "2 el gebakken uitjes",
                "Japanse mayonaise",
                "sojasaus",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertIn(
            "Begin met het maken van de sushirijst. Wij houden hiervoor dit sushirijst recept aan. Tip: heb je weinig tijd? Gebruik dan pandan rijst in plaats van sushi rijst. Dit is een stuk sneller klaar.\nSnijd de avocado en komkommer in plakjes/reepjes.\nGiet een scheutje olie in een koekenpan en bak de kipschnitzels volgens de instructies op het pak. Tip: maak ook eens de kipschnitzels zelf. Snijd de kipschnitzels daarna in plakjes.\nVerdeel de rijst over twee kommen. Verdeel de komkommer, kip, peen julienne, avocado en gebakken uitjes hier overheen. Als laatste verdeel je wat Japanse mayonaise en sojasaus over het geheel.",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "Een heerlijke poké bowl met kip, avocado, peen julienne en edamame bonen. Een makkelijk gerecht dat in 30 minuten op tafel staat én waarmee je heel goed kunt variëren.",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("nl-NL", self.harvester_class.language())
