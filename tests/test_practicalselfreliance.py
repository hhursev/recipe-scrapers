from recipe_scrapers.practicalselfreliance import PracticalSelfReliance
from tests import ScraperTest


class TestPracticalSelfRelianceScraper(ScraperTest):

    scraper_class = PracticalSelfReliance

    def test_host(self):
        self.assertEqual("practicalselfreliance.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://practicalselfreliance.com/zucchini-relish/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Zucchini Relish")

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_total_time(self):
        self.assertEqual(150, self.harvester_class.total_time())

    def test_image(self):
        self.assertEqual(
            "https://i0.wp.com/practicalselfreliance.com/wp-content/uploads/2021/02/Zucchini-Relish-21.jpg?resize=720%2C720&ssl=1",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 cups zucchini, diced (about 3 medium)",
                "1 cup onion, diced (about 1 medium)",
                "1 cup red bell pepper, diced (about 2 small or 1 large)",
                "2 Tablespoons Salt (pickling and canning salt, or kosher salt)",
                "1 3/4 cups sugar",
                "2 teaspoons celery seed (whole)",
                "1 teaspoon mustard seed (whole)",
                "1 cup cider vinegar (5% acidity)",
                "Pickle Crisp Granules (optional, helps veggies stay firm after canning)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Wash vegetables.\nRemove stem and blossom ends from zucchini and dice into 1/4 to 1/2 inch pieces. Measure 2 cups.\nPeel and dice onion. Measure 1 cup.\nPeel and dice onion. Measure 1 cup.\nStem and seed peppers, then dice. Measure 1...\nStem and seed peppers, then dice. Measure 1 cup.\nImportant, don't skip this step! Combine diced vegetables in a large bowl and sprinkle salt over the top. Stir gently to distribute the salt, then add water until vegetables are completely submerged. Allow the vegetables to soak in the saltwater for 2 hours, then drain completely.\nPrepare a water bath canner (optional, only if canning).\nIn a separate saucepan or stockpot, bring vinegar, sugar, and spices to a gentle simmer (180 degrees F). Do not add salt, the salt is only used to soak veggies before draining.\nAdd drained vegetables to the simmering vinegar/spices and gently simmer for 10 minutes.\nPack hot relish into prepared half-pint or pint jars, leaving 1/2 inch headspace.\nIf not canning, just seal jars and allow them to cool on the counter before storing in the refrigerator.\nIf canning, de-bubble jars, wipe rims, and adjust headspace to ensure 1/2 inch. Seal with 2 part canning lids.\nProcess in a water bath canner for 10 minutes, then turn off the heat. Allow the jars to sit in the canner for another 5 minutes to cool slightly, then remove the jars to cool on a towel on the counter.\nLeave the jars undisturbed for 24 hours, then check seals. Store any unsealed jars in the refrigerator for immediate use. Properly canned and sealed jars should maintain peak quality on the pantry shelf for 12-18 months.",
            self.harvester_class.instructions(),
        )
