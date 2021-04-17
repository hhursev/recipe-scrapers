from recipe_scrapers.simplyquinoa import SimplyQuinoa
from tests import ScraperTest


class TestSimplyQuinoaScraper(ScraperTest):

    scraper_class = SimplyQuinoa

    def test_host(self):
        self.assertEqual("simplyquinoa.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.simplyquinoa.com/gluten-free-pancake-recipe/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "The Best Quinoa Flour Pancakes")

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("14 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 cup quinoa flour",
                "1 cup oat flour",
                "2 teaspoons baking powder",
                "1 1/4 cup almond milk (or milk of choice)",
                "2 large eggs (or flax eggs)",
                "2 tablespoons maple syrup",
                "2 tablespoons oil",
                "1/3 cup blueberries",
                "1/3 cup chocolate chips",
                "2 tablespoons lemon zest",
                "1 cup grated apple (from 1 small apple)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Whisk together the dry ingredients.\nIn a separate bowl, whisk together the wet ingredients.\nPour the wet ingredients into the dry and stir to combine. Once you have a smooth batter, it's time to cook!\nPreheat a pan over medium-low heat. Use a little cooking spray to grease it. Spoon 1/4 cup of batter onto the pan and gently spread it out with the back of a spoon. Cook the pancakes until bubbles begin to form, about 1 minute, then flip and cook another 1 - 2 minutes. Repeat until all the batter has been used.\nServe the pancakes immediately with your favorite toppings. You can also freeze these pancakes and reheat them in the toaster oven.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        # Ratings value set to zero
        self.assertEqual(0.0, self.harvester_class.ratings())
