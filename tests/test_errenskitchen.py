# mypy: allow-untyped-defs

from recipe_scrapers.errenskitchen import ErrensKitchen
from tests import ScraperTest


class TestErrensKitchenScraper(ScraperTest):
    scraper_class = ErrensKitchen

    def test_host(self):
        self.assertEqual("errenskitchen.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.errenskitchen.com/chicken-sundried-tomato-pasta/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Erren Hart", self.harvester_class.author())

    def test_category(self):
        self.assertEqual("Dinner", self.harvester_class.category())

    def test_cuisine(self):
        self.assertEqual("Italian", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "A delectable dish of Creamy Sun-Dried Tomato Pasta with Chicken flavored with Parmesan cheese, sun-dried tomatoes, onions, and garlic.",
            self.harvester_class.description(),
        )

    def test_image(self):
        self.assertEqual(
            "https://www.errenskitchen.com/wp-content/uploads/2022/05/Chicken-Sundried-Tomato-Pasta-06.jpg",
            self.harvester_class.image(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_title(self):
        self.assertEqual(
            "Creamy Sun-Dried Tomato Pasta with Chicken", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_ingredients(self):
        expected_ingredients = [
            "1 tablespoon olive oil",
            "2 lbs boneless chicken thighs (or breasts, cubed)",
            "1 onion (chopped)",
            "¼ cup sun-dried tomatoes (drained and chopped)",
            "2 tablespoons sun-dried tomato paste",
            "3 garlic cloves (minced)",
            "¾ cup chicken stock",
            "¾ cup freshly grated Parmesan cheese",
            "1½ cups half and half (or whipping cream)",
            "1 pound pasta",
            "1 tablespoon fresh basil (chopped)",
            "Salt and pepper to taste",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = "\n".join(
            [
                "Pat the chicken meat dry with paper towels. Cut it into evenly cut bite-sized pieces and season well with salt and pepper.",
                "In a large pot, start a pot of salted water to cook the pasta.",
                "While waiting for the water to boil, heat the olive oil in a large skillet over medium heat. Add the cubed chicken, seasoned with salt and pepper, and cook until golden brown and thoroughly cooked. Once done, set the chicken aside.",
                "Use the same skillet to sauté the chopped onion until it becomes soft and translucent. Follow this by adding the chopped sun-dried tomatoes, sun-dried tomato paste, and minced garlic, cooking for an additional minute.",
                "Mix in the chicken stock half and half, and freshly grated Parmesan cheese. Stir to combine the ingredients and bring the mixture to a boil. Lower the heat to low, and simmer for 5 to 10 minutes to reduce and thicken.",
                "Meanwhile, cook the pasta in the boiling water, making sure to undercook it by about 2-3 minutes less than the package instructions for al dente pasta. Remember to reserve a cup of the pasta water before draining.",
                "Drain the slightly undercooked pasta and add it directly into the skillet containing the sauce. Mix the pasta well into the sauce, gradually adding the reserved pasta water until the sauce reaches your desired thickness.",
                "Finally, add the cooked chicken back into the skillet, stirring it into the mixture. Allow everything to simmer together for a few minutes until the pasta is fully cooked and has absorbed some of the flavorful sauce (adding pasta water if necessary to loosen).",
                "Taste for seasoning and season the pasta with salt and pepper as needed. Serve right away.",
            ]
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())
