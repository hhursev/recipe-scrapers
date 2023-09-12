# mypy: allow-untyped-defs

from recipe_scrapers.wellplated import WellPlated
from tests import ScraperTest


class TestWellPlatedScraper(ScraperTest):

    scraper_class = WellPlated

    def test_host(self):
        self.assertEqual("wellplated.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual("Egg Fried Rice", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Main Course", self.harvester_class.category())

    def test_author(self):
        self.assertEqual("Erin Clarke", self.harvester_class.author())

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.wellplated.com/wp-content/uploads/2023/07/Egg-Fried-Rice-Recipe.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1/4 cup oyster sauce*",
                "1 tablespoon soy sauce (I use low-sodium) (plus additional to taste)",
                "2 tablespoons unsalted butter (divided, or butter with canola oil spread)",
                "3 large eggs (lightly beaten)",
                "1 tablespoon canola oil",
                "1 large red, yellow, or orange bell pepper (cut into 1/4-inch dice (about 1 1/4 cups))",
                "1 bag frozen peas and carrots (thawed (12 ounces))",
                "1 cup frozen shelled edamame (thawed (optional, but great for extra protein))",
                "2 cloves garlic (minced)",
                "2 1/2 cups COLD cooked brown rice (break up large clumps with your fingers)",
                "1/2 cup chopped green onions (about 3 medium)",
                "Red pepper flakes (Sriracha, or hot sauce of choice (optional))",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ratings(self):
        self.assertEqual(4.96, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Asian, Chinese", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "How to make easy egg fried rice from scratch that's better than takeout! Simple, healthy ingredients and ready in 15 minutes!",
            self.harvester_class.description(),
        )

    def test_instructions(self):
        expected_instructions = "Stir\nIn a small bowl, stir together the oyster sauce and soy sauce. Set aside. Grab a small bowl and a large, flexible rubber spatula, and keep both handy.\nHeat a 12-inch nonstick skillet over medium heat until hot, about 2 minutes. Add 1/2 tablespoon butter and swirl to coat the bottom of the pan. Add the eggs, and cook without stirring until they barely start to set, about 20 seconds. With your spatula, scramble and break the eggs into little, bite-sized pieces. Continue to cook, stirring constantly, until eggs are just cooked through but not yet browned, about 1 additional minute. Transfer eggs to the small bowl and set aside.\nAdd\nReturn the skillet to the heat, and increase the heat to high. Let the skillet warm until it is nice and hot, about 1 minute. Add the canola oil, and swirl to coat. Add the diced bell pepper, and cook until it is crisp-tender, about 4 minutes.\nBrown\nAdd the remaining 1 1/2 tablespoons butter, peas and carrots, and edamame. Cook, stirring constantly, for 30 seconds. Stir in the garlic and cook until fragrant, about 30 seconds (do not let the garlic burn!).\nCook\nAdd the brown rice and the oyster sauce mixture. Continue cooking, stirring constantly and breaking up any remaining rice clumps, until the mixture is heated through, about 3 minutes.\nAdd reserved eggs and green onions. Cook and stir until the mixture is completely heated through, about 1 minute more. Enjoy immediately with a sprinkle of red pepper flakes or dash of hot sauce and additional soy sauce as desired."
        self.assertEqual(expected_instructions, self.harvester_class.instructions())
