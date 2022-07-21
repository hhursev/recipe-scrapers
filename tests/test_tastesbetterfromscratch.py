from recipe_scrapers.tastesbetterfromscratch import TastesBetterFromScratch
from tests import ScraperTest


class TestTastesBetterFromScratch(ScraperTest):

    scraper_class = TastesBetterFromScratch

    def test_host(self):
        self.assertEqual("tastesbetterfromscratch.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://tastesbetterfromscratch.com/pulled-pork/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "How to make Pulled Pork")

    def test_total_time(self):
        self.assertEqual(320, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://tastesbetterfromscratch.com/wp-content/uploads/2020/05/Pulled-Pork-5.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertSetEqual(
            set(
                [
                    "4 lb pork shoulder (, or butt)",
                    "2 Tablespoons oil (optional if searing)",
                    "1 Tbsp brown sugar",
                    "1 tablespoon chili powder",
                    "1 teaspoon onion powder",
                    "1 teaspoon garlic powder",
                    "1 teaspoon cumin",
                    "1 teaspoon kosher salt",
                    "1 teaspoon black pepper",
                    "12 ounces coke (not diet)",
                    "bbq sauce for coating meat (optional)",
                ]
            ),
            set(self.harvester_class.ingredients()),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Trim pork of excess fat and cut into 4 pieces.",
                    "Combine spices in a small bowl and rub all over the pork. (This can be done the night before).",
                    "Sear (optional): Heat a few tablespoons of oil in a Dutch oven pot over medium-high heat. Add the meat and sear for a few seconds on all sides.",
                    "Oven Method: Preheat oven to 300 degrees F. Pour coke around the pork in the Dutch oven pot. Cover pot with lid and cook for 3 hours. Remove lid and cook for an additional 1-2 hours, until pork is tender and easily pulls apart with a fork. Remove from oven and shred meat. Toss in barbecue sauce, if desired.",
                    "Slow Cooker Method: Place pork in slow cooker and pour coke around it. Cover and cook on LOW (recommended) 8 hours or high for 4-5 hours, until pork is tender and shreds easily with a fork.",
                    "Instant Pot Method: Place pork in instant pot and pour coke around it. Cook on Manual/High pressure for 70 minutes. When timer beeps, allow the pot to naturally release pressure, about 15 minutes longer. Remove lid and shred the meat.",
                ]
            ),
            self.harvester_class.instructions(),
        )
