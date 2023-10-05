# mypy: allow-untyped-defs

from recipe_scrapers.bluejeanchef import BlueJeanChef
from tests import ScraperTest


class TestBlueJeanChefScraper(ScraperTest):

    scraper_class = BlueJeanChef
    test_file_name = "bluejeanchef_1"

    def test_host(self):
        self.assertEqual("bluejeanchef.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://bluejeanchef.com/recipes/chicken-tortilla-soup/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("theyadmin", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Chicken Tortilla Soup", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Entrées,Soups", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(22, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://bluejeanchef.com/uploads/2019/05/Chicken-Tortilla-Soup-1280-1205.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "2 tablespoons olive oil",
            "1 onion (finely diced (about 1 cup))",
            "2 cloves garlic (minced)",
            "1 Jalapeño pepper (minced or sliced into rings)",
            "1 red bell pepper (chopped)",
            "1 tablespoon chili powder",
            "1 teaspoon ground cumin",
            "28 ounces fire-roasted tomatoes (diced)",
            "3 cups good-quality or homemade unsalted chicken stock",
            "15 ounces canned black beans (drained and rinsed)",
            "15 ounces canned red kidney beans (drained and rinsed)",
            "1 teaspoons salt",
            "2 boneless skinless chicken breasts",
            "3 cups corn tortilla chips (broken into pieces)",
            "1 avocado (peeled and sliced)",
            "½ cup fresh cilantro leaves",
            "1 cup Cheddar cheese (grated)",
            "1 lime (cut into wedges)",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        updated_instructions = [
            "Pre-heat the pressure cooker using the BROWN or SAUTE setting.",
            "Add the olive oil. Sauté the onion for 3 to 4 minutes, stirring occasionally. Add the garlic, Jalapeño pepper, red pepper and spices, and cook for another minute or two. Add the tomatoes, chicken stock, beans and salt, give it a good stir and push the chicken breasts under the liquid. Lock the lid in place.",
            "Pressure cook on HIGH for 8 minutes.",
            "Reduce the pressure with QUICK-RELEASE method and carefully remove the lid. Remove the chicken to a side plate and when cool enough to touch, shred the chicken with two forks into small pieces.",
            "Return the chicken to the soup and season to taste with salt and freshly ground black pepper. Place some tortilla chips into each bowl and ladle the soup on top. Garnish with avocado, cilantro, Cheddar cheese and a lime wedge to squeeze.",
        ]
        self.assertEqual(
            "\n".join(updated_instructions), self.harvester_class.instructions()
        )

    def test_ratings(self):
        self.assertEqual(4.34, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Tex-Mex", self.harvester_class.cuisine())

    def test_description(self):
        expected_description = "It doesn’t happen very often in my house that I have any leftover or stale tortilla chips, but if you do…chicken tortilla soup is a great way to use them up. If you don't have leftover tortilla chips, this is still a great soup to make. In fact, it's even better to serve with some chips, salsa, guacamole and other toppings along side."
        self.assertEqual(expected_description, self.harvester_class.description())
