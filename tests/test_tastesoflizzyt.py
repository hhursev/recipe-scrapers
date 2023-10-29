from recipe_scrapers.tastesoflizzyt import TastesOfLizzyT
from tests import ScraperTest


class TestTastesOfLizzyTScraper(ScraperTest):
    scraper_class = TastesOfLizzyT

    def test_host(self):
        self.assertEqual("tastesoflizzyt.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.tastesoflizzyt.com/soft-baked-gingerbread-cookies/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Soft Baked Molasses Cookies")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Julie Clark")

    def test_total_time(self):
        self.assertEqual(27, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("60 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 cup shortening",
                "1 cup brown sugar (packed)",
                "1 cup molasses",
                "1 cup buttermilk",
                "5 1/2 cups all-purpose flour",
                "4 teaspoons baking soda",
                "1 teaspoon ginger",
                "3/4 teaspoon cinnamon",
                "1/4 teaspoon nutmeg",
                "1/4 teaspoon cloves",
                "1 teaspoons salt",
                "1/2 cup extra sugar for rolling dough",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "In a large bowl, mix together the shortening, brown sugar, molasses and buttermilk. The mixture will look curdled, but don't worry...it will all come together with the dry ingredients.\nIn a separate bowl, sift together the flour, baking soda, ginger, cinnamon, nutmeg, cloves and salt.\nAdd the dry ingredients to the creamed sugar mixture and mix well. The dough will be very soft and slightly sticky, but you should be able to roll\nRoll the dough into balls and then roll the balls in sugar.\nPlace the cookie dough balls on an ungreased cookie sheet and bake at 350 degrees Fahrenheit for 8-10 minutes. Don't over bake the cookies. We remove them before they get browned.\nAllow the cookies to cool on the pan for 3-5 minutes before moving to a wire rack to cool completely. Then store in an airtight container at room temperature.",
            self.harvester_class.instructions(),
        )
