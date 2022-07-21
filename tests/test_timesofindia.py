from recipe_scrapers.timesofindia import TimesOfIndia
from tests import ScraperTest


class TestTimesOfIndiaScraper(ScraperTest):

    scraper_class = TimesOfIndia

    def test_host(self):
        self.assertEqual("recipes.timesofindia.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("TNN", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Stuffed Tortellini Recipe", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://static.toiimg.com/thumb/71330969.cms?width=1200&height=900",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "500 gm cherry tomatoes",
                "1 teaspoon spice oregano",
                "black pepper as required",
                "2 cloves garlic",
                "1/4 cup parmesan cheese",
                "water as required",
                "4 tablespoon extra virgin olive oil",
                "salt as required",
                "250 gm pasta tortelleni",
                "2 teaspoon pesto sauce",
                "6 basil",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "To prepare this palatable dish, preheat the oven at 200 degrees Celsius. Meanwhile, spread a baking sheet, place cherry tomatoes topped with a drizzle of 2 tablespoons of extra virgin olive oil. Season the tomatoes with salt, black pepper, and oregano spice. Make sure the tomatoes are evenly coated with the seasoned oil by rolling them over and over inside the baking sheet itself.\nBy now, the oven should be ready to roast. Place the baking sheet with tomatoes inside the oven and roast the tomatoes for 15 minutes or until they start to burst out.\nWhile the tomatoes are roasting in the oven, put a large pan over medium flame and boil water in it. Add the tortellini pasta with a pinch of salt and a little olive oil. Once cooked, drain the water and keep the pasta aside until required.\nNow, heat 2 tablespoons of extra virgin olive oil in a skillet over low-medium heat. After the oil turns hot, add minced garlic and saute until it turns golden brown. Turn off the flame and to the garlic, add roasted tomatoes and pesto sauce. Using a fork, stab the tomatoes to break them open. Stir the mixture and then add cooked tortellini. Pour some more pesto sauce over the tortellini and continue stirring. Sprinkle shredded parmesan cheese and garnish with torn or chopped basil leaves.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_language(self):
        self.assertEqual("en", self.harvester_class.language())

    def test_cuisine(self):
        self.assertEqual("Italian", self.harvester_class.cuisine())
