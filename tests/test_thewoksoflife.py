from recipe_scrapers.thewoksoflife import Thewoksoflife
from tests import ScraperTest


class TestThewoksoflifeScraper(ScraperTest):

    scraper_class = Thewoksoflife

    def test_host(self):
        self.assertEqual("thewoksoflife.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://thewoksoflife.com/whole-wheat-mantou/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "The Perfect Whole Wheat Mantou Recipe"
        )

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://thewoksoflife.com/wp-content/uploads/2018/01/whole-wheat-mantou-9-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 \u2154 cups warm milk ((400 ml))",
                "1 teaspoon active dry yeast ((3 grams))",
                "1 tablespoon sugar ((12 grams))",
                "2 \u00be cups all-purpose flour ((400 grams))",
                "1\u00bc to 1\u00bd cups whole wheat flour ((about 170-200 grams; how much you\u2019ll need is dependent on the humidity in your kitchen))",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions_list(self):
        self.assertEqual(
            [
                "Heat the milk until warm to the touch (not hot). Then stir in the yeast and sugar until it dissolves. Combine the milk mixture with 2 ¾ cups of all-purpose flour in a large mixing bowl. The mixture will be wet. Cover with a damp cloth and let proof in a warm spot for 1-2 hours until the mixture doubles in size. Since it’s winter, I let the dough proof near a heat vent!",
                "Now mix in the whole wheat flour, a quarter cup at a time, until the dough is smooth, soft, pliable, and not sticky. Cover the dough, and let it rest for 20 minutes.",
                "Now, prepare your steamer with cold water. Make sure the water doesn’t touch the mantou during steaming. Brush the steam rack with a bit of vegetable oil, or prepare 12 small (3” x 3”) squares of parchment paper to prevent the mantou from sticking to the steam rack.",
                "Now knead the dough and divide it into 12 equal pieces using a kitchen scale. Form each piece into a ball. You can also roll the dough into a long tube and cut it into 12 equal pieces. Space the mantou out on a steaming rack about 1-inch apart. You will need 2-3 racks, or you can steam them in a few separate batches.",
                "Let the mantou rest in the steamer for 30-45 minutes until the dough doubles in size before turning your stove on to high to start the steaming process. Steam for 15 minutes using high heat, then turn off the heat, and wait 5 minutes before opening the lid to check your mantou. The last step will ensure your mantou come out full and smooth! Otherwise, they will collapse and look lumpy.",
                "You can enjoy these mantou immediately or store them in a plastic bag after they’ve cooled completely. They will last about a week in the refrigerator, or you can freeze them. To reheat, I usually steam them for about 8-10 minutes. Microwaving for 30-60 seconds also works!",
            ],
            self.harvester_class.instructions_list(),
        )
