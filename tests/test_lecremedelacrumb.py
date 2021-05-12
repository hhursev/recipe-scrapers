from recipe_scrapers.lecremedelacrumb import LeCremeDeLaCrumb
from tests import ScraperTest


class TestLeCremeDeLaCrumbScraper(ScraperTest):

    scraper_class = LeCremeDeLaCrumb

    def test_host(self):
        self.assertEqual("lecremedelacrumb.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.lecremedelacrumb.com/instant-pot-shredded-chicken-tacos/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Instant Pot Shredded Chicken Tacos"
        )

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.skipTest(
            reason="Re-enable when harvester produces expected 'yields' output"
        )
        self.assertEqual("None", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.lecremedelacrumb.com/wp-content/uploads/2019/01/instant-pot-shredded-chicken-tacos-5.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "3-4 medium to large boneless skinless chicken breasts",
                "1 cup chicken broth or water",
                "1 teaspoon salt",
                "1 teaspoon ground cumin",
                "1 teaspoon chili powder",
                "1 teaspoon garlic powder",
                "1 15-ounce can fire roasted tomatoes",
                "corn or flour taco-size tortillas",
                "avocado, tomatoes, cheese, cilantro, sour cream (for serving)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "In your instant pot/pressure cooker combine chicken, broth or water, cumin, chili powder, garlic powder, and fire roasted tomatoes (with liquid).\nCover and set to PRESSURE COOK or MANUAL for 20 minutes. (30 minutes if using frozen chicken breasts)\nDo a quick release (turn vent knob to the VENT position and allow to de-pressurize until the float valve drops down) then uncover and shred chicken with two forks.\nServe chicken in tortillas topped with cheese, tomatoes, avocado, cilantro, or any other favorite toppings.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.64, self.harvester_class.ratings())
