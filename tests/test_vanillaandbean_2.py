from recipe_scrapers.vanillaandbean import VanillaAndBean
from tests import ScraperTest


class TestVanillaAndBeanScraper(ScraperTest):
    scraper_class = VanillaAndBean
    test_file_name = "vanillaandbean_2"

    def test_host(self):
        self.assertEqual("vanillaandbean.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://vanillaandbean.com/healthy-waffles/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Healthy Almond Orange Oat Waffles Recipe"
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Traci York")

    def test_yields(self):
        self.assertEqual("9 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://vanillaandbean.com/wp-content/uploads/2020/02/waffle-9.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 C (175g) Old Fashioned Rolled Oats (gluten free if needed)",
                "3/4 C (85g) Almond Flour",
                "1 (150g) Medium Banana (soft and with plenty of brown spots)",
                "3 tsp Apple Cider Vinegar",
                "3/4 C (180g) Plant Milk (I use homemade cashew milk)",
                "Orange Zest (from one large orange, two if you have it)",
                "1/2 C (140g) Fresh Squeezed Orange Juice (from one large orange)",
                "1 1/2 tsp Vanilla Extract",
                "1 Tbs Maple Syrup",
                "1 1/4 tsp Baking Powder",
                "1 tsp Baking Soda",
                "1/4 tsp salt",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat the waffle iron according to manufacturer's directions, including whether to oil/butter the iron or not (see note). Preheat the oven to 185F (85C) and place a sheet pan in the oven.\nA. For the Blender (I use VitaMix): To the blender container add the oats, almond flour, apple cider vinegar, banana, milk, orange juice, zest, vanilla extract, maple syrup, baking powder, baking soda, and salt. Blend for one minute on medium to medium high. The batter will be thick and completely smooth. ORB. For the Food Processor (I use a 12 C bowl): To the work bowl with the S attachment, add the oats, almond flour, apple cider vinegar, banana, milk, orange juice, zest, vanilla extract, maple syrup, baking powder, baking soda, and salt. Whirl for 2.5-3 minutes scraping the bowl down once during processing. The batter will be thick and not quite completely smooth.\nScoop out 1/3 C of batter and pour into the waffle iron. Bake until golden (according to manufacturer's directions). Mine take about 8-9 minutes to bake and they're dark. Gently remove the waffles using a fork and place them on the sheet pan in the preheated oven. Finish baking the remaining batter.\nShare with butter, real maple syrup and/or a dollop of your favorite unsweetened yogurt. I like to add orange zest and a touch of maple to yogurt and then dollop it on top of the waffles.\nTo Freeze: Allow the waffles to cool completely before storing them in a storage container. They can stack one on top of another - freeze for up to two weeks (beyond that and I start getting freezer burn unless individually wrapped). From the Freezer: Bake at 300F (150C) for about 8-10 minutes or until warmed through or toast on the toaster setting in a toaster oven. Keep an eye on them so they don't get too dark.",
            self.harvester_class.instructions(),
        )
