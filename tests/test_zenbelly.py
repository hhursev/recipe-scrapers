from recipe_scrapers.zenbelly import ZenBelly
from tests import ScraperTest


class TestZenBellyScraper(ScraperTest):

    scraper_class = ZenBelly

    def test_host(self):
        self.assertEqual("zenbelly.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.zenbelly.com/gingerbread/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Paleo Gingerbread")

    def test_yields(self):
        self.assertEqual("20 servings", self.harvester_class.yields())

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_image(self):
        self.assertEqual(
            "https://www.zenbelly.com/wp-content/uploads/2019/01/gingerbread-3-225x225.jpeg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "butter (ghee, or shortening for greasing the pan)",
                "3 cups almond flour",
                "1 1/2 cups tapioca starch (plus more for flouring pan)",
                "1/2 cup coconut flour",
                "1 1/2 teaspoons baking soda",
                "2 teaspoons ground ginger",
                "1 teaspoons ground cinnamon",
                "1/4 teaspoon ground allspice",
                "1/4 teaspoon ground cardamom",
                "1/2 teaspoon finely ground sea salt",
                "1 cup coconut sugar",
                "1 cup molasses (use true molasses if you can find it)",
                "2 teaspoons fresh ginger",
                "1 cup boiling water",
                "4 eggs",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Preheat the oven to 350ºF. Grease a 9×13-inch cake pan.",
                    "In a large bowl, whisk together the almond flour, tapioca starch, coconut flour, baking soda, ground ginger, cinnamon, allspice, cardamom, and salt.",
                    "In a medium heat proof bowl, whisk together the coconut sugar, molasses, fresh ginger, and boiling water. Once it’s lukewarm (the molasses and coconut sugar should take the temperature down enough), whisk in the eggs.",
                    "Pour the wet ingredients into the dry ingredients and whisk until there are no lumps.",
                    "Pour into the prepared pan and bake for 28-35 minutes*",
                ]
            ),
            self.harvester_class.instructions(),
        )
