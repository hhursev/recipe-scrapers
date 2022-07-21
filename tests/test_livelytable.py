from recipe_scrapers.livelytable import LivelyTable
from tests import ScraperTest


class TestLivelyTableScraper(ScraperTest):

    scraper_class = LivelyTable

    def test_host(self):
        self.assertEqual("livelytable.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://livelytable.com/easy-chipotle-shrimp-tacos/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Easy Chipotle Shrimp Tacos")

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://livelytable.com/wp-content/uploads/2017/05/chipotle-shrimp-tacos-225x225.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 lb raw large shrimp, peeled and deveined",
                "1/2 tsp chipotle powder",
                "1/2 tsp garlic powder",
                "1/2 tsp ground cumin",
                "1 tbsp olive or avocado oil",
                "Juice from 1/2 lime",
                "1/2 jalapeño, seeded and diced",
                "1/4 cup cilantro leaves",
                "2/3 cup nonfat plain greek yogurt",
                "Juice from 1/2 lime",
                "6 corn tortillas, warmed",
                "Shredded purple cabbage",
                "Cilantro",
                "Crumbled cotija cheese",
                "Lime wedges",
                "Guacamole or diced avocado",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Place shrimp in a medium, nonreactive bowl.\nIn a small bowl, combine chipotle, garlic powder, and cumin. Sprinkle over shrimp. Add oil and lime juice and stir well until shrimp are evenly coated. Set aside while you prepare the cilantro jalapeño sauce.\nIn a food processor or blender, combine jalapeño, cilantro, yogurt, and lime juice. Process until smooth and pour into a small bowl for serving.\nPrepare remaining taco toppings.\nHeat a large non-stick skillet over medium heat. Add shrimp and cook about 3 minutes per side or until cooked through.\nServe with warm corn tortillas and top as desired. Enjoy!",
            self.harvester_class.instructions(),
        )
