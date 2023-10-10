from recipe_scrapers.fitmencook import FitMenCook
from tests import ScraperTest

# test recipe's URL
# https://fitmencook.com/healthy-chili-recipe/


class TestFitMenCookScraper(ScraperTest):

    scraper_class = FitMenCook

    def test_host(self):
        self.assertEqual("fitmencook.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://fitmencook.com/recipes/healthy-chili-recipe/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Lean Chili with Plantains", self.harvester_class.title())

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Kevin Curry")

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("5 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 tablespoon avocado oil (or olive oil)",
                "1 tablespoon garlic, minced",
                "2/3 cup onion, diced",
                "1 bell pepper, diced",
                "1 1/2 lb 95% lean beef (I used lean bison)",
                "1 tablespoon chili powder",
                "2 teaspoons smoked paprika",
                "2 teaspoons cumin",
                "1/2 teaspoon cinnamon",
                "2 teaspoons (Mexican) oregano",
                "2 cups low sodium beef stock",
                "4 tablespoons tomato paste (NOT sauce)",
                "1 can (14.5oz /411g) no salt added diced tomatoes",
                "1 ripe plantain (~200g), cut into 1-inch pieces",
                "sea salt & pepper to taste",
                "cilantro",
                "jalapeño",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Set a pot on medium heat. Once hot, add the oil, garlic, onion and bell pepper. Cook for 2 – 3 minutes until the onion is browned along the edges.\nAdd the beef and chop it up finely as it cooks in the pot for 3 – 5 minutes. Sprinkle in the seasoning as the meat cooks.\nAdd the remaining ingredients EXCEPT plantain and stir everything together and bring to a light simmer. Cover and cook for 10 minutes.\nAdd the plantain after 10 minutes and stir everything together. ONLY if needed, add tablespoons of beef stock (or water) to the chili if it’s too thick, but also monitor the heat and make sure it’s not too high. Cover and cook for an additional 10 minutes.\nSeason to taste with sea salt & pepper (and lime) and garnish with cilantro and jalapeño.",
            self.harvester_class.instructions(),
        )
