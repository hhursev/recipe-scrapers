from recipe_scrapers.lovingitvegan import Lovingitvegan
from tests import ScraperTest


class TestLovingitveganScraper(ScraperTest):

    scraper_class = Lovingitvegan

    def test_host(self):
        self.assertEqual("lovingitvegan.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://lovingitvegan.com/kale-smoothie/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Kale Smoothie")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Alison Andrews")

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://lovingitvegan.com/wp-content/uploads/2018/08/Kale-Smoothie-8.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 1/4 cups Soy Milk ((300ml) or Almond Milk)",
                "2 Frozen Bananas ((200g) previously peeled, broken into quarters and frozen for at least 12 hours)",
                "1/2 cup Raw Cashews ((75g))",
                "2 cups Kale ((56g) Torn up, packed)",
                "4 Medjool Dates (Pitted)",
                "1 tsp Minced Ginger",
                "1/8 tsp Cinnamon",
                "1 Tbsp Lime Juice (freshly squeezed)",
                "1 cup Ice Cubes",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Add the soy milk to your blender jug and then the frozen bananas, cashews, kale, dates, minced ginger, cinnamon and fresh lime juice. Top with ice cubes.\nBlend until very smooth.\nPour out into glasses and serve immediately.",
            self.harvester_class.instructions(),
        )
