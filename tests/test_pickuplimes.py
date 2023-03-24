# mypy: allow-untyped-defs

from recipe_scrapers.pickuplimes import PickUpLimes
from tests import ScraperTest


class TestPickUpLimesScraper(ScraperTest):

    scraper_class = PickUpLimes

    def test_host(self):
        self.assertEqual("pickuplimes.com", self.harvester_class.host())

    def test_site_name(self):
        self.assertEqual("Pick Up Limes", self.harvester_class.site_name())

    def test_author(self):
        self.assertEqual("Pick Up Limes", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Cinnamon-Spiced Orange & Thyme Mocktail", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Drink", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_cook_time(self):
        self.assertEqual(5, self.harvester_class.cook_time())

    def test_prep_time(self):
        self.assertEqual(10, self.harvester_class.prep_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cdn.pickuplimes.com/cache/42/6f/426f6a364519b60424e36e0563858649.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "½ cup water",
                "¼ cup maple syrup",
                "4 sprig fresh thyme",
                "½ tsp ground cinnamon",
                "2 Tbsp freshly grated ginger",
                "½ lemon",
                "2 cup ice cube",
                "2 cup orange juice",
                "2 cup ginger ale",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Add the water, maple syrup, thyme sprigs, and cinnamon to a small pan. Bring to a simmer.\nReduce the heat to low and let it steep for about 3 minutes. Then let it cool to room temperature.\nFill a shaker or mason jar halfway with ice cubes and strain in the thyme syrup. Add the grated ginger and lemon juice and shake well for 10 seconds.\nDivide the ice cubes between your cups, strain the contents from the shaker over top, and add the orange juice and ginger ale in equal parts.\nGarnish as desired, and enjoy!",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.9, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "The sweet oranges bring a lovely citrus flavour to this drink, while the cinnamon gives a hint of warmth and the thyme brings a savoury taste. This drink fits perfectly into any season, but when the glass is decorated well, it will turn this mocktail into an extra festive one.",
            self.harvester_class.description(),
        )
