# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.themagicalslowcooker import TheMagicalSlowCooker
from tests import ScraperTest


class TestTheMagicalSlowCookerScraper(ScraperTest):

    scraper_class = TheMagicalSlowCooker
    test_file_name = "themagicalslowcooker_2"

    def test_host(self):
        self.assertEqual("themagicalslowcooker.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Sarah Olson", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Slow Cooker Pork Roast with Gravy", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Main Course", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(510, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.themagicalslowcooker.com/wp-content/uploads/2023/02/crockpot-pork-pot-roast-4.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "4 lbs. boneless pork shoulder",
                "¼ cup brown sugar",
                "1 tsp. onion powder",
                "1 tsp. garlic powder",
                "1 tsp. mustard powder",
                "1 tsp. dried thyme",
                "½ tsp. salt",
                "½ tsp. black pepper",
                "2 Tbsp. olive oil",
                "1 lb baby carrots",
                "1 lb red potatoes (Quartered)",
                "1 large yellow onion (Quartered)",
                "6 cloves garlic",
                "1 cup chicken broth",
                "2 Tbsp. apple cider vinegar",
                "1 Tbsp. dijon mustard",
                "2 Tbsp. cornstarch",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "4 lbs. boneless pork shoulder",
                        "¼ cup brown sugar",
                        "1 tsp. onion powder",
                        "1 tsp. garlic powder",
                        "1 tsp. mustard powder",
                        "1 tsp. dried thyme",
                        "½ tsp. salt",
                        "½ tsp. black pepper",
                        "2 Tbsp. olive oil",
                    ],
                    purpose="For the pork/pork rub",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 lb baby carrots",
                        "1 lb red potatoes (Quartered)",
                        "1 large yellow onion (Quartered)",
                        "6 cloves garlic",
                        "1 cup chicken broth",
                        "2 Tbsp. apple cider vinegar",
                        "1 Tbsp. dijon mustard",
                    ],
                    purpose="For the vegetables/cooking liquid",
                ),
                IngredientGroup(
                    ingredients=["2 Tbsp. cornstarch"],
                    purpose="To make the gravy",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Using paper towels, pat dry the pork shoulder and set aside. In a small bowl, mix together the brown sugar, onion powder, granulated garlic, mustard powder, thyme, salt and pepper. Rub the spice mixture on all sides of the pork roast.\nHeat a large skillet over medium high heat, drizzle on the olive oil and sear the pork roast on all sides, about 2-3 minutes per side.\nTo the slow cooker pot, add the carrots, potatoes, onion, and garlic to the bottom of the pot. Place the seared pork roast over the vegetables.\nIn a small bowl, whisk together the chicken stock, apple cider vinegar and dijon mustard. Pour over the pork roast and put the lid on the slow cooker.\nCook on HIGH for 4-6 hours or LOW for 8-10 hours. The pork is done when very tender and easily shreddable.\nWhen done, transfer the cooking liquid to a 4 quart stock pot and heat over medium on the stove top.\nMix the 2 Tbsp of cornstarch with 2 Tbsp of the cooking liquid and whisk it into the stock pot on the stove. Continuous stirring until the gravy has thickened.\nTransfer the pork roast and vegetables to a serving platter, shred the pork into larger pieces and serve with the gravy. Enjoy",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Pork is so flavorful; why not make a pot roast dinner with it?! The recipe has everything you need from the meat, vegetables and even the gravy.",
            self.harvester_class.description(),
        )
