# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.bluejeanchef import BlueJeanChef
from tests import ScraperTest


class TestBlueJeanChefScraper(ScraperTest):

    scraper_class = BlueJeanChef
    test_file_name = "bluejeanchef_2"

    def test_host(self):
        self.assertEqual("bluejeanchef.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://bluejeanchef.com/recipes/no-bake-layered-cheesecake/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Meredith", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("No Bake Layered Cheesecake", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Desserts/Sweets", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(510, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://bluejeanchef.com/uploads/2023/07/No-Bake-Cheesecake-1280-9439.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1¾ cups Graham cracker crumbs",
            "½ cup melted unsalted butter",
            "2 tablespoons granulated sugar",
            "24 ounces cream cheese",
            "1½ cups powdered sugar (divided)",
            "⅓ cup sour cream",
            "2 teaspoons pure vanilla extract",
            "Juice of 1 lemon",
            "1¼ cups heavy whipping cream",
            "1 cup fresh raspberries (puréed)",
            "1 cup fresh blueberries (puréed)",
            "Whipped cream and fresh berries for garnish",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1¾ cups Graham cracker crumbs",
                        "½ cup melted unsalted butter",
                        "2 tablespoons granulated sugar",
                    ],
                    purpose="Crust:",
                ),
                IngredientGroup(
                    ingredients=[
                        "24 ounces cream cheese",
                        "1½ cups powdered sugar (divided)",
                        "⅓ cup sour cream",
                        "2 teaspoons pure vanilla extract",
                        "Juice of 1 lemon",
                        "1¼ cups heavy whipping cream",
                        "1 cup fresh raspberries (puréed)",
                        "1 cup fresh blueberries (puréed)",
                        "Whipped cream and fresh berries for garnish",
                    ],
                    purpose="Filling:",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = [
            "To make the crust, combine the Graham cracker crumbs, melted butter and sugar in a bowl. Line the bottom of a 9-inch springform pan with parchment paper. Press the Graham cracker crumb mixture firmly on the bottom of the pan and place it in the refrigerator.",
            "Using an electric mixer, beat the cream cheese and ¾ cup of the powdered sugar together until smooth. Add the sour cream, vanilla extract and lemon juice, and mix until smooth.",
            "In a separate bowl, whip the heavy cream using an electric mixer on high speed until it starts to thicken. Then add the remaining ¾ cup powdered sugar and continue to whip the cream into stiff peaks. Fold the whipped cream into the cream cheese mixture until well combined. This is your plain cheesecake base.",
            "In another bowl, combine 2 cups of the cheesecake base with the puréed blueberries. In yet another separate bowl, combine 2 cups of the cream cheese mixture with the puréed raspberries. Now you have three bowls of flavored cheesecake batter.",
            "Spread the blueberry batter into the bottom of the springform pan on top of the crust. Use an off-set spatula to spread it out evenly in the pan. Gently spoon the plain batter over the blueberry layer and spread it out evenly. Then spoon the raspberry batter on top of the plain layer and spread it out evenly.",
            "Cover or wrap the pan with plastic wrap and chill for at least 8 hours to overnight.",
            "When ready to serve, run a knife around the edge of the pan and unmold the cheesecake. Transfer to a serving platter, removing the parchment paper on the bottom. Garnish with whipped cream and fresh berries. Cut into wedges to serve, dipping your knife in warm water and wiping clean in between cutting each slice. Serve chilled.",
        ]
        self.assertEqual(
            "\n".join(expected_instructions), self.harvester_class.instructions()
        )

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "No oven needed for this no bake layered cheesecake! Layer blueberry, plain and raspberry cheesecake batters on top of each other and chill well for a delightfully refreshing summer dessert.",
            self.harvester_class.description(),
        )
