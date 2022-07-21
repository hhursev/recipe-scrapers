from recipe_scrapers.woolworths import Woolworths
from tests import ScraperTest


class TestWoolworthsScraper(ScraperTest):

    scraper_class = Woolworths

    def test_host(self):
        self.assertEqual("woolworths.com.au", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Fresh Ideas", self.harvester_class.author())

    def test_category(self):
        self.assertEqual("Salads", self.harvester_class.category())

    def test_title(self):
        self.assertEqual(
            "Asparagus Salad With Lemon Vinaigrette Recipe | Woolworths",
            self.harvester_class.title(),
        )

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_prep_time(self):
        self.assertEqual(10, self.harvester_class.prep_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://foodhub.scene7.com/is/image/woolworthsltdprod/2010-asparagus-salad-with-lemon-vinaigrette:Square-1300x1300",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 bunches asparagus, trimmed, halved diagonally",
                "100g snow peas, trimmed, halved diagonally",
                "2 gem lettuce, trimmed, leaves separated",
                "2 radishes, trimmed, thinly sliced into rounds",
                "80g feta, crumbled",
                "0.5 cup small basil leaves",
                "2 tbs natural sliced almonds, toasted",
                "1 tbs white wine vinegar",
                "2 tsp Dijon mustard",
                "0.25 tsp sea salt flakes",
                "0.25 tsp caster sugar",
                "0.25 cup extra virgin olive oil",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Bring a medium saucepan of water to the boil over high heat. Cook asparagus and snow peas for 2 minutes or until just tender. Drain. Refresh under cold water. Drain.
Meanwhile, to make the vinaigrette, whisk all the ingredients together in a small jug until combined, then season.
Arrange lettuce, asparagus, snow peas and radish on a platter. Scatter over feta, drizzle with dressing, top with basil and almonds, then serve.""",
            self.harvester_class.instructions(),
        )

    def test_cuisine(self):
        self.assertEqual("French", self.harvester_class.cuisine())

    def test_cook_time(self):
        self.assertEqual(5, self.harvester_class.cook_time())

    def test_nutrients(self):
        self.assertEqual({}, self.harvester_class.nutrients())

    def test_language(self):
        self.assertEqual("en-AU", self.harvester_class.language())

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())

    def test_site_name(self):
        self.assertEqual(
            "Woolworths | Fresh Ideas For You", self.harvester_class.site_name()
        )
