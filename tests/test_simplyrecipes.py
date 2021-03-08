from recipe_scrapers.simplyrecipes import SimplyRecipes
from tests import ScraperTest


class TestSimplyRecipesScraper(ScraperTest):

    scraper_class = SimplyRecipes

    def test_host(self):
        self.assertEqual("simplyrecipes.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.simplyrecipes.com/recipes/one_pot_chicken_and_rice_soup/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "One-Pot Chicken and Rice Soup")

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        # 6 to 8 servings (makes about 3 quarts), debatable it should be 8 servings.
        self.assertEqual("8 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 bone-in chicken breasts, skin removed (1 to 1 1/2 pounds)",
                "1 cup long-grain white rice, like basmati",
                "2 celery ribs, diced small",
                "2 medium carrots, peeled and diced small",
                "1 onion, diced small",
                "2 cloves garlic, peeled but left whole",
                "1 teaspoon salt, plus more to taste (see Recipe Note)",
                "1/2 teaspoon ground black pepper",
                "2 quarts unsalted or low-sodium chicken stock",
                "Juice of 1/2 lemon (about 3 tablespoons)",
                "Chopped fresh parsley, for serving",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Assemble the soup and bring to a simmer : Combine the chicken, white rice, celery, carrots, onions, garlic, salt, and pepper in a large pot. Add the chicken stock and bring to a boil over high heat. Once the soup is boiling, reduce the heat to keep the soup at a gentle simmer.",
                    "Simmer for about 25 minutes : As the soup simmers, skim off any foam that collects on the surface with a spoon. Continue to simmer until the rice and vegetables are tender, about 25 minutes. Remove the soup from heat.",
                    "Shred the chicken and make the garlic paste : Remove the chicken and garlic cloves using a slotted spoon or tongs. Transfer the chicken breasts to a bowl and shred with two forks. Discard the bones. Return the shredded chicken to the pot. Smash the garlic cloves into a paste against a cutting board using a fork or the flat of your knife. Stir the paste back into the soup.",
                    "Season and serve: : Stir the lemon juice into to the soup, and taste. The soup should taste rich, barely salty, and with just a hint of lemon. Add more salt or lemon juice as needed until it tastes good to you. Divide among bowls and sprinkle with some parsley for serving. Leftovers will keep for about a week refrigerated, or up to 3 months frozen.",
                ]
            ),
            self.harvester_class.instructions(),
        )
