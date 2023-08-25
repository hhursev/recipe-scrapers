from recipe_scrapers.thespruceeats import TheSpruceEats
from tests import ScraperTest


class TestTheSpruceEatsScraper(ScraperTest):

    scraper_class = TheSpruceEats
    test_file_name = "thespruceeats_1"

    def test_host(self):
        self.assertEqual("thespruceeats.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.thespruceeats.com/doner-kebab-recipe-4171703",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Homemade Doner Kebab")

    def test_total_time(self):
        self.assertEqual(140, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.thespruceeats.com/thmb/cvoXe0xiaLRO4FO8T8OTXWSw5K0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/aqIMG_1498fsq-5b343910c9e77c001a218bd0.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            sorted(
                [
                    "1 pound ground lamb",
                    "1 large egg",
                    "4 clove garlic",
                    "1 teaspoon ground cumin",
                    "1 teaspoon ground coriander",
                    "1 teaspoon smoked paprika",
                    "1 teaspoon dried oregano",
                    "1/2 teaspoon kosher salt",
                    "1/4 teaspoon ground black pepper",
                    "1 tablespoon oil",
                    "4 large pita",
                    "1 cup lettuce",
                    "1 large tomato,",
                    "1/2 medium English cucumber",
                    "1/4 large red onion",
                ]
            ),
            sorted(self.harvester_class.ingredients()),
        )

    def test_instructions(self):
        expected_instructions = (
            "Gather the ingredients.\n"
            "Preheat the oven to 350 F.\n"
            "In a large bowl, combine the ground lamb, egg, garlic, ground cumin, ground coriander, smoked paprika, dried oregano, salt, and black pepper.\n"
            "Place the mixture into an oiled 9 x 5-inch loaf pan and cook in the oven for approximately 30 minutes or until the top is a light golden brown.\n"
            "You can slice the loaf immediately if you like but, for best results, cool completely, wrap in aluminum foil, and refrigerate until firm.\n"
            "To reheat, add a little olive oil to a large skillet, slice the loaf very thinly and crisp up the slices in the hot pan for a few minutes.\n"
            "Assemble the sandwiches with pita, warmed and toasted through. Spread on some tzatziki or tahini sauce, add lettuce, tomato, cucumber, onion, and top with more sauce.\n"
            "Serve and enjoy."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())
