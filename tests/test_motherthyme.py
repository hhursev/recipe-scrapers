from recipe_scrapers.motherthyme import MotherThyme
from tests import ScraperTest


class TestMotherThymeScraper(ScraperTest):

    scraper_class = MotherThyme

    def test_host(self):
        self.assertEqual("motherthyme.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "http://www.motherthyme.com/2014/01/cinnamon-roll-oatmeal.html",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Cinnamon Roll Oatmeal")

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 3/4 cup milk",
                "2 tablespoons brown sugar",
                "1 tablespoon sugar",
                "1/2 teaspoon vanilla extract",
                "1/4 teaspoon salt",
                "1 1/2 cups old-fashioned rolled oats",
                "Topping",
                "2 tablespoons butter melted",
                "3 tablespoons packed light brown sugar",
                "1 1/2 teaspoons cinnamon",
                "Glaze",
                "1 ounce cream cheese softened",
                "1 tablespoon milk",
                "1/8 teaspoon vanilla extract",
                "5 tablespoons confectioners' sugar",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Oatmeal\nIn a large saucepan add milk, sugars, vanilla and salt and bring to a boil over medium heat.\nStir in oats, return to a boil and continue to cook, stirring occasionally for 3-5 minutes until oatmeal begins to thicken.\nCover and remove from heat. Let sit for about 3 minutes.\nTopping\nIn a small bowl mix butter, brown sugar and cinnamon until combined.\nGlaze\nMicrowave cream cheese in a small bowl for about 10 seconds until just melted.\nStir in confectioners' sugar until combined.\nStir in milk and vanilla until creamy.\nNote: Add in a little more confectioners' sugar if glaze is too thin or a little more milk if glaze is too thick until desired consistency.\nAssemble\nPlace desired amount of oatmeal in serving bowl. Drizzle with some of the cinnamon sugar topping and then drizzle on top of that some of the cream cheese glaze.\nServe warm.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.91, self.harvester_class.ratings())
