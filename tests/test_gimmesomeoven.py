from tests import ScraperTest

from recipe_scrapers.gimmesomeoven import Gimmesomeoven


class TestGimmesomeovenScraper(ScraperTest):

    scraper_class = Gimmesomeoven

    def test_host(self):
        self.assertEquals(
            'gimmesomeoven.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEquals(
            self.harvester_class.title(),
            'Baked Eggplant Parmesan'
        )

    def test_yields(self):
        self.assertEquals("8 -10 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEquals(
            'https://www.gimmesomeoven.com/wp-content/uploads/2015/07/Baked-Eggplant-Parmesan-Recipe-1-225x225.jpg',
            self.harvester_class.image()
        )

    def test_ingredients(self):
        self.assertCountEqual([
            "2 medium eggplants (about 2 pounds total), sliced into 1/2-inch thick rounds",
            "2 cups Panko breadcrumbs",
            "1 tablespoon Italian seasoning",
            "1 teaspoon garlic powder",
            "1 teaspoon fine sea salt (plus extra for sweating the eggplant if desired)",
            "1/2 teaspoon freshly-cracked black pepper",
            "2 large eggs",
            "4 cups marinara sauce, homemade or store-bought*",
            "2 cups shredded Mozzarella cheese",
            "2/3 cup finely-grated or shaved Parmesan cheese, plus extra for serving",
            "1 cup chopped fresh basil leaves"],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        self.assertTrue(self.harvester_class.instructions().startswith(
            'Sweat the eggplant (optional). If '))
        self.assertEquals(len(self.harvester_class.instructions()), 2491)
