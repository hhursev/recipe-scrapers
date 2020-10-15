from tests import ScraperTest

from recipe_scrapers.cuisineaz import CuisineAZ


class CuisineAZScraper(ScraperTest):

    scraper_class = CuisineAZ

    def test_host(self):
        self.assertEqual("cuisineaz.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Filer")

    def test_yields(self):
        self.assertEqual("2 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://lovingitvegan.com/wp-content/uploads/2018/08/Kale-Smoothie-8-225x225.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 and 1/4 cups (300ml) Soy Milk (or sub almond milk)",
                "2 Frozen Bananas (~200g, previously peeled, broken into quarters and frozen for at least 12 hours)",
                "1/2 cup (75g) Raw Cashews",
                "2 cups (56g) Kale (torn up, packed)",
                "4 Medjool Dates (pitted)*",
                "1 tsp Minced Ginger",
                "1/8 tsp Cinnamon",
                "1 Tbsp Lime Juice (freshly squeezed)",
                "1 cup Ice Cubes",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Add the soy milk to your blender jug and then the frozen bananas, cashews, kale, dates, minced ginger, cinnamon and fresh lime juice. Top with ice cubes.\nBlend until very smooth.\nPour out into glasses and serve.",
            self.harvester_class.instructions(),
        )
