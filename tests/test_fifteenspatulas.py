from recipe_scrapers.fifteenspatulas import FifteenSpatulas
from tests import ScraperTest


class TestFifteenSpatulasScraper(ScraperTest):

    scraper_class = FifteenSpatulas

    def test_host(self):
        self.assertEqual("fifteenspatulas.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.fifteenspatulas.com/orange-scented-creme-brulee/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Orange Creme Brulee")

    def test_yields(self):
        self.assertEqual("6 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.fifteenspatulas.com/wp-content/uploads/2019/05/Orange-Creme-Brulee-Fifteen-Spatulas-16.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "zest of 4 oranges ((about 2 tsp))",
                "3 cups heavy cream",
                "5 large egg yolks",
                "1/2 cup sugar +1 tsp for each crème brûlée",
                "1 tsp vanilla extract",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Combine the orange zest and cream in a saucepan, and let it sit in the fridge for 2 hours.\nPreheat the oven to 300 degrees F.\nWhisk together the egg yolks and 1/2 cup sugar for 1 minute, until well blended.\nHeat the orange zest cream over medium high heat until 180F, bringing it almost to a boil, but not quite. You’ll know when bubbles begin forming on the side, but it's best to use a thermometer.\nWhile whisking constantly, slowly dribble the hot cream into the egg yolk mixture, gradually over a minute.\nAdd the vanilla, then pour the mixture through a sieve to strain out the orange zest and any coagulated egg.\nPour the strained custard into six 4-ounce ramekins until nearly full (you may use other size ramekins, but you'll need to adjust bake time).\nPlace the ramekins in a large baking pan and add enough boiling water to come halfway up the outsides of the ramekins.\nBake for 35-40 minutes, until the creme brulees jiggle slightly when shaken, and have set. Take the ramekins out of the water bath and let cool to room temperature. Then cover the tops with plastic wrap and refrigerate until they firm up, 4-6 hours.\nWhen you’re ready to serve the creme brulee, sprinkle 1 tsp of sugar evenly on top of each one.\nIdeally, use a blowtorch to quickly caramelize the tops of each creme brulee, and serve immediately. This will give you the crunchy top layer you want, while keeping the creme brulee from getting warm.\nIf you don't have a torch, you can use the broiler of your oven to caramelize the top. Set the oven rack as close as possible to the broiler, and preheat to high. Place the ramekins on a sheet pan, and broil for 1-2 minutes, until the top caramelizes, making sure you keep your eye on the browning (it's easier to burn the sugar using the broiler). Serve promptly and enjoy!",
            self.harvester_class.instructions(),
        )
