# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.tidymom import TidyMom
from tests import ScraperTest


class TestTidyMomScraper(ScraperTest):
    scraper_class = TidyMom
    test_file_name = "tidymom_2"

    def test_host(self):
        self.assertEqual("tidymom.net", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://tidymom.net/red-velvet-rose-birthday-cake/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("TidyMom", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Red Velvet Cake With Cinnamon Buttercream", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Cake Recipes", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(205, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("9 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://tidymom.net/blog/wp-content/uploads/2023/01/red-velvet-cake-pic-720x720.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 cups all-purpose unbleached flour",
                "1/2 cup natural cocoa powder",
                "2 teaspoons baking powder",
                "1/2 teaspoon baking soda",
                "4 Tablespoons powdered ButterMilk",
                "1 teaspoon salt",
                "1 cup water",
                "1 tablespoon vanilla extract",
                "4 tablespoons (2 ounces) liquid red food coloring (or 2-3 teaspoons if using gel color)",
                "1 cup unsalted butter; can be cold from the refrigerator",
                "1 1/2 cups sugar",
                "4 large eggs, room temp",
                "1 cup butter (softened)",
                "1 cup vegetable shortening",
                "1 pinch of salt",
                "1/4 teaspoons vanilla extract",
                "4 cups powdered sugar",
                "1-2 teaspoons ground cinnamon",
                "1/3 cup heavy whipping cream",
                "1 cup butter, at room temperature",
                "16 ounces cream cheese, at room temperature",
                "2 teasoons vanilla extract (clear vanilla will help keep frosting white)",
                "8 cups powdered sugar",
                "3-6 Tablespoons heavy whipping cream",
                "White gel food coloring (optional, but makes your frosting nice and white)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "2 cups all-purpose unbleached flour",
                        "1/2 cup natural cocoa powder",
                        "2 teaspoons baking powder",
                        "1/2 teaspoon baking soda",
                        "4 Tablespoons powdered ButterMilk",
                        "1 teaspoon salt",
                        "1 cup water",
                        "1 tablespoon vanilla extract",
                        "4 tablespoons (2 ounces) liquid red food coloring (or 2-3 teaspoons if using gel color)",
                        "1 cup unsalted butter; can be cold from the refrigerator",
                        "1 1/2 cups sugar",
                        "4 large eggs, room temp",
                    ],
                    purpose="Red Velvet Cake",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 cup butter (softened)",
                        "1 cup vegetable shortening",
                        "1 pinch of salt",
                        "1/4 teaspoons vanilla extract",
                        "4 cups powdered sugar",
                        "1-2 teaspoons ground cinnamon",
                        "1/3 cup heavy whipping cream",
                    ],
                    purpose="Cinnamon Butter Cream",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 cup butter, at room temperature",
                        "16 ounces cream cheese, at room temperature",
                        "2 teasoons vanilla extract (clear vanilla will help keep frosting white)",
                        "8 cups powdered sugar",
                        "3-6 Tablespoons heavy whipping cream",
                        "White gel food coloring (optional, but makes your frosting nice and white)",
                    ],
                    purpose="Vanilla Cream Cheese Frosting",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = (
            "Preheat to 350° F\n"
            "Generously grease two, 9- x 2-inch pans with non-stick spray or shortening.\n"
            "In a medium-sized bowl, after measuring, sift together the flour, cocoa powder, baking powder, baking soda, powdered buttermilk, and salt. Stir together with a spoon. Set aside.\n"
            "Mix the water with the food coloring and vanilla extract. Set aside.\n"
            "Using a stand mixer with a paddle attachment, beat the butter on low speed until soft. (If the butter is cold, it will warm quickly from the beaters - taking about 60 seconds).\n"
            "Slowly add sugar in a steady stream at the side of the bowl. Increase speed to medium and beat for 2 minutes until light yellow and fluffy. Stop the mixer and scrape the side and bottom of the bowl with a large rubber spatula.\n"
            "With the mixer on low, add the eggs one at a time and beat for 20 seconds after each addition.\n"
            "Increase the mixer speed to medium and beat the mixture for 2 minutes. be sure to use a kitchen timer to help you keep track of the time. The mixture will become fluffy and aerated.\n"
            "Add the flour mixture in 3 equal portions, alternating with the water in 2 equal portions, beginning and ending with the flour. (If the water is cold, the batter will curdle slightly. It's ok. It will come together when you add the flour.) Mix on low and work quickly so you don't over-mix.\n"
            "After completing the last addition of flour, stop the mixer, and scrape the side and bottom of the bowl with a large rubber spatula.\n"
            "Then, let the mixer run for 30 seconds on LOW. The batter will be thick and fluffy. STOP the mixer. Do NOT overmix.\n"
            "With a large rubber spatula, give the batter ONE or TWO quick folds to incorporate any stray flour or liquid left at the sides and bottom of the bowl. do not continue mixing!\n"
            "Divide the batter equally into the prepared pans and lightly smooth their tops. The pans should be about 1/2-full.(I use my kitchen scale to be sure both pans are equal)\n"
            "Bake the cake layers for 20 to 30 minutes or until the top feels firm and gives slightly when touched. (inserted a toothpick in the middle should have a few moist crumbs attached, but not batter.)\n"
            "Loosen the sides with a small metal spatula or sharp knife. Invert onto a cake rack and place upright to cool completely until they are no longer warm. Then, wrap the cakes up tight with plastic wrap and put them in the fridge for at least 2-3 hours or overnight before frosting.\n"
            "In a mixing bowl, blend butter and shortening until smooth. Add a pinch of salt, vanilla, and cinnamon. Continue mixing until well blended. Gradually add powdered sugar 1 cup at a time, beating well after each addition. Eventually, you will have a very thick gooey mixture. On the highest speed of your mixer, stream in the heavy whipping cream- pour nice and slow.\n"
            "Continue beating on high speed until the frosting is fluffy\n"
            "Place butter in a large mixing bowl and blend slightly. Add cream cheese and blend until combined, about 30 seconds.\n"
            "Add vanilla and sugar and blend on low until combined. Increase to medium speed and beat until it begins to get fluffy.\n"
            "Slowly add the cream a little at a time until desired consistency is met. (you want it thick enough to hold its shape if you are going to pipe on roses)I added some bright white gel coloring at this point to make my frosting nice and white.\n"
            "Beat until fluffy, about 1 minute.\n"
            "Remove cakes from the fridge.\n"
            "Using a long serrated knife, slice both cold cake layers in half horizontally, yielding 4 cake layers (you can leave your cake as 2 thicker layers with one layer of filling if you'd prefer).\n"
            "Top each cake layer with about 1 cup of cinnamon buttercream.\n"
            "Frost the outside of the cake with Vanilla Cream Cheese Frosting.\n"
            "You can go to youtube to follow a rose cake tutorial.\n"
            "Enjoy!"
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "This rose cake is sure to make any birthday or special occasion spectacular. The red velvet cake made from scratch is soft, moist and tender, with the perfect red velvet flavor. Inside you will find fluffy cinnamon buttercream between the layers and topped with a delicious cream cheese frosting. A cake they will never forget!",
            self.harvester_class.description(),
        )
