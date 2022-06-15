from recipe_scrapers.averiecooks import AverieCooks
from tests import ScraperTest


class TestAverieCooksScraper(ScraperTest):

    scraper_class = AverieCooks

    def test_host(self):
        self.assertEqual("averiecooks.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.averiecooks.com/balsamic-watermelon-and-cucumber-salad/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Balsamic Watermelon and Cucumber Salad"
        )

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.averiecooks.com/wp-content/uploads/2020/07/watermelonsalad-5-480x480.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "500 millilters balsamic vinegar",
                "1 cup granulated sugar, divided",
                "3 cups watermelon, seeded and cubed (I recommend seedless, firm watermelon)",
                "1 large cucumber or English cucumber, peeled and cubed",
                "1 cup argula (1 heaping handful)",
                "1/3 cup goat cheese, crumbled or as desired",
                "1/3 cup candied nuts, or as desired",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            """To a high-sided medium/large kettle (use one bigger than you think you need), add the vinegar, 1/2 cup sugar, and heat over medium to medium-high until mixture boils and can sustain a fast rolling boil. Boil for about 15 to 20 minutes, or until reduced by about 80% and has thickened and is syrupy; stir intermittently and keep an eye on it so it doesn't bubble over.
When the sauce looks like it's about halfway done, taste the sauce, and if it's too vinegary and bitter for you, add part of or all of the remaining sugar. I personally use almost 1 cup. Sauce will thicken up more as it cools. Alternatively, you can use store bought balsamic glaze.
To a medium bowl, add all the remaining ingredients, stir to combine, and drizzle as much of the balsamic reduction as desired. You will have lots of balsamic reduction leftover, but it will keep for weeks in a sealed container in the fridge. As long as you're going to the trouble to make it, you may as well have extra for future recipes, because it's great drizzled over chicken, salmon, etc.""",
            self.harvester_class.instructions(),
        )
