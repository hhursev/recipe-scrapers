from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.budgetbytes import BudgetBytes
from tests import ScraperTest


class TestBudgetBytesScraper(ScraperTest):
    scraper_class = BudgetBytes

    def test_host(self):
        self.assertEqual("budgetbytes.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.budgetbytes.com/smash-burger/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Smash Burgers")

    def test_image(self):
        self.assertEqual(
            self.harvester_class.image(),
            "https://www.budgetbytes.com/wp-content/uploads/2023/05/Smash-Burger-plated.jpg",
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Monti - Budget Bytes")

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 lb ground beef ($6.99)",
                "4 Tbsp frozen salted butter, divided ($0.56)",
                "3 tsp Homemade Burger Seasoning ($0.33)",
                "4 burger buns ($2.99)",
                "4 leaves iceberg lettuce ($0.37)",
                "1 tomato, sliced into thin rounds ($0.45)",
                "1/4 small red onion, sliced into thin rounds ($0.16)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 lb ground beef ($6.99)",
                        "4 Tbsp frozen salted butter, divided ($0.56)",
                        "3 tsp Homemade Burger Seasoning ($0.33)",
                        "4 burger buns ($2.99)",
                        "4 leaves iceberg lettuce ($0.37)",
                        "1 tomato, sliced into thin rounds ($0.45)",
                        "1/4 small red onion, sliced into thin rounds ($0.16)",
                    ],
                    purpose=None,
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Separate the ground beef into four equal portions.\nGrate 1/2 tablespoon of frozen butter onto each portion. Wrap the meat around the butter and shape it into a ball. Chill the beef until you are ready to cook. Place an ungreased cast iron skillet over high heat. Turn on your exhaust fan. Open a window.\nWhen the skillet is smoking hot, sprinkle a 3/4 teaspoon of burger seasoning all over the beef ball, then place it in the pan.\nSmash down with a spatula and keep the spatula on the burger as it cooks. When you see the top of the patty change color (about 2 minutes), carefully work the spatula under the patty. Take your time with this step, as the patty will be stuck to the pan.*\nWhen you have loosened the patty, flip it and smash it again. Cook for 2 minutes more, remove the patty from the pan, and rest it on a cooling rack. Wipe the pan down with a paper towel and cook the remaining patties.\nWhile the patties rest, place a rack in the top third of your oven and put it on broil. Melt the remaining 2 tablespoons of butter and brush it onto the inside of the buns. Place them buttered side up on a sheet pan and toast in the oven for a few minutes until golden.\nAssemble the burgers. Place the burger on the bottom bun and top with onion rounds, tomato slices, and lettuce. Add the top bun and enjoy the crispiest, smokiest, burger ever!",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.5, self.harvester_class.ratings())
