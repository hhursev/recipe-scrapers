# mypy: allow-untyped-defs

from recipe_scrapers.onceuponachef import OnceUponAChef
from tests import ScraperTest


class TestOnceUponAChefScraper(ScraperTest):

    scraper_class = OnceUponAChef
    test_file_name = "onceuponachef_1"

    def test_host(self):
        self.assertEqual("onceuponachef.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("By Jenn Segal", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Pumpkin Bread", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Breads", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(90, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 items", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.onceuponachef.com/images/2009/09/Pumpkin-Bread-100.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 cups all-purpose flour, spooned into measuring cup and leveled-off",
                "½ teaspoon salt",
                "1 teaspoon baking soda",
                "½ teaspoon baking powder",
                "1 teaspoon ground cloves",
                "1 teaspoon ground cinnamon",
                "1 teaspoon ground nutmeg",
                "1½ sticks (¾ cup) unsalted butter, softened",
                "2 cups sugar",
                "2 large eggs",
                "1 (15-oz) can 100% pure pumpkin (I use Libby's)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Preheat the oven to 325°F and set an oven rack in the middle position. Generously grease two 8 x 4-inch loaf pans with butter and dust with flour (alternatively, use a baking spray with flour in it, such as Pam with Flour or Baker's Joy).\n"
            "In a medium bowl, combine the flour, salt, baking soda, baking powder, cloves, cinnamon, and nutmeg. Whisk until well combined; set aside.\n"
            "In a large bowl of an electric mixer, beat the butter and sugar on medium speed until just blended. Add the eggs one at a time, beating well after each addition. Continue beating until very light and fluffy, a few minutes. Beat in the pumpkin. The mixture might look grainy and curdled at this point -- that's okay.\n"
            "Add the flour mixture and mix on low speed until combined.\n"
            "Turn the batter into the prepared pans, dividing evenly, and bake for 65 – 75 minutes, or until a cake tester inserted into the center comes out clean. Let the loaves cool in the pans for about 10 minutes, then turn out onto a wire rack to cool completely.\n"
            "Fresh out of the oven, the loaves have a deliciously crisp crust. If they last beyond a day, you can toast individual slices to get the same fresh-baked effect.\n"
            "Freezer-Friendly Instructions: The bread can be frozen for up to 3 months. After it is completely cooled, wrap it securely in aluminum foil, freezer wrap or place in a freezer bag. Thaw overnight in the refrigerator before serving.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Kids love it, grown-ups love it...this pumpkin bread is hard to beat!",
            self.harvester_class.description(),
        )
