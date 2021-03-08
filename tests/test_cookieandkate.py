from recipe_scrapers.cookieandkate import CookieAndKate
from tests import ScraperTest


class TestCookieAndKateScraper(ScraperTest):

    scraper_class = CookieAndKate

    def test_host(self):
        self.assertEqual("cookieandkate.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://cookieandkate.com/broccoli-cheddar-spinach-frittata/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Broccoli, Cheddar & Spinach Frittata"
        )

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "8 SimplyNature Organic Cage Free Eggs",
                "½ cup milk of choice",
                "2 small-to-medium cloves garlic, pressed or minced",
                "½ teaspoon sea salt, divided",
                "Freshly ground black pepper",
                "1 cup freshly grated cheddar cheese, divided",
                "1 tablespoon SimplyNature Organic Extra Virgin Olive Oil, more as needed",
                "1 small yellow onion, chopped",
                "⅓ cup water",
                "2 cups thinly sliced broccoli florets",
                "2 cups SimplyNature Organic Baby Spinach, roughly chopped",
                "⅓ cup thinly sliced green onions",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat the oven to 425 °F. In a large bowl, whisk together the eggs, milk, garlic, ¼ teaspoon of the salt and about 5 twists of freshly ground black pepper until well blended. Then whisk in about half of the cheese, reserving the other half for later.\nIn a 10-inch, well-seasoned cast iron skillet or oven-safe sauté pan, warm the olive oil over medium heat until shimmering. Add the onion and the remaining ¼ teaspoon salt. Cook, stirring frequently, until the onion is tender and translucent, about 3 to 5 minutes.\nAdd the broccoli and water to the pan, then cover it with a lid (or a baking sheet) and steam the mixture until the broccoli is brighter green and easily pierced by a fork, about 2 to 3 minutes. Uncover, and add the spinach and green onions. Cook, stirring constantly, until the spinach has wilted, about 30 to 60 seconds.\nArrange the mixture in an even layer across the skillet. Whisk the egg mixture one last time and pour it into the pan. Sprinkle the frittata with the remaining cheese. Put the pan in the oven and bake until you can shimmy the pan by the handle (careful, it’s hot!) and see that the middle is just barely set, about 12 to 15 minutes.\nOnce the frittata is done baking, let it rest for 5 to 10 minutes before slicing it into 6 large or 8 smaller wedges. Serve immediately. Leftover frittata will keep well, covered and refrigerated, for up to 3 days. Enjoy chilled or gently reheat.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.9, self.harvester_class.ratings())
