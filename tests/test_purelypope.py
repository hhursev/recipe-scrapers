from recipe_scrapers.purelypope import PurelyPope
from tests import ScraperTest


class TestPurelyPopeScraper(ScraperTest):

    scraper_class = PurelyPope

    def test_host(self):
        self.assertEqual("purelypope.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://purelypope.com/sweet-chili-brussel-sprouts/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Sweet Chili Brussel Sprouts")

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://purelypope.com/wp-content/uploads/2020/05/IMG_5412-1-150x150.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 cups brussel sprouts, stems removed & cut in half",
                "2 tbsp coconut aminos",
                "1 tbsp sriracha",
                "1/2 tbsp maple syrup",
                "1 tsp sesame oil",
                "Everything bagel seasoning or sesame seeds, to top",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Instructions\n\nBrussel Sprout Time!\n\nPreheat oven to 350 degrees.\nWhisk the sauce (coconut aminos, sriracha, maple syrup & sesame oil) together in a large bowl.\nToss in brussel sprouts and coat mixture evenly over the brussels.\nRoast for 30 minutes.\nTurn oven to broil for 2-3 minutes to crisp (watch carefully to not burn.)\nTop with everything or sesame seeds.",
            self.harvester_class.instructions(),
        )
