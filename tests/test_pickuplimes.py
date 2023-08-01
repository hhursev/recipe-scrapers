# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.pickuplimes import PickUpLimes
from tests import ScraperTest


class TestPickUpLimesScraper(ScraperTest):
    scraper_class = PickUpLimes

    def test_host(self):
        self.assertEqual("pickuplimes.com", self.harvester_class.host())

    def test_site_name(self):
        self.assertEqual("Pick Up Limes", self.harvester_class.site_name())

    def test_author(self):
        self.assertEqual("Pick Up Limes", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            'Vegan "Honey" Mustard Tofu Wraps', self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Main", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_cook_time(self):
        self.assertEqual(10, self.harvester_class.cook_time())

    def test_prep_time(self):
        self.assertEqual(20, self.harvester_class.prep_time())

    def test_yields(self):
        self.assertEqual("5 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cdn.pickuplimes.com/cache/8e/5b/8e5b4da2c59d5acde583334469ed79bf.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "15.873 oz firm tofu",
                "¼ cup cornstarch",
                "2 Tbsp cold water",
                "sodium-reduced soy sauce",
                "⅔ cup panko breadcrumbs",
                "2 Tbsp nutritional yeast flakes",
                "½ tsp garlic powder",
                "½ tsp smoked sweet paprika powder",
                "2 Tbsp vegetable oil",
                "⅓ cup maple syrup",
                "⅓ cup dijon mustard",
                "¼ cup vegan mayonnaise",
                "apple cider vinegar",
                "¼ tsp salt",
                "1 cup shredded red cabbage",
                "1 cup shredded green cabbage",
                "1 carrot",
                "5 large soft tortilla",
                "½ head butter lettuce",
                "2 medium tomato",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "15.873 oz firm tofu",
                        "¼ cup cornstarch",
                        "2 Tbsp cold water",
                        "sodium-reduced soy sauce",
                        "⅔ cup panko breadcrumbs",
                        "2 Tbsp nutritional yeast flakes",
                        "½ tsp garlic powder",
                        "½ tsp smoked sweet paprika powder",
                        "2 Tbsp vegetable oil",
                    ],
                    purpose="Tofu tenders",
                ),
                IngredientGroup(
                    ingredients=[
                        "⅓ cup maple syrup",
                        "⅓ cup dijon mustard",
                        "¼ cup vegan mayonnaise",
                        "apple cider vinegar",
                        "¼ tsp salt",
                    ],
                    purpose="Honey mustard",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 cup shredded red cabbage",
                        "1 cup shredded green cabbage",
                        "1 carrot",
                        "5 large soft tortilla",
                        "½ head butter lettuce",
                        "2 medium tomato",
                    ],
                    purpose="Assembly",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Cut the tofu into 3-inch x ½ inch (8 cm x 1 cm) sticks.\nIn a medium bowl, mix together the cornstarch, water and soy sauce.\nIn another bowl, mix together the breadcrumbs, nutritional yeast, garlic and paprika powders.\nDip the tofu sticks in the wet mixture, and then into the breadcrumbs to coat. Transfer to a plate.\nHeat a large pan over medium-high heat and add the oil. Cook the tofu for 1 - 2 minutes on each side, or until golden on all sides.\nMix together the maple syrup and mustard in a medium bowl.\nUse a silicone pastry brush to coat each cooked tofu strip in the maple-mustard sauce.\nMix the leftover maple-mustard sauce together with the mayo, vinegar and salt.\nAdd the shredded cabbage and carrot to the bowl with the mustard sauce and mix together.\nAssemble the wraps by filling each tortilla with lettuce, tomato, cabbage mix and tofu tenders.\nFold and roll up like a burrito. Then toast them in a pan if desired and enjoy!",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.8, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "These wraps are not only visually appealing but also full of surprising flavours. We prepare our own crunchy tofu strips, sweet and tangy honey mustard sauce, and vegan coleslaw. Paired with a medley of fresh and crisp vegetables, you've got yourself a wrap that's nothing short of perfection!",
            self.harvester_class.description(),
        )
