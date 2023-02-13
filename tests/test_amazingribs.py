from recipe_scrapers.amazingribs import AmazingRibs
from tests import ScraperTest


class TestAmazingRibsScraper(ScraperTest):

    scraper_class = AmazingRibs

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
        self.assertEqual(self.harvester_class.author(), "Meathead")

    def test_total_time(self):
        self.assertEqual(165, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                {
                    "name": "whole black peppercorns",
                    "quantity": 2.0,
                    "unit": "teaspoon",
                },
                {
                    "name": "fresh ground black pepper",
                    "quantity": 2.0,
                    "unit": "teaspoon",
                },
                {
                    "name": "mild American paprika",
                    "quantity": 1.0,
                    "unit": "tablespoon",
                },
                {"name": "garlic powder", "quantity": 2.0, "unit": "teaspoon"},
                {
                    "name": "Morton Coarse Kosher Salt",
                    "quantity": 2.0,
                    "unit": "teaspoon",
                },
                {"name": "rubbed sage", "quantity": 2.0, "unit": "teaspoon"},
                {
                    "name": "cayenne, chipotle, or other hot chile powder or flakes",
                    "quantity": 2.0,
                    "unit": "teaspoon",
                },
                {
                    "name": "medium green jalapeño",
                    "quantity": 1.0,
                    "unit": "dimensionless",
                },
                {"name": "small onion", "quantity": 0.5, "unit": "dimensionless"},
                {"name": "garlic cloves", "quantity": 3.0, "unit": "dimensionless"},
                {"name": "ground pork butt", "quantity": 20.0, "unit": "ounce"},
                {"name": "ground beef chuck", "quantity": 12.0, "unit": "ounce"},
                {
                    "name": "very cold water",
                    "quantity": 0.3333333333333333,
                    "unit": "cup",
                },
                {"name": "pork sausage casings", "quantity": 4.0, "unit": "foot"},
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
