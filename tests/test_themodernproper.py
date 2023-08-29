# mypy: allow-untyped-defs

from recipe_scrapers.themodernproper import TheModernProper
from tests import ScraperTest


class TestTheModernProperScraper(ScraperTest):

    scraper_class = TheModernProper

    def test_host(self):
        self.assertEqual("themodernproper.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("The Modern Proper", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Easy Swedish Meatball Recipe", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("lunch, dinner, appetizers", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://images.themodernproper.com/billowy-turkey/production/posts/2018/swedish-meatballs-13.jpg?w=960&h=540&q=82&fm=jpg&fit=crop&dm=1599768329&s=a12d3adcc54b1d30b5aa25dc6b922e3f",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 lb ground beef",
                "1 lb ground pork",
                "¼ cup flat leaf parsley, minced",
                "½ tsp ground allspice",
                "½ tsp ground nutmeg",
                "¾ cup yellow onion, grated (about 1 medium onion)",
                "2 tsp salt",
                "½ tsp pepper, freshly ground",
                "4 cloves garlic, minced",
                "¾ cup panko*",
                "2 eggs",
                "2 tbsp olive oil",
                "½ cup butter",
                "½ cup flour*",
                "4 cups beef broth",
                "1 tsp salt",
                "¼ tsp pepper",
                "1 tbsp lemon juice",
                "¼ tsp ground allspice",
                "¼ tsp ground nutmeg",
                "1 cup heavy cream",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "In a large bowl, mix the beef, pork, parsley, allspice, nutmeg, grated onion, salt, pepper, garlic, panko and eggs until combined\nUsing a tablespoon or cookie scoop, measure out the meat mixture into roughly 35 (1.5 inch) balls.**In a large pan, heat 2 tablespoon of olive oil over medium-high heat\nAdd ½ of the meatballs and cook until browned on all sides\nThis takes about 5 minutes\nSet aside **When all of the meatballs are browned, pour off any excess grease in the pan, into a heatproof vessel\nLower the heat to medium and add the butter to the pan\nWhen the butter begins to bubble, sprinkle in the flour and cook for 1 minute\nAdd the beef broth to the pan a little at a time.*** Whisk the gravy until the broth is all incorporated\nAdd salt, pepper, lemon juice, allspice and nutmeg\nWhisk a few more times\nSlowly add the cream.Once the gravy begins to simmer****, add the meatballs back into the pan\nSimmer until the gravy has thicken up a bit and the meatballs are cooked all the way through*****, about 8-10 minutes\nServe warm over mashed potatoes or egg noodles, alongside steamed veggies and lingonberry jam",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Swedish", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "These Swedish meatballs are the best you'll ever have. Gently warmed with spices and covered in a heavenly creamy gravy sauce, then served with fluffy mashed potatoes!",
            self.harvester_class.description(),
        )
