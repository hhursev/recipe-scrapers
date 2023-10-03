from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.nhshealthierfamilies import NHSHealthierFamilies
from tests import ScraperTest


class TestNHSHealthierFamiliesScraper(ScraperTest):

    scraper_class = NHSHealthierFamilies
    test_file_name = "nhshealthierfamilies_2"

    def test_host(self):
        self.assertEqual("nhs.uk", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("NHS Better Health", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Good old fish and chips", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(50, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://assets.nhs.uk/campaigns-cms-prod/images/Recipes-square-healthy-fish-and-chips.width-320.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "4 potatoes, scrubbed, each cut into 8 wedges",
            "1 tablespoon vegetable oil",
            "75g dried white or wholemeal breadcrumbs",
            "1 egg, beaten with 2 tbsp cold water",
            "4 fillets skinless white fish, like haddock, cod or pollock",
            "300g mushy peas",
            "1 pinch ground black pepper (optional)",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "4 potatoes, scrubbed, each cut into 8 wedges",
                        "1 tablespoon vegetable oil",
                        "75g dried white or wholemeal breadcrumbs",
                        "1 egg, beaten with 2 tbsp cold water",
                        "4 fillets skinless white fish, like haddock, cod or pollock",
                    ],
                    purpose=None,
                ),
                IngredientGroup(
                    ingredients=[
                        "300g mushy peas",
                        "1 pinch ground black pepper (optional)",
                    ],
                    purpose="Swappable or optional",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Preheat the oven to 200C (fan 180C, gas mark 6). Lightly grease a baking sheet with a little vegetable oil.",
                    "Put the potato wedges into a roasting tin. Add the remaining vegetable oil and toss to coat. Season with black pepper. Transfer to the oven to bake for 35 to 40 minutes, turning them over after 20 minutes.",
                    "Meanwhile, sprinkle the breadcrumbs onto a large plate. Season with a little pepper. Dip each fish fillet in the beaten egg, then coat in the breadcrumbs. Place on the baking sheet, then transfer to the oven when you turn the potatoes, so that it cooks for 15 to 20 minutes. To check that the fish is cooked, it should flake easily when tested with a fork.",
                    "Heat the mushy peas in a saucepan, then serve with the fish and chips.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_description(self):
        expected_description = "Try our recipe for healthier, homemade fish and chips! Click to read the ingredients and a step-by-step guide to making it"
        self.assertEqual(expected_description, self.harvester_class.description())
