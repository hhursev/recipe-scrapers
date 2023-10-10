# mypy: allow-untyped-defs

from recipe_scrapers.barefootcontessa import BareFootContessa
from tests import ScraperTest


class TestBareFootContessaScraper(ScraperTest):

    scraper_class = BareFootContessa
    test_file_name = "barefootcontessa_1"

    def test_host(self):
        self.assertEqual("barefootcontessa.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://barefootcontessa.com/recipes/roasted-vegetable-lasagna",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Ina Garten", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Roasted Vegetable Lasagna | Recipes", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Dinner", self.harvester_class.category())

    def test_yields(self):
        self.assertEqual("10 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://d14iv1hjmfkv57.cloudfront.net/assets/recipes/roasted-vegetable-lasagna/_1200x630_crop_center-center_82_none/126-web-horizon.jpg?v=1696019460",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1½ pounds eggplant, unpeeled, sliced lengthwise ¼ inch thick",
            "¾ pound zucchini, unpeeled, sliced lengthwise ¼ inch thick",
            "⅔ cup good olive oil",
            "1 tablespoon dried oregano",
            "Kosher salt and freshly ground black pepper",
            "1 tablespoon minced garlic (3 cloves)",
            "10 ounces lasagna noodles, such as De Cecco",
            "16 ounces fresh whole-milk ricotta",
            "8 ounces creamy garlic and herb goat cheese, at room temperature",
            "2 extra-large eggs, lightly beaten",
            "½ cup chopped fresh basil leaves, lightly packed",
            "1 cup freshly grated Parmesan cheese, divided",
            "4½ cups good bottled marinara sauce, such as Rao’s (40 ounces)",
            "1 pound lightly salted fresh mozzarella, very thinly sliced",
        ]

        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = (
            "Preheat the oven to 375 degrees. Arrange the eggplant and zucchini in single layers on 3 sheet pans lined with parchment paper. Brush them generously with the olive oil on both sides, using all of the oil. Sprinkle with the oregano (I crush it in my hands), 1 tablespoon salt, and 1½ teaspoons pepper. Roast for 25 minutes, sprinkle the garlic evenly on the vegetables, and roast for another 5 minutes, until the vegetables are cooked through. Remove from the oven and lower the temperature to 350 degrees.\n"
            "Meanwhile, fill a very large bowl with the hottest tap water and add enough boiling water to bring the temperature to 140 degrees. One at a time, place the noodles in the water and soak them for 15 -minutes, swirling occasionally so they don’t stick together. Drain and slide the noodles around again.\n"
            "Combine the ricotta, goat cheese, eggs, basil, ½ cup of the Parmesan, 1½ teaspoons salt, and ¾ teaspoon pepper in the bowl of an electric mixer fitted with the paddle attachment and mix on low speed.\n"
            "Spread 1 cup of the marinara in a 9 × 13 × 2-inch baking dish. Arrange a third of the vegetables on top, then a layer of the noodles (cut to fit), a third of the mozzarella, and a third of the ricotta mixture in large dollops between the mozzarella. Repeat twice, starting with the marinara. Spread the last 1½ cups of marinara on top and sprinkle with the remaining ½ cup of Parmesan. Place the dish on a sheet pan lined with parchment paper and bake for 60 to 70 minutes, until the lasagna is browned and bubbly. Allow to rest for 10 minutes and serve hot."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())
