from recipe_scrapers.halfbakedharvest import HalfBakedHarvest
from tests import ScraperTest


class TestHalfBakedHarvestScraper(ScraperTest):

    scraper_class = HalfBakedHarvest

    def test_host(self):
        self.assertEqual("halfbakedharvest.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.halfbakedharvest.com/brown-butter-corn-and-feta-orzo/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Brown Butter Corn and Feta Orzo with Crispy Prosciutto",
        )

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.halfbakedharvest.com/wp-content/uploads/2020/07/Brown-Butter-Corn-and-Feta-Orzo-with-Crispy-Prosciutto-1-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 pound dry orzo pasta",
                "3 ounces prosciutto, torn",
                "4 tablespoon salted butter",
                "2 tablespoons extra virgin olive oil",
                "1 shallot, finely chopped",
                "1 jalapeño, seeded if desired, and chopped",
                "2 tablespoons fresh thyme leaves",
                "2 tablespoons fresh lemon juice",
                "2 tablespoons champagne or apple cider vinegar",
                "2 teaspoons honey",
                "1/2 cup fresh basil, roughly chopped",
                "1/4 cup fresh chopped chives",
                "4 ears grilled or steamed corn, kernels removed from the cobb",
                "2 cups cherry tomatoes, halved",
                "8 ounces crumbled feta cheese",
                "2 avocados, sliced",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            """1. Bring a large pot of salted water to a boil. Boil the pasta to al dente, according to package directions. Drain and add the pasta right back to the pot. 2. Meanwhile, cook the prosciutto in a large skillet set over medium heat until crispy, about 2 minutes per side. Remove the prosciutto from the skillet. 3. To the skillet, add the butter. Allow the butter to brown until it smells toasted and is a deep golden color, about 3-4 minutes. Stir in the olive oil, shallot, jalapeño, and thyme. Cook 1-2 minutes, then remove from the heat. Pour the browned butter over the hot orzo. Toss to combine. 4. To the orzo, add the basil, chives, lemon juice, vinegar, and honey. Season with salt and pepper and toss. Stir in the corn, tomatoes, and feta. Top the pasta with crispy prosciutto and avocado. Serve warm or at room temp.""",
            self.harvester_class.instructions(),
        )
