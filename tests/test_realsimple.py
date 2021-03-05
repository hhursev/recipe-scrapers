from recipe_scrapers.realsimple import RealSimple
from tests import ScraperTest


class TestRealSimpleScraper(ScraperTest):

    scraper_class = RealSimple

    def test_host(self):
        self.assertEqual("realsimple.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.realsimple.com/food-recipes/browse-all-recipes/vanilla-cheesecake",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Vanilla Cheesecake")

    def test_total_time(self):
        self.assertEqual(540, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("9 item(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "3 8-ounce packages cream cheese, at room temperature",
                "4 eggs",
                "1 1/4 cups sugar",
                "2 teaspoons pure vanilla extract",
                "1 prebaked Ginger Graham Cracker Crust",
                "1 cup sour cream",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Make the Ginger Graham Cracker Crust.\nPreheat oven to 325° F.\nIn a large mixing bowl, beat the cream cheese until smooth, about 1 minute. Beat in the eggs one at a time. Add 1 cup of the sugar and 1 teaspoon of the vanilla and mix until well combined.\nPour the batter into the crust and bake until set, 45 to 50 minutes.\nIn a small bowl, whisk together the sour cream and the remaining sugar and vanilla. Pour the mixture over the cheesecake, spreading it to the edge. Bake 5 minutes.\nCool and refrigerate overnight before serving.",
            self.harvester_class.instructions(),
        )
