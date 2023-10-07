from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.domesticateme import DomesticateMe
from tests import ScraperTest


class TestDomesticateMeScraper(ScraperTest):

    scraper_class = DomesticateMe
    test_file_name = "domesticateme_2"

    def test_host(self):
        self.assertEqual("domesticate-me.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            self.harvester_class.canonical_url(),
            "https://domesticate-me.com/summer-squash-toast/",
        )

    def test_author(self):
        self.assertEqual("Serena Wolf", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Summer Squash Toasts with Sun-Dried Tomato White Bean Spread",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual(
            "Breakfast,Recipes,Summer,Vegetarian", self.harvester_class.category()
        )

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://domesticate-me.com/wp-content/uploads/2018/08/Summer-Squash-Toast-5.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1 tablespoon extra-virgin olive oil",
            "2 medium zucchini (diced small)",
            "1 medium summer squash (diced small)",
            "Kosher salt",
            "¼-½ teaspoon crushed red pepper flakes (depending on how much heat you like)",
            "4 large eggs",
            "4 large slices of bread (I recommend sourdough or a seeded loaf)",
            "Chopped chives for garnish (optional)",
            "One 15-ounce can cannellini beans (drained and rinsed)",
            "1/3 cup sun-dried tomatoes packed in extra-virgin olive oil (drained, patted dry, and roughly chopped)",
            "1 large garlic clove (peeled and smashed)",
            "1 tablespoon balsamic vinegar",
            "Kosher salt",
            "Freshly ground black pepper",
            "3 tablespoons olive oil from the sun-dried tomato jar",
            "3-4 tablespoons water",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = (
            "Add the cannellini beans, sun-dried tomatoes, garlic, balsamic, and a good pinch of salt to the bowl of a food processor. Process for about a minute until relatively smooth (some small pieces of tomato are fine), scraping down the sides of the bowl a few times if necessary. With the processor running, slowly add the olive oil and process until well incorporated. Add the water one tablespoon at a time until the spread is smooth and spreadable. Season with extra salt and freshly ground black pepper to taste. Briefly set aside.\n"
            "Heat the olive oil in a large skillet over high heat. When the oil is hot and shimmering (but not smoking!), add the zucchini, summer squash, a large pinch of salt, and crushed red pepper. Cook for about 4 minutes, shaking the pan occasionally, or until the squash is just tender and browned in spots. Transfer to a bowl and cover with foil to keep warm while you cook the eggs.\n"
            "Poach or fry the eggs, depending on your preference.\n"
            "While the eggs are cooking, toast (or grill!) the bread.\n"
            "Assembly the toasts: Spread each piece of toast with a thick layer of sun-dried tomato white bean spread. Top with cooked squash and an egg. Garnish with chives and extra salt and fresh ground pepper if you like, and serve immediately."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 tablespoon extra-virgin olive oil",
                        "2 medium zucchini (diced small)",
                        "1 medium summer squash (diced small)",
                        "Kosher salt",
                        "¼-½ teaspoon crushed red pepper flakes (depending on how much heat you like)",
                        "4 large eggs",
                        "4 large slices of bread (I recommend sourdough or a seeded loaf)",
                        "Chopped chives for garnish (optional)",
                    ],
                    purpose=None,
                ),
                IngredientGroup(
                    ingredients=[
                        "One 15-ounce can cannellini beans (drained and rinsed)",
                        "1/3 cup sun-dried tomatoes packed in extra-virgin olive oil (drained, patted dry, and roughly chopped)",
                        "1 large garlic clove (peeled and smashed)",
                        "1 tablespoon balsamic vinegar",
                        "Kosher salt",
                        "Freshly ground black pepper",
                        "3 tablespoons olive oil from the sun-dried tomato jar",
                        "3-4 tablespoons water",
                    ],
                    purpose="For the spread:",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )
