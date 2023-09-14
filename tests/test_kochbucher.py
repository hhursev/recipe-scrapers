# mypy: allow-untyped-defs

from recipe_scrapers.kochbucher import Kochbucher
from tests import ScraperTest


class TestKochbucherScraper(ScraperTest):

    scraper_class = Kochbucher

    def test_host(self):
        self.assertEqual("kochbucher.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Kochbucher", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Putengeschnetzeltes mit Reis und Blattsalat", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Salzige Gerichte", self.harvester_class.category())

    def test_image(self):
        self.assertEqual(
            "https://kochbucher.com/wp-content/uploads/2023/07/360032370_811443810387852_6360593443735502032_n-1000x600.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        ingredients_data = [
            "500 g Putenfleisch",
            "1 Zwiebel",
            "1 EL Tomatenmark",
            "50 Rohschinkenwürfel light",
            "1 EL Speisestärke",
            "250 ml Cremefine",
            "200 ml Wasser",
            "1 TL Tessiner Kräuter Gewürzmischung",
            "Pfeffer",
            "Salz",
            "Etwas Öl zum Anbraten",
        ]
        ingredients_list = self.harvester_class.ingredients()
        self.assertEqual(ingredients_data, ingredients_list)

    def test_instructions(self):
        expected_instructions = [
            "Zwiebel würfeln, Fleisch in Streifen schneiden",
            "Gemeinsam in etwas Öl rundherum braun anbraten",
            "Tomatenmark hinzufügen, kurz anrösten",
            "Schinkenwürfel hinzufügen",
            "Mit Stärke bestäuben und gut vermischen",
            "Wasser und Cremefine hinzufügen, aufkochen lassen",
            "Gewürze hinzufügen",
        ]
        expected_instructions = "\n".join(expected_instructions)
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def language(self):
        return "de"
