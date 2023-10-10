from recipe_scrapers.delish import Delish
from tests import ScraperTest


class TestDelishScraper(ScraperTest):

    scraper_class = Delish
    test_file_name = "delish_1"

    def test_host(self):
        self.assertEqual(self.harvester_class.host(), "delish.com")

    def test_canonical_url(self):
        self.assertEqual(
            self.harvester_class.canonical_url(),
            "https://www.delish.com/cooking/recipe-ideas/recipes/a56732/pumpkin-cheesecake-roll-recipe/",
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Pumpkin Cheesecake Roll")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Lena Abraham")

    def test_total_time(self):
        self.assertEqual(self.harvester_class.total_time(), 60)

    def test_yields(self):
        self.assertEqual(self.harvester_class.yields(), "8 servings")

    def test_image(self):
        self.assertEqual(
            self.harvester_class.image(),
            "https://hips.hearstapps.com/hmg-prod/images/pumpkin-cheesecake-roll-index-64f7952c6df54.jpg?crop=0.500xw:1.00xh;0.249xw,0&resize=1200:*",
        )

    def test_ingredients(self):
        self.assertEqual(
            self.harvester_class.ingredients(),
            [
                "Cooking spray",
                "3/4 c. all-purpose flour",
                "1/2 tsp. kosher salt",
                "1 tsp. baking soda",
                "1/2 tsp. pumpkin spice",
                "3 large eggs",
                "1 c. granulated sugar",
                "2/3 c. pumpkin puree",
                "Powdered sugar, for rolling",
                "12 oz. cream cheese, softened",
                "1 tbsp. butter, melted",
                "1/2 tsp. kosher salt",
                "1 tsp. pure vanilla extract",
                "1 1/4 c. powdered sugar",
            ],
        )

    def test_instructions(self):
        self.assertEqual(
            self.harvester_class.instructions(),
            "For the cake:\nPreheat oven to 350°. Line a 15” x 10” jelly roll pan with parchment and grease with cooking spray.\nIn a medium bowl, whisk together flour, salt, baking soda, and pumpkin spice. In a separate large bowl, whisk together eggs, sugar, and pumpkin puree by hand until smooth. Add dry ingredients to pumpkin mixture and whisk just until combine.\nSpread into prepared pan and bake until a toothpick inserted in center of cake comes out clean, 15 minutes.\nMeanwhile, lay out a large kitchen towel on your counter (try to use one with little to no texture) and dust with powdered sugar. When cake is done baking, flip onto kitchen towel and gently peel off parchment paper.\nStarting at a short end, gently but tightly roll cake into a log. Let cool completely.\nFor the filling:\nIn a large bowl, combine cream cheese, melted butter, and salt. Using a hand mixer, whisk until light and fluffy.\nAdd powdered sugar and vanilla and continue to mix until smooth.\nWhen cake is cooled, gently unroll (it’s ok if it remains slightly curled) and spread with cream cheese filling. Roll back up and dust with more powdered sugar. Slice and serve.",
        )
