from responses import GET

from recipe_scrapers.woolworths import Woolworths
from tests.legacy import ScraperTest


class TestWoolworthsScraper(ScraperTest):
    scraper_class = Woolworths

    @classmethod
    def expected_requests(cls):
        yield GET, "https://www.woolworths.com.au/shop/recipes/smoothie-fruit-cubes", "tests/legacy/test_data/woolworths.testhtml"
        yield GET, "https://foodhub.woolworths.com.au/content/woolworths-foodhub/en/smoothie-fruit-cubes.model.json", "tests/legacy/test_data/woolworths.testjson"

    def test_host(self):
        self.assertEqual("woolworths.com.au", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.woolworths.com.au/shop/recipes/smoothie-fruit-cubes",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Fresh Ideas", self.harvester_class.author())

    def test_category(self):
        self.assertEqual("Drinks", self.harvester_class.category())

    def test_title(self):
        self.assertEqual(
            "Smoothie Fruit Cubes Recipe | Woolworths",
            self.harvester_class.title(),
        )

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_prep_time(self):
        self.assertEqual(15, self.harvester_class.prep_time())

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://foodhub.scene7.com/is/image/woolworthsltdprod/fi-2401-smoothie-fruit-cubes:Square-1300x1300",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "300g fruit of choice (see tip)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            (
                "Place fruit in a blender and blitz until smooth. Transfer to a small jug.\n"
                "Pour mixture equally into a 12-hole (1 tbs-/20ml-capacity) ice-cube tray and freeze for 6 hours or overnight until set.\n"
                "Transfer cubes to an airtight container and store in the freezer until required. (Once ready to use, place cubes in a blender with yoghurt and milk, then blitz until smooth.)"
            ),
            self.harvester_class.instructions(),
        )

    def test_cuisine(self):
        self.assertEqual("Australian", self.harvester_class.cuisine())

    def test_cook_time(self):
        self.assertEqual(None, self.harvester_class.cook_time())

    def test_nutrients(self):
        self.assertEqual(
            {
                "calories": "6 calories",
                "carbohydrateContent": "1.1 grams",
                "fatContent": "0.1 grams",
                "fiberContent": "0.2 grams",
                "proteinContent": "0.2 grams",
                "sodiumContent": "10 milligrams",
                "sugarContent": "1.1 grams",
            },
            self.harvester_class.nutrients(),
        )

    def test_language(self):
        self.assertEqual("en-AU", self.harvester_class.language())

    def test_site_name(self):
        self.assertEqual(
            "Woolworths | Fresh Ideas For You", self.harvester_class.site_name()
        )
