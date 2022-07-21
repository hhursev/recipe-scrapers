from recipe_scrapers.ethanchlebowski import EthanChlebowski
from tests import ScraperTest


class TestEthanChlebowskiScraper(ScraperTest):

    scraper_class = EthanChlebowski

    def test_host(self):
        self.assertEqual("ethanchlebowski.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Ethan Chlebowski", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Huevos Rancheros", self.harvester_class.title())

    def test_category(self):
        self.assertEqual(None, self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(13, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("1 serving", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://i.imgur.com/hzIuWpU.jpg", self.harvester_class.image()
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 small corn tortillas",
                "2 eggs",
                "Salsa Ranchera (recipe below)",
                "Neutral oil for toasting tortillas and cooking eggs",
                "Chopped Cilantro",
                "Cotija cheeese or Queso fresco",
                "Pickled onions",
                "Seasoned Pinto Beans (recipe below)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        test_instructions = "Heat the salsa ranchera in the microwave or a pan until warmed through.\nSet a pan over medium-high heat and add a little bit of oil. Once hot, lightly fry the corn tortillas similar to enchiladas where they are still malleable or until crisp. Drain on a paper towel. Low-calorie option - Spritz with baking spray and toast tortillas under the broiler.\nIn the same pan and oil, fry the eggs sunny side up basting them with oil as needed. Low-calorie option - Poach the eggs in water.\nPlace the cooked eggs over the tortillas and spoon the warmed sauce over the whites. Top with some crumbling cheese and cilantro. Serve with seasoned pintos beans if you would like! Slice the yolk open and mix with the sauce to enjoy."

        self.assertEqual(test_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Huevos rancheros are one of the simplest and most common breakfasts in Mexico, all you have to do is make the salsa ranchera, pair it with some fried tortillas and eggs and it's ready.",
            self.harvester_class.description(),
        )
