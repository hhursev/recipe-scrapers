from recipe_scrapers.seriouseats import SeriousEats
from tests import ScraperTest


class TestSeriousEats(ScraperTest):

    scraper_class = SeriousEats

    @property
    def test_file_name(self):
        return "{}_2".format(self.scraper_class.__name__.lower())

    def test_host(self):
        self.assertEqual("seriouseats.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.seriouseats.com/spaghetti-with-canned-clam-sauce",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Sho Spaeth")

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Spaghetti With Canned-Clam Sauce Recipe"
        )

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        # image has hash keys in it so the full url isn't consistent
        self.assertTrue("canned-clams-pasta-sho-spaeth" in self.harvester_class.image())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "4 tablespoons (60g) unsalted butter, cut into 4 pieces and divided",
                "2 celery ribs (5 oz; 140g), peeled (optional) and cut into small dice",
                "2 medium shallots (60g), minced",
                "1/2 cup (30g) finely chopped fresh parsley leaves, divided",
                "4 medium garlic cloves (15g), finely minced",
                "1 fresh green Thai chili (4g), thinly sliced (optional, see note)",
                "Freshly ground black pepper",
                "Two (8-ounce; 237ml) bottles clam juice",
                "Two (6.5-ounce; 184g) cans chopped or minced clams, clams and liquid divided",
                "1 lb (450g) spaghetti",
                "1 teaspoon (5ml) soy sauce",
                "Kosher salt",
                "Celery leaves (pale yellow-green leaves from the celery heart), for garnish",
                "Lemon wedges, for serving",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "In a 12-inch stainless steel skillet, melt 2 tablespoons of butter over medium heat, and swirl pan until foaming subsides. Add celery, shallots, half the parsley (1/4 cup; 15g), garlic, Thai chili (if using), and a couple healthy grinds of black pepper to pan and cook, stirring occasionally, until vegetables are soft and mixture is fragrant, 1 to 2 minutes. Add bottled clam juice along with liquid from canned clams but not the clam meat. Increase heat to high and bring mixture to a boil, then reduce heat to a simmer until liquid is slightly reduced and vegetables have infused broth, about 5 minutes—there should be enough liquid in the pan to fully submerge the pound of cooked pasta. Turn off heat and add clam meat and soy sauce.",
                    'In a pot of salted, boiling water, cook spaghetti, stirring frequently, until about 4 minutes shy of the way you like your pasta cooked (some would say "al dente"). When spaghetti is almost at that point of doneness, bring pan of clam sauce to a boil over high heat.',
                    "Using tongs, transfer spaghetti to pan with clam sauce, distributing pasta so it is mostly submerged in sauce. Cook, tossing and stirring occasionally, until pasta is cooked to your liking and sauce has thickened slightly, about 4 minutes. Taste for seasoning, and add salt if necessary.",
                    "Turn off heat, add remaining butter and parsley, and toss and stir spaghetti vigorously to incorporate parsley and emulsify butter into sauce. Divide pasta among four serving plates, spooning sauce and clams evenly over each portion. Garnish with celery leaves, and serve immediately, passing lemon wedges, for squeezing, at the table.",
                ]
            ),
            self.harvester_class.instructions(),
        )
