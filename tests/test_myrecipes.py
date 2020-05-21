from tests import ScraperTest

from recipe_scrapers.myrecipes import MyRecipes


class TestMyRecipesScraper(ScraperTest):

    scraper_class = MyRecipes

    def test_host(self):
        self.assertEqual("myrecipes.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Cacio e Pepe")

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '6 oz. bucatini pasta',
                '1 1/2 tsp. kosher salt, divided',
                '3 Tbsp. olive oil',
                '1 tsp. black pepper, plus more for garnish',
                '1 1/2 oz. pecorino Romano, grated (about 3/4 cups), plus more for garnish',
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\nAdd pasta to a large skillet over high; cover with water, and add 1 teaspoon of the salt. Bring to a boil, and cook, stirring occasionally, until nearly tender, about 6 minutes.\nMeanwhile, heat oil in a medium skillet over medium; stir in black pepper, and cook until toasted, about 1 minute. Remove from heat.\nWhisk 3 tablespoons of the pasta cooking water into oil and pepper. Using tongs, transfer pasta into oil and pepper mixture, reserving pasta cooking water in skillet. Cook over low, stirring constantly, while sprinkling in cheese.\nAdd more cooking water as needed, 1 tablespoon at a time, to create a creamy sauce. Stir in remaining 1/2 teaspoon salt. Divide pasta between 2 bowls, and garnish with pepper and cheese. Serve immediately.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())
