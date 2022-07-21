from recipe_scrapers.melskitchencafe import MelsKitchenCafe
from tests import ScraperTest


class TestMelsKitchenCafeScraper(ScraperTest):

    scraper_class = MelsKitchenCafe

    def test_host(self):
        self.assertEqual("melskitchencafe.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.melskitchencafe.com/licorice-caramels/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Licorice Caramels")

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.melskitchencafe.com/wp-content/uploads/2013/12/licorice-caramels3-320x320.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1/2 cup (4 ounces) water",
                "2 cups (1 pound) sugar",
                "1 can (14 ounce) sweetened condensed milk",
                "1 cup (12 ounces) light corn syrup",
                "1 1/2 sticks butter",
                "2 teaspoons anise extract (see note)",
                "1/2 teaspoon black food coloring paste (optional; see note)",
                "1/4 teaspoon vanilla extract",
                "1/4 teaspoon salt",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Lightly butter an 8X8- or 9X9-inch pan and set aside.\nIn a heavy-bottomed 4-quart saucepan, combine the water, sugar, condensed milk, corn syrup, and butter. Bring the mixture to a boil over medium heat, stirring constantly with a heat-resistant rubber spatula. Clip a candy thermometer to the side of the pan, ensuring that the tip of the thermometer isn’t touching the bottom of the pan and is inserted at least 1-2 inches into the liquid (or according to your thermometer’s directions).\nContinue stirring gently while the mixture boils and cooks, until the caramels reach 242-244 degrees F. If the caramels seem to be scorching on the bottom of the pan, moderate the heat to a lower temperature. You can also test the caramels using a spoon and dropping a pea-sized amount of the hot caramel into cold water. If the cooled piece of caramel is firm but not hard, the caramel is properly cooked.\nRemove the pot from the heat and stir in the anise extract, food coloring, vanilla extract and salt. Pour the caramels into the prepared pan and allow to cool completely to room temperature, at least 2 hours.\nWhen cool, remove the sheet of caramels from the pan. Cut the caramels into pieces using a large knife or bench scraper. Wrap each caramel square in a bit of wax paper, twisting the ends to secure.",
            self.harvester_class.instructions(),
        )
