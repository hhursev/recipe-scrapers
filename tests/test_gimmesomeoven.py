from recipe_scrapers.gimmesomeoven import GimmeSomeOven
from tests import ScraperTest


class TestGimmeSomeOvenScraper(ScraperTest):

    scraper_class = GimmeSomeOven

    def test_host(self):
        self.assertEqual("gimmesomeoven.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.gimmesomeoven.com/sangria/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Sangria")

    def test_total_time(self):
        self.assertEqual(10, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.gimmesomeoven.com/wp-content/uploads/2019/06/Authentic-Spanish-Sangria-Recipe-3-1-225x225.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 bottles Spanish red wine (Rioja wine is most popular)",
                "1/2 cup brandy",
                "2 oranges, one juiced and one diced",
                "1 green apple, diced",
                "1 lemon, diced",
                "1 cinnamon stick",
                "optional sweetener: simple syrup* or maple syrup",
                "optional bubbles: lemon-lime soda, ginger ale or sparkling water",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Add the wine, brandy, orange juice, diced orange, diced apple, diced lemon and cinnamon stick to a large pitcher. Stir to combine. Taste and add in a few tablespoons of sweetener, if desired.\nCover and refrigerate for at least 30 minutes or up to 4 hours.\nServe the sangria over ice, topping off each glass with a splash of bubbly soda (or sparkling water) if desired.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
