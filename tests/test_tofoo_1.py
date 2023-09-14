# mypy: allow-untyped-defs

from recipe_scrapers.tofoo import Tofoo
from tests import ScraperTest


class TestTofooScraper(ScraperTest):

    scraper_class = Tofoo
    test_file_name = "tofoo_1"

    def test_host(self):
        self.assertEqual("tofoo.co.uk", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("The Tofoo co.", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Banh Mi", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Vegan", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual(1, self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://tofoo.co.uk/wp-content/uploads/2020/09/Tofoo_Banh_Mi3134_v3_WebHeader.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "100g Naked Tofoo, sliced",
            "1 demi baguette",
            "1/2 tsp soy sauce",
            "1/2 lime, zested",
            "1/2 tsp grated ginger",
            "1/4 tsp garlic paste",
            "10g daikon, shredded",
            "10g carrot, shredded",
            "10g cucumber, shredded",
            "1 tbsp rice vinegar",
            "oil",
            "1g red chilli, sliced",
            "10g radish, sliced",
            "20g coriander (approx 10 sprigs)",
            "Freshly ground black pepper.",
            "1/4 tsp Sriracha",
            "Squeeze of lime",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = [
            "Slice the Baguette in half lengthways. Mix together the soy sauce, lime zest, ginger, and garlic in a bowl.",
            "Marinade the Tofoo for 30 minutes.",
            "Shred the Daikon, Carrot & Cucumber and lightly pickle in the rice vinegar for 10-20 minutes.",
            "Heat a frying pan, add the oil, and lightly fry the Tofoo for a few minutes until it turns golden brown. Allow to cool.",
            "Place all the fillings into the baguette, in layers, and drizzle over the Sriracha. Season with pepper and finish with a squeeze of lime.",
        ]
        expected_instructions = "\n".join(expected_instructions)
        self.assertEqual(expected_instructions, self.harvester_class.instructions())
