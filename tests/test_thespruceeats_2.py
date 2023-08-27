from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.thespruceeats import TheSpruceEats
from tests import ScraperTest


class TestTheSpruceEatsScraper(ScraperTest):

    scraper_class = TheSpruceEats
    test_file_name = "thespruceeats_2"

    def test_host(self):
        self.assertEqual("thespruceeats.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Jessie Sheehan", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Peppermint Swirl Brownies", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("9 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.thespruceeats.com/thmb/ACSQpDA6gMM5sqOI58di9oHkbnM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/peppermint-swirl-brownies-hero-01-00280-7d6d862ae03f4aecab0639e457946a55.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1 tablespoon unsalted butter, softened",
            "8 ounces cream cheese, room temperature",
            "1/3 cup confectioners' sugar",
            "1/4 teaspoon fine sea salt",
            "1 large egg",
            "1 teaspoon peppermint extract",
            "2 to 3 drops liquid or gel red food coloring",
            "4 ounces (1/2 cup) unsalted butter, melted",
            "2/3 cup (53 grams) Dutch process cocoa powder",
            "1 cup (200 grams) granulated sugar",
            "1/2 teaspoon peppermint extract",
            "2 large eggs, room temperature",
            "1/4 teaspoon fine salt",
            "2/3 cup (87 grams) all-purpose flour",
            "2/3 cup crushed peppermint candies, such as Star Brite mints or candy canes, divided",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 tablespoon unsalted butter, softened",
                        "8 ounces cream cheese, room temperature",
                        "1/3 cup confectioners' sugar",
                        "1/4 teaspoon fine sea salt",
                        "1 large egg",
                        "1 teaspoon peppermint extract",
                        "2 to 3 drops liquid or gel red food coloring",
                    ],
                    purpose="For the Peppermint Swirl:",
                ),
                IngredientGroup(
                    ingredients=[
                        "4 ounces (1/2 cup) unsalted butter, melted",
                        "2/3 cup (53 grams) Dutch process cocoa powder",
                        "1 cup (200 grams) granulated sugar",
                        "1/2 teaspoon peppermint extract",
                        "2 large eggs, room temperature",
                        "1/4 teaspoon fine salt",
                        "2/3 cup (87 grams) all-purpose flour",
                        "2/3 cup crushed peppermint candies, such as Star Brite mints or candy canes, divided",
                    ],
                    purpose="For the Brownies:",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = (
            "Gather the ingredients.\n"
            "Position a rack in the center of the oven and heat to 350 F. Grease an 8-inch square cake pan with softened butter. Line the bottom with a large sheet of parchment paper that extends up and over two opposite sides of the pan.\n"
            "To make the peppermint swirl, place the cream cheese, confectioners' sugar, salt, egg, extract, and food coloring in a medium bowl and beat with a hand mixer on medium to medium high speed until combined and fluffy. You can also use a stand mixer.\n"
            "To make the brownies, microwave the butter, cocoa powder, and sugar on high in a large microwave-safe bowl in a few 30-second bursts, whisking after each, until combined. The batter will be quite thick and fudgy-looking. If you do not have a microwave, you may place the ingredients in a heat-proof bowl over a pot of simmering water on the stovetop until combined.\n"
            "Whisk in the extract. Gently whisk in the eggs one at a time.\n"
            "Sprinkle the salt over the wet ingredients and whisk it in.\n"
            "Finally, fold in the flour and 1/3 cup of the crushed candy until the last streak of flour disappears. Don’t overmix.\n"
            "Scrape the batter into the prepared pan, reserving 3/4 cup of it.\n"
            "Dollop the swirl mixture over the brownie batter in the pan—about 9 dollops, using a 1 1/2 tablespoon portion scoop, if you have it.\n"
            "Dollop the reserved brownie batter in between the swirl dollops. Run a long wooden skewer through both the brownie batter and the pink cream cheese mixture, until the top is completely covered in decorative swirls. Don’t swirl too much: big swirls are what you want, as they are most dramatic. And don’t swirl too deep or the swirl can get lost in the batter.\n"
            "Bake for 30 to 35 minutes, rotating the pan at the halfway point. At the 25 minute mark, sprinkle the remaining 1/3 cup of candy over the top of the brownies. The brownies are ready when a cake tester inserted into the brownie—not the swirl—comes out with a few moist crumbs—do not over bake.\n"
            "Let cool to room temperature. Lift the brownies out of the pan by the parchment handles. Run a butter knife around the edges not covered by the paper, if there’s resistance. Slice into 9 equal sized squares and serve room-temperature, or refrigerate for an hour and serve chilled (my preference)."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(3.5, self.harvester_class.ratings())
