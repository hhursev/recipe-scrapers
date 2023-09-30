from recipe_scrapers.bakingsense import BakingSense
from tests import ScraperTest


class TestBakingSense(ScraperTest):

    scraper_class = BakingSense
    test_file_name = "bakingsense_1"

    def test_host(self):
        self.assertEqual("baking-sense.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.baking-sense.com/2020/05/13/sourdough-bundt-cake/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Sourdough Bundt Cake with Buttermilk Glaze"
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Eileen Gray")

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("16 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.baking-sense.com/wp-content/uploads/2020/05/sourdough-bundt-9a.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 large eggs (room temperature)",
                "2 large yolks (room temperature)",
                "1 tablespoon vanilla extract",
                "8 oz sourdough discard (1 cup, room temperature)",
                "9 oz cake flour (2 cups)",
                "11 oz granulated sugar (1 1/3 cups)",
                "2 teaspoons baking powder",
                "1/2 teaspoon table salt",
                '6 oz unsalted butter (room temperature, cut into 1" chunks)',
                "4 oz buttermilk (1/2 cup, room temperature)",
                "8 oz confectioner's sugar (2 cups)",
                "1 teaspoon vanilla",
                "2 oz buttermilk (1/4 cup)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat the oven to 350°F. Generously butter and flour a 12 cup Bundt pan.\nMake the batter\nWhisk together the eggs, yolks, vanilla and the discard, set aside.\nSift the flour, sugar, baking powder and salt into a mixer bowl. Mix on low speed to combine the dry ingredients. With the mixer running, toss the chunks of butter into the flour mixture.\nAdd the buttermilk and increase the speed to medium. Mix on medium high for 2 minutes to aerate the batter. Scrape the bowl and beater.\nAdd the egg mixture in 3 batches, scraping the bowl between each addition. Pour the batter into the prepared pan.\nBake until the cake springs back when lightly pressed or a toothpick inserted into the center comes out clean, about 40 minutes.\nCool for 10 minutes in the pan. Invert the cake onto a cooling rack set over a clean sheet pan. Cool until slightly warm before glazing.\nMake the Glaze\nCombine the sugar, vanilla and buttermilk in a small bowl and whisk until smooth.\nPour the glaze over the still slightly warm cake. You can scoop up the glaze from the sheet pan and use it to fill in any gaps in the glaze or leave it with the drips.\nCool completely and allow the glaze to set. Transfer to a serving plate.",
            self.harvester_class.instructions(),
        )
