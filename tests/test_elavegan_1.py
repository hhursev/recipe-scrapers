# mypy: allow-untyped-defs

from recipe_scrapers.elavegan import ElaVegan
from tests import ScraperTest


class TestElaVeganScraper(ScraperTest):
    scraper_class = ElaVegan
    test_file_name = "elavegan_1"

    def test_host(self):
        self.assertEqual("elavegan.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://elavegan.com/red-lentil-dahl/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Ela", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Red Lentil Dahl", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Dinner", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://elavegan.com/wp-content/uploads/2019/10/Red-Lentil-Dhal-with-rice.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 1/2 cups dry red lentils",
                "1 large carrot (finely diced (see notes))",
                "1 small bell pepper",
                "1 large onion (chopped)",
                "4 cloves of garlic (minced)",
                "1 heaped tbsp fresh ginger (minced)",
                "1/2 tbsp vegetable oil",
                "3 cups vegetable broth (or water)",
                "1 cup canned coconut milk ((see notes))",
                "1 1/2 tsp ground cumin",
                "1 tbsp curry powder",
                "1/2 tbsp sweetener of choice",
                "1 tsp ground turmeric",
                "1 tsp paprika",
                "Sea salt and black pepper (to taste)",
                "1/3 tsp red pepper flakes ((optional))",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        expected_instructions = [
            "You can watch the short video for visual instructions.Rinse lentils under running water. Chop the onion, garlic, ginger, bell pepper, and carrot.\nHeat oil in a pot and sauté onion for about 3-4 minutes over medium heat. Add ginger, garlic, carrot, and bell pepper.",
            "Add all spices, sweetener, lentils, and vegetable broth or water. Bring to a boil and let simmer for about 10 minutes.",
            "Finally, add coconut milk and cook for a further 5 minutes or until the desired thickness of the dahl is reached.",
            "Season with black pepper and salt. Taste and adjust the seasonings as needed.",
            "Serve warm with basmati rice, potatoes, or naan (flatbread) and garnish with fresh herbs.",
        ]
        expected_instructions = "\n".join(expected_instructions)
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(4.95, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Indian", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "This easy, creamy red lentil dahl (masoor dal curry) is frugal, hearty, comforting, flavorful, packed with plant-based protein, and ready in just 30 minutes! Serve with home-cooked rice and naan bread for a gluten-free, dairy-free Indian-inspired feast!",
            self.harvester_class.description(),
        )
