from recipe_scrapers.thevintagemixer import TheVintageMixer
from tests import ScraperTest


class TestTheVintageMixerScraper(ScraperTest):

    scraper_class = TheVintageMixer

    def test_host(self):
        self.assertEqual("thevintagemixer.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.thevintagemixer.com/cherry-baby-birthday-cake-party/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Gluten Free and Sugar Free Cherry Baby Smash Cake",
        )

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_image(self):
        self.assertEqual(
            "https://d6h7vs5ykbiug.cloudfront.net/wp-content/uploads/2017/08/Cherry-Baby-Birthday-Party-2-1-150x150.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 tablespoons coconut flour, +1 teaspoon",
                "1/4 cup almond flour",
                "1/4 teaspoon baking powder",
                "1/6 teaspoon baking soda",
                "1/4 teaspoon salt",
                "1 ripe banana, about 1/2 cup",
                "2 tablespoons coconut oil, room temp",
                "2 tablespoons almond butter, room temp",
                "1 large egg, beaten",
                "1 tablespoon pure maple syrup",
                "1/2 teaspoon pure vanilla extract",
                "1/2 cup cherries, pitted and chopped",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat the oven to 375 and grease two small ramekins* with coconut oil.\nIn a small mixing bowl combine the dry ingredients: coconut flour, almond flour, baking powder, baking soda, and salt.\nIn a separate, medium-sized, bowl mash the banana then add in the coconut oil, almond butter, maple syrup and vanilla. Stir in the egg.\nCombine the dry ingredients to the wet and mix only until combined and smooth.\nToss the chopped cherries with a teaspoon or so of coconut flour. Stir these into the batter. Spoon batter out into ramekins and bake at 375 for 20-25 minutes.\nLet cool 5 minutes in the pan then remove to a wire rack to cool completely. Wrap in plastic and freeze.\nAbout 1 hour before serving, remove cakes from freezer. If the cakes are puffed up at the top slice off the top to even them out and make it flat to layer the cakes.\nDap a small amount of frosting under the first cake on the plate so it won't wiggle as you ice it then add a spoonful on top of the cake to place the second layer on top. Frost gently around the sides of the cake and on top. Top the cake with a few fresh cherries.",
            self.harvester_class.instructions(),
        )
