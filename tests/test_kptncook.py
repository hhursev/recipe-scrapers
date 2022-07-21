import responses

from recipe_scrapers.kptncook import KptnCook
from tests import ScraperTest


class TestKptnCookScraper(ScraperTest):

    scraper_class = KptnCook

    @property
    def expected_requests(self):
        yield responses.GET, "https://mobile.kptncook.com/recipe/pinterest/Low-Carb-Tarte-Flamb%C3%A9e-with-Serrano-Ham-%26-Cream-Cheese/315c3c32?lang=en", "tests/test_data/kptncook.testhtml"
        yield responses.POST, "https://mobile.kptncook.com/recipes/search?kptnkey=6q7QNKy-oIgk-IMuWisJ-jfN7s6&lang=en", "tests/test_data/kptncook.testjson"

    def test_host(self):
        self.assertEqual("mobile.kptncook.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual(
            "Laura (http://lauraleanskitchen.com/de/)", self.harvester_class.author()
        )

    def test_title(self):
        self.assertEqual(
            "Low Carb Tarte Flambée with Serrano Ham & Cream Cheese",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual("Pork", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_prep_time(self):
        self.assertEqual(20, self.harvester_class.prep_time())

    def test_cook_time(self):
        self.assertEqual(5, self.harvester_class.cook_time())

    def test_yields(self):
        self.assertEqual(1, self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://d2am1qai33sroc.cloudfront.net/image/59b8e8a6950000a90949a083?kptnkey=6q7QNKy-oIgk-IMuWisJ-jfN7s6",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        ingredients = [
            "1.0 egg",
            "0.5 cup(s) cream cheese / curd cheese",
            "salt",
            "pepper",
            "2.0 tbsp cream cheese",
            "2.0 slice(s) serrano ham",
            "0.5 cup(s) arugula",
            "0.5 cup(s) cherry tomato",
            "0.5 tsp herbes de Provence, dried",
            "0.25 tsp chili flake",
        ]
        self.assertEqual(ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        instructions = "All set?\nPreheat oven to 360°F (conventional, recommended) or 325°F (fan).\nMix curd, eggs, chili flakes, herbes de Provence, salt, and pepper to a bowl and mix.\nPlace the mass on a lined baking sheet, spread thinly (make sure the layer is very thin) and bake for 10-15 min.\nWash and slice cherry tomatoes.\nWash and drain arugula.\nRemove the base from the oven and spread with cream cheese. Top with tomatoes and Serrano ham, and bake for another 5 min.\nRemove the tarte flambée from the oven, top with arugula, and enjoy."
        self.assertEqual(instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Flourless but so delicious!", self.harvester_class.description()
        )

    def test_language(self):
        self.assertEqual("en", self.harvester_class.language())

    def test_nutrients(self):
        self.assertEqual(
            {"calories": 368, "protein": 34, "fat": 22, "carbohydrate": 9},
            self.harvester_class.nutrients(),
        )

    def test_canonical_url(self):
        self.assertEqual(
            "https://mobile.kptncook.com/recipe/pinterest/Low-Carb-Tarte-Flamb%C3%A9e-with-Serrano-Ham-%26-Cream-Cheese/315c3c32?lang=en",
            self.harvester_class.canonical_url(),
        )
