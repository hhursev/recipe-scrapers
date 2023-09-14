from recipe_scrapers.myrecipes import MyRecipes
from tests import ScraperTest


class TestMyRecipesScraper(ScraperTest):

    scraper_class = MyRecipes

    def test_host(self):
        self.assertEqual("myrecipes.com", self.harvester_class.host())

    def test_image(self):
        self.assertEqual(
            "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F19%2F2018%2F01%2F25%2Fmyrecipestrending_1-09-18_1772_1-2000.jpg",
            self.harvester_class.image(),
        )

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.myrecipes.com/recipe/cacio-e-pepe",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Cacio e Pepe")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Adam Dolge")

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 items", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "6 ounces bucatini pasta",
                "1 ½ teaspoons kosher salt, divided",
                "3 tablespoons olive oil",
                "1 teaspoon black pepper, plus more for garnish",
                "1 ½ ounces pecorino Romano, grated (about 3/4 cups), plus more for garnish",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Add pasta to a large skillet over high; cover with water, and add 1 teaspoon of the salt. Bring to a boil, and cook, stirring occasionally, until nearly tender, about 6 minutes.",
                    "Meanwhile, heat oil in a medium skillet over medium; stir in black pepper, and cook until toasted, about 1 minute. Remove from heat.",
                    "Whisk 3 tablespoons of the pasta cooking water into oil and pepper. Using tongs, transfer pasta into oil and pepper mixture, reserving pasta cooking water in skillet. Cook over low, stirring constantly, while sprinkling in cheese.",
                    "Add more cooking water as needed, 1 tablespoon at a time, to create a creamy sauce. Stir in remaining 1/2 teaspoon salt. Divide pasta between 2 bowls, and garnish with pepper and cheese. Serve immediately.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings_raises_exception(self):
        self.assertEqual(3.0, self.harvester_class.ratings())


# https://www.myrecipes.com/recipe/cacio-e-pepe
