from recipe_scrapers.cookingcircle import CookingCircle
from tests import ScraperTest


class TestCookingCircleScraper(ScraperTest):

    scraper_class = CookingCircle

    def test_host(self):
        self.assertEqual("cookingcircle.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Charlotte Roberts", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Vegan Lemon Cupcakes", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("30 mins or less", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://sharkninja-cookingcircle.s3.eu-west-1.amazonaws.com/wp-content/uploads/2022/02/23144350/Vegan-Lemon-Cupcakes-2220x1000.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "125ml non dairy milk",
                "1 tsp apple cider vinegar",
                "60ml olive oil",
                "100g caster sugar",
                "96g gluten free self raising flour",
                "1 tsp baking powder",
                "50g oat flour",
                "1 zest from lemon",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Step 1 Preheat your oven to 180c and line a cupcake tray with cases.",
                    "Step 2 Combine the non-dairy milk and cider vinegar, then set aside and allow to thicken.",
                    "Step 3 In your Ninja food processor, add in all of your dry ingredients and pulse to combine.",
                    "Step 4 Pour in the oil, milk mixture and lemon zest and blend for a few seconds to create a smooth batter.",
                    "Step 5 Transfer this into your cupcake cases (makes around 6 cupcakes) and bake in the oven for 25 minutes or until cooked through.",
                    "Step 6 Whilst allowing your cupcakes to cool, use an electric mixer to cream the butter until light and fluffy.",
                    "Step 7 Gradually add in the sugar and powders whilst mixing until fully combined.",
                    "Step 8 Once cooled, pipe the butter cream into each of your cakes and decorate.",
                ]
            ),
            self.harvester_class.instructions(),
        )
