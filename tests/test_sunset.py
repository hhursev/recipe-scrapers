from recipe_scrapers.sunset import Sunset
from tests import ScraperTest


class TestSunsetScraper(ScraperTest):

    scraper_class = Sunset

    def test_host(self):
        self.assertEqual("sunset.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.sunset.com/recipe/crisp-top-sourdough-stuffing",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Crisp-Top Sourdough Stuffing",
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Angela Brassinga")

    def test_total_time(self):
        self.assertEqual(90, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://img.sunset02.com/sites/default/files/styles/4_3_horizontal_-_900x675/public/crisp-top-sourdough-stuffing-su.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 1-pound loaf sourdough, at least 1 day old",
                "1/4 cup salted butter",
                "2 cups chopped onion (1 large)",
                "1 cup chopped celery (2 or 3 stalks)",
                "1/4 cup chopped flat-leaf parsley",
                "1 tablespoon finely chopped fresh sage",
                "About 1/2 tsp. kosher salt",
                "About 1/2 tsp. pepper",
                "About 3 cups turkey broth, reduced-sodium chicken broth, or mushroom or other vegetable broth",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Step 1\n Slice bread into 1 1/2-in.-thick slices and tear into irregular 1- to 2-in. pieces. Spread on a rimmed baking sheet and leave to dry at room temperature until needed (up to 2 days). For the best stuffing, the bread should be very dry.\nStep 2\n Preheat oven to 350°. Melt butter in a large frying pan over medium heat. Pour out 2 tbsp. butter and set aside.\nStep 3\n Add onion, celery, herbs, and 1/2 tsp. each salt and pepper to hot pan. Cook until onions are translucent and celery is tender-crisp, about 15 minutes. Transfer to a large bowl.\nStep 4\n Add torn bread and broth to vegetables and mix in until bread is soaked. Add salt and pepper to taste.\nStep 5\n Generously coat a 9- by 13-in. glass baking pan with 1 tsp. reserved melted butter. Pour stuffing into pan and drizzle with remaining melted butter.\nStep 6\n Cover with foil; bake 25 minutes. Remove foil and bake until starting to brown on top, about 30 minutes more.\nStep 7\nMake ahead: Up to 2 days, chilled. Reheat at 350°, covered, until hot (about 30 minutes). Remove foil and cook 10 more minutes for a crunchy top layer.\nStep 8\nVARIATIONS\nStep 9\nCrisp-Top Sourdough Stuffing with Sausage and Greens: Add 8 oz. sautéed crumbled Italian \xadsausage and 1 lb. briefly sautéed fresh spinach leaves to stuffing before baking.\nStep 10\nScandinavian Stuffing: Replace sourdough with a 1-lb. loaf of crusty rye bread, then add 1 cup chopped fresh dill and 8 oz. diced smoked pork chops to stuffing before baking. Top with 2 tbsp. fresh dill sprigs before serving.",
            self.harvester_class.instructions(),
        )
