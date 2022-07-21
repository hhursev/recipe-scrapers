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
        self.assertEqual("1 serving", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://joyfoodsunshine.com/wp-content/uploads/2016/06/easy-homemade-pizza-dough-recipe-4.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "▢ 1 cup warm water 105-110 degrees F",
                "▢ 1 TBS sugar",
                "▢ 1 TBS active dry yeast",
                "▢ 1 TBS olive oil",
                "▢ 2 to 2 ½ cups all-purpose flour*",
                "▢ 1 tsp salt",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Preheat oven to 450 degrees F. Grease a pizza pan or large jelly roll pan and set aside.\nPut warm water into a large mixing bowl.\nAdd sugar and yeast and stir to combine.\nLet mixture sit for 5 minutes, or until it becomes frothy and bubbles form.\nAdd olive oil and gently stir to combine.\nAdd 2 cups of flour and salt and mix with a spatula until a ball begins to form (dough will still be slightly sticky). Add more flour as needed to form a dough ball.\nTransfer to a floured surface and knead into a smooth dough, adding up to ½ cup extra flour if needed.\nRoll dough into your desired shape and gently transfer to your prepared pan.\nTo ensure the dough doesn't form air pockets, use a fork to prick to the dough all around (gently so you do not poke holes all the way through the crust).\nBake on the lower rack of your preheated oven for 5 minutes and remove from your oven. (this is just to very slightly prebake the dough). If you notice air bubbles forming, poke them with a fork to let the air out.\nAdd pizza sauce and toppings of choice!\nBake on the lower rack of your oven for around 15-20 minutes until the crust looks crispy and lightly browned.\nLet cool, cut and serve.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.96, self.harvester_class.ratings())
