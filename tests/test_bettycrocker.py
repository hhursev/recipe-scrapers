from recipe_scrapers.bettycrocker import BettyCrocker
from tests import ScraperTest


class TestBettyCrocker(ScraperTest):

    scraper_class = BettyCrocker

    def test_host(self):
        self.assertEqual("bettycrocker.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.bettycrocker.com/recipes/eclair-bars/0cb1d3f0-f074-400b-aa5a-5e729102c4ec",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Éclair Bars")

    def test_total_time(self):
        self.assertEqual(290, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("24 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://images-gmi-pmc.edge-generalmills.com/e1306219-6178-4e15-afaf-ba6e527f1e6b.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        return self.assertEqual(
            [
                "1 can (8 oz) refrigerated Pillsbury™ Original Crescent Dough Sheet",
                "2 boxes (3.4 oz each) Jell-O™ vanilla-flavor instant pudding & pie filling mix",
                "3 cups cold half-and-half",
                "1 1/2 cups semisweet chocolate chips",
                "3/4 cup heavy whipping cream",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Heat oven to 375°F. Spray bottom only of 13x9-inch pan with cooking spray.",
                    "Unroll crescent dough; press in bottom of pan. Bake 12 to 14 minutes or until golden brown and baked through. Remove from oven to cooling rack; cool 20 minutes.",
                    "In medium bowl, beat dry pudding mixes and half-and-half with whisk about 2 minutes or until thick. Spread over cooled bar base.",
                    "In medium microwavable bowl, microwave chocolate chips and whipping cream uncovered on High 1 minute; stir. Microwave 30 seconds; stir until smooth. Carefully spread mixture on top of pudding layer. Refrigerate about 4 hours or until cooled completely.",
                    "When ready to serve, using a sharp knife and up-and-down sawing motion for cleaner cuts, cut into 6 rows by 4 rows. Store covered in refrigerator.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.5, self.harvester_class.ratings())
