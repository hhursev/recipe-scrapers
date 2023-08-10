from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.realfoodtesco import RealFoodTesco
from tests import ScraperTest


class TestRealFoodTescoScraper2(ScraperTest):
    scraper_class = RealFoodTesco
    test_file_name = "realfoodtesco_2"
    maxDiff = None

    def test_host(self):
        self.assertEqual("realfood.tesco.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Tesco Real Food", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "BBQ cauliflower steaks and herb sauce", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(22, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://realfood.tesco.com/media/images/RFO-1400x919-CauliflowerSteaks-9b3cfef8-bc5e-4d41-b25b-1341fa3db1e0-0-1400x919.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "2 cauliflowers, outer leaves removed",
                        "6 tbsp extra virgin olive oil",
                        "1 tsp caraway seeds",
                        "2 garlic cloves, crushed",
                    ],
                    purpose=None,
                ),
                IngredientGroup(
                    ingredients=[
                        "30g fresh basil, finely chopped",
                        "30g fresh parsley, finely chopped",
                        "3 spring onions, trimmed and finely chopped",
                        "1 green chilli, finely chopped",
                        "1-2 lemons",
                    ],
                    purpose="For the herb sauce",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Preheat the barbecue. Trim the base of the cauliflowers so that they sit flat, then cut into 2cm-thick slices (see Tip, below).
In a small bowl, mix together 3 tbsp of the oil with the caraway seeds and garlic. Season, then brush the oil all over the cauliflower steaks.
Cook on the preheated barbecue, away from the main heat, for 5-6 mins on each side until charred and just tender. Alternatively, cook the steaks (2 at a time, depending on their size) in a griddle pan over a medium-low heat for the same time.
Meanwhile, mix together the chopped herbs, spring onions, chilli and remaining 3 tbsp of oil in a small bowl. Squeeze in the juice of ½ a lemon and taste – add a little more lemon juice or oil to taste. Season.
Drizzle the herb sauce over the steaks and serve with the remaining lemon cut into wedges.""",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
