# mypy: allow-untyped-defs

from recipe_scrapers.goodhousekeeping import GoodHousekeeping
from tests import ScraperTest


class TestGoodHousekeepingScraper(ScraperTest):
    scraper_class = GoodHousekeeping
    test_file_name = "goodhousekeeping_3"

    def test_host(self):
        self.assertEqual("goodhousekeeping.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual(
            "The Good Housekeeping Cookery Team", self.harvester_class.author()
        )

    def test_title(self):
        self.assertEqual(
            "Slow Cooker Chocolate Fondant Dessert", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("winter,dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(200, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://hips.hearstapps.com/hmg-prod/images/slow-cooker-chocolate-fondant-dessert-1612954641.jpg?crop=1.00xw:1.00xh;0,0&resize=1200:*",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "175 g unsalted butter, chopped, plus extra to grease",
                "150 g dark chocolate (70% cocoa solids), chopped",
                "300 g caster sugar",
                "3 medium eggs, lightly beaten",
                "40 g cocoa powder",
                "75 g plain flour",
                "Icing sugar, optional, to dust",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        instructions = [
            "Line the pot of slow cooker with foil then a layer of baking parchment.",
            "Melt the butter and chocolate together in a heatproof bowl set over a pan of barely simmering water (make sure the base of the bowl doesn't touch the water). When the mixture is melted and smooth, lift the bowl off the pan.",
            "Whisk the sugar into the chocolate mixture, followed by the eggs, cocoa powder and flour.",
            "Scrape the mixture into the prepared pot, cover the top with a tea towel (don’t let the towel touch the mixture) and put the lid on top. Turn the slow cooker on to its low setting (see GH TIP) and cook for about 2hr 45min until the middle feels softly set - it will look glossy but not feel sticky when pressed lightly with a finger. Uncover and cook for a further 30min. Turn off the cooker.",
            "Lift the fondant out and dust with icing sugar, if you like. Serve immediately with ice cream or double cream.",
        ]
        self.assertEqual("\n".join(instructions), self.harvester_class.instructions())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_nutrients(self):
        self.assertEqual(
            {},
            self.harvester_class.nutrients(),
        )

    def test_description(self):
        self.assertEqual(
            "Chocolate Fondant Dessert: You can cook desserts in a slow cooker as well as stews. Try this chocolate fondant dessert.",
            self.harvester_class.description(),
        )
