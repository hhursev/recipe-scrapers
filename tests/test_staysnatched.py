# mypy: allow-untyped-defs

from recipe_scrapers.staysnatched import StaySnatched
from tests import ScraperTest


class TestStaySnatchedScraper(ScraperTest):

    scraper_class = StaySnatched

    def test_host(self):
        self.assertEqual("staysnatched.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            "Slow Cooker Chili Mac and Cheese", self.harvester_class.title()
        )

    def test_author(self):
        self.assertEqual("Brandi Crawford", self.harvester_class.author())

    def test_category(self):
        self.assertEqual("dinner,lunch", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(210, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("7 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.staysnatched.com/wp-content/uploads/2016/12/crock-pot-chili-mac-6.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 cup chopped onions",
                "1/2 cup chopped red peppers",
                "1/2 cup chopped green peppers",
                "3 garlic cloves (Minced)",
                "1 pound ground beef or ground turkey",
                "2 cups elbow macaroni",
                "15 oz fire roasted tomatoes",
                "15 oz canned black beans (Drained. You can use any canned beans you like.)",
                "15 oz canned chili beans (Drained.)",
                "1 cup beef broth",
                "1 cup shredded cheddar cheese ( I use sharp.)",
                "1 cup shredded Monterey jack cheese",
                "1 tablespoon chili powder",
                "1 teaspoon cumin",
                "1 teaspoon oregano (Dried or ground.)",
                "1 teaspoon cayenne pepper (Optional for spicy. Adjust to taste.)",
                "salt and pepper to taste",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Heat a skillet on medium-high heat.\nAdd the ground beef and the chili seasoning. Break down the ground beef with a meat chopper.\nStir and cook until the beef is no longer pink. Drain any excess fat from the beef if necessary.\nAdd in the red peppers, green peppers, onions, and garlic. Cook until the vegetables are soft.\nAdd the cooked beef and vegetables to the slow cooker along with the remaining ingredients (with the exception of the cheese).\nCook on Low for 3 to 3 1/2 hours or on High for 1 1/2 to 2 hours. Check in periodically. It has finished cooking when the pasta is soft.\nAbout 10-15 minutes prior to serving, add the cheese to the cooker. Sprinkle it throughout the top.\nAllow 10-15 minutes for the cheese to melt.\nCool before serving.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.89, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "This Slow Cooker Chili Mac and Cheese is hearty, delicious, and loaded with veggies. Load up your Crockpot for this easy weeknight dinner.",
            self.harvester_class.description(),
        )
