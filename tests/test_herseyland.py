# mypy: allow-untyped-defs

from recipe_scrapers.herseyland import HerseyLand
from tests import ScraperTest


class TestHerseyLandScraper(ScraperTest):

    scraper_class = HerseyLand

    def test_host(self):
        self.assertEqual("hersheyland.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Herseyland", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            'HERSHEY\'S "Perfectly Chocolate" Chocolate Cake | Recipes',
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual("Tags", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("1 serving", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://publish-p50513-e440257.adobeaemcloud.com/content/dam/hersheyland/en-us/recipes/recipe-images/2_Hersheys_Perfectly_Chocolate_Cake_11-18.jpeg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 cups sugar",
                "1-3/4 cups all-purpose flour",
                "3/4 cup HERSHEY'S Cocoa",
                "1-1/2 tsps baking powder",
                "1-1/2 tsps baking soda",
                "1 tsp salt",
                "2 eggs",
                "1 cup milk",
                "1/2 cup vegetable oil",
                "2 tsps vanilla extract",
                "1 cup boiling water",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        expected_instructions = 'Step 1\nHeat oven to 350°F. Grease and flour two 9-inch round baking pans.\nStep 2\nStir together sugar, flour, cocoa, baking powder, baking soda and salt in large bowl. Add eggs, milk, oil and vanilla; beat on medium speed of mixer 2 minutes. Stir in boiling water (batter will be thin). Pour batter into prepared pans.\nStep 3\nBake 30 to 35 minutes or until wooden pick inserted in center comes out clean. Cool 10 minutes; remove from pans to wire racks. Cool completely. Frost with "Perfectly Chocolate" Chocolate Frosting.'
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_description(self):
        expected_description = "The words “perfect” and “chocolate cake” basically have the same meaning, right? With HESHERY’S homemade chocolate cake this seems to be true. Baking from scratch is easier than you think when you mix HERSHEY’S cocoa with a few other simple ingredients. Bake this delicious dessert when you’re hosting the next family get-together, celebrating a birthday or wanting a bite of delicious chocolate cake after dinner. This “perfectly chocolate” cake was made for sharing, so get out your best plates, have a pitcher of milk ready and divvy out this chocolatey cake with your favorite people."
        self.assertEqual(expected_description, self.harvester_class.description())
