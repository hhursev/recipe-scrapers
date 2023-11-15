# mypy: allow-untyped-defs

from recipe_scrapers.goodhousekeeping import GoodHousekeeping
from tests import ScraperTest


class TestGoodHousekeepingScraper(ScraperTest):
    scraper_class = GoodHousekeeping
    test_file_name = "goodhousekeeping_1"

    def test_host(self):
        self.assertEqual("goodhousekeeping.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual(
            "The Good Housekeeping Cookery Team", self.harvester_class.author()
        )

    def test_title(self):
        self.assertEqual("Spiced pumpkin soup", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Halloween,dinner", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://hips.hearstapps.com/goodhousekeeping-uk/main/embedded/5444/t5-Spiced-Pumpkin-Soup-de.jpg?crop=1.00xw:1.00xh;0,0&resize=1200:*",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "600 g pumpkin flesh, roughly chopped",
                "2 celery sticks, roughly chopped",
                "1 garlic clove, roughly chopped",
                "1 tsp. each ground cumin and coriander",
                "800 mL vegetable stock",
                "200 mL coconut milk",
                "1 tbsp. pumpkin seeds",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        instructions = [
            "Put the pumpkin flesh into a food processor and whiz for 30sec until almost smooth. Add the celery, garlic and spices and whiz again for 30 seconds. Empty into a large pan.",
            "Pour over stock and coconut milk, bring to the boil, then cover and simmer for 15 minutes.",
            "Remove from heat and blend until smooth - do this in batches, if necessary. Check the seasoning and ladle into warmed soup bowls. Sprinkle with pumpkin seeds and freshly ground black pepper. Serve with crusty bread.",
        ]
        self.assertEqual("\n".join(instructions), self.harvester_class.instructions())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_nutrients(self):
        self.assertEqual(
            {
                "calories": "222",
                "fatContent": "20g",
                "saturatedFatContent": "15g",
                "sugarContent": "6g",
                "carbohydrateContent": "8g",
            },
            self.harvester_class.nutrients(),
        )

    def test_description(self):
        self.assertEqual(
            "Use the flesh from your Halloween pumpkin in this speedy spiced pumpkin soup recipe. It's the perfect comfort food for winter weather.",
            self.harvester_class.description(),
        )
