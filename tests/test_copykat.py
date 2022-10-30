from recipe_scrapers.copykat import CopyKat
from tests import ScraperTest


class TestCopyKat(ScraperTest):

    scraper_class = CopyKat

    def test_host(self):
        self.assertEqual("copykat.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://copykat.com/make-tender-beef-tips-in-gravy/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Make Tender Beef Tips and Gravy"
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Stephanie Manley")

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("10 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://copykat.com/wp-content/uploads/2020/11/Beef-Tips-and-Gravy-Pin2.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 cup flour",
                "1 teaspoon salt",
                "1/4 teaspoon black pepper",
                "3 pounds lean chuck roast",
                "48 ounces beef stock",
                "1 tablespoon vegetable oil",
                "2 teaspoons gravy master",
                "1 cup onions (chopped)",
                "16 ounces noodles (or rice for serving)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "In a small bowl add flour, salt, and pepper. Stir the salt and pepper into the flour. Cut and trim roast into small bite-sized pieces. Dredge beef pieces in seasoned flour shake off excess flour.\nInstant Pot Directions\nSet the Instant Pot to saute, add oil. When the oil has heated drop in several pieces of the beef. Cook seasoned beef on all sides until lightly browned. Cook beef in small batches. When all of the beef is cooked add it back to the Instant Pot.\nAdd 1 cup of onion, two teaspoons of Gravy Master, and beef stock. Place lid on high and cook for 15 minutes on high pressure. Release pot after cooking with either a quick release or a natural release.\nSlow Cooker Directions\nBrown the beef in a large skillet in small batches with some vegetable oil. Add the browned beef, beef broth, onion, and Gravy Master to the slow cooker. Cook for 4 to 6 hours on low.\nIf the liquid hasn't thickened up to your desired consistency, you can thicken it up by mixing 1 tablespoon of butter and one tablespoon of flour together. Stir this into the liquid and it will thicken up the gravy in the slow cooker.\nServing\nPrepare noodles or rice according to package instructions.\nServe beef tips and gravy over noodles or rice.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "You can make amazingly tender beef tips and gravy in an Instant Pot or slow cooker.",
            self.harvester_class.description(),
        )
