from recipe_scrapers.vegrecipesofindia import VegRecipesOfIndia
from tests import ScraperTest


class TestVegRecipesOfIndiaScraper(ScraperTest):

    scraper_class = VegRecipesOfIndia

    def test_host(self):
        self.assertEqual("vegrecipesofindia.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Dassana Amit", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Sarson ka Saag (Authentic Punjabi Style)", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(240, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("7 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://i2.wp.com/www.vegrecipesofindia.com/wp-content/uploads/2012/12/sarson-ka-saag-recipe-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 bunch mustard leaves ((sarson))",
                "½ bunch bathua leaves ((chenopodium))",
                "½ bunch spinach leaves",
                "1 cup chopped tender radish leaves ((mooli ke patte))",
                "2 to 3 inches white radish root",
                "1 cup fenugreek leaves, (chopped)",
                "2 medium sized onions, (chopped)",
                "3 medium sized tomatoes, (chopped)",
                "2 inch ginger, (chopped)",
                "2 green chilies, (chopped)",
                "7 to 8 garlic, (chopped)",
                "½ teaspoon red chili powder",
                "1 to 2 pinch asafoetida (or ¼ teaspoon asafoetida powder (hing))",
                "2 to 3 cups water",
                "2 tablespoon maize flour",
                "salt as required",
                "1 medium sized onion, (finely chopped)",
                "1 to 2 tablespoon oil",
                "3 bowls of cooked saag",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "making sarson ka saag\nFirstly clean and chop all the greens. then wash the greens well.\nIn a pressure cooker or pan add all the ingredients listed under saag except for maize flour.\nCover the pressure cook and cook for 6-7 minutes or more.\nIf cooking in a pan, then cover and let the greens cook till done. Do check occasionally.\nPour the greens along with the stock and maize flour in a blender. blend till smooth.\nIn another pan, pour the pureed greens.\nSimmer for a good 25-30 minutes.\ntempering for sarson ka saag\nIn another small pan, heat oil or ghee\nAdd the chopped onions and fry them till light brown.\nAdd the prepared saag. Stir and simmer for a couple of minutes.\nStir ocaasionally.\nServe sarson ka saag hot with some chopped onions, whole green chilies and a dollop of butter on the saag with makki di roti",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.9, self.harvester_class.ratings())
