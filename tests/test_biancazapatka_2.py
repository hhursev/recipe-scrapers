from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.biancazapatka import BiancaZapatka
from tests import ScraperTest


class TestBiancaZapatkaScraper(ScraperTest):
    scraper_class = BiancaZapatka
    test_file_name = "biancazapatka_2"

    def test_host(self):
        self.assertEqual("biancazapatka.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://biancazapatka.com/en/vegan-blueberry-cake/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Bianca Zapatka", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("The Best Vegan Blueberry Cake", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Cake,Dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(65, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://biancazapatka.com/wp-content/uploads/2023/07/kuchen-blaubeeren-brombeeren.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1 cup soy milk (or other plant milk, *see notes))",
            "juice of 1 lemon (approx. ¼ cup lemon juice)",
            "½ cup vegetable oil (e.g. canola or sunflower or butter-flavored Alba oil)",
            "1 tsp vanilla extract (or ground bourbon vanilla or the pulp of a vanilla bean)",
            "2 ½ cups flour (all-purpose, spelt or gluten-free flour)",
            "2 tsp baking powder",
            "1 tsp baking soda (or 2 tsp more baking powder)",
            "1 pinch of salt",
            "¾ cup raw cane sugar (or other sugar to taste)",
            "7 oz blueberries (or other berries)",
            "1 tbsp cornstarch (or more flour for rolling)",
            "3.5 oz dairy-free whipping cream",
            "3.5 oz dairy-free cream cheese",
            "2-3 tbsp powdered sugar",
            "2 tsp blueberry powder",
            "1 tsp San-apart (optional)",
            "2-3 tbsp lemon juice",
            "blueberries",
            "blackberries",
            "desiccated coconut",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 cup soy milk (or other plant milk, *see notes))",
                        "juice of 1 lemon (approx. ¼ cup lemon juice)",
                        "½ cup vegetable oil (e.g. canola or sunflower or butter-flavored Alba oil)",
                        "1 tsp vanilla extract (or ground bourbon vanilla or the pulp of a vanilla bean)",
                        "2 ½ cups flour (all-purpose, spelt or gluten-free flour)",
                        "2 tsp baking powder",
                        "1 tsp baking soda (or 2 tsp more baking powder)",
                        "1 pinch of salt",
                        "¾ cup raw cane sugar (or other sugar to taste)",
                        "7 oz blueberries (or other berries)",
                        "1 tbsp cornstarch (or more flour for rolling)",
                    ],
                    purpose="Blueberry Cake",
                ),
                IngredientGroup(
                    ingredients=[
                        "3.5 oz dairy-free whipping cream",
                        "3.5 oz dairy-free cream cheese",
                        "2-3 tbsp powdered sugar",
                        "2 tsp blueberry powder",
                        "1 tsp San-apart (optional)",
                        "2-3 tbsp lemon juice",
                    ],
                    purpose="Blueberry Frosting",
                ),
                IngredientGroup(
                    ingredients=["blueberries", "blackberries", "desiccated coconut"],
                    purpose="For Decorating (optional)",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Blueberry Cake",
                    "Preheat the oven to 356 °F (180 °C). Grease a 25-cm loaf pan and line with parchment paper (see photo above).",
                    "Whisk together the soy milk and lemon juice in a measuring cup and set aside for about 5 minutes until it has curdled into vegan buttermilk (this doesn't work well with other types of plant milks, however, it’s not a big deal when it doesn't work).",
                    "Meanwhile, sift flour and baking powder into a large bowl. Then whisk in baking soda, salt and sugar.",
                    "Add vegan buttermilk, oil and vanilla extract and stir briefly until all ingredients are just combined.",
                    "Wash the blueberries, pat them dry and toss them with a little cornstarch or flour (so that they don't seep onto the bottom and lose too much juice during baking). Then gently fold ¾ of them into the batter with a spatula.",
                    "Pour the batter into the baking pan and gently tap the pan a few times on the work surface to get rid of the air bubbles and smooth out the top.",
                    "Spread the remaining ¼ of blueberries on top and bake the cake for about 55 minutes, or until a toothpick comes out clean (don't skip the stick test! If the cake gets too dark during baking, cover loosely with a piece of parchment paper).",
                    "Allow to cool in the pan for 10-15 minutes. Then remove and let cool completely on a cooling rack.",
                    "Blueberry Frosting",
                    "In a mixing bowl, beat the dairy-free whipping cream with an electric hand mixer until stiff peaks form.",
                    "In another mixing bowl, mix the dairy-free cream cheese with powdered sugar, blueberry powder, San-apart and lemon juice until creamy. Then fold in the whipped cream.",
                    "Spread the blueberry cream on the cake and decorate with fresh blueberries, blackberries and desiccated coconut.",
                    "Slice and enjoy!",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("German", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "This simple vegan blueberry cake is incredibly moist, fruity, super delicious and just like grandma used to make! You can turn this recipe into a loaf cake, round cake, bundt cake, sheet cake, or into small muffins and cupcakes!",
            self.harvester_class.description(),
        )
