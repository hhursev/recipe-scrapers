from recipe_scrapers.bonappetit import BonAppetit
from tests import ScraperTest


class TestBonAppetitScraper(ScraperTest):

    scraper_class = BonAppetit

    def test_host(self):
        self.assertEqual("bonappetit.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.bonappetit.com/recipe/pork-chops-with-celery-and-almond-salad",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Pork Chops with Celery and Almond Salad"
        )

    def test_total_time(self):
        self.assertEqual(None, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://assets.bonappetit.com/photos/59e4d7dc3279981dd6c79847/16:9/w_1000,c_limit/pork-chops-with-celery-and-almond-salad.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "¼ cup dried unsweetened cranberries",
                "3 tablespoons unseasoned rice vinegar",
                "2 1½-inch-thick bone-in pork rib chops (about 1 pound each), patted dry",
                "Kosher salt",
                "4 tablespoons extra-virgin olive oil, divided",
                "3 sprigs thyme",
                "3 garlic cloves, smashed",
                "3 tablespoons unsalted butter, cut into pieces",
                "1 small shallot, finely chopped",
                "6 large or 8 medium celery stalks, thinly sliced on a diagonal",
                "½ cup parsley leaves with tender stems",
                "¼ cup chopped salted, dry-roasted almonds",
                "1 ounce Parmesan, shaved",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            'Combine cranberries and vinegar in a small bowl and set aside.\nSeason pork generously with salt, then rub with 1 Tbsp. oil total. Heat a dry medium skillet, preferably cast iron, over medium. Cook pork chops, moving once or twice to hotter areas of skillet, until first side is deeply browned, 6–9 minutes. Turn pork chops and cook until second sides are browned, about 5 minutes. Working one at a time, set chops on fatty side with tongs to melt and brown fat cap, about 1 minute each. At this point an instant-read thermometer inserted into the center of each chop should register 135°.\nAdd thyme, garlic, and butter to skillet and swirl to melt butter. Tilt skillet toward you so butter pools in the pan and spoon foaming butter over chops continuously until butter is browned, about 1 minute. Transfer pork chops, thyme, and garlic to a cutting board and let meat rest while you assemble the salad.\nCombine shallot and a couple of pinches of salt in a large bowl. Pour vinegar from reserved cranberries into bowl. Whisking constantly, gradually add remaining 3 Tbsp. oil. Add cranberries, celery, parsley, almonds, Parmesan, and several pinches of salt; toss to combine.\nCut along bones to remove meat from pork chops; slice meat ½" thick. Transfer meat and bones to a platter along with garlic and thyme, then drizzle any accumulated juices left on cutting board over top. Serve with salad.',
            self.harvester_class.instructions(),
        )
