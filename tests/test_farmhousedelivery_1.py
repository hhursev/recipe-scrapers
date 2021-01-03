from tests import ScraperTest

from recipe_scrapers.farmhousedelivery import FarmhouseDelivery


class TestFarmhouseDeliveryScraper(ScraperTest):

    scraper_class = FarmhouseDelivery

    def setUp(self):
        options = {"exception_handling": False}
        options.update(getattr(self, "scraper_options", {}))

        with open(
            "tests/test_data/{}_1.testhtml".format(self.scraper_class.__name__.lower()),
            encoding="utf-8",
        ) as testfile:
            self.harvester_class = self.scraper_class(testfile, test=True, **options)

    def test_host(self):
        self.assertEqual("recipes.farmhousedelivery.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://recipes.farmhousedelivery.com/green-shakshuka/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Green Shakshuka", self.harvester_class.title())

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 yellow onion, slivered",
                "3 cloves garlic, minced",
                "2 Tbsp. olive oil",
                "1 jalapeno, seeded and minced",
                "4 big handfuls greens (mix kale & spinach), chopped and washed",
                "1/2 c cream",
                "4 eggs",
                "Salt & pepper",
                "Plain yogurt, for serving",
                "Sriracha or other hot sauce, for serving",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            [
                "Saute onions & garlic in olive oil in a large skillet until they take on a little color. Add jalapeno and continue cooking for 1-2 minutes. Add chopped greens, season with salt and pepper to taste and cover until greens are just wilted. Add cream and bring to a simmer. Crack eggs on top of greens, cover and cook until eggs are cooked to your preference. Serve in wide bowls with a dollop of yogurt and a drizzle of hot sauce and thick slices of warm bread on the side."
            ],
            self.harvester_class.instructions(),
        )

    def test_image(self):
        self.assertEqual(
            "http://recipes.farmhousedelivery.com/wp-content/uploads/2020/04/no-blob_clean-handle-1024x683.jpg",
            self.harvester_class.image(),
        )
