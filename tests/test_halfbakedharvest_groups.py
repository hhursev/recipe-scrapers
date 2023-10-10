import unittest

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.halfbakedharvest import HalfBakedHarvest
from tests import ScraperTest


class TestHalfBakedHarvestScraper(ScraperTest):
    scraper_class = HalfBakedHarvest
    test_file_name = "halfbakedharvest_groups"

    def test_host(self):
        self.assertEqual("halfbakedharvest.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.halfbakedharvest.com/street-corn-pasta-salad/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Street Corn Pasta Salad",
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "halfbakedharvest")

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.halfbakedharvest.com/wp-content/uploads/2023/08/Street-Corn-Pasta-Salad-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "4 ounces cream cheese, at room temperature",
                "1/3 cup sour cream",
                "2 tablespoons extra virgin olive oil",
                "1-2 cloves garlic, grated",
                "1 tablespoon chopped fresh chives",
                "kosher salt and black pepper",
                "3/4 cup crumbled cotija or feta cheese",
                "1 pound short cut pasta",
                "1 head romaine lettuce, shredded",
                "2 cups grilled or roasted corn ((3-4 raw))",
                "1/2 cup fresh basil leaves, torn",
                "1/2 cup fresh cilantro, chopped",
                "1/2 cup spicy cheddar cheese, cubed",
                "1 avocado, chopped",
                "4 tablespoons salted butter",
                "2 teaspoons smoked paprika",
                "2 tablespoons chili powder",
                "1/2-2 teaspoons cayenne pepper, to your taste",
                "1/4 cup mayo or yogurt",
                "2 tablespoons lime juice",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        return self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "4 ounces cream cheese, at room temperature",
                        "1/3 cup sour cream",
                        "2 tablespoons extra virgin olive oil",
                        "1-2 cloves garlic, grated",
                        "1 tablespoon chopped fresh chives",
                        "kosher salt and black pepper",
                        "3/4 cup crumbled cotija or feta cheese",
                    ],
                    purpose="Dressing",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 pound short cut pasta",
                        "1 head romaine lettuce, shredded",
                        "2 cups grilled or roasted corn ((3-4 raw))",
                        "1/2 cup fresh basil leaves, torn",
                        "1/2 cup fresh cilantro, chopped",
                        "1/2 cup spicy cheddar cheese, cubed",
                        "1 avocado, chopped",
                        "4 tablespoons salted butter",
                        "2 teaspoons smoked paprika",
                        "2 tablespoons chili powder",
                        "1/2-2 teaspoons cayenne pepper, to your taste",
                        "1/4 cup mayo or yogurt",
                        "2 tablespoons lime juice",
                    ],
                    purpose="Salad",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        return self.assertEqual(
            """1. To make the dressing. Combine all ingredients in a large salad bowl. Season with salt and pepper.2. Bring a pot of salted water to a boil. Boil the pasta to al dente, according to package directions. Drain. Immediately toss with the dressing. Add the lettuce, corn, cheddar, basil, cilantro, and avocado. Toss to combine. 3. In a skillet, melt the butter until golden. Mix in the chili powder, paprika, cayenne, and a pinch of salt. Cook another minute, then remove from the heat.4. Mix the mayo or yogurt with lime juice with a pinch of salt.5. Serve the pasta warm or cold, topped with lime mayo and chili butter. The salad will develop more flavor as it sits.""",
            self.harvester_class.instructions(),
        )

    @unittest.expectedFailure
    def test_multiple_instructions(self):
        # TODO: should this recipe in fact return multiple instructions?
        super().test_multiple_instructions()
