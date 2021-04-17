import os

from recipe_scrapers._exceptions import SchemaOrgException
from recipe_scrapers.myrecipes import MyRecipes
from tests import ScraperTest


class TestMyRecipesScraper(ScraperTest):

    scraper_class = MyRecipes

    def test_host(self):
        self.assertEqual("myrecipes.com", self.harvester_class.host())

    def test_image(self):
        self.assertEqual(
            "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fcdn-image.myrecipes.com%2Fsites%2Fdefault%2Ffiles%2Fstyles%2F4_3_horizontal_-_1200x900%2Fpublic%2Fmyrecipestrending_1-09-18_1772_1.jpg%3Fitok%3DL_jRbjls%261516215251",
            self.harvester_class.image(),
        )

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.myrecipes.com/recipe/cacio-e-pepe",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Cacio e Pepe")

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual(
            "Serves 2 (serving size: 1 1/2 cups)", self.harvester_class.yields()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "6 oz. bucatini pasta",
                "1 1/2 tsp. kosher salt, divided",
                "3 Tbsp. olive oil",
                "1 tsp. black pepper, plus more for garnish",
                "1 1/2 oz. pecorino Romano, grated (about 3/4 cups), plus more for garnish",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Add pasta to a large skillet over high; cover with water, and add 1 teaspoon of the salt. Bring to a boil, and cook, stirring occasionally, until nearly tender, about 6 minutes. Meanwhile, heat oil in a medium skillet over medium; stir in black pepper, and cook until toasted, about 1 minute. Remove from heat. Whisk 3 tablespoons of the pasta cooking water into oil and pepper. Using tongs, transfer pasta into oil and pepper mixture, reserving pasta cooking water in skillet. Cook over low, stirring constantly, while sprinkling in cheese. Add more cooking water as needed, 1 tablespoon at a time, to create a creamy sauce. Stir in remaining 1/2 teaspoon salt. Divide pasta between 2 bowls, and garnish with pepper and cheese. Serve immediately.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())

    def test_ratings_raises_exception(self):
        os.environ["RECIPE_SCRAPERS_SETTINGS"] = "recipe_scrapers.settings.default"
        with self.assertRaises(SchemaOrgException):
            self.assertEqual(None, self.harvester_class.ratings())


# https://www.myrecipes.com/recipe/cacio-e-pepe
