from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.nytimes import NYTimes
from tests import ScraperTest


class TestNYTimesScraper(ScraperTest):
    scraper_class = NYTimes
    test_file_name = "nytimes_groups"

    def test_host(self):
        self.assertEqual("cooking.nytimes.com", self.harvester_class.host())

    def test_image(self):
        self.assertEqual(
            "https://static01.nyt.com/images/2023/07/14/multimedia/14EVERYDAY-VEGETABLESrex1-pvqb/14EVERYDAY-VEGETABLESrex1-pvqb-mediumSquareAt3X.jpg",
            self.harvester_class.image(),
        )

    def test_canonical_url(self):
        self.assertEqual(
            "https://cooking.nytimes.com/recipes/1024397-crispy-potato-tacos",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Crispy Potato Tacos", self.harvester_class.title())

    def test_author(self):
        self.assertEqual("Hetty Lui McKinnon", self.harvester_class.author())

    def test_ratings(self):
        self.assertEqual(4.0, self.harvester_class.ratings())

    def test_total_time(self):
        self.assertEqual(75, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "Sea salt",
                "1 1/2 pounds potatoes (any variety), scrubbed and cut into 1 1/2-inch pieces",
                "1 1/2 cups grated Cheddar",
                "Handful of cilantro, leaves and stems finely chopped",
                "1 small garlic clove, finely chopped",
                "1 teaspoon ground cumin",
                "1 teaspoon paprika",
                "16 to 18 corn tortillas",
                "Neutral oil, as needed",
                "Any combination of sliced lettuce or cabbage, very finely sliced red onion or sour cream (all optional), for serving",
                "3 tomatoes (about 1 pound), chopped",
                "1/2 red onion, roughly chopped",
                "Small handful of cilantro, leaves and stems roughly chopped",
                "1 fresh serrano or Fresno chile (seeded, if you prefer less spice)",
                "1 garlic clove, chopped",
                "1 teaspoon ground cumin",
                "1 teaspoon dried oregano",
                "1 teaspoon granulated sugar",
                "Sea salt",
                "3/4 cup vegetable stock",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_goups(self):
        return self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "Sea salt",
                        "1 1/2 pounds potatoes (any variety), scrubbed and cut into 1 1/2-inch pieces",
                        "1 1/2 cups grated Cheddar",
                        "Handful of cilantro, leaves and stems finely chopped",
                        "1 small garlic clove, finely chopped",
                        "1 teaspoon ground cumin",
                        "1 teaspoon paprika",
                        "16 to 18 corn tortillas",
                        "Neutral oil, as needed",
                        "Any combination of sliced lettuce or cabbage, very finely sliced red onion or sour cream (all optional), for serving",
                    ],
                    purpose="For the Tacos",
                ),
                IngredientGroup(
                    ingredients=[
                        "3 tomatoes (about 1 pound), chopped",
                        "1/2 red onion, roughly chopped",
                        "Small handful of cilantro, leaves and stems roughly chopped",
                        "1 fresh serrano or Fresno chile (seeded, if you prefer less spice)",
                        "1 garlic clove, chopped",
                        "1 teaspoon ground cumin",
                        "1 teaspoon dried oregano",
                        "1 teaspoon granulated sugar",
                        "Sea salt",
                        "3/4 cup vegetable stock",
                    ],
                    purpose="For the Spicy Red Salsa",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Bring a large saucepan of salted water to a boil. Add the potatoes and cook for 15 to 20 minutes, until tender. (Check them by inserting a fork or knife into the largest potato piece. If it goes in and out easily, the potato is ready.) Drain and allow to cool for a few minutes.\nMake the spicy red salsa: Place tomatoes, onion, cilantro, chile, garlic, cumin, oregano, sugar and 1 teaspoon salt into a blender or food processor and blitz until completely smooth. Pour the purée into a saucepan, add the vegetable stock and bring to a boil. Reduce the heat to low and simmer for 15 to 20 minutes until darker in color and slightly thickened, while you prepare the remaining ingredients.\nPlace the cooled potatoes in a bowl and roughly mash them. (It does not have to be smooth; a chunky texture is great.) Add the Cheddar, cilantro, garlic, cumin, paprika and 1 teaspoon sea salt and mix to combine.\nPlace a large skillet over medium-high heat and, working in batches, add the corn tortillas and heat until soft and pliable. Remove from the pan and cover the tortillas with a clean kitchen towel to keep them warm. Fill each warmed tortilla with 1 to 2 tablespoons of the potato mixture, then fold in half and press down lightly.\nIn the same skillet, add enough oil to cover the bottom of the pan and warm over medium-high heat. Place three or four tacos in the oil, pressing down lightly with a spatula so that the edges are in the oil, and fry for 1 to 2 minutes, until golden and crispy. Flip them over and repeat on the other side. Repeat with the remaining tacos.\nServe the tacos with the spicy red salsa and any of the optional serving suggestions. (The potatoes can be cooked and mashed 2 days ahead and stored in an airtight container in the fridge. The salsa can be made 2 days ahead and kept in the fridge. For freezing info, see Tip.)",
            self.harvester_class.instructions(),
        )


# https://cooking.nytimes.com/recipes/1024397-crispy-potato-tacos
