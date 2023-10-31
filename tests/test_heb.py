from recipe_scrapers.heb import HEB
from tests import ScraperTest


class TestHEBScraper(ScraperTest):
    scraper_class = HEB

    def test_host(self):
        self.assertEqual("heb.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.heb.com/recipe/recipe-detail/truffled-spaghetti-squash",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Truffled Spaghetti Squash", self.harvester_class.title())

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "H-E-B")

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 Large spaghetti squash",
                "1 tsp Truffle salt",
                "4 Tbsp Unsalted butter",
                "1 Tbsp White truffle oil",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Preheat oven to 400˚F. Cut spaghetti squash in half from top to bottom (lengthwise).",
                    "Place the spaghetti squash halves, cut side down onto a sheet pan. Roast for 30-45 minutes or until a knife can pierce the outside of skin easily, like a baked potato.",
                    "Once Squash is fully cooked and soft remove it from oven and let it cool for 10 minutes before scooping out meat of squash. In a serving bowl scoop or with a fork scrape out squash and add truffle salt, butter and truffle oil.",
                    "Toss all ingredients together until butter is fully melted. Season to taste if needed and serve warm.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_image(self):
        self.assertEqual(
            "https://images.heb.com/is/image/HEBGrocery/Test/truffled-spaghetti-squash-recipe.jpg",
            self.harvester_class.image(),
        )
