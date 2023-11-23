# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.carlsbadcravings import CarlsBadCravings
from tests import ScraperTest


class TestCarlsBadCravingsScraper(ScraperTest):
    scraper_class = CarlsBadCravings
    test_file_name = "carlsbadcravings_2"

    def test_host(self):
        self.assertEqual("carlsbadcravings.com", self.harvester_class.host())

    def canonical_url(self):
        self.assertEqual(
            "https://carlsbadcravings.com/easy-cranberry-pistachio-cheese-log/",
            self.harvester_class.host(),
        )

    def test_author(self):
        self.assertEqual("Jen", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Easy Cranberry Pistachio Cheese Log", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_image(self):
        self.assertEqual(
            "https://carlsbadcravings.com/wp-content/uploads/2017/11/christmas-2.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 1/4 cups fresh cranberries",
                "1 cup shelled roasted, salted pistachios",
                "7-8 oz. goat cheese log or tub",
                "4 oz. cream cheese, softened",
                "2 tablespoons honey",
                "1/4 tsp EACH ground ginger, ground cinnamon, salt, dried thyme, dried rosemary",
                "1/8 teaspoon pepper",
                "1/2 cup Cranberry Pistachio Coating mixture ((in directions))",
                "honey",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 1/4 cups fresh cranberries",
                        "1 cup shelled roasted, salted pistachios",
                    ],
                    purpose="Cranberry Pistachio Coating",
                ),
                IngredientGroup(
                    ingredients=[
                        "7-8 oz. goat cheese log or tub",
                        "4 oz. cream cheese, softened",
                        "2 tablespoons honey",
                        "1/4 tsp EACH ground ginger, ground cinnamon, salt, dried thyme, dried rosemary",
                        "1/8 teaspoon pepper",
                        "1/2 cup Cranberry Pistachio Coating mixture ((in directions))",
                    ],
                    purpose="Cheese Log",
                ),
                IngredientGroup(
                    ingredients=["honey"],
                    purpose="Garnish",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Add cranberries and pistachios to your food processor and chop into small pieces (but don't over-process). Remove ½ cup and add it to a medium bowl. Add all remaining Goat Cheese Log ingredients to the bowl and stir to combine.",
                    "Add this cheese mixture to a large piece of plastic wrap, and form into the shape of a log. Wrap in plastic wrap. Freezer for 20-30 minutes. We want the cheese log slightly firm so it holds its shape but is still soft enough for the Coating to be pressed into it.",
                    "Line counter with about a large piece parchment paper. Add Coating ingredients to parchment and spread into a single layer square a little larger than the length of the cheese log. Add cheese log to the edge of the Coating and roll in Coating (see photos) until evenly coated, pressing coating into the cheese so it sticks. The cheese log can be refrigerated at this point until ready to serve or serve immediately.",
                    "When ready to serve, remove from refrigerator 15 minutes beforehand so it can soften. Drizzle generously with honey just before serving. Serve with crackers.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_yields(self):
        self.assertEqual("16 servings", self.harvester_class.yields())

    def test_description(self):
        self.assertEqual(
            "10 Minute prep creamy, sweet and tangy Cranberry Pistachio Cheese Log is the EASIEST yet most impressive appetizer you will ever make! This festive goat cheese log can be made DAYS in advance so it’s the perfect stress-free appetizer for Thanksgiving, Christmas or any holiday party!",
            self.harvester_class.description(),
        )
