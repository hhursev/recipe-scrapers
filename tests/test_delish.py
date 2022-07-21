from recipe_scrapers.delish import Delish
from tests import ScraperTest


class TestDelishScraper(ScraperTest):

    scraper_class = Delish

    def test_host(self):
        self.assertEqual(self.harvester_class.host(), "delish.com")

    def test_canonical_url(self):
        self.assertEqual(
            self.harvester_class.canonical_url(),
            "https://www.delish.com/cooking/recipe-ideas/recipes/a56732/pumpkin-cheesecake-roll-recipe/",
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Pumpkin Cheesecake Roll")

    def test_total_time(self):
        self.assertEqual(self.harvester_class.total_time(), 60)

    def test_yields(self):
        self.assertEqual(self.harvester_class.yields(), "8 servings")

    def test_image(self):
        self.assertEqual(
            self.harvester_class.image(),
            "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-190814-pumpkin-roll-0029-portrait-pf-1567187757.jpg?crop=1.00xw:0.667xh;0,0.0545xh&resize=768:*",
        )

    def test_ingredients(self):
        self.assertEqual(
            self.harvester_class.ingredients(),
            [
                "Cooking spray",
                "1 c. granulated sugar",
                "3/4 c. all-purpose flour",
                "1/2 tsp. kosher salt",
                "1 tsp. baking soda",
                "1/2 tsp. pumpkin spice",
                "3 large eggs",
                "2/3 c. pumpkin puree",
                "Powdered sugar, for rolling",
                "12 oz. cream cheese, softened",
                "1 tbsp. melted butter",
                "1 tsp. pure vanilla extract",
                "1 1/4 c. powdered sugar",
                "1/2 tsp. kosher salt",
            ],
        )

    def test_instructions(self):
        self.assertEqual(
            self.harvester_class.instructions(),
            "Preheat oven to 350°. Line a 15” x 10” jelly roll pan with parchment and grease with cooking spray. In a large bowl, combine sugar, flour, salt, baking soda, pumpkin spice, eggs, and pumpkin puree until just combined. Spread into prepared pan and bake until a toothpick inserted in center of cake comes out clean, 15 minutes.\nMeanwhile, lay out a large kitchen towel on your counter (try to use one with little to no texture) and dust with powdered sugar. When cake is done baking, flip onto kitchen towel and gently peel off parchment paper.\nStarting at a short end, gently but tightly roll cake into a log. Let cool completely.\nMeanwhile, make filling: In a large bowl, combine cream cheese, melted butter, vanilla, powdered sugar, and salt. Using a hand mixer, whip until smooth.\nWhen cake is cooled, gently unroll (it’s ok if it remains slightly curled) and spread with cream cheese filling. Roll back up and dust with more powdered sugar. Slice and serve.",
        )


class TestDelishRogueOlScraper(ScraperTest):

    scraper_class = Delish
    test_file_name = "delish_rogue_ol"

    def test_host(self):
        self.assertEqual(self.harvester_class.host(), "delish.com")

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.delish.com/cooking/recipe-ideas/a46303/baileys-cheesecake-recipe/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Baileys Cheesecake")

    def test_total_time(self):
        self.assertEqual(self.harvester_class.total_time(), 25)

    def test_yields(self):
        self.assertEqual(self.harvester_class.yields(), "10 servings")

    def test_ingredients(self):
        self.assertEqual(
            self.harvester_class.ingredients(),
            [
                "26 Oreo cookies",
                "4 tbsp. butter, melted, plus more for pan",
                "Pinch of kosher salt",
                "4 (8-oz.) bars cream cheese, softened",
                "1 1/2 c. granulated sugar",
                "1/4 c. cornstarch",
                "4 large eggs",
                "2/3 c. Baileys Irish Cream",
                "1 tsp. pure vanilla extract",
                "2/3 c. heavy cream",
                "2 c. semisweet chocolate chips",
            ],
        )

    def test_instructions(self):
        self.assertTrue(self.harvester_class.instructions())

        self.assertEqual(
            self.harvester_class.instructions(),
            'Preheat oven to 325º and butter an 8" or 9" springform pan.\nMake crust: In a food processor, blend Oreos with melted butter and salt. Pat into a springform pan and set aside while you make filling.\nMake cheesecake: In a large bowl using a hand mixer, beat cream cheese and sugar until completely smooth and fluffy. Add cornstarch, then add eggs. Add Baileys and vanilla.\nPour batter into crust and place on a large baking sheet.\nBake until center of cheesecake is only slightly jiggly, 1 hour 20 minutes to 1 hour 30 minutes. Let cheesecake cool in oven, 1 hour, then refrigerate until completely cool, 4 hours or up to overnight. (If you\'d like to use a water bath, tightly wrap outside of springform pan with two layers of aluminum foil. Transfer to a deep roasting pan and pour in enough boiling water to reach halfway up the cheesecake pan. Bake as directed.)\nWhen ready to serve, make ganache: In a small saucepan over low heat, heat heavy cream. Place chocolate in a heatproof bowl and pour hot cream on top. Let sit 3 minutes, then stir until creamy, until no lumps remain. Refrigerate ganache until slightly thick, 15 minutes, and spread all over cheesecake. Let set 10 minutes, then serve.',
        )
