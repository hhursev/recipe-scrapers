from recipe_scrapers.skinnytaste import SkinnyTaste
from tests import ScraperTest


class TestSkinnyTasteScraper(ScraperTest):

    scraper_class = SkinnyTaste

    def test_host(self):
        self.assertEqual("skinnytaste.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.skinnytaste.com/grilled-chicken-with-spinach-and-melted/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Grilled Chicken with Spinach and Melted Mozzarella",
        )

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.skinnytaste.com/wp-content/uploads/2011/03/Grilled-Chicken-with-Spinach-and-Melted-Mozzarella-10.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "24 oz 3 large chicken breasts sliced in half lengthwise to make 6",
                "kosher salt and pepper to taste",
                "1 tsp olive oil",
                "3 cloves garlic (crushed)",
                "10 oz frozen spinach (drained)",
                "3 oz shredded part skim mozzarella",
                "1/2 cup roasted red pepper (sliced in strips (packed in water))",
                "olive oil spray",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            """Preheat oven to 400°F. Season chicken with salt and pepper. Lightly spray a grill or grill pan with oil. Cook chicken until no longer pink, about 2 to 3 minutes per side.
Heat a skillet over medium heat. Add oil and garlic, sauté a 30 seconds, add spinach, salt and pepper. Cook until heated through, 2 to 3 minutes.
Place chicken on a baking sheet, divide spinach evenly between the 6 pieces and place on top. Top each with 1/2 oz mozzarella, roasted peppers and bake until melted, about 3 minutes.""",
            self.harvester_class.instructions(),
        )

    def test_total_time(self):
        self.assertEqual(
            17,
            self.harvester_class.total_time(),
        )

    def test_ratings(self):
        self.assertEqual(
            5,
            self.harvester_class.ratings(),
        )
