from recipe_scrapers.amazingribs import AmazingRibs
from tests import ScraperTest


class TestAmazingRibsScraper(ScraperTest):

    scraper_class = AmazingRibs

    def test_host(self):
        self.assertEqual("amazingribs.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://amazingribs.com/tested-recipes/sausage-recipes/texas-hot-guts-smoked-sausage",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Texas Hot Guts Recipe", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(165, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 teaspoons whole black peppercorns",
                "2 teaspoons fresh ground black pepper",
                "1 tablespoon mild American paprika",
                "2 teaspoons garlic powder",
                "2 teaspoons Morton’s kosher salt",
                "2 teaspoons rubbed sage",
                "2 teaspoons cayenne, chipotle, or other hot chile powder or flakes",
                "1 medium green jalapeno",
                "1/2 small onion",
                "3 garlic cloves",
                "20 ounces ground pork butt",
                "12 ounces ground beef chuck",
                "1/3 cup very cold water",
                "4’ pork sausage casings",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Method\n\n1) Prep. Put the whole black peppercorns into a plastic bag and smash the heck outta them with a small frying pan until you have chunks of cracked peppercorns. Mix them with the rest of the black pepper, paprika, garlic powder, salt, sage, and chile powder in a small bowl. Remove the seeds and stems from the jalapeno and mince it into tiny bits. Peel the onion and garlic and mince them too. Now, go to our article on the Science of Making Sausage and follow steps (1) through (16).\n\n17) Smoke. Set up your grill or smoker and maintain a steady 225ºF. Smoke the sausages at 225°F until they hit 160°F internal temperature, about 1 to 2 hours. As long as they hit that internal temp, you can experiment with the time to get your preferred level of smoke on the sausage.\n\n18) Serve. You can serve Hot Guts nekkid on a plate with some saltine crackers and hot sauce (traditional Texas style) or with some potatoes and a salad, or on a bun, or incorporate them into a dish like German Potato Salad or Choucroute Garnie, the classic Alsatian hot dish of sauerkraut, potatoes, various charcuterie, and mustard.",
            self.harvester_class.instructions(),
        )
