from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.twopeasandtheirpod import TwoPeasAndTheirPod
from tests import ScraperTest


class TestTwoPeasAndTheirPodScraper(ScraperTest):

    scraper_class = TwoPeasAndTheirPod
    test_file_name = "twopeasandtheirpod_1"

    def test_host(self):
        self.assertEqual("twopeasandtheirpod.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.twopeasandtheirpod.com/baked-chicken-taquitos/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Chicken Taquitos")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Maria Lichty")

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("20 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 cups shredded chicken, (we use rotisserie chicken)",
                "1/2 teaspoon ground cumin",
                "1/2 teaspoon ground chili powder",
                "1/2 teaspoon kosher salt",
                "1/4 teaspoon garlic powder",
                "1/4 teaspoon paprika",
                "2 teaspoons fresh lime juice",
                "1 cup shredded cheddar or Mexican blend cheese",
                "20 corn tortillas",
                "Shredded lettuce",
                "Diced tomatoes",
                "Guacamole",
                "Sour Cream",
                "Chopped Green Onion",
                "Crumbled Queso Fresco",
                "Pico de Gallo",
                "Salsa",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "2 cups shredded chicken, (we use rotisserie chicken)",
                        "1/2 teaspoon ground cumin",
                        "1/2 teaspoon ground chili powder",
                        "1/2 teaspoon kosher salt",
                        "1/4 teaspoon garlic powder",
                        "1/4 teaspoon paprika",
                        "2 teaspoons fresh lime juice",
                        "1 cup shredded cheddar or Mexican blend cheese",
                        "20 corn tortillas",
                    ],
                    purpose="For the Taquitos:",
                ),
                IngredientGroup(
                    ingredients=[
                        "Shredded lettuce",
                        "Diced tomatoes",
                        "Guacamole",
                        "Sour Cream",
                        "Chopped Green Onion",
                        "Crumbled Queso Fresco",
                        "Pico de Gallo",
                        "Salsa",
                    ],
                    purpose="For the Toppings:",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat the oven to 425 degrees F. Spray a large baking sheet with nonstick cooking spray and set aside.\nIn a medium bowl, combine the shredded chicken with the cumin, chili powder, salt, garlic powder, paprika, and fresh lime juice. Stir until chicken is well coated with the seasonings. Stir in the shredded cheese.\nGet two paper towels damp and place two tortillas at a time in between the paper towels. Place in the microwave for 20-30 seconds. Remove from the microwave and roll up the taquitos.\nPlace a heaping tablespoon of the chicken and cheese mixture in the center of the tortilla and roll it up tightly. Place the taquito, seam side down on the prepared baking sheet. Continue rolling taquitos until the tortillas and filling are gone. You should have about 20 taquitos.\nSpray the taquitos generously with nonstick cooking spray. Bake for 15-20 minutes or until taquitos are golden brown and crispy. Remove from the oven and serve warm with desired toppings.",
            self.harvester_class.instructions(),
        )

    def test_image(self):
        return self.assertEqual(
            "https://www.twopeasandtheirpod.com/wp-content/uploads/2017/03/Baked-Chicken-Taquitos-1.jpg",
            self.harvester_class.image(),
        )
