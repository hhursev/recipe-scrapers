from recipe_scrapers.thekitchenmagpie import TheKitchenMagPie
from tests import ScraperTest


class TestTheKitchenMagPie(ScraperTest):
    scraper_class = TheKitchenMagPie

    def test_host(self):
        self.assertEqual("thekitchenmagpie.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.thekitchenmagpie.com/salmon-loaf/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Salmon Loaf", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(70, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "16 ounces of canned salmon (drained)",
                "1 cup seasoned fine breadcrumbs",
                "½ cup onion (finely chopped)",
                "1 tsp dill weed",
                "2 large eggs (beaten)",
                "1 tablespoon lemon juice",
                "½ tsp salt",
                "¼ tsp black pepper",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat your oven to 375 °F. Grease a baking sheet and set aside.\nDrain the salmon well and if desired, remove any skin and bones from the salmon. You can leave them in, some people love those the best! They will bake right in, don't worry.\nFlake the salmon with a fork and then mix with the breadcrumbs, onion, dill, egg, lemon juice, salt and pepper.\nWith clean hands, shape into a loaf on the greased baking sheet.\nBake for 40-50 minutes OR until nicely browned AND reaches an internal temperature of at least 165 °F.\nLet cool for 5 minutes, then slice and serve. Garnish with fresh parsley and lemon wedges. This is excellent with lemon juice squeezed on top!",
            self.harvester_class.instructions(),
        )
