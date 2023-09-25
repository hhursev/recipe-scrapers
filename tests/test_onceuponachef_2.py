# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.onceuponachef import OnceUponAChef
from tests import ScraperTest


class TestOnceUponAChefScraper(ScraperTest):

    scraper_class = OnceUponAChef
    test_file_name = "onceuponachef_2"

    def test_host(self):
        self.assertEqual("onceuponachef.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("By Jenn Segal", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Black Bean & Corn Salad with Chipotle-Honey Vinaigrette",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual("Salads", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.onceuponachef.com/images/2014/06/Black-Bean-and-Corn-Salad.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "2 ears fresh corn",
            "1 cup chopped red onion",
            "1 (14.5 oz) can black beans",
            "1 red bell pepper, diced (about 1 cup)",
            "½ cup loosely packed fresh chopped cilantro (plus a bit more for garnish, if desired)",
            "1 avocado",
            "2 tablespoons red wine vinegar",
            "2 tablespoons fresh lime juice, from 1-2 limes",
            "2 tablespoons honey",
            "¼ cup plus 2 tablespoons vegetable oil",
            "1 large garlic clove, roughly chopped",
            "¼ teaspoon dried oregano",
            "¾ teaspoon cumin",
            "¾ teaspoon salt",
            "¼ teaspoon black pepper",
            "2 canned chipotle peppers in adobo sauce (2 peppers, not 2 cans; use smaller peppers and if they are all large, use only 1½)",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "2 ears fresh corn",
                        "1 cup chopped red onion",
                        "1 (14.5 oz) can black beans",
                        "1 red bell pepper, diced (about 1 cup)",
                        "½ cup loosely packed fresh chopped cilantro (plus a bit more for garnish, if desired)",
                        "1 avocado",
                    ],
                    purpose="For the Salad",
                ),
                IngredientGroup(
                    ingredients=[
                        "2 tablespoons red wine vinegar",
                        "2 tablespoons fresh lime juice, from 1-2 limes",
                        "2 tablespoons honey",
                        "¼ cup plus 2 tablespoons vegetable oil",
                        "1 large garlic clove, roughly chopped",
                        "¼ teaspoon dried oregano",
                        "¾ teaspoon cumin",
                        "¾ teaspoon salt",
                        "¼ teaspoon black pepper",
                        "2 canned chipotle peppers in adobo sauce (2 peppers, not 2 cans; use smaller peppers and if they are all large, use only 1½)",
                    ],
                    purpose="For the Dressing",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = "Bring a large pot of salted water to a boil. Add the corn, cover, and turn the heat down to low. Simmer for 10 minutes. Remove the corn from the water and let cool.\nMeanwhile, place the chopped red onions in a small bowl and cover with water. Let sit about ten minutes, then drain completely in a sieve and set aside.\nPlace the beans in a sieve; run under cold water to rinse well. Let drain completely and set aside.\nHolding the cooled corn upright in a large bowl, cut the kernels off the cob in strips. Add the beans, red onion, red bell pepper and cilantro.\nMake the dressing by combining all of the ingredients in a blender or mini food processor; process until smooth.\nPour the dressing over the salad and toss well. Cover and refrigerate for at least 1 hour or, preferably, overnight.\nRight before serving, slice the avocado in half. Remove the pit; using a butter knife, cut a grid in each half. Holding the avocado halves over the salad, use a spoon to scoop out the diced flesh. Toss the salad gently, then taste and adjust seasoning if necessary (I usually add a squeeze of fresh lime to freshen it up). Garnish with a bit of fresh chopped cilantro if desired. Serve cold."
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Mexican, Tex-Mex", self.harvester_class.cuisine())

    def test_description(self):
        expected_description = "This make-ahead black bean and corn salad is a real crowd-pleaser. Bonus: it doubles as a dip!"
        self.assertEqual(expected_description, self.harvester_class.description())
