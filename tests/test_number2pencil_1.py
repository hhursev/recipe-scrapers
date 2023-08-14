# mypy: allow-untyped-defs

from recipe_scrapers.number2pencil import Number2Pencil
from tests import ScraperTest


class TestNumber2PencilScraper(ScraperTest):

    scraper_class = Number2Pencil
    test_file_name = "number2pencil_1"

    def test_host(self):
        self.assertEqual("number-2-pencil.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Melissa", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Sheet Pan Shrimp Fajitas", self.harvester_class.title())

    def test_category(self):
        self.assertEqual(
            "Dinner, One Sheet Pan, Recipes, Shrimp", self.harvester_class.category()
        )

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.number-2-pencil.com/wp-content/uploads/2016/09/Sheet-Pan-Shrimp-Fajitas_-6.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 1/2 pounds shrimp (peeled and deveined)",
                "1 yellow bell pepper (sliced thin)",
                "1 red bell pepper (sliced thin)",
                "1 orange bell pepper (sliced thin)",
                "1 small red onion (sliced thin)",
                "1 1/2 tablespoons extra virgin olive oil",
                "1 teaspoon kosher salt",
                "several turns of freshly ground pepper",
                "2 teaspoon chili powder",
                "1/2 teaspoon garlic powder",
                "1/2 teaspoon onion powder",
                "1/2 teaspoon ground cumin",
                "1/2 teaspoon smoked paprika",
                "lime",
                "fresh cilantro for garnish",
                "tortillas (warmed)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Preheat oven to 450 degrees.\nIn a large bowl, combine onion, bell pepper, shrimp, olive oil, salt and pepper and spices.\nToss to combine.\nSpray baking sheet with non stick cooking spray.\nSpread shrimp, bell peppers and onions on baking sheet.\nCook at 450 degrees for about 8 minutes. Then turn oven to broil and cook for additional 2 minutes or until shrimp is cooked through.\nSqueeze juice from fresh lime over fajita mixture and top with fresh cilantro.\nServe in warm tortillas.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.96, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "This shrimp fajita recipe is seriously so easy and delicious! All you have to do is scoop the juicy shrimp, tender bell pepper and onions into a soft warm tortilla for a super fast and easy weeknight dinner!",
            self.harvester_class.description(),
        )
