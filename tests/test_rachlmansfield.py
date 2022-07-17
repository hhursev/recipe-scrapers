from recipe_scrapers.rachlmansfield import RachlMansfield
from tests import ScraperTest


class TestRachlMansfieldScraper(ScraperTest):

    scraper_class = RachlMansfield

    def test_host(self):
        self.assertEqual("rachlmansfield.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Rachel", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Healthy Flourless Brownies (nut-free + gluten-free)",
        )

    def test_total_time(self):
        self.assertEqual(27, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("9 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://rachlmansfield.com/wp-content/uploads/2019/12/B6984237-A840-46A7-93FD-417FAA609A78-scaled-225x225.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 cup tahini*",
                "1/4 cup maple syrup",
                "1/2 cup coconut sugar",
                "2 pasture-raised eggs*",
                "1 teaspoon vanilla extract",
                "1/3 cup + 2 tablespoons cacao powder",
                "1 teaspoon baking powder",
                "1/2 cup Hu Kitchen Dark Chocolate Gems (code RACHL for free shipping)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions_list(self):
        self.assertEqual(
            [
                "Preheat oven to 350 degrees and line an 8×8 baking dish with parchment paper and grease well",
                "Cream together the tahini, maple syrup, coconut sugar, eggs and vanilla",
                "Mix in the cacao powder and baking powder until well combined (it will be thick!)",
                "Fold in dark chocolate gems then add batter to baking dish",
                "Bake in oven for 22-25 minutes (or until toothpick comes out clean when you poke the brownies)",
                "Allow the brownies to cool for a few minutes (this is key so they set!) then slice and enjoy!",
            ],
            self.harvester_class.instructions_list(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
