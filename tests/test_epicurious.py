from recipe_scrapers.epicurious import Epicurious
from tests import ScraperTest


class TestEpicurious(ScraperTest):

    scraper_class = Epicurious

    def test_host(self):
        self.assertEqual("epicurious.com", self.harvester_class.host())

    def test_canonical_url(self):
        # TODO: Find a way to supply original content base URL at test-time (via WARC-file?)
        self.assertEqual(
            "https://test.example.com/epicurious.testhtml_files/ramen-noodle-bowl-with-escarole-and-spicy-tofu-crum_002.html",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Ramen Noodle Bowl with Escarole and Spicy Tofu Crumbles",
        )

    def test_total_time(self):
        self.assertEqual(None, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://assets.epicurious.com/photos/568194b8fb9544f72b678fd4/6:4/w_274%2Ch_169/Ramen-Noodle-Bowl-With-Escarole.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 (5.5-ounce) servings fresh or dried ramen noodles",
                "4 cups torn escarole",
                "3 tablespoons Roasted Garlic Chili Sauce",
                "Kosher salt",
                "4 Pickled Scallions",
                "Spicy Tofu Crumbles, thinly sliced radish, and chopped peanuts (for serving)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            'Cook noodles according to package directions. During the last minute of cooking, add escarole. Drain and rinse under cold water.\nToss noodles, escarole, and chili sauce in a large bowl until coated; season with salt. Divide noodles between bowls. Slice scallions into 1" pieces and place on top of noodles along with some tofu crumbles, radishes, and peanuts.',
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        return self.assertGreaterEqual(self.harvester_class.ratings(), 0.99)

    def test_reviews(self):
        self.assertCountEqual(
            "This was yummy, the tofu especially. The sauce for the tofu really made the dish. In light of that, I'd like to try this again with rice noodles instead of ramen and chicken instead of tofu. I didn't really dig the fresh ramen as much as I thought I would (too eggy). I'm not sure chicken will work quite so well as the tofu but it's worth a shot.",
            self.harvester_class.reviews()[-1]["review_text"],
        )

        self.assertEqual(self.harvester_class.reviews()[-1]["rating"], 4)
