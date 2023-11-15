from recipe_scrapers.lekkerensimpel import LekkerEnSimpel
from tests import ScraperTest


class TestLekkerEnSimpelScraper3(ScraperTest):
    scraper_class = LekkerEnSimpel
    test_file_name = "lekkerensimpel_3"

    def test_host(self):
        self.assertEqual("lekkerensimpel.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            "Hartige taart met gehakt en sperziebonen", self.harvester_class.title()
        )

    def test_image(self):
        self.assertEqual(
            "https://www.lekkerensimpel.com/wp-content/uploads/2016/10/IMG_1300.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "200 gr sperziebonen",
                "250 gr gehakt",
                "1 ui",
                "150 ml creme fraiche",
                "3 eieren",
                "2 tl paprikapoeder",
                "1 tl kerriepoeder",
                "halve tl komijnpoeder",
                "handje geraspte kaas",
                "snufje zout en peper",
                "5 plakjes bladerdeeg (ontdooid)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertIn(
            "Verwarm de oven voor op 200 graden. Snipper de ui. Kook de sperziebonen ongeveer 5 minuten. Giet een scheutje olie in een pan en fruit de ui. Voeg daarna het gehakt en de kruiden toe en bak het gehakt rul. Meng het gehakt en de sperziebonen door elkaar.\n\nVerdeel de plakjes bladerdeeg over een ingevette (spring)vorm. Prik met een vork wat gaatjes in de bodem. Eventueel kun je nog een laagje paneermeel over het bladerdeeg verdelen, zodat het bladerdeeg niet zompig wordt. Schep het gehakt-sperziebonen mengsel hier overheen.\n\nEieren, creme fraiche en snufje zout en peper mengen in een bakje. Giet dit over het gehakt mengsel. Strooi een beetje geraspte kaas er overheen.",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "Hartige taarten zijn lekker en leuk om te maken omdat je er zo goed mee kunt variëren. Wat dacht je van een hartige taart met gehakt?",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("nl-NL", self.harvester_class.language())
