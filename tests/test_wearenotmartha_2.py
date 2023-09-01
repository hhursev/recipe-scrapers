# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.wearenotmartha import WeAreNotMartha
from tests import ScraperTest


class TestWeAreNotMarthaScraper(ScraperTest):

    scraper_class = WeAreNotMartha
    test_file_name = "wearenotmartha_2"

    def test_host(self):
        self.assertEqual("wearenotmartha.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Sues", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Chocolate Cream Cold Brew", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Drink", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("1 serving", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://wearenotmartha.com/wp-content/uploads/chocolate-cream-cold-brew-featured.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "10 oz. cold brew",
                "Ice",
                "1 oz. vanilla syrup ((store-bought or recipe below))",
                "1/3 cup chocolate cream cold foam ((recipe below)*)",
                "1 cup water",
                "1 cup granulated sugar",
                "1 vanilla bean",
                "3/4 cup 2% milk",
                "1/4 cup heavy cream",
                "2 Tbsp vanilla syrup",
                "2 1/2 Tbsp chocolate malt powder",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "10 oz. cold brew",
                        "Ice",
                        "1 oz. vanilla syrup ((store-bought or recipe below))",
                        "1/3 cup chocolate cream cold foam ((recipe below)*)",
                    ],
                    purpose=None,
                ),
                IngredientGroup(
                    ingredients=[
                        "1 cup water",
                        "1 cup granulated sugar",
                        "1 vanilla bean",
                    ],
                    purpose="Vanilla Syrup",
                ),
                IngredientGroup(
                    ingredients=[
                        "3/4 cup 2% milk",
                        "1/4 cup heavy cream",
                        "2 Tbsp vanilla syrup",
                        "2 1/2 Tbsp chocolate malt powder",
                    ],
                    purpose="Chocolate Cream Cold Foam",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = (
            "Pour cold brew into an ice-filled glass. Stir in vanilla syrup.\n"
            "Top drink with chocolate cream cold foam and enjoy.\n"
            "Vanilla Syrup\n"
            "Put water and sugar in a medium saucepan and bring to a boil. Lower heat and let mixture simmer for about 10 minutes until sugar is completely dissolved and mixture has thickened a bit.\n"
            "Pour syrup into a heat-proof jar or container. Scrape out some of the seeds from the sliced open vanilla pod with a sharp knife and add them and the vanilla bean into the syrup.\n"
            "Place syrup in fridge and let steep for at least 6 hours**. Syrup will thicken more as it cools. If you want a more intense vanilla flavor, you can leave the bean in after 6 hours.\n"
            "For a quicker vanilla syrup, you can use vanilla extract instead of a vanilla bean. Stir about a Tablespoon of the extract into the saucepan right when you remove it from the heat. Syrup will be ready to use as soon as it cools.\n"
            "Chocolate Cream Cold Foam\n"
            "Mix milk, cream, vanilla syrup, and chocolate malt powder in a bowl until well combined. Or place all ingredients in a mason jar and shake. Keep in fridge until ready to use.\n"
            "To turn into foam, you can either use an electric frother, hand mixer, or blender. Alternatively, you can shake the mixture in a mason jar until it's frothy."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())
