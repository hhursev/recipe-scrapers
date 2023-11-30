# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.williamssonoma import WilliamsSonoma
from tests import ScraperTest


class TestWilliamsSonomaScraper(ScraperTest):
    scraper_class = WilliamsSonoma
    test_file_name = "williamssonoma_2"

    def test_host(self):
        self.assertEqual("williams-sonoma.com", self.harvester_class.host())

    def canonical_url(self):
        self.assertEqual(
            "https://www.williams-sonoma.com/recipe/double-chocolate-layer-cake.html",
            self.harvester_class.host(),
        )

    def test_author(self):
        self.assertEqual("Williams Sonoma", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Double Chocolate Layer Cake", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(80, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://assets.wsimgs.com/wsimgs/ab/images/dp/recipe/202327/0003/img5l.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        ingredients = [
            "2 1/2 cups (12 1/2 oz./390 g) all-purpose flour",
            "2 cups (1 lb./500 g) sugar",
            "1 cup (3 oz./90 g) unsweetened cocoa powder",
            "1 1/2 tsp. baking powder",
            "1 1/2 tsp. baking soda",
            "1/2 tsp. ground cinnamon",
            "1 1/2 tsp. salt",
            "3 eggs",
            "1 1/2 cups (12 fl. oz./375 ml) buttermilk",
            "1 Tbs. vanilla extract",
            "1/2 cup (4 fl. oz./125 ml) vegetable oil",
            "1 cup (8 fl. oz./250 ml) boiling water",
            "1 tsp. espresso powder",
            "2 cups (12 oz./375 g) semisweet chocolate chips",
            "2/3 cup (5 fl. oz./160 ml) plus 2 Tbs. heavy cream",
            "Cocoa powder for dusting (optional)",
        ]
        self.assertEqual(ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "2 1/2 cups (12 1/2 oz./390 g) all-purpose flour",
                        "2 cups (1 lb./500 g) sugar",
                        "1 cup (3 oz./90 g) unsweetened cocoa powder",
                        "1 1/2 tsp. baking powder",
                        "1 1/2 tsp. baking soda",
                        "1/2 tsp. ground cinnamon",
                        "1 1/2 tsp. salt",
                        "3 eggs",
                        "1 1/2 cups (12 fl. oz./375 ml) buttermilk",
                        "1 Tbs. vanilla extract",
                        "1/2 cup (4 fl. oz./125 ml) vegetable oil",
                        "1 cup (8 fl. oz./250 ml) boiling water",
                        "1 tsp. espresso powder",
                    ],
                    purpose=None,
                ),
                IngredientGroup(
                    ingredients=[
                        "2 cups (12 oz./375 g) semisweet chocolate chips",
                        "2/3 cup (5 fl. oz./160 ml) plus 2 Tbs. heavy cream",
                        "Cocoa powder for dusting (optional)",
                    ],
                    purpose="For the frosting:",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = (
            "Preheat an oven to 350°F (180°C). Grease three 8-inch (20-cm) round cake pans. Line the bottom of each pan with a round of parchment paper and grease the parchment.\n"
            "In a mixing bowl, whisk together the flour, sugar, cocoa powder, baking powder, baking soda, cinnamon and salt. Set aside. In the bowl of a stand mixer fitted with the whisk attachment, combine the eggs, buttermilk, vanilla and vegetable oil. Beat on medium speed until thoroughly combined. Reduce the speed to low, slowly add the flour mixture and mix until combined, stopping the mixer and scraping down the sides of the bowl as necessary.\n"
            "In a small bowl, combine the boiling water and espresso powder and whisk until combined. With the mixer running on low speed, slowly add the espresso mixture to the batter. Stop the mixer and scrape down the sides of the bowl, then mix again until thoroughly combined, about 30 seconds.\n"
            "Divide the batter evenly among the prepared cake pans. Smooth the tops with an offset spatula and tap the pans on the countertop to evenly distribute the batter. Bake until the cakes begin pull away from the sides of the pan and a toothpick inserted into the center comes out clean, about 30 minutes. Transfer the pans to wire racks and let cool for 10 minutes, then turn the cakes out onto the racks and peel off the parchment paper. Let cool completely.\n"
            "Meanwhile, make the frosting: Place the chocolate chips in a large heatproof mixing bowl. In a small saucepan over medium heat, warm the 2/3 cup cream until simmering. Pour the hot cream over the chocolate chips and let stand for 5 minutes. Whisk the chocolate and cream until a smooth ganache forms. Let cool to room temperature. Transfer to the bowl of a stand mixer fitted with the whisk attachment and beat on high speed until the mixture begins to thicken. Add the remaining 2 Tbs. cream and continue to beat on high speed until stiff peaks form, 3 to 4 minutes.\n"
            "To assemble the cake, place 1 cake layer, top side up, on a cake stand or serving plate. Using an icing spatula, generously spread the cake layer with about a third of the frosting. Repeat the process with remaining cake layers, spreading the remaining frosting on the last layer. Lightly dust the top of the cake with cocoa powder before cutting into slices and serving. Serves 12.\n"
            "Williams-Sonoma Test Kitchen"
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_cuisine(self):
        self.assertEqual("AMERICAN", self.harvester_class.cuisine())
