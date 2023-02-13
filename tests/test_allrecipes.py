from recipe_scrapers.allrecipes import AllRecipesCurated, AllRecipesUser
from tests import ScraperTest


class TestAllRecipesCuratedScraper(ScraperTest):

    scraper_class = AllRecipesCurated

    def test_host(self):
        self.assertEqual("allrecipes.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Michelle", self.harvester_class.author())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.allrecipes.com/recipe/133948/four-cheese-margherita-pizza/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Four Cheese Margherita Pizza")

    def test_description(self):
        self.assertEqual(
            self.harvester_class.description(),
            "This is a fantastic version of an Italian classic. The feta cheese adds a rich flavor that brings this dish to life. Incredibly easy and incredibly delicious!",
        )

    def test_cook_time(self):
        self.assertEqual(10, self.harvester_class.cook_time())

    def test_prep_time(self):
        self.assertEqual(15, self.harvester_class.prep_time())

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F694708.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                {"name": "olive oil", "quantity": 0.25, "unit": "cup"},
                {"name": "minced garlic", "quantity": 1.0, "unit": "tablespoon"},
                {"name": "sea salt", "quantity": 0.5, "unit": "teaspoon"},
                {
                    "name": "Roma tomatoes, sliced",
                    "quantity": 8.0,
                    "unit": "dimensionless",
                },
                {
                    "name": "(12 inch) pre-baked pizza crusts",
                    "quantity": 2.0,
                    "unit": "dimensionless",
                },
                {
                    "name": "shredded Mozzarella cheese",
                    "quantity": 8.0,
                    "unit": "ounce",
                },
                {"name": "shredded Fontina cheese", "quantity": 4.0, "unit": "ounce"},
                {
                    "name": "fresh basil leaves, washed, dried",
                    "quantity": 10.0,
                    "unit": "dimensionless",
                },
                {
                    "name": "freshly grated Parmesan cheese",
                    "quantity": 0.5,
                    "unit": "cup",
                },
                {"name": "crumbled feta cheese", "quantity": 0.5, "unit": "cup"},
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Stir together olive oil, garlic, and salt; toss with tomatoes, and allow to stand for 15 minutes. Preheat oven to 400 degrees F (200 degrees C).\nBrush each pizza crust with some of the tomato marinade. Sprinkle the pizzas evenly with Mozzarella and Fontina cheeses. Arrange tomatoes overtop, then sprinkle with shredded basil, Parmesan, and feta cheese.\nBake in preheated oven until the cheese is bubbly and golden brown, about 10 minutes.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.8, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("", self.harvester_class.cuisine())

    def test_category(self):
        self.assertEqual(
            "World Cuisine Recipes,European,Italian", self.harvester_class.category()
        )


class TestAllRecipesUserScraper(ScraperTest):

    scraper_class = AllRecipesUser

    def test_host(self):
        self.assertEqual("allrecipes.com/cook", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("AOSWALT", self.harvester_class.author())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.allrecipes.com/cook/1052065/recipe/78989010-fddc-3e4a-b54f-10e3ad110564",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Amy's Fabulous Meat Rub")

    def test_total_time(self):
        self.assertEqual(5, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("1 serving", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.allrecipes.com/img/misc/og-default.png",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                {"name": "white sugar", "quantity": 2.0, "unit": "tablespoon"},
                {"name": "brown sugar", "quantity": 1.0, "unit": "tablespoon"},
                {"name": "garlic powder", "quantity": 1.5, "unit": "teaspoon"},
                {"name": "chili powder", "quantity": 1.5, "unit": "teaspoon"},
                {"name": "paprika", "quantity": 1.5, "unit": "teaspoon"},
                {"name": "ground cumin", "quantity": 1.5, "unit": "teaspoon"},
                {"name": "salt", "quantity": 1.0, "unit": "teaspoon"},
                {"name": "onion powder", "quantity": 1.0, "unit": "teaspoon"},
                {"name": "ground black pepper", "quantity": 1.5, "unit": "teaspoon"},
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "In a small bowl, combine all ingredients. Rub down your choice of meat, and let marinate for at least an hour.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        return self.assertIsNone(self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_category(self):
        self.assertEqual(None, self.harvester_class.category())
