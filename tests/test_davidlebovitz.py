from recipe_scrapers.davidlebovitz import DavidLebovitz
from tests import ScraperTest


class TestDavidLebovivtzScraper(ScraperTest):

    scraper_class = DavidLebovitz

    def test_host(self):
        self.assertEqual("davidlebovitz.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("David", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Faux Gras", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(None, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("0 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.davidlebovitz.com/wp-content/uploads/2015/06/Faux-Gras-Lentil-Pate-8.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "12 medium-sized (100g, about 1 cup) button mushrooms",
                "2 tablespoons olive oil",
                "2 tablespoons butter (salted or unsalted)",
                "1 small onion (peeled and diced)",
                "2 cloves garlic (peeled and minced)",
                "2 cups (400g) cooked green lentils",
                "1 cup (140g) toasted walnuts or pecans",
                "2 tablespoons freshly squeezed lemon juice",
                "1 tablespoon soy sauce or tamari",
                "2 teaspoons minced fresh rosemary",
                "2 teaspoons fresh thyme (minced)",
                "2 tablespoons fresh sage or flat leaf parsley",
                "optional: 2 teaspoons Cognac or brandy",
                "1 teaspoon brown sugar",
                "1/8 teaspoon cayenne pepper",
                "salt and freshly ground black pepper",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Wipe the mushrooms clean. Slice off a bit of the stem end (the funky parts) and slice them. Heat the olive oil and butter in a skillet or wide saucepan. Add the onions and garlic, and cook, stirring frequently, until the onions become translucent, 5 to 6 minutes. Add the mushrooms and cook, stirring occasionally, until they’re soft and cooked through, another 5 to 8 minutes. Remove from heat.\nIn a food processor, combine the cooked lentils, nuts, lemon juice, soy sauce, rosemary, thyme, sage or parsley, Cognac (if using), brown sugar, and cayenne. Scrape in the cooked mushroom mixture and process until completely smooth. Taste, and add salt, pepper, and additional cognac, soy sauce, or lemon juice, if it needs balancing.\nScrape the pâté into a small serving bowl and refrigerate for a few hours, until firm.""",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            """Adapted from Très Green, Très Clean, Très Chic by Rebecca Leffler Lentils double in volume when cooked, so 1 cup (160g) of dried lentils will yield close to the correct amount. They usually take about 20 to 30 minutes to cook until soft, but check the directions on the package for specific guidelines. If avoiding gluten, use tamari instead of soy sauce. For a vegan version, replace the butter with the same quantity of olive oil, for a total of 1/4 cup (60ml) of olive oil. The cognac or brandy is optional, but it does give the faux gras a little je ne sais quoi.""",
            self.harvester_class.description(),
        )
