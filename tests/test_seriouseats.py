from recipe_scrapers.seriouseats import SeriousEats
from tests import ScraperTest


class TestSeriousEats(ScraperTest):

    scraper_class = SeriousEats

    def test_host(self):
        self.assertEqual("seriouseats.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.seriouseats.com/homemade-preserved-horseradish-recipe",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Homemade Preserved Horseradish Recipe"
        )

    def test_total_time(self):
        self.assertEqual(10, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("1 serving(s)", self.harvester_class.yields())

    def test_image(self):
        # image has hash keys in it so the full url isn't consistent
        # i.e. https://www.seriouseats.com/thmb/gnvQg8_1sB7B1moyDaadHT3pQJo=/960x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__recipes__images__2015__07__20150727-horseradish-vicky-wasik-14-2819caaee55a40cfab06ef8cd257094d.jpg
        self.assertTrue(
            "seriouseats.com__recipes__images__2015__07__20150727-horseradish-vicky-wasik"
            in self.harvester_class.image()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 horseradish root, ends trimmed, peeled, cut into 1-inch chunks (see note)",
                "Distilled white vinegar, for soaking",
                "Kosher salt",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "In a food processor or blender, process horseradish to fine shreds. Add enough vinegar to cover, then season with salt. If it tastes too pungent, add water, 1 tablespoon at a time, until the flavor is a little less harsh (though it should still be very strong and pungent). Keep refrigerated in an airtight container, up to 3 weeks.",
            self.harvester_class.instructions(),
        )
