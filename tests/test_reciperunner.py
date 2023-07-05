from recipe_scrapers.reciperunner import RecipeRunner
from tests import ScraperTest


class TestRecipeRunnerScraper(ScraperTest):

    scraper_class = RecipeRunner

    def test_host(self):
        self.assertEqual("reciperunner.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://reciperunner.com/vanilla-chocolate-pizzelles/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Vanilla and Chocolate Pizzelles"
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Danae Halliday")

    def test_yields(self):
        self.assertEqual("70 servings", self.harvester_class.yields())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_image(self):
        self.assertEqual(
            "https://reciperunner.com/wp-content/uploads/2014/12/Vanilla-Chocolate-Pizzelles-Pic-720x720.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 3/4 cup all purpose flour",
                "2 teaspoons baking powder",
                "1/4 teaspoon fine sea salt",
                "3 eggs",
                "3/4 cup granulated sugar",
                "1/2 cup unsalted butter, melted",
                "1 tablespoon vanilla extract",
                "1 3/4 cup all purpose flour",
                "1/4 cup unsweetened cocoa powder",
                "2 teaspoons baking powder",
                "1/4 teaspoon fine sea salt",
                "3 eggs",
                "3/4 cup granulated sugar",
                "1/2 cup unsalted butter, melted",
                "1 1/2 teaspoons vanilla extract",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Preheat the pizzelle press according to manufacturers instructions. In a bowl whisk together the flour, baking powder and salt.",
                    "In the bowl of a stand mixer or using a hand held mixer beat the eggs for about a minute. Gradually pour in the sugar, beating until smooth. Add in the vanilla and with the mixer on, slowly pour in the melted butter.",
                    "Beat on medium speed for another minute and then add in the dry ingredients. Beat just until combined, scraping down the sides of the bowl as needed.",
                    "Once the pizzelle press is hot use a 2 teaspoon size cookie scoop and drop the dough in the center of the cookie grid. Close the lid and lock or press down gently depending on your pizzelle press. Bake for about 30-45 seconds then remove the cookies onto a wire cooling rack. Continue the process until all of the dough is gone.",
                    "For the chocolate pizzelles the process is the same except that you will whisk the cocoa powder in with the flour, salt and baking powder.",
                ]
            ),
            self.harvester_class.instructions(),
        )
