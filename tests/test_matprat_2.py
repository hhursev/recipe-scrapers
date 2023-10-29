from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.matprat import Matprat
from tests import ScraperTest


class TestMatprat(ScraperTest):
    scraper_class = Matprat
    test_file_name = "matprat_2"

    def test_host(self):
        self.assertEqual("matprat.no", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.matprat.no/oppskrifter/sunn/mangosalat/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Mangosalat")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "MatPrat")

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://images.matprat.no/5qallzq3pg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 stk. modne mango",
                "0,5 stk. rødløk",
                "1 rød chili",
                "0,5 pk ruccula",
                "1 stk. lime",
                "0,5 bunt frisk koriander",
                "0,5 potte frisk mynte",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        return self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "2 stk. modne mango",
                        "0,5 stk. rødløk",
                        "1 rød chili",
                        "0,5 pk ruccula",
                        "1 stk. lime",
                        "0,5 bunt frisk koriander",
                        "0,5 potte frisk mynte",
                    ],
                    purpose=None,
                )
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Skrell og del mango i små terninger. Kutt rødløk i syltynne skiver og finhakk chili.\nBland sammen mangobiter, rødløk, chili og ruccola i en vid bolle. Press over limesaft og press over limesaft.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.85, self.harvester_class.ratings())

    def test_nutrients(self):
        self.assertEqual(
            {
                "Energi": "281 kcal",
                "Fett": "11,5 g",
                "Protein": "6,3 g",
                "Karbohydrater": "38,15 g",
                "Jern": "1,1 mg",
            },
            self.harvester_class.nutrients(),
        )
