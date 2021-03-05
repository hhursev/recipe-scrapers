from recipe_scrapers.littlespicejar import LittleSpiceJar
from tests import ScraperTest


class TestLittleSpiceJarScraper(ScraperTest):

    scraper_class = LittleSpiceJar

    def test_host(self):
        self.assertEqual("littlespicejar.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Easy Addicting Crab Cake Bites (Crab Cake Cups)",
        )

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("24 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://littlespicejar.com/wp-content/uploads/2020/12/Addicting-Mini-Crab-Cake-Bites-1-scaled-720x720.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "Cooking spray, for pan",
                "1 cup panko bread crumbs",
                "½ cup parmesan cheese (shredded or grated)",
                "6 tablespoon melted butter",
                "8 ounces lump crab meat",
                "¾ brick (6 ounces) cream cheese, softened to room temp",
                "1 large egg, lightly beaten",
                "¼ cup mayonnaise",
                "½ cup sour cream",
                "½ teaspoon EACH: garlic powder AND smoked paprika",
                "1 teaspoon EACH: old bay seasoning AND lemon zest",
                "2 teaspoons lemon juice",
                "1 tablespoon chopped chives (plus more for topping)",
                "Salt and white pepper (or black)",
                "Serve with sauce (in notes)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "PANKO: Position a rack in the center of the oven and preheat the oven to 400ºF. Grease a mini muffin pan with cooking spray. Mix together the panko, parmesan cheese, and melted butter. Place roughly 2 teaspoons of the panko mixture in the bottom of each muffin cup using your fingers or the bottom of a measuring teaspoon (or tablespoon) gently pack into a tight shape.\nCRAB MIXTURE: Combine the crab meat, cream cheese, mayonnaise, egg, sour cream garlic powder, smoked paprika, old bay seasoning, lemon juice + zest, chopped chives, and ¼ teaspoon kosher salt, and ¼ teaspoon pepper. Spoon roughly 1 tablespoon of the crab mixture into each mini muffin cup.\nBAKE: Until the edges begin to turn golden, 14-18 minutes. Allow the crab cakes to cool in the pan for several minutes before attempting to remove them. You can run an offset spatula or a pairing knife along the edges to help pop out the bites. Serve crab bites warm or allow them to cool to room temperature before serving. I like to top them with more chopped chives before serving and serve with lemon wedges and prepared sauce.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
