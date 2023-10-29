# mypy: allow-untyped-defs

from recipe_scrapers.nutritionfacts import NutritionFacts
from tests import ScraperTest


class TestNutritionFactsScraper(ScraperTest):
    scraper_class = NutritionFacts
    test_file_name = "nutritionfacts_1"

    def test_host(self):
        self.assertEqual("nutritionfacts.org", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://nutritionfacts.org/recipe/sweet-potato-taquitos/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Michael Greger M.D. FACLM", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Sweet Potato Taquitos", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Main Course", self.harvester_class.category())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://nutritionfacts.org/app/uploads/2022/05/potato-taquitos-2-scaled.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2½ -3 cups chopped sweet potatoes (about 1 large or 2 medium sweet potatoes)",
                "1 cup chopped carrots (about 3 medium carrots)",
                "3 cloves garlic, minced",
                "1 cup chopped red onion",
                "1½ cups cooked black beans",
                "1 teaspoon chili powder",
                "½ teaspoon onion powder",
                "½ teaspoon paprika or smoked paprika",
                "½ teaspoon ground turmeric",
                "¼ teaspoon black pepper",
                "12-14 small corn tortillas",
                "Cashew Cream (optional)",
                "Avocado (optional)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Boil the potatoes and carrots in 3-4 cups water until soft. Drain the water off. Mash the potatoes and carrots until reaches desired consistency. Feel free to add a splash of unsweetened soy milk or water for a smoother texture.",
                    "In a pan, sauté the garlic and onion with 2-3 tablespoons of water. Add the spices and cook until the onions are translucent. Stir in the cooked beans.",
                    "In a bowl, combine the potato and carrot mixture with the black beans mixture. Stir together.",
                    "Preheat the oven 425F or feel free to use an air fryer with a bake setting.",
                    "Place a small scoop of the potato and bean mixture on to a tortilla, spread it out, and then roll tightly. Place the seam-side of the tortilla down on a baking sheet lined with a silicon mat or parchment paper (or an air fryer basket). Repeat this process for the remaining tortillas.",
                    "Bake the tortillas for about 10-15 minutes.",
                    "Prepare the Cashew Cream, if desired. Thin it out a bit to drizzle on top of the Taquitos or use it as a dip. Optional to top with diced avocado. Enjoy!",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.33, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "Sweet Potato Taquitos are a delicious way to check-off a few Daily Dozen servings! This dish combines beans, whole grains, spices, and vegetables for a satisfying meal. Top with cashew cream and avocados, if desired. Pair with a green leafy salad to check even more Daily Dozen boxes off.",
            self.harvester_class.description(),
        )
