from recipe_scrapers.amazingribs import AmazingRibs
from tests import ScraperTest


class TestAmazingRibsScraper(ScraperTest):

    scraper_class = AmazingRibs
    test_file_name = "amazingribs_1"

    def test_host(self):
        self.assertEqual("amazingribs.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://amazingribs.com/tested-recipes/sausage-recipes/texas-hot-guts-smoked-sausage/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Texas Hot Guts Recipe", self.harvester_class.title())

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Meathead, BBQ Hall of Famer")

    def test_total_time(self):
        self.assertEqual(165, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 teaspoons whole black peppercorns",
                "2 teaspoons fresh ground black pepper",
                "1 tablespoon mild American paprika",
                "2 teaspoons garlic powder",
                "2 teaspoons Morton Coarse Kosher Salt",
                "2 teaspoons rubbed sage",
                "2 teaspoons cayenne, chipotle, or other hot chile powder or flakes",
                "1 medium green jalapeño",
                "½ small onion",
                "3 garlic cloves",
                "20 ounces ground pork butt",
                "12 ounces ground beef chuck",
                "⅓ cup very cold water",
                "4 feet pork sausage casings",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            [
                "Prep. Put the whole black peppercorns into a plastic bag and smash the heck outta them with a small frying pan until you have chunks of cracked peppercorns. Mix them with the rest of the black pepper, paprika, garlic powder, salt, sage, and chile powder in a small bowl. Remove the seeds and stems from the jalapeño and mince it into tiny bits. Peel the onion and garlic and mince them too. Now, go to our article on the Science of Making Sausage and follow steps (1) through (16).",
                "Smoke. Set up your grill or smoker and maintain a steady 225°F (107.2°C). Smoke the sausages at 225°F (107.2°C) until they hit 160°F (71.1°C) internal temperature, about 1 to 2 hours. As long as they hit that internal temp, you can experiment with the time to get your preferred level of smoke on the sausage.",
                "Serve. You can serve Hot Guts nekkid on a plate with some saltine crackers and hot sauce (traditional Texas style) or with some potatoes and a salad, or on a bun, or incorporate them into a dish like German Potato Salad or Choucroute Garnie, the classic Alsatian hot dish of sauerkraut, potatoes, various charcuterie, and mustard.",
            ],
            self.harvester_class.instructions_list(),
        )
