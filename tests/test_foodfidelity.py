# mypy: allow-untyped-defs

from recipe_scrapers.foodfidelity import FoodFidelity
from tests import ScraperTest


class TestFoodFidelityScraper(ScraperTest):

    scraper_class = FoodFidelity

    def test_host(self):
        self.assertEqual("foodfidelity.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.foodfidelity.com/strawberry-oatmeal/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Marwin Brown", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Strawberry Oatmeal with Orange Juice", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Breakfast", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(7, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.foodfidelity.com/wp-content/uploads/2020/06/stovetop-Orange-juice-oatmeal-w-strawberries-tight-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 cup Old-Fashioned Oats",
                "1/2 tbsp Clarified Butter (Ghee or regular unsalted butter)",
                "1 pinch salt",
                "1 cup Orange Juice",
                "1 cup Almond Milk",
                "1/2 cup Strawberries",
                "1 tbsp Honey",
                "1/2 tsp Orange Zest",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Heat sauce pan over medium heat. Add ghee and then toast the oats for 1-2 minutes.\nAdd the orange juice, salt, almond milk, and oats then cook according to package directions (bring to a boil then simmer for 5 minutes).\nMix in the honey then top with the strawberry. Add zest and serve.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Creamy strawberry oatmeal recipe featuring old-fashioned oats cooked in almond-milk and orange juice based broth then topped with fresh strawberries for a totally not boring breakfast. #oatmeal #oatmealrecipes #strawberryoatmeal #breakfast #healthystart",
            self.harvester_class.description(),
        )
