from recipe_scrapers.insanelygoodrecipes import InsanelyGoodRecipes
from tests import ScraperTest


class TestInsanelyGoodRecipes(ScraperTest):

    scraper_class = InsanelyGoodRecipes

    def test_host(self):
        self.assertEqual("insanelygoodrecipes.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("insanelygood", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Crockpot Angel Chicken (Easy Slow Cooker Recipe)",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual("Chicken,Recipes", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(250, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://insanelygoodrecipes.com/wp-content/uploads/2023/08/Creamy_and_Flavorful_Homemade_Crockpot_Angel_Chicken_with_Pasta_In_a_Bowl.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "6 boneless chicken breasts",
                "1/2 cup butter",
                "1 (1-ounce) package of dried Italian salad dressing mix",
                "1 (10-1/2 ounce) can of Campbell’s Golden Mushroom soup",
                "1/2 cup white wine, chicken stock, or water",
                "4 ounces cream cheese with chives and onions",
                "Angel hair pasta",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Remove the chicken from the packaging, and place it in the crock pot.\nUsing a medium saucepan, melt the butter on low heat.\nAdd the cream of mushroom soup, dried Italian salad dressing mix, cream cheese, and wine. Stir it until it's melted and creamy.\nPour the cheesy mixture over the chicken breasts, and cover with a lid.\nCook on low for 4-5 hours.\nBefore serving, prepare the angel hair pasta according to the directions on the back of the box.\nPortion the angel hair pasta and chicken on a plate, and spoon the sauce on top. Dig in!",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "Dinner is easy with this Crockpot angel chicken! With just 7 ingredients, it's a heavenly meal everyone will love.",
            self.harvester_class.description(),
        )
