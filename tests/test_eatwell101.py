# mypy: allow-untyped-defs

from recipe_scrapers.eatwell101 import EatWell101
from tests import ScraperTest


class TestEatWell101Scraper(ScraperTest):
    scraper_class = EatWell101

    def test_host(self):
        self.assertEqual("eatwell101.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.eatwell101.com/creamy-spinach-turkey-meatballs-recipe",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Christina Cherrier", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Creamy Spinach Turkey Meatballs", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual(
            "Chicken, Cook, Cooking & Meals, main dish recipes, Poultry recipes, ",
            self.harvester_class.category(),
        )

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.eatwell101.com/wp-content/uploads/2021/05/Creamy-Turkey-Meatballs-Recipe.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1/2 lb (220g) ground turkey meat",
            "1/2 lb (220g) ground chicken meat",
            "1/2 cup shredded mozzarella (or cheddar, provolone…)",
            "4 cloves garlic, grated + 4 cloves garlic, minced",
            "1 teaspoon Italian seasoning",
            "1/2 teaspoon red crushed chili pepper flakes, optional",
            "1 crumbled bouillon cube, optional",
            "Salt and fresh cracked black pepper, to taste",
            "1 cup fresh chopped cilantro (or parsley), divided",
            "2 teaspoons olive oil",
            "2 tablespoons butter",
            "1 small yellow onion, diced",
            "1/3 cup (80ml) vegetable broth",
            "5 ounces (150g) jarred sun-dried tomato in oil, drained of oil",
            "1 3/4 cups heavy cream",
            "Salt and pepper, to taste",
            "3 cups baby spinach leaves",
            "1/2 cup grated Parmesan",
            "1 tablespoon fresh parsley, chopped",
        ]

        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = (
            "1. To make the creamy spinach turkey meatballs: In a large bowl, combine ground turkey and ground chicken, cheese, grated garlic, Italian seasoning, bouillon cube, red chili pepper flakes, chopped cilantro, and black pepper. Mix well with your hands or fork and form medium balls. Arrange the turkey meatballs on a plate and set them aside.\n"
            "2. Melt 2 tablespoons butter in a large skillet over medium-low heat. Cook the turkey meatballs for 8 – 10 minutes on all sides until browned and cooked through. Remove to a clean plate and set aside.\n"
            "3. In the same pan, melt the butter in the remaining cooking juices. Add in the garlic and fry until fragrant (about one minute). Add onion and stir fry until translucent. Add the sun-dried tomatoes and fry for 1-2 minutes, so they release their flavors. Finally, pour in the vegetable broth, and allow the sauce to reduce slightly.\n"
            "4. Reduce heat to low, add in the heavy cream, and bring to a gentle simmer while stirring occasionally. Season the cream sauce with salt and pepper to taste.\n"
            "5. Add in the baby spinach and allow to wilt in the sauce. Finally, add in the parmesan cheese. Allow cream sauce to simmer for a further minute until the cheese melts through.\n"
            "6. Add the cooked turkey meatballs back into the pan; sprinkle with the parsley, and spoon the sauce over each meatball. Serve the creamy garlic spinach Tuscan meatballs over steamed veg or cauliflower rice for Keto dieters, or rice or pasta for non-Keto. Enjoy! ❤️"
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "These turkey meatballs are Gluten-free, low-carb, and keto-friendly - Perfect for a crowd-pleasing weeknight dinner. The creamy spinach turkey and chicken meatballs just melt in your mouth, it's so good!",
            self.harvester_class.description(),
        )
