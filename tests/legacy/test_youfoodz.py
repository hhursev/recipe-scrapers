from responses import GET

from recipe_scrapers.youfoodz import Youfoodz
from tests.legacy import ScraperTest


class TestYoufoodz(ScraperTest):
    scraper_class = Youfoodz

    @classmethod
    def expected_requests(cls):
        yield GET, "https://www.youfoodz.com/recipes/nonnas-spaghetti-bolognese-with-italian-herbs-and-garlic-300g-660a602770e8f6aef4341177?week=2024-W19", "tests/legacy/test_data/youfoodz.testhtml"
        expected_headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTc1MDU0NjUsImlhdCI6MTcxNDg3NTcyMiwiaXNzIjoic2VuZiIsImp0aSI6ImQyZmVhZjMyLTk5N2MtNDliMy04NGIxLWZjYTNiOTFlMjM5NCJ9.Hx7E6HTxML10NiPsP9jZpZ17YzUOeqf9iiJx4yDJmcg"
        }
        yield GET, "https://www.youfoodz.com/gw/recipes/recipes/660a602770e8f6aef4341177", "tests/legacy/test_data/youfoodz.testjson", expected_headers

    def test_host(self):
        self.assertEqual("youfoodz.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Youfoodz", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Nonna's Spaghetti Bolognese with Italian Herbs & Garlic",
            self.harvester_class.title(),
        )

    def test_prep_time(self):
        self.assertEqual(None, self.harvester_class.prep_time())

    def test_total_time(self):
        self.assertEqual(None, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("1 serving", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://d3hvwccx09j84u.cloudfront.net/0,0/image/660a602770e8f6aef4341177-bd71d766.jpeg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            ["Bolognese Mince", "Spaghetti"], self.harvester_class.ingredients()
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Remove cardboard sleeve from tray.",
                    "Peel back corner of film.",
                    "Microwave on high for 3 min^ (or until hot).",
                    "Peel off film completely from tray. Enjoy!",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_cuisine(self):
        self.assertEqual("Italian", self.harvester_class.cuisine())

    def test_category(self):
        self.assertEqual("Beef", self.harvester_class.category())

    def test_ratings(self):
        self.assertEqual(0, self.harvester_class.ratings())

    def test_ratings_count(self):
        self.assertEqual(0, self.harvester_class.ratings_count())

    def test_description(self):
        self.assertEqual(
            "There’s nothing quite like a hearty serve of Spaghetti Bolognese. It’s packed with protein, veg and a generous serving of carbs, making this meal a top contender for your personalised meal plan. Our beef bolognese is made rich with juicy tomatoes, onion, garlic, carrot & red wine, cooked to perfection before being popped on top of al dente spaghetti.\n**Ingredients: ** Spaghetti (61%) (Durum Wheat), Bolognese Sauce (57%) (Beef Mince, Crushed Tomato (Tomato, Acid (330)), Tomato Paste (Acidity Regulator (330)), Carrot, Celery, Onion, Red Wine (Sulphites) (Preservative (220)), Garlic (1%), Beef Booster, Mushroom Booster (Flavour Enhancer (635), Acid (330)), Natural Flavour, Brown Sugar, Sweet Paprika, Italian Herbs, Black Pepper, Parsley, Salt).\nMade in Australia from at least 75% Australian Ingredients.",
            self.harvester_class.description(),
        )

    def test_nutrients(self):
        self.assertEqual(
            {
                "calories": "396kcal",
                "fatContent": "10.3g",
                "saturatedContent": "4.7g",
                "carbohydrateContent": "49.5g",
                "sugarContent": "9.1g",
                "fiberContent": "5.4g",
                "proteinContent": "25.6g",
                "sodiumContent": "822mg",
            },
            self.harvester_class.nutrients(),
        )

    def test_language(self):
        self.assertEqual("en-AU", self.harvester_class.language())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.youfoodz.com/recipes/nonnas-spaghetti-bolognese-with-italian-herbs-and-garlic-300g-660a602770e8f6aef4341177",
            self.harvester_class.canonical_url(),
        )
