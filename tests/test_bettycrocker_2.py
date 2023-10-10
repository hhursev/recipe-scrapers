from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.bettycrocker import BettyCrocker
from tests import ScraperTest


class TestBettyCrocker(ScraperTest):

    scraper_class = BettyCrocker
    test_file_name = "bettycrocker_2"

    def test_host(self):
        self.assertEqual("bettycrocker.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.bettycrocker.com/recipes/strawberry-pretzel-salad/376aa27c-19a2-4114-9c80-20a431fc269b",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Jessica Walker", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Strawberry-Pretzel Salad", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(400, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://images-gmi-pmc.edge-generalmills.com/6ec084f7-ffd9-4df2-8302-877825ecc321.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "2 packages (4-serving size each) Jell-O® strawberry-flavored gelatin",
            "2 cups boiling water",
            "2 boxes (16 oz each) frozen sweetened strawberries, thawed",
            "2 cups pretzels, crushed",
            "3/4 cup butter, melted",
            "3 tablespoons sugar",
            "1 container (8 oz) Cool Whip frozen whipped topping, thawed",
            "1 package (8 oz) cream cheese, softened",
            "1 cup sugar",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "2 packages (4-serving size each) Jell-O® strawberry-flavored gelatin",
                        "2 cups boiling water",
                        "2 boxes (16 oz each) frozen sweetened strawberries, thawed",
                    ],
                    purpose="Topping",
                ),
                IngredientGroup(
                    ingredients=[
                        "2 cups pretzels, crushed",
                        "3/4 cup butter, melted",
                        "3 tablespoons sugar",
                    ],
                    purpose="Crust",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 container (8 oz) Cool Whip frozen whipped topping, thawed",
                        "1 package (8 oz) cream cheese, softened",
                        "1 cup sugar",
                    ],
                    purpose="Filling",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Dissolve gelatin in boiling water. Stir in strawberries; refrigerate until partially set, about 1 hour 45 minutes.",
                    "Heat oven to 350° F. In medium bowl, mix Crust ingredients. Press into ungreased 13 x 9-inch baking dish. Bake 10 minutes. Cool on cooling rack.",
                    "In medium bowl, beat Filling ingredients with electric mixer on medium speed until smooth. Spread over cooled crust. Cover and refrigerate until cool and gelatin topping in bowl is partially set.",
                    "Carefully spoon gelatin topping over filling. Refrigerate 4 to 6 hours or until firm. To serve, cut into 4 rows by 3 rows.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.5, self.harvester_class.ratings())
