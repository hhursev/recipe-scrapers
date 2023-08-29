# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.livelytable import LivelyTable
from tests import ScraperTest


class TestLivelyTableScraper(ScraperTest):

    scraper_class = LivelyTable
    test_file_name = "livelytable_2"

    def test_host(self):
        self.assertEqual("livelytable.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Kaleigh", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Easy Chipotle Shrimp Tacos", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("main dish", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://livelytable.com/wp-content/uploads/2017/05/chipotle-shrimp-tacos-225x225.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1 lb raw large shrimp, peeled and deveined",
            "1/2 tsp chipotle powder",
            "1/2 tsp garlic powder",
            "1/2 tsp ground cumin",
            "1 tbsp olive or avocado oil",
            "Juice from 1/2 lime",
            "1/2 jalapeño, seeded and diced",
            "1/4 cup cilantro leaves",
            "2/3 cup nonfat plain greek yogurt",
            "Juice from 1/2 lime",
            "6 corn tortillas, warmed",
            "Shredded purple cabbage",
            "Cilantro",
            "Crumbled cotija cheese",
            "Lime wedges",
            "Guacamole or diced avocado",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 lb raw large shrimp, peeled and deveined",
                        "1/2 tsp chipotle powder",
                        "1/2 tsp garlic powder",
                        "1/2 tsp ground cumin",
                        "1 tbsp olive or avocado oil",
                        "Juice from 1/2 lime",
                    ],
                    purpose=None,
                ),
                IngredientGroup(
                    ingredients=[
                        "1/2 jalapeño, seeded and diced",
                        "1/4 cup cilantro leaves",
                        "2/3 cup nonfat plain greek yogurt",
                        "Juice from 1/2 lime",
                    ],
                    purpose="For the cilantro jalapeño sauce:",
                ),
                IngredientGroup(
                    ingredients=[
                        "6 corn tortillas, warmed",
                        "Shredded purple cabbage",
                        "Cilantro",
                        "Crumbled cotija cheese",
                        "Lime wedges",
                        "Guacamole or diced avocado",
                    ],
                    purpose="For serving:",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = (
            "Place shrimp in a medium, nonreactive bowl.\n"
            "In a small bowl, combine chipotle, garlic powder, and cumin. Sprinkle over shrimp. Add oil and lime juice and stir well until shrimp are evenly coated. Set aside while you prepare the cilantro jalapeño sauce.\n"
            "In a food processor or blender, combine jalapeño, cilantro, yogurt, and lime juice. Process until smooth and pour into a small bowl for serving.\n"
            "Prepare remaining taco toppings.\n"
            "Heat a large non-stick skillet over medium heat. Add shrimp and cook about 3 minutes per side or until cooked through.\n"
            "Serve with warm corn tortillas and top as desired. Enjoy!"
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())
