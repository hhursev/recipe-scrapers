from recipe_scrapers.wikicookbook import WikiCookbook
from tests import ScraperTest


class TestWikiCookbookScraper(ScraperTest):

    scraper_class = WikiCookbook

    def test_host(self):
        self.assertEqual("en.wikibooks.org", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://en.wikibooks.org/wiki/Cookbook:Pumpkin_Pie",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Pumpkin Pie")

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Pumpkin_Pie.jpg/300px-Pumpkin_Pie.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 cups (480ml) milk, scalded",
                "2 cups (450g) pumpkin, cooked and strained (or plain canned pumpkin). Use the smaller 'Sugar Pumpkin' instead of the big 'Jack O Lantern' pumpkin. The smaller 'Sugar Pumpkin' has a firm and smooth texture while the larger 'Jack O Lantern' pumpkin has more stringy or fibrous texture and more watery for a flesh.",
                "1 cup (240ml) maple syrup",
                "1/8 cup (30g) sugar",
                "1 Tbsp. flour",
                "½ tsp. salt",
                "1 tsp. ginger",
                "1 tsp. cinnamon",
                "1/4 tsp. nutmeg (optional)",
                "2 large eggs, beaten",
                "1 unbaked nine-inch pie shell",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat oven to 350 °F (180 °C).\nBlend all ingredients, except the pie shell, together.\nPour into the unbaked pie shell.\nBake at 350 °F (180 °C) for 45 minutes.\nLet cool and serve.",
            self.harvester_class.instructions(),
        )
