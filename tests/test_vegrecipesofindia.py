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
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.vegrecipesofindia.com/wp-content/uploads/2012/12/sarson-ka-saag-recipe-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 bunch mustard greens ((sarson))",
                "½ bunch bathua leaves ((chenopodium/goosefoot/melde))",
                "½ bunch spinach leaves ((palak))",
                "1 cup chopped radish leaves (- use tender leaves, (mooli ke patte))",
                "3 to 4 inches white radish root",
                "1 cup fenugreek leaves (- chopped)",
                "1 cup chopped onions (or 2 medium sized onions)",
                "1.5 cups chopped tomatoes (or 3 medium-sized tomatoes)",
                "2 inches ginger (- chopped)",
                "2 green chilies (- chopped)",
                "7 to 8 garlic (- medium sized, chopped)",
                "½ teaspoon red chili powder",
                "2 to 3 pinches asafoetida (or ⅛ teaspoon asafoetida powder (hing))",
                "2 to 3 cups water (or add as required)",
                "2 tablespoon maize flour (or fine cornmeal)",
                "salt (as required)",
                "⅓ cup finely chopped onions (or 1 small to medium-sized onion)",
                "1 to 2 tablespoons oil (or ghee)",
                "2 cups cooked saag (or as required)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Making sarson ka saag\nFirstly clean and chop all the greens. Then wash or rinse the greens very well in running water.\nIn a 5 litre stovetop pressure cooker or pan add all the ingredients listed under "for sarson ka saag" except for maize flour.\nCover the pressure cook and cook for 6 to 7 minutes or more on medium-high heat.\nIf cooking in a pan, then cover and let the greens cook till tender and softened. Do check occasionally.\nPour the greens along with the stock and maize flour in a blender. Blend till smooth.\nIn another deep pan or in the same cooker, pour the pureed greens.\nSimmer for a good 25 to 30 minutes on a low heat stirring at intervals.\nTempering for sarson da saag\nIn another small pan, heat oil. Use any neutral oil. You can also make the tempering with ghee if you prefer.\nAdd the chopped onions and saute them till light brown on medium-low heat.\nAdd the prepared saag. Stir and simmer for a couple of minutes.\nStir ocaasionally when the saag is simmering.\nServing Suggestions\nServe sarson ka saag hot with a side of some chopped onions, whole green chilies or mango pickle. Top the saag with a dollop of white butter and serve with Makki di Roti. Also serve a few jaggery cubes by the side.\nFor a vegan saag, omit adding white butter or use vegan butter.\nStorage\nStore the pureed and simmered saag in an airtight container for 4 to 5 days in the refrigerarot. You can also freeze it for a month.\nWhen ready to serve, remove the quantity you need from the refrigerator and temper it with the required amout of oil and onions.""",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.92, self.harvester_class.ratings())
