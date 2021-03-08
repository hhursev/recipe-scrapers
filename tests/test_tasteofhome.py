from recipe_scrapers.tasteofhome import TasteOfHome
from tests import ScraperTest


class TestTasteOfHomeScraper(ScraperTest):

    scraper_class = TasteOfHome

    def test_host(self):
        self.assertEqual("tasteofhome.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Taste of Home", self.harvester_class.author())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.tasteofhome.com/recipes/pressure-cooker-sauerbraten/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Pressure-Cooker Sauerbraten")

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings.", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://tmbidigitalassetsazure.blob.core.windows.net/rms3-prod/attachments/37/1200x1200/Pressure-Cooker-Sauerbraten_EXPS_THN18_39243_E06_06_2b.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "4 whole cloves",
                "4 whole peppercorns",
                "1 bay leaf",
                "1/2 cup water",
                "1/2 cup white vinegar",
                "2 teaspoons sugar",
                "1/2 teaspoon salt",
                "Dash ground ginger",
                "1 pound boneless beef top round steak, cut into 1-inch cubes",
                "3 medium carrots, cut into 1/2-inch slices",
                "2 celery ribs, cut into 1/2-inch slices",
                "1 small onion, chopped",
                "1/3 cup crushed gingersnaps",
                "Hot cooked egg noodles",
                "Optional: Chopped fresh parsley and coarsely ground pepper",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Place cloves, peppercorns and bay leaf on a double thickness of cheesecloth; bring up corners of cloth and tie with kitchen string to form a bag. In a large bowl, combine the water, vinegar, sugar, salt and ginger. Add beef and spice bag; let stand at room temperature for 30 minutes.\nTransfer all to a 6-qt. electric pressure cooker. Add carrots, celery and onion. Lock the lid and close pressure-release valve. Adjust to pressure-cook on high for 10 minutes. Quick-release pressure. Select saute setting and adjust for medium heat; bring liquid to a boil. Discard the spice bag. Stir in gingersnaps; cook and stir until thickened, about 3 minutes. Serve with egg noodles. If desired, top with parsley and pepper.\nFreeze option: Freeze cooled sauerbraten in freezer containers. To use, partially thaw in refrigerator overnight. Heat through in a saucepan, stirring occasionally; add a little broth or water if necessary.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.25, self.harvester_class.ratings())
