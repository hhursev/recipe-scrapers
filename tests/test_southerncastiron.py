from recipe_scrapers.southerncastiron import SouthernCastIron
from tests import ScraperTest


class TestSouthernCastIronScraper(ScraperTest):

    scraper_class = SouthernCastIron

    def test_host(self):
        self.assertEqual("southerncastiron.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.southerncastiron.com/apple-cider-doughnuts/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Apple Cider Doughnuts")

    def test_yields(self):
        self.assertEqual("10 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.southerncastiron.com/wp-content/uploads/2018/10/doughnuts-featured-470x470.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "4 cups apple cider*",
                "2 tablespoons unsalted butter, softened",
                "1½ cups sugar, divided",
                "1 teaspoon vanilla extract",
                "1 large egg",
                "⅔ cup sour cream",
                "2¼ cups all-purpose flour",
                "1½ teaspoons baking powder",
                "1¼ teaspoons apple pie spice, divided",
                "½ teaspoon kosher salt",
                "½ cup grated Golden Delicious apple",
                "Vegetable oil, for frying",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "In a small Dutch oven, bring apple cider to a boil over medium-high heat. Boil until cider is reduced to 1 cup, about 40 minutes. Remove from heat. Let cool to room temperature.\nIn a large bowl, beat butter, ½ cup sugar, and vanilla with a mixer at medium speed until combined. Add egg, beating until thick and pale, about 2 minutes. Beat in sour cream.\nIn a medium bowl, whisk together flour, baking powder, ¼ teaspoon apple pie spice, and salt. With mixer on low speed, gradually add flour mixture to butter mixture, beating until combined. Add apple, beating just until combined. Wrap dough in plastic wrap. (Dough will be slightly sticky.) Refrigerate for 30 minutes.\nOn a lightly floured surface, gently knead dough 3 or 4 times. Roll dough to ½ inch thick. Using a 3-inch cutter, cut dough, rerolling scraps as necessary.\nFill a cast-iron Dutch oven halfway full with oil, and heat over medium heat until a deep-fry thermometer registers 350°. Add doughnuts to hot oil in batches; fry until golden brown, about 1½ minutes per side. Fry doughnut holes for about 1 minute. Remove using a slotted spoon, and let drain on paper towels. Let cool slightly.\nIn a large bowl, combine remaining 1 cup sugar and remaining 1 teaspoon apple pie spice. Dip doughnut holes in sugar mixture, shaking off excess. Drizzle with apple cider syrup.",
            self.harvester_class.instructions(),
        )
