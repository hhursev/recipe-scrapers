from recipe_scrapers.tastykitchen import TastyKitchen
from tests import ScraperTest


class TestTastyKitchenScraper(ScraperTest):

    scraper_class = TastyKitchen

    def test_host(self):
        self.assertEqual("tastykitchen.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.thepioneerwoman.com/food-cooking/recipes/a11059/restaurant-style-salsa/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Restaurant Style Salsa")

    def test_total_time(self):
        self.assertEqual(10, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://tastykitchen.com/recipes/wp-content/uploads/sites/2/2010/01/TPW_5376.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 can (28 Ounce) Whole Tomatoes With Juice",
                "2 cans (10 Ounce) Rotel (diced Tomatoes And Green Chilies)",
                "¼ cups Chopped Onion",
                "1 clove Garlic, Minced",
                "1 whole Jalapeno, Quartered And Sliced Thin",
                "¼ teaspoons Sugar",
                "¼ teaspoons Salt",
                "¼ teaspoons Ground Cumin",
                "½ cups Cilantro (more To Taste!)",
                "½ whole Lime Juice",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Note: this is a very large batch. Recommend using a 12-cup food processor, or you can process the ingredients in batches and then mix everything together in a large mixing bowl.",
                    "Combine whole tomatoes, Rotel, onion, jalapeno, garlic, sugar, salt, cumin, lime juice, and cilantro in a blender or food processor. Pulse until you get the salsa to the consistency you’d like—I do about 10 to 15 pulses. Test seasonings with a tortilla chip and adjust as needed.",
                    "Refrigerate salsa for at least an hour. Serve with tortilla chips or cheese nachos.",
                ]
            ),
            self.harvester_class.instructions(),
        )
