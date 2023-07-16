from recipe_scrapers.jimcooksfoodgood import JimCooksFoodGood
from tests import ScraperTest


class TestJimCooksFoodGoodScraper(ScraperTest):

    scraper_class = JimCooksFoodGood

    def test_host(self):
        self.assertEqual("jimcooksfoodgood.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Jim", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("German Potato Salad", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://jimcooksfoodgood.com/wp-content/uploads/2019/09/1282A83C-D784-4DF4-9623-C580DC9B9840.jpeg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "3 Pounds Yukon Gold Potatoes ((Or a small white potato))",
                "2/3 Cup Sherry or Apple Cider Vinegar",
                "1/2 Cup dijon mustard",
                "1/2 Cup Bread and Butter Pickles",
                "1/4 Cup olive oil",
                "4 Tablespoons capers ((Plus a splash of brine))",
                "2 Teaspoons salt",
                "1/2 Cup Fresh Parsley",
                "1/4 Cup scallions",
                "1 Sprig Fresh Rosemary",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Preheat oven to 400 deg F. Cut potatoes into rough bitesize chunks, it doesn't have to be exact. Arrange on two non-stick sprayed baking sheets, season with 1/2 of the salt, and roast for 30 minutes.",
                    "As potatoes cook, roughly chop the pickles, capers, rosemary, scallions, and parsley. Combine thoroughly with vinegar, mustard, oil, remaining teaspoon of salt, and some heavy grinds of black pepper.",
                    "When potatoes are cooked, immediately transfer to very large mixing bowl. Add the dressing slowly as you mix; the potatoes should gently break apart, which is a good thing. Serve warm or at room temperature.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
