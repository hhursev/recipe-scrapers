from recipe_scrapers.justataste import JustATaste
from tests import ScraperTest


class TestJustATasteScraper(ScraperTest):

    scraper_class = JustATaste

    def test_host(self):
        self.assertEqual("justataste.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Baked Chicken and Cheese Taquitos (Oven or Air Fryer)",
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Kelly Senyei")

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.justataste.com/wp-content/uploads/2018/04/baked-air-fryer-cheese-taquitos.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 Tablespoons extra-virgin olive oil",
                "1 cup diced yellow onion",
                "2 cloves garlic, minced",
                "2 Tablespoons fresh lime juice",
                "1 1/2 teaspoons ground cumin",
                "1 1/2 teaspoons paprika",
                "1/4 teaspoon kosher salt",
                "1/4 teaspoon fresh black pepper",
                "3 cups shredded rotisserie chicken",
                "1 cup shredded cheddar or Mexican blend cheese",
                "12 (6-inch) flour tortillas",
            ],
            self.harvester_class.ingredients(),
        )

    def test_total_time(self):
        return self.assertEqual(55, self.harvester_class.total_time())

    def test_ratings(self):
        return self.assertEqual(4.5, self.harvester_class.ratings())

    def test_instructions(self):
        return self.assertEqual(
            "Preheat the oven to 425ºF and line a baking sheet with parchment paper. (See Kelly's Notes for air fryer instructions.)\nIn a large saucepan, heat the olive oil over medium heat. Add the diced onion and cook until it's translucent, 3 to 5 minutes. Add the garlic, and cook, stirring occasionally, for about 3 minutes until it's golden and fragrant.\nReduce the heat to low, and then add the lime juice, cumin, paprika, salt and black pepper to the pan, stirring to combine. Add the shredded chicken, tossing to combine.\nTransfer the chicken mixture to a large bowl and let it cool for 10 minutes, and then stir in the shredded cheese.\nArrange the tortillas on work surface then place about 3 tablespoons of the chicken mixture on the lower third of each tortilla. Tightly roll up the tortilla, secure it with a toothpick, and then place it seam-side down on the prepared baking sheet. Repeat the filling and rolling process with the remaining tortillas.\nBake the taquitos for 15 to 20 minutes until golden brown and crispy. (See below for air fryer instructions.) Serve with guacamole and salsa.\nKelly's Notes:\nTaquitos are traditionally made with corn tortillas, however you can use flour tortillas, which are much more pliable, and thus easier to roll.\nTo cook the taquitos in an air fryer: Preheat the air fryer to 400°F. Grease the basket with cooking spray then arrange a portion of the taquitos in an even layer. Coat the taquitos with cooking spray then air-fry them until golden brown and crispy, about 8 minutes.",
            self.harvester_class.instructions(),
        )
