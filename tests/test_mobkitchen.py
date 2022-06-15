from recipe_scrapers.mobkitchen import MobKitchen
from tests import ScraperTest


class TestMobKitchenScraper(ScraperTest):

    scraper_class = MobKitchen

    def test_host(self):
        self.assertEqual("mobkitchen.co.uk", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Mob", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Chilli Cheese Paratha", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Munchies, Comfort, Speedy", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://mobkitchen-objects.imgix.net/recipes/9K8A6392-2.jpg?auto=format&crop=focalpoint&domain=mobkitchen-objects.imgix.net&fit=crop&fp-x=0.5&fp-y=0.5&h=827&ixlib=php-3.3.1&q=82&w=1300&s=412bb43eb2623e3afb2bebc5cc73b572",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "200g Plain Flour",
                "140ml Hot Water",
                "7 Garlic Cloves",
                "3 Tsp Chilli Powder",
                "Handful Of Coriander",
                "3 Spring Onions",
                "250g Mozzarella",
                "250g Cheddar Cheese",
                "Salt",
                "Vegetable Oil",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Combine the plain flour, a pinch of salt and hot water (from the kettle) in a bowl and mix with a wooden spoon. Once it is cool enough to handle, knead the dough for 5 minutes until smooth. Pour in a tablespoon of oil and knead through. Cover and rest for 10 minutes
Meanwhile, prepare the garlic chilli oil. Grate the garlic into a small microwaveable bowl with the chilli powder, ¼ teaspoon salt and 2 tablespoons of oil. Microwave for 1 minute to soften and cook the garlic.
Roughly chop your coriander and finely slice your spring onions.
Divide the dough into quarters, and then the quarters into halves to form eight even balls.
Roll two balls into large circles about 2mm thick so they are about the same size. Spread ½ a teaspoon of the chilli garlic paste on to one circle, sprinkle on a handful of shredded mozzarella and shredded cheddar. Sprinkle on your coriander and spring onions, then press a second dough circle on top – you can use some water along the edges to help it stick if you need it too
Heat up a frying pan and pour in a small glug of oil. Slap on the paratha and cook on a high heat on both sides for 2 minutes. Flip using a large spatula.
Cut into quarters and serve whilst still hot and oozing with cheese.""",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Indian", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "This Indian snack is oozing with molten cheese and chilli garlicky goodness. They will be demolished in seconds, I can promise you that. Seema x",
            self.harvester_class.description(),
        )
