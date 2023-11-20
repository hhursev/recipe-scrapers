# mypy: allow-untyped-defs

from recipe_scrapers.williamssonoma import WilliamsSonoma
from tests import ScraperTest


class TestWilliamsSonomaScraper(ScraperTest):
    scraper_class = WilliamsSonoma
    test_file_name = "williamssonoma_1"

    def test_host(self):
        self.assertEqual("williams-sonoma.com", self.harvester_class.host())

    def canonical_url(self):
        self.assertEqual(
            "https://www.williams-sonoma.com/recipe/bacon-fat-hash-browns.html",
            self.harvester_class.host(),
        )

    def test_author(self):
        self.assertEqual("Williams Sonoma", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Bacon Fat Hash Browns", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://assets.wsimgs.com/wsimgs/rk/images/dp/recipe/202341/0005/img28l.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        ingredients = [
            "2 large russet potatoes, peeled",
            "Fine sea salt and freshly ground pepper",
            "2 Tbs. rendered bacon fat",
            "Flaky sea salt",
        ]
        self.assertEqual(ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = (
            "Using the large holes of a box grater, grate the potatoes over a kitchen towel. Wring the towel with the potatoes inside over a bowl to remove as much moisture as possible. Reserve the liquid from the potatoes in the bowl. Place the potatoes in a separate bowl.\n"
            "Set the bowl of potato liquid aside so the starch has time to settle to the bottom. Carefully pour off the water from the top, leaving the starch in the bottom. Add the starch to the grated potatoes and season with fine sea salt and pepper.\n"
            "In a small nonstick sauté pan over high heat, warm the bacon fat. Form individual hash brown cakes, about the size of your fist. Working in batches (if they won’t all fit in the pan at the same time), add the cakes to the pan and press down flat with a spatula, ensuring an even thickness throughout.\n"
            "Reduce the heat to medium-low and cook until evenly golden brown, about 4 minutes. When the bottom is nicely browned, flip and use your spatula to flatten the hash browns again. Continue to cook until this side is evenly golden brown, about 2 minutes.\n"
            "Transfer the hash browns to a serving plate, sprinkle with flaky sea salt and serve. Serves 3 or 4.\n"
            "Adapted from At Home by Gavin Kaysen (Spoon Thief Publishing, 2023)"
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_cuisine(self):
        self.assertEqual("AMERICAN", self.harvester_class.cuisine())
