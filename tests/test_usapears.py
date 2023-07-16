# mypy: allow-untyped-defs

from recipe_scrapers.usapears import USAPears
from tests import ScraperTest


class TestUSAPearsScraper(ScraperTest):

    scraper_class = USAPears

    def test_host(self):
        self.assertEqual("usapears.org", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Jamie Lauren & Mollie Katzen", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Sauteed Bosc Pears", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://usapears.org/wp-content/uploads/2014/10/Sauteed-Bosc-Pears1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 tablespoons butter",
                "¼ teaspoon cinnamon",
                "¼ teaspoon ground nutmeg",
                "¼ teaspoon ground allspice",
                "6 Bosc USA Pears, peeled, cored, and quartered",
                "Juice of ½ lemon (about 3 tablespoons)",
                "1 ½ cup nonfat vanilla yogurt or frozen yogurt",
                "½ cup chopped, toasted California walnuts",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "To prepare pears, melt butter in a large skillet over medium heat. Stir in spices and cook for 30 seconds or until aromatic. Add pears and cook for 15 minutes or until tender, stirring frequently. Stir in lemon juice.\n\nServe with nonfat vanilla yogurt or frozen yogurt and top with walnuts.",
            self.harvester_class.instructions(),
        )

    def test_cuisine(self):
        self.assertEqual("", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "This simple, tasty pear recipe was created by Chef Jamie Lauren of Absinthe Brasserie and Bar in San Francisco and cookbook author Mollie Katzen. If you can’t find Bosc pears at your local grocery store, red or green Anjou pears also work well.",
            self.harvester_class.description(),
        )
