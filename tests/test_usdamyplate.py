from recipe_scrapers.usdamyplate import USDAMyPlate
from tests import ScraperTest

# test recipe's URL
# https://www.myplate.gov/recipes/supplemental-nutrition-assistance-program-snap/fabulous-fig-bars


class TestUSDAMyPlateRecipesScraper(ScraperTest):

    scraper_class = USDAMyPlate

    def test_host(self):
        self.assertEqual("myplate.gov", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Fabulous Fig Bars")

    def test_total_time(self):
        self.assertEqual(75, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("24 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "3 cups dried figs (chopped, 16 ounces)",
                "1/2 cup walnuts (chopped)",
                "1/3 cup sugar",
                "1/4 cup orange juice (juice from 1/2 orange)",
                "2 tablespoons hot water",
                "1/2 cup margarine (softened, or butter)",
                "1 cup packed brown sugar",
                "1 large egg",
                "1 1/2 cups all-purpose flour",
                "1/2 teaspoon baking soda",
                "1 1/4 cups old fashioned rolled oats",
            ],
            self.harvester_class.ingredients(),
        )

    def test_image(self):
        self.assertEqual(
            "https://myplate-prod.azureedge.net/sites/default/files/styles/recipe_525_x_350_/public/2021-03/FigBars.jpg",
            self.harvester_class.image(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Wash hands with soap and water.\nPreheat oven to 350 degrees F. Lightly grease a 9x13-inch baking pan.\nCombine figs, walnuts, sugar, orange juice and hot water in a mixing bowl and set aside.\nMix together margarine or butter and brown sugar until creamy. Add egg and mix until smooth.\nMix flour and baking soda. Stir into egg mixture. Blend in oats to make soft dough.\nReserve 1 cup of dough for topping. With floured fingertips, press the remaining dough into a thin layer on the bottom of the baking pan.\nSpread fig mixture evenly over the dough. Crumble reserved dough over top, allowing fig mixture to show.\nBake 30 minutes or until golden brown. Cool completely in baking pan. Cut into 24 bars (about 2.5 x 2 inches).",
            self.harvester_class.instructions(),
        )
