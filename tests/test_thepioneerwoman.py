from recipe_scrapers.thepioneerwoman import ThePioneerWoman
from tests import ScraperTest


class TestThePioneerWomanScraper(ScraperTest):

    scraper_class = ThePioneerWoman

    def test_host(self):
        self.assertEqual("thepioneerwoman.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "http://thepioneerwoman.com/cooking/patty-melts/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Patty Melts")

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://pioneerwoman.files.wordpress.com/2012/08/pattymelt2.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 stick Butter",
                "1 whole Large Onion, Halved And Sliced",
                "1-1/2 pound Ground Beef",
                "Salt And Pepper, to taste",
                "5 dashes Worcestershire Sauce",
                "8 slices Swiss Cheese",
                "8 slices Rye Bread",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "In a medium skillet, melt 2 tablespoons of butter over medium-low heat.\n Throw in the sliced onions and cook slowly for 20 to 25 minutes, stirring occasionally, until the onions are golden brown and soft.\n In a medium bowl, mix together the ground beef, salt & pepper, and Worcestershire.\n Form into 4 patties.\nMelt 2 tablespoons butter in a separate skillet over medium heat.\n Cook the patties on both sides until totally done in the middle.\n Assemble patty melts this way: Slice of bread, slice of cheese, hamburger patty, 1/4 of the cooked onions, another slice of cheese, and another slice of bread.\n On a clean griddle or in a skillet, melt 2 tablespoons butter and grill the sandwiches over medium heat until golden brown.\n Remove the sandwiches and add the remaining 2 tablespoons of butter to the skillet.\n Turn the sandwiches to the skillet, flipping them to the other side.\n Cook until golden brown and crisp, and until cheese is melted.\n Slice in half and serve immediately!",
            self.harvester_class.instructions(),
        )
