from recipe_scrapers.castironketo import CastIronKeto
from tests import ScraperTest


class TestCastIronKetoScraper(ScraperTest):

    scraper_class = CastIronKeto

    def test_host(self):
        self.assertEqual("castironketo.net", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.castironketo.net/blog/keto-jalapeno-popper-casserole-with-chicken/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Keto Jalapeño Popper Casserole with Chicken"
        )

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.castironketo.net/wp-content/uploads/2021/01/Keto-Jalapeño-Popper-Casserole.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 ½ lbs cooked shredded chicken breast",
                "4 green onions (chopped)",
                "1 teaspoon garlic salt",
                "½ teaspoon onion powder",
                "½ teaspoon paprika",
                "8 oz cream cheese (softened)",
                "½ cup heavy cream",
                "¼ cup chicken broth",
                "5 jalapeno peppers (halved (ribs removed if you like less spice))",
                "1 cup shredded sharp cheddar cheese",
                "6 slices bacon (cooked and crumbled)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat the oven to 425° F.\nPlace the chicken in the bottom of a 10” or larger cast iron skillet. Top with green onions.\nCombine the garlic salt, onion powder, paprika, cream cheese, heavy cream, and chicken bone broth in a small bowl. Mix until combined.\nPour the cream cheese mixture over the chicken then top with the slices of jalapeno. Sprinkle the cheddar cheese over the top then top with the crumbled bacon.\nTransfer the skillet to the oven and bake for 15 minutes until the cheese is bubbly. Serve immediately.",
            self.harvester_class.instructions(),
        )
