from recipe_scrapers.thespruceeats import TheSpruceEats
from tests import ScraperTest


class TestTheSpruceEatsScraper(ScraperTest):

    scraper_class = TheSpruceEats

    @property
    def test_file_name(self):
        return "{}_1".format(self.scraper_class.__name__.lower())

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
            "https://www.thespruceeats.com/thmb/64k5P_k2qFJCa0tjuXIrZ4yDlU8=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/aqIMG_1498fsq-5b343910c9e77c001a218bd0.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 pound ground lamb (or 1/2 pound each of ground lamb and ground beef)",
                "1 large egg",
                "4 clove garlic, peeled and finely minced",
                "1 teaspoon ground cumin",
                "1 teaspoon ground coriander",
                "1 teaspoon smoked paprika",
                "1 teaspoon dried oregano",
                "1/2 teaspoon kosher salt",
                "1/4 teaspoon ground black pepper",
                "1 tablespoon oil, more for the pan",
                "4 large pita, naan, or flatbread",
                "1 cup assorted lettuce leaves",
                "1 large tomato, sliced",
                "1/2 medium English cucumber, sliced",
                "1/4 large red onion, peeled and sliced",
                "Tzatziki sauce or tahini sauce",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Gather the ingredients.\nPreheat the oven to 350 F.\nIn a large bowl, combine the ground lamb, egg, garlic, ground cumin, ground coriander, smoked paprika, dried oregano, salt, and black pepper.\nPlace the mixture into an oiled 9 x 5-inch loaf pan and cook in the oven for approximately 30 minutes or until the top is a light golden brown.\nYou can slice the loaf immediately if you like but, for best results, cool completely, wrap in aluminum foil, and refrigerate until firm.\nTo reheat, add a little olive oil to a large skillet, slice the loaf very thinly and crisp up the slices in the hot pan for a few minutes.\nAssemble the sandwiches with pita, warmed and toasted through. Spread on some tzatziki or tahini sauce, add lettuce, tomato, cucumber, onion, and top with more sauce.\nServe and enjoy.",
            self.harvester_class.instructions(),
        )
