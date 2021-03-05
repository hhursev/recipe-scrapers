from recipe_scrapers.purplecarrot import PurpleCarrot
from tests import ScraperTest


class TestPurpleCarrotScraper(ScraperTest):

    scraper_class = PurpleCarrot

    def test_host(self):
        self.assertEqual("purplecarrot.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.purplecarrot.com/recipe/roasted-cauliflower-lentil-bowl-with-avocado-curried-balsamic-vinaigrette",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            "Roasted Cauliflower Lentil Bowl with Avocado & Curried Balsamic Vinaigrette",
            self.harvester_class.title(),
        )

    def test_yields(self):
        self.assertEqual("2 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://images.purplecarrot.com/uploads/product/image/1357/_1400_700_Vegan_TB12_RoastedCauli_Hero-4-fcfead9e8b8f0df11875ae6baae25ab0.jpg",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "¾ cup brown lentils",
                "6 oz cauliflower florets",
                "1 tbsp curry powder",
                "2 mini sweet peppers",
                "4 oz red grapes",
                "1 avocado",
                "2 tbsp balsamic vinaigrette",
                "4 oz Arcadian greens",
                "1 tsp vegetable oil*",
                "Salt and pepper*",
                "*Not included",
                "For full ingredient list, see Nutrition",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "1 - Start the lentils. 2 - Roast the cauliflower . 3 - Prepare the toppings. 4 - Make the curried balsamic vinaigrette. 5 - Make the salad. 6 - Serve.",
            self.harvester_class.instructions(),
        )
