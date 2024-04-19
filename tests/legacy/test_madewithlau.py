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
                "12 oz Thai jasmine rice (uncooked)",
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
            + "Add the rice and water to the rice cooker pot. Place the pot in the cooker, then activate it.\n"
            + "When the rice is cooked, use chopsticks to fluff the grains and release the steam.\n"
            + "Dice the green onions, using both the green and white parts.\n"
            + "Wash the ginger (if needed), then cut into thin slices. Lay the down slices and cut them into strips.\n"
            + "Wash the lettuce. Peel off leaves and stack them on top of each other, then cut into thin strips.\n"
            + "Cut the chicken into slices. Turn them 90 degrees, then cut into small 1/2- inch cubes. Place the chicken in a bowl.\n"
            + "Add the oyster sauce, white pepper, cornstarch, and water to the bowl.Mix to thoroughly combine.\n"
            + "Cut off head of the salted fish and save for use in other recipes, if preferred.\n"
            + "Use kitchen shears to trim off the dorsal fins on the back of the fish.\n"
            + "Rinse the fish in water, then pat dry with a paper towel.\n"
            + "It's time to debone the fish. Using a small knife, cut out the main spine and bones, separating into two halves if necessary. You can use the bones in other recipes.\n"
            + "(Chef's Tip: For safety, lay the fish down on the cutting board and use your knife to gently pry out any bones.)\n"
            + "Once all the bones have been removed, cut the fish into 1/4-inch thick strips. Rotate 90 degrees and dice into pea-sized pieces.\n"
            + "Crack the eggs into bowl.\n"
            + "Heat a wok on high, then add the oil.\n"
            + "Beat the eggs and add to wok, stir frying for 20 to 30 seconds. Remove and set aside.\n"
            + "Add more oil (0.32 tablespoon) to the hot wok.",
            self.harvester_class.instructions(),
        )

    def test_ingredient_groups(self):
        return self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "12 oz Thai jasmine rice (uncooked)",
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
