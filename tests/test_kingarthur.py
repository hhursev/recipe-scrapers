from recipe_scrapers.kingarthur import KingArthur
from tests import ScraperTest


class TestKingArthurScraper(ScraperTest):

    scraper_class = KingArthur

    def test_host(self):
        self.assertEqual("kingarthurbaking.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.kingarthurbaking.com/recipes/spiced-rye-ginger-cookies-recipe",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Spiced Rye Ginger Cookies")

    def test_yields(self):
        self.skipTest(
            reason="Re-enable when harvester produces expected 'yields' output"
        )
        self.assertEqual("22 item(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.kingarthurbaking.com/sites/default/files/2020-07/spiced-rye-ginger-cookies.jpg",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_rating(self):
        self.assertEqual(4.70, self.harvester_class.ratings())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 cups (212g) medium rye flour",
                "1 teaspoon baking soda",
                "1/2 teaspoon salt",
                "2 teaspoons ginger",
                "3/4 teaspoon black pepper",
                "1/2 teaspoon cinnamon",
                "1/2 teaspoon cardamom",
                "3/4 cup (149g) granulated sugar",
                "1/2 cup (99g) vegetable oil",
                "1 large egg",
                "1/4 cup (85g) molasses",
                "1/3 cup (76g) coarse sparkling sugar or 1/3 cup (66g) granulated sugar",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat the oven to 325°F. Lightly grease (or line with parchment) two baking sheets.\n, Weigh your flour; or measure it by gently spooning it into a cup, then sweeping off any excess.\n, In a medium bowl, whisk together the flour, baking soda, salt, and spices. Set aside.\n, In a large mixing bowl, using either a hand whisk, an electric mixer, or a stand mixer, whisk the sugar and oil until combined.\n, Add the egg and whisk until smooth.\n, Stir in the molasses.\n, Add the dry ingredients to the bowl and stir until well combined.\n, Use a spoon (or a tablespoon cookie scoop) to portion 1 1/4\u0022 balls of dough.\n, Roll the dough balls in granulated or sparkling sugar to coat before placing onto the prepared baking sheets. Leave 2\u0022 between them on all sides; they\u0027ll spread as they bake.\n, Bake the cookies for 12 to 15 minutes, until they\u0027re puffed and their edges are set.\n, Remove the cookies from the oven, and cool completely right on the pan.  \n, Store cookies, well wrapped, at room temperature for several days; freeze for longer storage.",
            self.harvester_class.instructions(),
        )
