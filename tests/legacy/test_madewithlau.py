from responses import GET

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.madewithlau import MadeWithLau
from tests.legacy import ScraperTest


class TestMadeWithLauScraper(ScraperTest):
    scraper_class = MadeWithLau

    @classmethod
    def expected_requests(cls):
        yield GET, "https://www.madewithlau.com/recipes/salted-fish-chicken-fried-rice", "tests/legacy/test_data/madewithlau.testhtml"
        yield GET, "https://www.madewithlau.com/api/trpc/recipe.bySlug?input=%7B%22json%22%3A+%7B%22slug%22%3A+%22salted-fish-chicken-fried-rice%22%7D%7D", "tests/legacy/test_data/madewithlau.testjson"

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.madewithlau.com/recipes/salted-fish-chicken-fried-rice",
            self.harvester_class.canonical_url(),
        )

    def test_host(self):
        self.assertEqual("madewithlau.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Salted Fish and Chicken Fried Rice (鹹魚雞粒炒飯)",
        )

    def test_description(self):
        self.assertEqual(
            "This classic Cantonese fried rice is a restaurant favorite—here's how to recreate it at home with tips from an expert chef.",
            self.harvester_class.description(),
        )

    def test_image(self):
        self.assertEqual(
            "https://cdn.sanity.io/images/2r0kdewr/production/8780473204dc219733935ace16299db745863380-1000x668.jpg",
            self.harvester_class.image(),
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Made With Lau")

    def test_category(self):
        self.assertEqual("Main Course, Dinner", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "12 oz Thai jasmine rice",
                "10 oz water",
                "1 oz green onions",
                "0.5 oz ginger",
                "3 oz lettuce",
                "4 oz chicken breast",
                "2 oz salted fish",
                "2 large eggs",
                "2 tablespoon oil",
                "0.25 teaspoon white pepper",
                "2 teaspoon fish sauce",
                "1 tablespoon oyster sauce",
                "0.125 teaspoon white pepper",
                "1 teaspoon cornstarch",
                "1 tablespoon water",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Wash the rice 2 to 3 times with clean water, draining out the water each time.\n"
            + "Add the rice and water to the rice cooker pot. Place the pot  in the cooker, then activate it.\n"
            + "When the rice is cooked, use chopsticks to fluff the grains and release the steam.\n",
            self.harvester_class.instructions(),
        )

    def test_ingredient_groups(self):
        return self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "12 oz Thai jasmine rice",
                        "10 oz water",
                        "1 oz green onions",
                        "0.5 oz ginger",
                        "3 oz lettuce",
                        "4 oz chicken breast",
                        "2 oz salted fish",
                        "2 large eggs",
                        "2 tablespoon oil",
                        "0.25 teaspoon white pepper",
                        "2 teaspoon fish sauce",
                    ],
                    purpose="Main Ingredients",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 tablespoon oyster sauce",
                        "0.125 teaspoon white pepper",
                        "1 teaspoon cornstarch",
                        "1 tablespoon water",
                    ],
                    purpose="Marinade Ingredients",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )
