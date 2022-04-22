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
        self.assertEqual("22 items", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.kingarthurbaking.com/sites/default/files/2021-11/Spiced-Rye-Ginger_SOCIAL_HERO_33683-1.jpg",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_rating(self):
        self.assertEqual(4.80, self.harvester_class.ratings())

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
            """Preheat the oven to 325°F. Lightly grease (or line with parchment) two baking sheets.\nWeigh your flour; or measure it by gently spooning it into a cup, then sweeping off any excess.\nIn a medium bowl, whisk together the flour, baking soda, salt, and spices. Set aside.\nIn a large mixing bowl, using either a hand whisk, an electric mixer, or a stand mixer, whisk the sugar and oil until combined.\nAdd the egg and whisk until smooth.\nStir in the molasses.\nAdd the dry ingredients to the bowl and stir until well combined.\nUse a spoon (or a tablespoon cookie scoop) to portion 1 1/4" balls of dough.\nRoll the dough balls in granulated or sparkling sugar to coat before placing onto the prepared baking sheets. Leave 2" between them on all sides; they'll spread as they bake.\nBake the cookies for 12 to 15 minutes, until they're puffed and their edges are set.\nRemove the cookies from the oven, and cool completely right on the pan.\nStore cookies, well wrapped, at room temperature for several days; freeze for longer storage.""",
            self.harvester_class.instructions(),
        )


class TestKingArthurScraperBeautifulBuns(ScraperTest):

    scraper_class = KingArthur
    test_file_name = "kingarthur_beautiful_buns"

    def test_host(self):
        self.assertEqual("kingarthurbaking.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.kingarthurbaking.com/recipes/beautiful-burger-buns-recipe",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Beautiful Burger Buns")

    def test_yields(self):
        self.assertEqual("8 items", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.kingarthurbaking.com/sites/default/files/2021-08/beautiful-burger-buns.jpg",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(160, self.harvester_class.total_time())

    def test_rating(self):
        self.assertEqual(4.70, self.harvester_class.ratings())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "3 1/2 cups (420g) King Arthur Unbleached All-Purpose Flour",
                "3/4 to 1 cup (170g to 227g) water lukewarm*",
                "2 tablespoons (28g) butter at room temperature",
                "1 large egg",
                "1/4 cup (50g) granulated sugar",
                "1 1/4 teaspoons salt",
                "1 tablespoon (9g) instant yeast",
                "3 tablespoons (43g) butter melted; divided",
                "1 large egg white whisked with 2 tablespoons cold water*",
                "sesame seeds or the seeds of your choice",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            """Weigh your flour; or measure it by gently spooning it into a cup, then sweeping off any excess.\nTo make the dough: Mix and knead all of the dough ingredients — by hand, mixer, or bread machine — to make a soft, smooth dough.\nCover the dough and let it rise until it's nearly doubled in bulk, about 1 to 2 hours.\nTo shape the buns: Gently deflate the dough and divide it into eight pieces (about 100g each); to make smaller or larger buns see "tips," below. Shape each piece into a ball.\nFlatten each dough ball with the palm of your hand until it's about 3" across.\nPlace the buns on a lightly greased or parchment-lined baking sheet. Cover and let rise until noticeably puffy, about an hour. Toward the end of the rising time, preheat the oven to 375°F.\nBrush the buns with about half of the melted butter. To make seeded buns, brush the egg white/water mixture right over the melted butter; it'll make the seeds adhere. Sprinkle buns with the seeds of your choice.\nTo bake the buns: Bake the buns for 15 to 18 minutes, until golden. Remove them from the oven and brush with the remaining melted butter; this will give the buns a satiny, buttery crust. If you've made seeded buns apply the melted butter carefully, to avoid brushing the seeds off the buns.\nCool the buns on a rack before slicing in half, horizontally. Use as a base for burgers (beef or plant-based) or any favorite sandwich filling.\nStorage information: Store leftover buns, well-wrapped, at room temperature for several days; freeze for longer storage.""",
            self.harvester_class.instructions(),
        )
