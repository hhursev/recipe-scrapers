from recipe_scrapers.wholefoods import WholeFoods
from tests import ScraperTest


class TestWholeFoodsScraper(ScraperTest):

    scraper_class = WholeFoods

    def test_host(self):
        self.assertEqual("www.wholefoodsmarket.com", self.harvester_class.host())

    def test_host_domain(self):
        self.assertEqual(
            "www.wholefoodsmarket.co.uk", self.harvester_class.host(domain="co.uk")
        )

    def test_title(self):
        self.assertEqual("Grilled Cheese and Greens", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 tablespoons extra-virgin olive oil, divided",
                "1 clove garlic, thinly sliced",
                "1 bunch (about 8 ounces) kale, thick stems removed and leaves shredded",
                "8 slices whole grain bread",
                "8 slices Swiss or Le Gruyère cheese (about 8 ounces total)",
                "1/4 teaspoon kosher salt",
                "1/8 teaspoon ground black pepper",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """In a large skillet, heat 1 teaspoon olive oil over medium-high heat until hot.
Add kale, garlic, salt and pepper. Cover and cook, stirring occasionally, until kale begins to wilt, about 5 minutes.
Uncover, reduce heat to medium and continue to cook, stirring frequently, until kale is very soft, about 5 minutes.
Arrange 4 bread slices on a work surface. Top each with one slice of cheese, an even layer of the kale, another slice of cheese, and then a piece of bread.
Brush both sides of each sandwich with remaining olive oil.
Heat a large nonstick skillet over medium heat until hot.
Place stacked sandwiches in the pan and cook until bread is golden brown and cheese has melted, pressing flat with a spatula occasionally, 4 to 5 minutes per side. Serve immediately. Depending on the size of your skillet, you might need to cook these in batches. If so, the first batch can be kept warm in a 200°F oven while finishing the second batch.""",
            self.harvester_class.instructions(),
        )

    def test_image(self):
        self.assertEqual(
            "http://assets.wholefoodsmarket.com/recipes/3604/460/290/3604-1.jpg",
            self.harvester_class.image(),
        )
