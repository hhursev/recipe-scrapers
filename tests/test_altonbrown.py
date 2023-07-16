from recipe_scrapers.altonbrown import AltonBrown
from tests import ScraperTest


class TestAltonBrownScraper(ScraperTest):

    scraper_class = AltonBrown

    def test_host(self):
        self.assertEqual("altonbrown.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Sarah Chanin", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("A Far, Far Better Cake", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Sweets", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(210, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://altonbrown.com/wp-content/uploads/2020/08/A-Far-Far-Better-Cake_RecipeImage.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 cup (2 sticks) unsalted butter, at room temperature, plus extra for the pan",
                "1 cup all-purpose flour, plus extra for the pan",
                "1 cup cake flour",
                "1 tablespoon baking powder",
                "1 1/2 cups plus 3 tablespoons sugar",
                "1/4 teaspoon fine sea salt",
                "8 large egg yolks, at room temperature",
                "1 1/4 cups whole milk, at room temperature",
                "1 teaspoon vanilla extract",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Place an oven rack in the top third of the oven and crank the box to 350°F. Then prep two 9-inch round aluminum cake pans by rubbing on a thin layer of butter on the bottoms and sides, and then flour. Finally, line the bottoms of both with a round of parchment paper.\nSiftYou can use a sifter for this or a fine sieve. the flours together with the baking powder and set aside.\nLoad the paddle attachment onto your stand mixer and beat the butter on low speed just until smooth, about 1 minute. Follow with the sugar and salt, boosting the speed to medium. Continue to beat until the mixture is light and fluffy, about 4 minutes, stopping to scrape down the sides of the bowl after each minute or so.\nWith the mixer still on medium, add the egg yolks one at a time, fully incorporating one before adding the next. When all eight are in, kill the mixer and scrape the bowl. Return the speed to low and slowly addI like to use a paper plate to dose in the flour...great multitasker. half the flour mixture.\nWhen the first half of the flour mix is worked in, add half of the milk and all of the vanilla. Stop and scrape the bowl yet again then return to low and slowly add the remaining flour. Then scrape one more time, making sure there’s no dry flour hiding in the bottom of the bowl. Congratulations, you’ve conquered the creaming method.\nDivide the mixture between the two pans. I use a scale to ensure even distribution and that means about 660 grams per pan. Smooth the tops with a rubber spatula and tap the pans against the counter to remove any air pockets.\nBake until the cakes reach an internal temperature of between 207 and 210°F, which typically takes between 30 and 35 minutes. The cakes should be golden brown and a toothpick inserted into the center of the cakes should come out clean.\nRemove from oven and cool cakes on a wire rack for 15 minutes then de-pan onto the rack and cool to room temp before frosting.""",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.3, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            """Way back in 2003, I created a yellow cake that was dry, crumbly, and not nearly the cake the world deserves. After all these years I can finally say: we’re golden...cake that is. All we needed was more moisture and less starch, proof positive that small, balanced changes can radically improve or...disprove a cake.This recipe first appeared in Season 2 of Good Eats: Reloaded.""",
            self.harvester_class.description(),
        )
