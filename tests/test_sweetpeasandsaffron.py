from recipe_scrapers.sweetpeasandsaffron import SweetPeasAndSaffron
from tests import ScraperTest


class TestSweetPeasAndSaffron(ScraperTest):

    scraper_class = SweetPeasAndSaffron

    def test_host(self):
        self.assertEqual("sweetpeasandsaffron.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://sweetpeasandsaffron.com/healthy-steel-cut-oats-recipes/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            "7 Healthy Steel Cut Oats Recipes", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual("25", self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cdn.statically.io/img/sweetpeasandsaffron.com/wp-content/uploads/2017/05/steel-cut-oats-7-ways-TEXT-150x150.jpg?quality=100&f=auto",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "butter 1 tablespoon",
                "steel cut oats 1 cup",
                "Instant Pot or 4 (slow cooker, stove-top) cups water 3 teaspoon",
                "vanilla extract 1 teaspoon",
                "cinnamon 1 tablespoons",
                "After cooking: 2 cup",
                "maple syrup 1 cup",
                "large apple 1 teaspoon",
                "unsweetened apple sauce 1/3 teaspoon",
                "chopped pecans 1/4 teaspoon",
                "ground nutmeg 1/4 cup",
                "ground cloves 1 tablespoons",
                "vanilla extract 1 cups",
                "pumpkin puree 2 tablespoon",
                "pumpkin seeds/pepitas 1-2 tablespoons",
                "zest from 1 lemon 1 cups",
                "blueberries 2 teaspoon",
                "chia seeds 1-2 tablespoon",
                "cocoa powder 1 cups",
                "peanut butter 1 cup",
                "berries 1-2 cup",
                "chia seeds 1/4 cup",
                "coconut extract 1 teaspoon",
                "key lime zest 1/4 cup",
                "strawberries 1 cups",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "(Optional but adds extra flavor). Select the 'sauté' function on the Instant Pot. Add the butter and melt. Add the steel cut oats and sauté, stirring occasionally for 5 or so minutes, until fragrant and golden.",
                    "Add the water, vanilla and cinnamon (and other ingredients as needed for flavor variations)",
                    "Cook on high pressure for 2 minutes, followed by natural pressure release (let the Instant Pot sit for 20 minutes up to 120 minutes).",
                    "Remove lid and stir in maple syrup and any other ingredients for the flavor variations.",
                    "(Optional but adds extra flavor). Heat a pan over medium heat. Add the butter and melt. Add the steel cut oats and sauté, stirring occasionally for 5 or so minutes, until fragrant and golden.",
                    "Spray the inside of your slow cooker with cooking spray or use a slow cooker liner. Transfer steel cut oats and add the water, vanilla and cinnamon (and other ingredients as needed for flavor variations)",
                    "Cover and cook on low for 6-8 hours.",
                    "Stir in maple syrup and any other ingredients for the flavor variations.",
                    "Heat a 4 quart pot over medium heat. Add the butter and melt. Add the steel cut oats and sauté, stirring occasionally for 5 or so minutes, until fragrant and golden.",
                    "Add the water, vanilla and cinnamon (and other ingredients as needed for flavor variations).",
                    "Reduce heat and simmer, stirring occasionally, for 25-35 minutes.",
                    "Remove from heat and stir in maple syrup and any other ingredients for the flavor variations.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        return self.assertEqual("4.89", self.harvester_class.ratings())

    def test_author(self):
        return self.assertEqual("Denise Bustard", self.harvester_class.author())
