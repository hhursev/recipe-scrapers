from recipe_scrapers.onehundredonecookbooks import OneHundredOneCookBooks
from tests import ScraperTest


class TestOneHundredOneCookBooksScraper(ScraperTest):
    scraper_class = OneHundredOneCookBooks

    def test_host(self):
        self.assertEqual("101cookbooks.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Heidi Swanson", self.harvester_class.author())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.101cookbooks.com/broccoli-soup-with-coconut-milk/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            "Broccoli Soup with Coconut Milk", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_cook_time(self):
        self.assertEqual(10, self.harvester_class.cook_time())

    def test_prep_time(self):
        self.assertEqual(10, self.harvester_class.prep_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://images.101cookbooks.com/coconut_broccoli_soup.jpg?w=1200&auto=format",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 14- ounce can of full fat coconut milk",
                "3 cloves garlic, smashed",
                "1 large yellow onion, chopped",
                "1 small serrano chile, stemmed and chopped",
                "2 teaspoons fine grain sea salt",
                "4 1/2 cups water",
                "2-3 large heads of broccoli (~1 1/2 lb.), cut into small florets",
                "2-3 large handfuls of spinach",
                "to serve: lots of pan-fried tofu cubes, toasted almonds, scallions, chive flowers (optional)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Scoop a big spoonful of thick coconut cream from the top of the coconut milk can. Add it to a large pan over medium-high heat. When hot, stir in the garlic, onions, chile, and salt. Sauté for a couple minutes, just long enough for everything to soften up.\nAdd the remaining coconut milk, and the water, and bring to a simmer before adding the broccoli and spinach. Simmer just long enough for the broccoli to get tender throughout, 2 - 4 minutes.\nImmediately remove the soup from heat and puree with an immersion blender. Add more water if you feel the need to thin the soup out. Taste and add more salt if needed.\nServe sprinkled with tofu cubes, toasted almonds, and lots of scallions.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_nutrients(self):
        self.assertEqual(
            {
                "calories": "143 kcal",
                "carbohydrateContent": "9 g",
                "proteinContent": "4 g",
                "fatContent": "12 g",
                "saturatedFatContent": "10 g",
                "sodiumContent": "629 mg",
                "fiberContent": "3 g",
                "sugarContent": "2 g",
                "unsaturatedFatContent": "2 g",
                "servingSize": "1 serving",
            },
            self.harvester_class.nutrients(),
        )

    def test_description(self):
        self.assertEqual(
            "This broccoli soup with coconut milk is so good and super easy. It's a simple broccoli and spinach affair made with a coconut milk broth a topped with good stuff like pan-fried tofu croutons, toasted almonds, and shredded scallions. Time to break out your blender.",
            self.harvester_class.description(),
        )

    def test_cuisine(self):
        self.assertEqual(
            "California,Easy,Vegan,Vegetarian", self.harvester_class.cuisine()
        )
