from recipe_scrapers.indianhealthyrecipes import IndianHealthyRecipes
from tests import ScraperTest


class TestIndianHealthyRecipesScraper(ScraperTest):

    scraper_class = IndianHealthyRecipes

    def test_host(self):
        self.assertEqual("indianhealthyrecipes.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Swasthi", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Banana cake", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(50, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("16 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.indianhealthyrecipes.com/wp-content/uploads/2015/12/banana-cake-2.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 cups whole wheat flour (or all-purpose (refer notes))",
                "2 ½ teaspoons baking powder",
                "½ teaspoon salt ((or ⅓ teaspoon table salt))",
                "1 cup fine sugar ((prefer organic))",
                "100 grams unsalted butter ((soft & cold) (around ½ cup))",
                "2 eggs",
                "2 teaspoons vanilla extract",
                "½ cup milk (+ 2½ tablespoons)",
                "1 cup ripe banana (mashed)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Preparation\nBring all the ingredients to room temperature except butter before you begin to prepare the batter.\nButter has to be cold, yet soft and should hold its structure. To check press the block of cold butter with your finger, it should dent slightly yet hold its solid structure and should not be too soft.\nGrease a 8 by 8 inch cake tray and line with parchment paper. If you do not have a parchment paper, you may sprinkle flour all over the tray including the sides. Invert and dust off the excess in your kitchen sink.\nPreheat the oven to 170 C or 340 F for at least 15 minutes. If you have a fan forced oven then preheat to 160 C or 320 F.\nFluff up the flour in the jar/ pack with a fork. Then spoon it to the measuring cup and level it with a knife or a straight edged spoon. Sieve flour, baking powder and salt. Set aside.\nHow to make banana cake\nMake sure butter is soft but still cold before this step. Add butter and sugar to a mixing bowl. Using a whisk, beat together until light, pale & fluffy.\nPour vanilla extract and add 1 egg at a time and beat just until creamy.\nAdd the other egg and beat again just until creamy.\nNext add the sieved flour, salt and baking powder. Mix it gently.\nAdding milk in 2 batches, mix the flour on a medium speed until smooth. Do not over mix it.\nAdd banana puree and mix until just combined. Avoid over mixing.\nPour the batter to a lined cake tray and knock it against the counter a few times. Bake for 25 to 30 mins if using a 8 by 8 square pan. If using a different size pan, then the timing varies.\nA skewer/ tester inserted in the center of the cake comes out clean when the cake is done.\nPlace the cake pan on a wired rack and cool for 10 minutes. Then invert the banana cake on the wire rack.\nCool completely before slicing. Serve banana cake plain with milk or tea.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.86, self.harvester_class.ratings())
