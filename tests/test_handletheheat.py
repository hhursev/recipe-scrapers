from recipe_scrapers.handletheheat import HandleTheHeat
from tests import ScraperTest


class TestHandleTheHeatScraper(ScraperTest):

    scraper_class = HandleTheHeat

    def test_host(self):
        self.assertEqual("handletheheat.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://handletheheat.com/chewy-brownies/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Best Ever Chewy Brownies")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Tessa Arias")

    def test_yields(self):
        self.assertEqual("9 servings", self.harvester_class.yields())

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_image(self):
        self.assertEqual(
            "https://handletheheat.com/wp-content/uploads/2017/03/Chewy-Brownies-Square-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "5 tablespoons (71 grams) unsalted butter",
                "1 1/4 cups (249 grams) granulated sugar",
                "2 large eggs plus 1 egg yolk, (cold)",
                "1 teaspoon vanilla extract",
                "1/3 cup vegetable oil",
                "3/4 cup (75 grams) unsweetened cocoa powder",
                "1/2 cup (63 grams) all-purpose flour",
                "1/8 teaspoon baking soda",
                "1 tablespoon cornstarch",
                "1/4 teaspoon salt",
                "3/4 cup (128 grams) semisweet chocolate chips",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat the oven to 325°F. Line a 8 by 8-inch pan with foil or parchment paper and spray with nonstick cooking spray.\nIn a microwave safe bowl, add the butter and sugar. Microwave for about 1 minute, or until the butter is melted. Whisk in the eggs, egg yolk, and vanilla. Stir in the oil and cocoa powder.\nWith a rubber spatula, stir in the flour, baking soda, cornstarch, and salt until combined. Stir in the chocolate chips.\nSpread the brownie batter evenly into the prepared pan. Place in the oven and bake for 30 minutes, or until the brownies are set and a cake tester inserted into the center has moist crumbs attached. Do not overcook. Let cool completely before cutting and serving.\nBrownies can be stored in an airtight container at room temperature for up to 3 days.",
            self.harvester_class.instructions(),
        )
