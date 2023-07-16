from recipe_scrapers.kitchenstories import KitchenStories
from tests import ScraperTest


class TestKitchenStoriesScraper(ScraperTest):

    scraper_class = KitchenStories

    def test_host(self):
        self.assertEqual("kitchenstories.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            "Special strawberry jam with matcha", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Jams & Marmalades", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(80, self.harvester_class.total_time())

    def test_cook_time(self):
        self.assertEqual(0, self.harvester_class.cook_time())

    def test_prep_time(self):
        self.assertEqual(20, self.harvester_class.prep_time())

    def test_image(self):
        self.assertEqual(
            "https://images.kitchenstories.io/wagtailOriginalImages/R2630-photo-final-1.jpg",
            self.harvester_class.image(),
        )

    def test_nutrients(self):
        self.assertEqual(
            {
                "calories": "359 cal",
                "carbohydrateContent": "91 g",
                "fatContent": "1 g",
                "proteinContent": "2 g",
                "servingSize": "1 Servings",
            },
            self.harvester_class.nutrients(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1.75 lbs strawberries",
                "1.5 cups jam sugar",
                "1 tsp matcha powder",
                "0.33 cup water",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Place a small plate in the freezer. Wash the strawberries and cut them into quarters. In a large pot, combine the jam sugar and strawberries, stirring until well combined. Let that sit for approx. 1 hr.\nIn the meantime, mix the matcha powder with half of the water in a small bowl to make a paste. Gradually stir in the remaining water until everything is well mixed and dissolved. Set aside.\nAfter the strawberries have rested and there's some juice in the pot, set the pot over medium heat and bring to a simmer. Cook for approx. 5 min., then add the matcha to the pot and continue cooking for approx. 1 min.\nTo test whether the jam will set up once it's cooled, place a small spoonful of the hot jam on the plate from the freezer and hold the plate at an angle. If the mass becomes solid after a short time and you can swipe your finger through the jam leaving an unconnected gap, the test is passed and the jam is ready; if not, continue cooking and repeating the test. Pour the still hot jam into sterilized preserving jars, seal, and let cool. Enjoy!",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(1.0, self.harvester_class.ratings())

    def test_author(self):
        self.assertEqual("Christian Ruß", self.harvester_class.author())

    def test_cuisine(self):
        self.assertEqual("International", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "This recipe gives homemade strawberry jam an exciting update: Matcha!",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("en", self.harvester_class.language())
