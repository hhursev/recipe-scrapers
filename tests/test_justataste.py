from recipe_scrapers.justataste import JustATaste
from tests import ScraperTest


class TestJustATasteScraper(ScraperTest):

    scraper_class = JustATaste

    def test_host(self):
        self.assertEqual("justataste.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Baked Chicken and Cheese Taquitos"
        )

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.justataste.com/wp-content/uploads/2013/04/Healthy-Baked-Chicken-Taquitos.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "3 Tablespoons olive oil",
                "1 cup diced onion",
                "2 cloves garlic, minced",
                "2 Tablespoons fresh lime juice",
                "1 1/2 teaspoons cumin",
                "1 1/2 teaspoons paprika",
                "1/4 teaspoon salt",
                "1/4 teaspoon fresh black pepper",
                "3 cups shredded rotisserie chicken",
                "1 cup shredded cheddar or Mexican blend cheese",
                "1 1/2 cups low sodium chicken broth",
                "12 (6-inch) corn tortillas (See Kelly's Notes)",
                "Homemade guacamole, for serving",
                "Homemade salsa, for serving",
            ],
            self.harvester_class.ingredients(),
        )

    def test_total_time(self):
        return self.assertEqual(55, self.harvester_class.total_time())

    def test_ratings(self):
        return self.assertEqual(4.5, self.harvester_class.ratings())

    def test_instructions(self):
        return self.assertEqual(
            "Preheat the oven to 425ºF and line a baking sheet with parchment paper.\nIn a large saucepan, heat the olive oil over medium heat. Add the diced onion and cook until it's translucent, 3 to 5 minutes. Add the garlic, and cook, stirring occasionally, for about 3 minutes until it's golden and fragrant.\nReduce the heat to low, and then add the lime juice, cumin, paprika, salt and black pepper to the pan, stirring to combine. Add the shredded chicken, tossing to combine.\nTransfer the chicken mixture to a large bowl and let it cool for 10 minutes, and then stir in the shredded cheese.\nIn a medium saucepan over medium heat, bring the chicken broth to a simmer. One at a time, dip each tortilla into the broth for 10 to 15 seconds, just until it's pliable enough to roll. Transfer the tortilla to your work surface and place about 3 tablespoons of the chicken mixture on the lower third of each tortilla. Tightly roll up the tortilla, and then place it seam-side down on the prepared baking sheet. Repeat the filling and rolling process with the remaining tortillas.\nBake the taquitos for 15 to 20 minutes until golden brown and crispy. Serve with guacamole and salsa.\nKelly's Notes:\nTaquitos are traditionally made with corn tortillas, however you can use flour tortillas, which are much more pliable, and thus easier to roll. The key to successfully rolling the corn tortillas (without them cracking), is to rely on the quick dip in the simmering (it must be warm!) chicken broth to loosen them up. Don't skip that step, or your corn tortillas will crack during the rolling process.\n★ Did you make this recipe? Don't forget to give it a star rating below!",
            self.harvester_class.instructions(),
        )
