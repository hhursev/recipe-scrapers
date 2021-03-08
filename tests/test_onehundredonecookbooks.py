from recipe_scrapers.onehundredonecookbooks import OneHundredOneCookBooks
from tests import ScraperTest


class TestOneHundredOneCookBooksScraper(ScraperTest):

    scraper_class = OneHundredOneCookBooks

    def test_host(self):
        self.assertEqual("101cookbooks.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Heidi Swanson", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Coconut Broccoli Soup", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://images.101cookbooks.com/coconut_broccoli_soup.jpg?w=680&auto=format",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 14-ounce can of full fat coconut milk",
                "3 cloves garlic, smashed",
                "1 large yellow onion, chopped",
                "1 small serrano chile, stemmed and chopped",
                "2 teaspoons fine grain sea salt",
                "4 1/2 cups water",
                "2-3 large heads of broccoli (~1 1/2 lb.), cut into small florets",
                "2-3 large handfuls of spinach",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Scoop a big spoonful of thick coconut cream from the top of the coconut milk can. Add it to a large pan over medium-high heat. When hot, stir in the garlic, onions, chile, and salt. Sauté for a couple minutes, just long enough for everything to soften up. Add the remaining coconut milk, and the water, and bring to a simmer before adding the broccoli and spinach. Simmer just long enough for the broccoli to get tender throughout, 2 - 4 minutes. Immediately remove the soup from heat and puree with an immersion blender.  Add more water if you feel the need to thin the soup out. Taste and add more salt if needed.\nServe sprinkled with tofu cubes, toasted almonds, and lots of scallions.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())
