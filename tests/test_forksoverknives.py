from recipe_scrapers.forksoverknives import ForksOverKnives
from tests import ScraperTest


class TestTimesOfIndiaScraper(ScraperTest):

    scraper_class = ForksOverKnives

    def test_host(self):
        self.assertEqual("forksoverknives.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Darshana Thacker", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Butternut Squash Mac and Cheese with Broccoli",
            self.harvester_class.title(),
        )

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 cups", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.forksoverknives.com/wp-content/uploads/butternut-broccoli-mac-and-cheese-wordpress.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 medium butternut squash (1¾ lb.)",
                "1 onion, finely chopped (1 cup)",
                "4 cloves garlic, minced",
                "½ teaspoon finely chopped fresh thyme",
                "2 cups unsweetened, unflavored plant milk, such as almond, soy, cashew, or rice",
                "2 tablespoons nutritional yeast",
                "1 tablespoon white wine vinegar",
                "¼ tsp. sea salt",
                "⅛ tsp. freshly ground black pepper",
                "3 cups dried whole grain penne pasta (8 oz.)",
                "3 cups small broccoli florets",
                "Fresh basil leaves",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Peel squash; halve squash and remove seeds. Cut squash into large pieces. Place squash pieces in a steamer basket in a large pan. Add water to saucepan to just below basket. Bring to boiling. Steam, covered, about 12 minutes or until tender.\nHeat a large saucepan over medium. Add onion, garlic, thyme, and ¼ cup water to pan. Cook about 10 minutes or until onion is tender, stirring occasionally and adding water, 1 to 2 Tbsp. at a time, as needed to prevent sticking.\nTransfer onion mixture to a blender. Add squash and the next five ingredients (through pepper). Cover and blend until smooth. Pour squash mixture into a large saucepan.\nCook pasta according to package directions, adding broccoli the last 5 minutes of cooking; drain. Add drained pasta and broccoli to squash mixture; toss to coat. Serve warm topped with fresh basil.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_language(self):
        self.assertEqual("en-US", self.harvester_class.language())
