# mypy: allow-untyped-defs

from recipe_scrapers.omnivorescookbook import OmnivoresCookbook
from tests import ScraperTest


class TestOmnivoresCookbookScraper(ScraperTest):

    scraper_class = OmnivoresCookbook
    test_file_name = "omnivorescookbook_1"

    def test_host(self):
        self.assertEqual("omnivorescookbook.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Maggie Zhu", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Stir Fried Bok Choy with Tofu Puffs", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Side", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://omnivorescookbook.com/wp-content/uploads/2022/02/211213_Stir-Fried-Bok-Choy-With-Tofu-Puffs_550.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 lb (450 g) bok choy , chopped to bite size pieces (see the cutting method in the post above)",
                "1 heaping cup (60 grams) tofu puffs , halved",
                "2 green onions , sliced",
                "1 tablespoon peanut oil (or vegetable oil)",
                "1 teaspoon sugar",
                "2 tablespoons light soy sauce (or soy sauce)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Heat 1 tablespoon of oil in a medium-sized wok or large skillet over high heat until hot. Add scallion and stir a few times until fragrant.\nAdd bok choy. Stir and cook for 1 to 2 minutes, to coat evenly with oil.\nSprinkle it with sugar and swirl in light soy sauce. Immediately stir a few times to mix well. Add deep fried tofu, then stir again for about 20 seconds.\nCover the wok and lower to medium-low heat. Steam for 30 seconds. Uncover and stir to check the doneness. Cover and cook for another 10 to 20 seconds again, if necessary, until the bok choy is cooked through and slightly caramelized on the edges. Turn off the heat and transfer everything to a serving plate.\nServe hot as a side dish or over steamed rice as a light main dish.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Chinese", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "A super quick and easy stir fried bok choy with tofu puffs that only uses five ingredients and takes 15 minutes to prep and cook.",
            self.harvester_class.description(),
        )
