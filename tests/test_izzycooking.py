# mypy: allow-untyped-defs

from recipe_scrapers.izzycooking import IzzyCooking
from tests import ScraperTest


class TestIzzyCookingScraper(ScraperTest):

    scraper_class = IzzyCooking

    def test_host(self):
        self.assertEqual("izzycooking.com", self.harvester_class.host())

    def author(self):
        self.assertEqual("izzycooking.com", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Oreo Cheesecake Bites Recipe (+Video)", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("16 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://izzycooking.com/wp-content/uploads/2018/06/Oreo-Cheesecake-Bites-Featured-Image.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "22 Oreo cookies ((Chop 6 of them into small pieces))",
            "16 ounces cream cheese (softened)",
            "1/2 cup granulated sugar",
            "1/2 tsp vanilla extract",
            "2 eggs",
            "1/2 cup sour cream ((or plain Greek yogurt))",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = "Preheat oven to 325°F. (Make sure your oven temperature is accurate, as a higher temp can cause the cheesecake to crack.)\nPlace cupcake paper liners into a muffin tin pan. Add one Oreo cookie into each paper cup. Set aside.\nAdd softened cream cheese and sugar to a medium mixing bowl. Beat on medium speed using a hand mixer.\nThen add vanilla and eggs. Mixing well until smooth without lumps.\nAdd sour cream, mix until combined. Tap bowl against your countertop a few times to release any large air bubbles.\nStir in chopped cookies, and mix generally using a spatula. (Be careful not to crush oreos into smaller crumbs.)\nSpoon the batter on top of the oreo, filling each to almost the top. Note that cheesecake won't rise as much as a regular cupcake.\nPlace in the lower third of the oven and bake for about 20-25 minutes until the edges just start to turn brown. Note that classic cheesecake is supposed to look pale, so you're not looking for golden brown.\nRemove from oven and transfer to cooling racks.\nChill in the fridge for 4 hours or overnight. Serve and enjoy! (You can store them in the fridge for up to 5 days.)"
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(4.92, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        expected_description = "Oreo Cheesecake Bites are creamy and soft mini cheesecakes with a delicious oreo crust at the bottom. They are so easy to make and a guaranteed hit at any party."
        self.assertEqual(expected_description, self.harvester_class.description())
