from recipe_scrapers.domesticateme import DomesticateMe
from tests import ScraperTest


class TestDomesticateMeScraper(ScraperTest):

    scraper_class = DomesticateMe

    def test_host(self):
        self.assertEqual("domesticate-me.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://domesticate-me.com/dude-diet-buffalo-chicken-quinoa-bake/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "The Dude Diet: Buffalo Chicken Quinoa Bake"
        )

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://domesticate-me.com/wp-content/uploads/2018/03/Buffalo-Chicken-Quinoa-Bake-2.jpg",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_rating(self):
        self.assertEqual(4.5, self.harvester_class.ratings())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 cup quinoa",
                "1½ cups low-sodium chicken broth",
                "1 tablespoon extra-virgin olive oil",
                "1½ cups cauliflower “rice” (aka very finely chopped cauliflower florets)",
                "½ medium yellow onion (minced)",
                "½ cup finely chopped carrots",
                "½ cup finely chopped celery",
                "2 cups diced or shredded chicken breast",
                "½ cup Frank’s Red Hot Buffalo Wing Sauce (plus extra for serving)",
                "¾ cup grated sharp cheddar cheese",
                "¾ cup grated provolone cheese (Gouda is also great!)",
                "¼ cup whole-wheat panko breadcrumbs",
                "3 scallions (thinly sliced (optional))",
                "For the Yogurt Ranch:",
                "1½ cups nonfat plain Greek yogurt",
                "1 teaspoon dried parsley (crushed (Just use your fingers to crush the flakes.))",
                "½ teaspoon dried dill weed",
                "½ teaspoon kosher salt",
                "¼ teaspoon garlic powder",
                "¼ teaspoon black pepper",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Combine the quinoa and chicken broth in a small saucepan and bring to a boil. Lower to a simmer, cover the saucepan with a lid, and cook for 14 minutes, or until all of the liquid has been absorbed. Let the quinoa rest, covered, for 5 minutes, then fluff with a fork.\nMeanwhile, whip up the yogurt ranch! In a medium bowl, whisk all the ingredients for the ranch. Briefly set that deliciousness aside.\nPre-heat the oven to 375 degrees.\nHeat the olive oil in a large ovenproof skillet or shallow Dutch oven over medium heat. When the oil is hot and shimmering, add the cauliflower, onion, carrot, and celery. Cook for 5 minutes until the onion is translucent and the vegetables are tender. Add the cooked quinoa, chicken, and Frank’s to the pan and fold everything together. Turn off the heat and fold in 1 cup of the yogurt ranch and half of the cheddar and provolone. Taste the filling. Add a little extra Frank’s if you deem it necessary.\nSmooth the top of the filling with a spatula. Add the remaining cheese in an even layer and sprinkle with the panko.\nBake for 25 minutes until the cheese is melted and bubbling. If you want to brown the top of the bake (I DO!!), pop the casserole under the broiler for 1 to 2 minutes until the bread crumbs turn golden brown.\nWhisk a tablespoon or so of water into the remaining yogurt ranch just until it has a drizzle-able consistency. Serve the quinoa bake drizzled with as much extra ranch and Frank’s as you like and garnish with scallions.",
            self.harvester_class.instructions(),
        )
