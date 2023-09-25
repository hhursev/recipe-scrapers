from recipe_scrapers.grouprecipes import GroupRecipes
from tests import ScraperTest


class TestGroupRecipes(ScraperTest):
    scraper_class = GroupRecipes

    def test_host(self):
        self.assertEqual("grouprecipes.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Slow Cooker Chicken & Biscuits Recipe"
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "MountainMamas")

    def test_image(self):
        self.assertEqual(
            "http://s2.grouprecipes.com/images/recipes/200/d1505068b3b6795944eeae48987109ba.jpg",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(180, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("5 servings", self.harvester_class.yields())

    def test_description(self):
        self.assertEqual(
            "A delicious comforting and hearty meal of Chicken and Dumplings (Biscuits) is just a perfect dinner that can be made in a crockpot while your at work or busy with the kids. This tender and juicy chicken is slow-cooked along side carrots and potatoes and a blend of savory spices.",
            self.harvester_class.description(),
        )

    def test_category(self):
        self.assertEqual(
            "slower cooker/crockpot, chicken, biscuits, gravy, slow-cook, nothing specific",
            self.harvester_class.category(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "3 chicken breasts, diced",
                "salt, to taste",
                "pepper, to taste",
                "2 cups broccoli florets",
                "2 cups baby carrots, diced",
                "21 oz condensed cream of chicken soup",
                "1 can refrigerated biscuit",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        expected_instructions = (
            "Place the chicken in a 7-quart (6 ½ liters) slow cooker. Sprinkle on salt & pepper.\n"
            "Add the veggies and condensed soup, and mix thoroughly.\n"
            "Cook on high for 3 hours.\n"
            "Rip biscuit dough into small pieces, and drop evenly over chicken. Cook an additional hour."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())
