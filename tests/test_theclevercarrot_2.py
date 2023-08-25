from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.theclevercarrot import TheCleverCarrot
from tests import ScraperTest


class TestTheCleverCarrotScraper(ScraperTest):

    scraper_class = TheCleverCarrot
    test_file_name = "theclevercarrot_2"

    def test_host(self):
        self.assertEqual("theclevercarrot.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("The Clever Carrot", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "dinner tonight: sweet chili shrimp stir-fry", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("3 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.theclevercarrot.com/wp-content/uploads/2012/12/IMG_1824-225x225.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        ingredients = [
            "1 lb. shrimp, cleaned and deveined",
            "1 garlic clove",
            "1/3 c. sweet chili sauce",
            "1 1/4 c. snow peas",
            "1 tbsp. olive oil",
            "1/2 tsp. sesame oil",
            "1/3 c. cashews, roughly chopped",
            "1 lime",
            "1 1/2 c. jasmine rice, uncooked (or another quick cooking variety)",
        ]
        self.assertEqual(ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = (
            "Grab a medium size pot and cook the rice according to the package instructions. Set aside.\n"
            "In a large, wide skillet warm the olive oil over moderate heat.\n"
            "Using a microplane, grate the garlic clove directly into the pan. Alternatively, you can mince the garlic instead. Saute until fragrant, about 30 seconds.\n"
            "Add the shrimp and saute until pink and cooked though, about 5 minutes depending on size. Remove from the pan.\n"
            "While the shrimp is cooking, trim the ends off of the snow peas. Cut each one into thirds, on a diagonal.\n"
            "Add the sesame oil to the pan and saute the snow peas until crisp tender, about 1-2 minutes.\n"
            "Return the shrimp to the pan and add the sweet chili sauce. Cook until warmed through. Add more chili sauce if necessary.\n"
            "Top each plate with some chopped cashews and fresh lime wedges to taste.\n"
            "Serve with jasmine rice."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 lb. shrimp, cleaned and deveined",
                        "1 garlic clove",
                        "1/3 c. sweet chili sauce",
                        "1 1/4 c. snow peas",
                        "1 tbsp. olive oil",
                        "1/2 tsp. sesame oil",
                    ],
                    purpose="Stir-fry",
                ),
                IngredientGroup(
                    ingredients=[
                        "1/3 c. cashews, roughly chopped",
                        "1 lime",
                    ],
                    purpose="Garnish",
                ),
                IngredientGroup(
                    ingredients=[
                        "1 1/2 c. jasmine rice, uncooked (or another quick cooking variety)",
                    ],
                    purpose="On the side",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_ratings(self):
        self.assertEqual(4.3, self.harvester_class.ratings())
