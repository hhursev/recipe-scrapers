from recipe_scrapers.foodnetwork import FoodNetwork
from tests import ScraperTest


class TestFoodNetworkScraper(ScraperTest):

    scraper_class = FoodNetwork

    def test_host(self):
        self.assertEqual("foodnetwork.com", self.harvester_class.host())

    def test_canonical_url(self):
        # TODO: Find a way to supply original content base URL at test-time (via WARC-file?)
        self.assertEqual(
            "https://test.example.com/foodnetwork.testhtml_files/chicken-marsala-recipe-1951778.html",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Chicken Marsala")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Tyler Florence")

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2009/4/10/1/FO1D47_24021_s4x3.jpg.rend.hgtvcom.406.305.suffix/1431766598136.jpeg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "4 skinless, boneless, chicken breasts (about 1 1/2 pounds)",
                "All-purpose flour, for dredging",
                "Kosher salt and freshly ground black pepper",
                "1/4 cup extra-virgin olive oil",
                "4 ounces prosciutto, thinly sliced",
                "8 ounces crimini or porcini mushrooms, stemmed and halved",
                "1/2 cup sweet Marsala wine",
                "1/2 cup chicken stock",
                "2 tablespoon unsalted butter",
                "1/4 cup chopped flat-leaf parsley",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Put the chicken breasts side by side on a cutting board and lay a piece of plastic wrap over them; pound with a flat meat mallet, until they are about 1/4-inch thick. Put some flour in a shallow platter and season with a fair amount of salt and pepper; mix with a fork to distribute evenly.\nHeat the oil over medium-high flame in a large skillet. When the oil is nice and hot, dredge both sides of the chicken cutlets in the seasoned flour, shaking off the excess. Slip the cutlets into the pan and fry for 5 minutes on each side until golden, turning once – do this in batches if the pieces don't fit comfortably in the pan. Remove the chicken to a large platter in a single layer to keep warm.\nLower the heat to medium and add the prosciutto to the drippings in the pan, saute for 1 minute to render out some of the fat. Now, add the mushrooms and saute until they are nicely browned and their moisture has evaporated, about 5 minutes; season with salt and pepper. Pour the Marsala in the pan and boil down for a few seconds to cook out the alcohol. Add the chicken stock and simmer for a minute to reduce the sauce slightly. Stir in the butter and return the chicken to the pan; simmer gently for 1 minute to heat the chicken through. Season with salt and pepper and garnish with chopped parsley before serving.",
            self.harvester_class.instructions(),
        )
