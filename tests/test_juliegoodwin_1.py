from recipe_scrapers.juliegoodwin import JulieGoodwin
from tests import ScraperTest


class TestJudyGoodwinScraper(ScraperTest):
    scraper_class = JulieGoodwin
    test_file_name = "juliegoodwin_1"

    def test_host(self):
        self.assertEqual("juliegoodwin.com.au", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://juliegoodwin.com.au/zucchini-slice-recipe/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Zucchini Slice", self.harvester_class.title())

    def test_author(self):
        self.assertEqual("Julie Goodwin", self.harvester_class.author())

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("Makes 1 Slice = 12 Pieces", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://juliegoodwin.com.au/wordpress/wp-content/uploads/2016/03/slice.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 zucchini, grated",
                "1 large onion finely chopped",
                "3 rashers bacon finely chopped",
                "1 cup tasty cheese grated",
                "1 cup self-raising flour",
                "½ cup of oil",
                "5 eggs",
                "salt/pepper",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Preheat oven to 170°C. Grease and line a non-stick lamington tin.",
                    "Combine zucchini, onion, bacon, flour and cheese in a large bowl. Add oil and lightly beaten eggs, and mix. Season with a little salt and pepper. Pour into lamington tin.",
                    "Bake for 35-40 mins until golden and set. Allow to cool slightly before cutting.",
                ]
            ),
            self.harvester_class.instructions(),
        )
