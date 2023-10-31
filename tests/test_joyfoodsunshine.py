from recipe_scrapers.joyfoodsunshine import Joyfoodsunshine
from tests import ScraperTest


class TestJoyfoodsunshineScraper(ScraperTest):
    scraper_class = Joyfoodsunshine

    def test_host(self):
        self.assertEqual("joyfoodsunshine.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://joyfoodsunshine.com/easy-homemade-pizza-dough/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Laura", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Easy Homemade Pizza Dough", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("14 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://joyfoodsunshine.com/wp-content/uploads/2018/09/easy-homemade-pizza-dough-recipe-2-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "▢ 1 cup warm water (105 degrees F)",
                "▢ 1 Tablespoon granulated sugar",
                "▢ 1 Tablespoon active dry yeast",
                "▢ 1 TBSaTablespoon olive oil",
                "▢ 2 to 2 ½ cups all-purpose flour*",
                "▢ 1 tsp fine sea salt",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Preheat oven to 500 degrees F. Put a pizza stone in the oven while it preheats, and let it warm at 500 degrees F for at least 10 minutes.*\n"
            "Combine warm water, yeast and sugar in a large mixing bowl and stir to combine.\n"
            "Let mixture sit for 5 minutes, or until it becomes frothy and bubbles form.\n"
            "Gently stir in olive oil.\n"
            "Add 2 cups of flour and salt and mix with a spatula until a ball begins to form (dough will still be slightly sticky). Add more flour as needed to form a dough ball.\n"
            "Transfer to a floured surface and knead into a smooth dough, adding up to ½ cup extra flour if needed.\n"
            "Optional. if desired, cover the bowl with a damp tea towel and let it rise for 10 minutes or up to 1 hour.\n"
            "Roll the dough into your desired shape and put it on a piece of parchment paper.\n"
            "Add pizza sauce, cheese and toppings of choice.\n"
            "Use a pizza peel to transfer the pizza to the preheated pizza stone in the oven.\n"
            "Bake on the preheated pizza stone for 12-15 minutes, or until the bottom of the crust is golden brown.\n"
            "Remove the pizza from the oven with the pizza peel and put it on a wire rack to cool for at 5-10 minutes before cutting and serving.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.98, self.harvester_class.ratings())
