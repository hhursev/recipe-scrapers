from recipe_scrapers.thespruceeats import TheSpruceEats
from tests import ScraperTest


class TestTheSpruceEatsScraper(ScraperTest):

    scraper_class = TheSpruceEats

    def test_host(self):
        self.assertEqual("thespruceeats.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.thespruceeats.com/doner-kebab-recipe-4171703",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Homemade Doner Kebab: A Turkish Classic"
        )

    def test_total_time(self):
        self.assertEqual(50, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 Servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.thespruceeats.com/thmb/DKGKiOeI7L3iiDtLzOllsoaGksA=/2105x1184/smart/filters:no_upscale()/aqIMG_1498fsq-5b343910c9e77c001a218bd0.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 lb. ground lamb (or 1/2 lb. each of ground lamb and ground beef)",
                "1 egg",
                "4 cloves garlic (peeled and finely minced)",
                "1 teaspoon ground cumin",
                "1 teaspoon ground coriander",
                "1 teaspoon smoked paprika",
                "1 teaspoon dried oregano",
                "1/2 teaspoon salt",
                "1/4 teaspoon ground black pepper",
                "4 rounds of pita (or naan or flatbread)",
                "1 cup assorted lettuce",
                "1 large tomato (sliced)",
                "1/2 seedless English cucumber (sliced)",
                "1/4 large red onion (peeled and sliced)",
                "Tzatziki sauce or tahini sauce",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Gather the ingredients.\nPre-heat the oven to 350 F.\nIn a large bowl, combine the ground lamb, egg, garlic, ground cumin, ground coriander, smoked paprika, dried oregano, salt, and black pepper.\nPlace the mixture into a loaf pan and cook in the oven for approximately 30 minutes or until the top is a light golden brown.\nYou can slice the loaf immediately if you like but, for best results, cool completely, wrap in aluminum foil, and refrigerate until firm.\nTo reheat, add a little olive oil to a large skillet, slice the loaf very thinly and crisp up the slices in the hot pan for a few minutes.\nAssemble the sandwiches with the vegetables and sauce.\nLamb\nkebab\ndinner\nmiddle eastern",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.0, self.harvester_class.ratings())
