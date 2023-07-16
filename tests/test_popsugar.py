from recipe_scrapers.popsugar import PopSugar
from tests import ScraperTest


class TestPopSugarScraper(ScraperTest):

    scraper_class = PopSugar

    def test_host(self):
        self.assertEqual("popsugar.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual("Rainbow Pasta", self.harvester_class.title())

    def test_image(self):
        self.assertEqual(
            "https://media1.popsugar-assets.com/files/thumbor/QpXN5ex3L8WRyMBIBlypdBwKX-Q/fit-in/1024x1024/filters:format_auto-!!-:strip_icc-!!-/2016/09/02/018/n/1922195/f31877d9_5cdf801a_Rainbow_Pasta_HERO/i/Rainbow-Pasta-Food-Video.jpg",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(49, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "4 tablespoons grated parmesan cheese",
                "Non-stick cooking spray",
                "4 baby beetroot bulbs, quartered",
                "1 2-inch piece of turmeric, grated",
                "1 red cabbage, roughly chopped",
                "1 teaspoon baking soda",
                "Water",
                "1 pound dry spaghetti, cooked 2 minutes below the recommended cooking time",
                "6 tablespoons unsalted butter",
                "3 garlic cloves, smashed",
                "1 shallot, roughly chopped",
                "2 tablespoons fresh chives, roughly chopped",
                "3 sprigs fresh thyme",
                "1 teaspoon lemon zest",
                "2 tablespoons lemon juice",
                "Kosher salt to taste",
                "Parmesan cheese, for garnish",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "For parmesan tuiles: Arrange the parmesan cheese into 4 piles on a greased 10-inch skillet. Turn the heat to medium and allow the cheese to melt and turn golden brown around the edges, about 4-6 minutes. Remove the pan from the heat and allow the parmesan tuiles to cool in the pan before transferring to a paper towel lined plate. Repeat with more cheese if desired.\nFor pasta: Add the beets to the bowl of a food processor and pulse about 10 times until coarsely chopped. Add the beet mixture to a small saucepan and add enough water to just cover the beets (about 2 cups). Simmer on medium for about 5 minutes until the water becomes a deep and vibrant pink color. Strain the liquid through a cheesecloth lined strainer into a small bowl and set aside to cool. Discard or store any leftover beet pulp.\nIn a clean saucepan, add the turmeric and 3 cups of water. Bring to a simmer for 5 minutes, strain through a cheesecloth-lined strainer into a small bowl and set aside to cool. The mixture will look slightly yellow/orange.\nLastly, add the cabbage to a large, heavy-bottom stock pot and just barely cover with water (about 5 cups). Bring the water to a boil over high heat, then lower the temperature to medium-low and simmer for about 8 minutes until the water becomes a deep purple color. Strain the liquid through a cheesecloth-lined strainer, evenly into 2 small bowls and set aside to cool. Add the baking soda to one of the bowls containing the cabbage liquid and delicately stir. The liquid will turn from purple to vibrant blue right before your eyes.\nIn another small bowl, combine equal parts blue and yellow dye to create a green shade. You should now have 5 natural food colors to dye the spaghetti with.\nDivide cooked pasta into 5 1-gallon resealable bags. Add each dye to the bag of spaghetti you'd like to color. The dye should just cover the pasta. Let sit for at least 20 minutes or up to 2 hours. Drain each batch of dyed pasta on a paper towel-lined plate or sheet tray and set aside.\nFor the sauce: In a small saucepan over medium-high heat, combine butter, garlic, shallot, chives, and thyme. Bring the butter to a boil and reduce the heat to medium-low. Simmer the aromatic herbs for about 6 minutes or until fragrant.\nRemove the butter from the heat and add lemon zest, lemon juice, and salt to taste. Strain the butter into a small bowl through a cheesecloth-lined strainer and toss with the rainbow pasta!\nGarnish your colorful creation with parmesan cheese and of course, the parmesan tuile you made earlier.",
            self.harvester_class.instructions(),
        )
