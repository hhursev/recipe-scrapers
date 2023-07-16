from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.rainbowplantlife import RainbowPlantLife
from tests import ScraperTest


class TestRainbowPlantLifeScraper(ScraperTest):
    scraper_class = RainbowPlantLife
    test_file_name = "rainbowplantlife_groups"

    def test_host(self):
        self.assertEqual("rainbowplantlife.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual("Vegan Pasta Salad", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("10 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://rainbowplantlife.com/wp-content/uploads/2022/06/vegan-pasta-salad-beauty-shot-1-of-2-scaled.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 pound fusilli, (rotini, or penne rigate (a ridged pasta))",
                "1 cup (112g) raw walnuts",
                "5 ounces (140g) sourdough loaf, (baguette, or country-style bread, sliced)",
                "1 (12-ounce/340g) jar of roasted red bell peppers**, (drained from the liquid in the jar)",
                "3 garlic cloves, (roughly chopped)",
                "1 medium lemon, (zested and juiced (3 tablespoons juice; save the zest for the Topping))",
                "½ to 1 teaspoon smoked paprika ((use 1 teaspoon for prominent smokiness))",
                "½ teaspoon red pepper flakes",
                "1 teaspoon kosher salt, (plus more to taste)",
                "Freshly cracked black pepper to taste",
                "⅓ cup (75g) extra virgin olive oil",
                "Reserved bread crumbs from Sauce",
                "Reserved lemon zest from Topping",
                "1 cup (16g) flat-leaf parsley, (finely chopped)",
                "1 ½ cups (24g) fresh basil, (finely chopped)",
                "3 tablespoons capers***, (chopped)",
                "¼ teaspoon red pepper flakes ((optional) )",
                "½ teaspoon flaky sea salt",
                "3 cups (60g) baby arugula, (chopped)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 pound fusilli, (rotini, or penne rigate (a ridged pasta))"
                    ],
                    purpose=None,
                ),
                IngredientGroup(
                    ingredients=[
                        "1 cup (112g) raw walnuts",
                        "5 ounces (140g) sourdough loaf, (baguette, or country-style bread, sliced)",
                        "1 (12-ounce/340g) jar of roasted red bell peppers**, (drained from the liquid in the jar)",
                        "3 garlic cloves, (roughly chopped)",
                        "1 medium lemon, (zested and juiced (3 tablespoons juice; save the zest for the Topping))",
                        "½ to 1 teaspoon smoked paprika ((use 1 teaspoon for prominent smokiness))",
                        "½ teaspoon red pepper flakes",
                        "1 teaspoon kosher salt, (plus more to taste)",
                        "Freshly cracked black pepper to taste",
                        "⅓ cup (75g) extra virgin olive oil",
                    ],
                    purpose="Sauce",
                ),
                IngredientGroup(
                    ingredients=[
                        "Reserved bread crumbs from Sauce",
                        "Reserved lemon zest from Topping",
                        "1 cup (16g) flat-leaf parsley, (finely chopped)",
                        "1 ½ cups (24g) fresh basil, (finely chopped)",
                        "3 tablespoons capers***, (chopped)",
                        "¼ teaspoon red pepper flakes ((optional) )",
                        "½ teaspoon flaky sea salt",
                        "3 cups (60g) baby arugula, (chopped)",
                    ],
                    purpose="Herby Bread Crumb Topping",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Preheat the oven to 350ºF/175ºC. Place bread slices on a rimmed sheet pan. Spread out walnuts in the empty spaces on the pan. Toast both in the oven for 8 to 10 minutes, tossing the walnuts and flipping the bread slices over halfway through, until the walnuts are toasty and lightly browned and the bread is also a bit toasty. Allow to cool a bit.\nCook the pasta. Bring a large pot of water to a boil, 4 quarts/liters or 128 ounces. Once boiling, season with 2 tablespoons of kosher salt. Add the pasta and, once it comes back to a boil, set a timer for 2 minutes longer than the upper range of the cook time for al dente pasta on the box instructions.***Before draining, reserve 1 cup of pasta water, then drain pasta in a colander. Rinse the pasta with cold water to bring to room temperature and shake off the excess water.\nMake the bread crumbs: Tear the toasted bread into small pieces. Add them to a food processor and pulse repeatedly until you get bread crumbs, but don’t blend continuously—this helps retain some texture. It'll take a couple minutes. Take out half of the bread crumbs and set aside in a medium bowl for the Topping.\nMake the roasted red pepper sauce****. To the remaining bread crumbs in the food processor, add the toasted walnuts, roasted bell peppers, garlic, lemon juice (save the zest for the topping), smoked paprika, red pepper flakes, 1 teaspoon kosher salt, and several cracks of pepper. Process until a thick paste forms. With the motor running, stream in the olive oil until a sauce forms, and blend until smooth and thick. Season to taste with salt and pepper as needed, but don’t add too much salt, as there’s also salt in the Topping.\nMake the Herby Bread Crumb Topping: In a bowl, combine the reserved bread crumbs, reserved lemon zest, chopped parsley and basil, chopped capers, red pepper flakes if using, and flaky salt. Stir well to combine.\nAssemble the pasta: toss the pasta with the roasted red pepper sauce until well coated. Add about ¾ cup (180 mL) of pasta water and toss to coat. Add more pasta water until it’s sufficiently saucy. Add the arugula and any other desired mix-ins***** and toss to combine. Add the Herby Bread Crumb Topping and gently toss just to combine.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.97, self.harvester_class.ratings())
