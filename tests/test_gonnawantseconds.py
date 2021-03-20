from recipe_scrapers.gonnawantseconds import GonnaWantSeconds
from tests import ScraperTest


class TestGonnaWantSeconds(ScraperTest):

    scraper_class = GonnaWantSeconds

    def test_host(self):
        self.assertEqual("gonnawantseconds.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.gonnawantseconds.com/sour-cream-chicken-enchiladas/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Sour Cream Chicken Enchiladas (30-Min. Meal!)",
        )

    def test_total_time(self):
        self.assertEqual("30", self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("5 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.gonnawantseconds.com/wp-content/uploads/2020/01/Sour-Cream-Enchiladas-03-360x361.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "Filling:",
                "2 tablespoons vegetable oil",
                "1 cup onion, diced",
                "1 package taco seasoning",
                "1 (10-ounce) can Rotel, drained",
                "1/2 teaspoon salt",
                "1/2 teaspoon black pepper",
                "2 cups cooked chicken, shredded",
                "1/2 cups sour cream",
                "1 cups Monterey jack cheese, shredded",
                "10 (8-inch) flour tortillas",
                "Sauce:",
                "3 tablespoons butter",
                "3 tablespoons all-purpose flour",
                "2 cups chicken broth",
                "1 cup sour cream",
                "1 (4-ounce) can chopped green chiles, drained",
                "Topping:",
                "2 cups Monterey jack cheese, shredded",
                "Garnish (optional): ",
                "2 tablespoons chopped cilantro or green onions",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Preheat oven to 350 degrees. Spray a 9X13 inch baking dish with nonstick cooking spray; set aside",
                    "Make Filling and Roll:",
                    "Add oil to a large skillet and saute onion until it's translucent and soft. Add taco seasoning, salt, pepper, and Rotel and stir to combine. Add shredded chicken and toss to evenly coat with onion and seasoning mixture. Remove from the heat, cover, and set aside.\nIn a medium bowl, stir together 1 cup Monterey Jack and 1/2 cup sour cream until evenly combined.\nFill tortillas with a layer of the chicken mixture then a layer of the cheese mixture and roll each one and place seam side down, in the prepared pan.",
                    "Make Sauce:",
                    "Melt the butter in a skillet. Sprinkle flour over melted butter and whisk to combine. Cook for 1 minute to remove the flour taste. Remove the skillet from heat and whisk in broth.\nPlace back on the heat and cook until the mixture has thickened and is bubbly. Cool sauce for 3-5 minutes. (Don't skip this step- if the sauce is too hot and you add the sour cream it will curdle it-yuck!) Add sour cream and chilies and stir until sauce is smooth and sour cream is completely dissolved.\nPour sauce over enchiladas and add remaining cheese over top. Bake in preheated oven for 20-25 minutes or until enchiladas are heated through and sauce is bubbly. Turn on the broiler and broil until the top is nicely golden. Garnish with chopped cilantro or green onions and serve.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "Sour cream chicken enchiladas bake to golden perfection in just 30 minutes with a sauce that will be your new obsession!!",
            self.harvester_class.description(),
        )
