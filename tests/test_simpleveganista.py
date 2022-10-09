# mypy: allow-untyped-defs

from recipe_scrapers.simpleveganista import SimpleVeganista
from tests import ScraperTest


class TestSimpleVeganistaScraper(ScraperTest):

    scraper_class = SimpleVeganista

    def test_host(self):
        self.assertEqual("simple-veganista.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Julie | The Simple Veganista", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Vegan Jambalaya", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Entree", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://simple-veganista.com/wp-content/uploads/2022/02/easy-vegan-jambalaya-recipe-5-225x225.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 tablespoon olive oil or 1/4 cup water",
                "1 medium onion, diced",
                "4 cloves garlic, minced",
                "3 large bell peppers (green, red & yellow), seeded and diced",
                "2 large celery ribs, diced",
                "2 teaspoons smoked paprika",
                "1 teaspoon EACH dried thyme + oregano",
                "1/4 – 1/2 teaspoon cayenne or red pepper flakes",
                "1 can (14oz) crushed tomatoes",
                "1 1/2 cups dry long-grain rice (for grain-free see notes)",
                "1 – 2 bay leaves",
                "3 1/2 – 4 cups low-sodium vegetable broth",
                "1 can (14oz) red kidney beans, drained and rinsed",
                "3 – 4 vegan sausages (about 14 oz), sliced and cooked (or extra can of beans)",
                "1 teaspoon pink salt, or to taste",
                "fresh cracked pepper, to taste",
                "sliced scallions (green onions)",
                "chopped parsley",
                "dash of hot sauce (Tabasco, Frank’s, or your favorite)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Vegan sausage\nIf using plant-based sausage, you’ll want to cook it first. Slice it into bite-size pieces and cook in a skillet with 1 tablespoon oil, over medium heat until browned, about 3 – 5 minutes on each side. Transfer to a small plate lined with a paper napkin to soak up excess oil.\nSaute\nIn a large pan, heat oil/water over medium-high heat, add the onion, garlic, celery, and bell peppers, saute for 5 minutes. Add the smoked paprika, thyme, oregano, and cayenne, and saute for 1 minute more.\nSimmer\nAdd the crushed tomatoes, rice, bay leaves, and broth, bring to a boil, reduce heat, cover askew, and simmer on low for 20 – 25 minutes, stirring every 7 minutes or so to keep the rice from sticking to the bottom of the pan. In the last 5 minutes, add the beans and/or sausage and continue to cook until warmed through. Remove bay leaves, season with salt and pepper.\nServe\nSpoon into serving bowls and top with garnish of choice.\nServes 6 – 8\nStore\nLeftovers can be stored for up to 5 days in the refrigerator. For longer storage, keep in the freezer for up to 2 months. Let thaw before reheating on the stovetop or in the microwave.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Creole", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Made in 1 pot, this easy Louisiana Vegan Jambalaya is loaded with healthy veggies and plant-based protein for a delicious Creole-style rice dish that even the picky eaters will love!",
            self.harvester_class.description(),
        )
