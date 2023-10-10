# mypy: allow-untyped-defs
from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.foodfidelity import FoodFidelity
from tests import ScraperTest


class TestFoodFidelity(ScraperTest):
    scraper_class = FoodFidelity
    test_file_name = "foodfidelity_groups"

    def test_host(self):
        self.assertEqual("foodfidelity.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.foodfidelity.com/citrus-israeli-couscous/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            "Citrus Israeli Couscous Salad With Asparagus and Cranberries",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual("Side Dish", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.foodfidelity.com/wp-content/uploads/2018/05/citrus-couscous.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 cup water",
                "2/3 cup orange juice",
                "1 1/3 cups pearl couscous",
                "1 cups sliced red onion",
                "1 clove garlic",
                "3 Tbsp white sugar",
                "1 Tbsp salt",
                "1/2 tsp peppercorns",
                "1 cup white vinegar",
                "1 pound asparagus trimmed",
                "3 tablespoons extra-virgin olive oil",
                "Kosher salt and freshly ground black pepper",
                "1 lemon",
                "1 cup white wine",
                "1 cup dried cranberries",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Couscous Instructions\nIn a medium saucepan, heat 1 tablespoon of the olive oil.\nAdd the couscous and cook over moderate heat, stirring, until lightly golden, about 3 minutes.\nAdd water and orange juice, cover and cook over low heat until the couscous is tender and all of the liquid is absorbed, about 10 minutes.\nTransfer the couscous to a bowl. Stir in the remaining ingredients, season with salt and pepper, garnish with fresh herbs and serve.\nRed Onions Instructions\nThinly slice the red onion and peel the garlic. Place the onion and garlic in a large glass.\nAdd the sugar, salt, and peppercorns to a small sauce pan. Add the vinegar and stir until the sugar and salt are dissolved. Place a lid on the pot and bring the mixture up to a boil over medium-high heat.\nOnce boiling, pour the vinegar over the sliced onion and garlic. Press the onion down so all the pieces are submerged, then let the mixture cool to room temperature.\nTransfer the onions and vinegar mixture to a lidded glass jar for storage in the refrigerator. The onions can be stored in the refrigerator for 3-4 weeks.\nGrilled Asparagus Instructions\nPreheat grill for high heat.\nLightly coat the asparagus spears with olive oil. Season with salt and pepper to taste.\nGrill over high heat for 2 to 3 minutes, or to desired tenderness. Drizzle with lemon juice.\nWine Soaked Cranberries Instructions\nPut the cranberries in a jar. Bring the wine to a boil in a small saucepan. Pour over the cranberries and let cool to room temperature. Let stand for 30 minutes, or cover and refrigerate for up to 1 month.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_author(self):
        self.assertEqual("Marwin Brown", self.harvester_class.author())

    def test_description(self):
        self.assertEqual(
            "Israeli couscous cooked in orange juice broth and topped with pickled red onions, grilled asparagus, and plump, juicy poached cranberries. #isrealicouscous #pearlcouscous #couscous #sidedish #easterrecipes #sidedish #dinner #foodfidelity www.foodfidelity.com",
            self.harvester_class.description(),
        )

    def test_ingredient_groups(self):
        return self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 cup water",
                        "2/3 cup orange juice",
                        "1 1/3 cups pearl couscous",
                    ],
                    purpose="Couscous Ingredients",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 cups sliced red onion",
                        "1 clove garlic",
                        "3 Tbsp white sugar",
                        "1 Tbsp salt",
                        "1/2 tsp peppercorns",
                        "1 cup white vinegar",
                    ],
                    purpose="Pickled red onions Ingredients",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 pound asparagus trimmed",
                        "3 tablespoons extra-virgin olive oil",
                        "Kosher salt and freshly ground black pepper",
                        "1 lemon",
                    ],
                    purpose="Grilled asparagus Ingredients",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 cup white wine",
                        "1 cup dried cranberries",
                    ],
                    purpose="Wine soaked cranberries Ingredients",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )
