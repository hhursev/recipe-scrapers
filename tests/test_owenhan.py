from recipe_scrapers.owenhan import OwenHan
from tests import ScraperTest


class TestOwenHanScraper(ScraperTest):

    scraper_class = OwenHan

    def author(self):
        self.assertEqual("Owen Han", self.harvester_class.host())

    def test_host(self):
        self.assertEqual("owen-han.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual("Chicken Bacon Ranch", self.harvester_class.title())

    def test_image(self):
        self.assertEqual(
            "http://static1.squarespace.com/static/627be79397093e2de753b260/627c408602fed77ca384eb11/63120c4090e9bf706973d712/1662127792157/IMG_2037.jpg?format=1500w",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "Baguette",
                "1 chicken breast",
                "3 slices bacon",
                "Salt + Pepper",
                "Oregano",
                "Pepper Jack cheese",
                "Avocado",
                "Pickled onions",
                "1 cup plain non fat greek yogurt",
                "1/3 cup buttermilk",
                "1 lemon juiced",
                "1 tbsp fresh parsley",
                "1 tbsp fresh dill",
                "2 tsp garlic powder",
                "2 tsp onion powder",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        expected_instructions = [
            "Cut the chicken and bacon into even thin strips.",
            "Place bacon in a skillet over medium heat. Cook until it's almost completely cooked, but not too crispy.",
            "Remove the bacon and add the chicken to the skillet.",
            "Season with oregano and lightly with salt. Cook until no longer pink.",
            "Turn off the heat, add the bacon back to the skillet and combine.",
            "Add pepper jack on top and cover to melt.",
            "For the ranch combine all the ingredients to a bowl and mix well to combine.",
            "Assemble: to a toasted baguette add the chicken and bacon then top with sliced avocado pickled onions, and ranch. Add some mixed greens to the other half. ",
            "Close the sandwich, cut in half and enjoy!",
        ]
        expected_instructions = "\n".join(expected_instructions)
        self.assertEqual(expected_instructions, self.harvester_class.instructions())
