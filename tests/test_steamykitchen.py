from recipe_scrapers.steamykitchen import SteamyKitchen
from tests import ScraperTest


class TestSteamyKitchenScraper(ScraperTest):

    scraper_class = SteamyKitchen

    def test_host(self):
        self.assertEqual("steamykitchen.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Rylee Foer", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Instant Pot Vietnamese Chicken Pho", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://steamykitchen.com/wp-content/uploads/2020/10/SteamyKitchen_2020_websmall.png",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "3 pounds bone-in chicken (either a whole chicken or bone-in parts: breast or thigh)",
                "1 tablespoon cooking oil",
                "2 teaspoons of whole coriander seeds (not ground coriander)",
                "2 star anise pods",
                '2" nub of ginger (peeled and sliced a few times)',
                "1/2 onion",
                "3 whole cloves garlic",
                "3 tablespoons fish sauce",
                "1 1/2 teaspoons sugar",
                "1 package dried rice noodles (about 10-12 ounces, prepared according to package instructions, and drained)",
                "1/2 onion (thinly sliced and soaked in cold water)",
                "1 handful fresh cilantro (chopped)",
                "few sprigs of Thai basil (or regular basil)",
                "1 lime (in wedges)",
                "1/2 pound fresh bean sprouts",
                "1 jalapeno chile (sliced)",
                "Sriracha and Hoisin Sauce",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            'Make the Broth\nTurn the pressure cooker to "sauté" and heat the oil until smoking. Add the onion, ginger slices and cook until nicely browned, about 4 minutes. Add the garlic cloves, coriander, and star anise and sauté for another 2 minutes until fragrant.\nAdd in the chicken and 2 quarts of water to cover the chicken and seal the pot. Set to pressure and cook 20 minutes on high.\nMake your rice noodles while your broth is cooking.\nWhen the cooking is complete, carefully release the pressure then remove the lid once all pressure is released. Remove the chicken from the pot and transfer to a large bowl and let chicken cool off a bit. Strain all the spices from the broth and discard. Turn the pressure cooker on "boil" or "sauté" to keep the broth very hot.\nSeason broth with the fish sauce and sugar. Taste. If the broth is too bland, adjust with more fish sauce and sugar.\nRemove the chicken meat from bones, shred with fingers. Set aside.\nMake the Pho Bowls\nDrain the onions, Set your table with the onions, all of the herbs and condiments so that each person can customize their own bowl.\nDivide the chicken and prepared noodles amongst the bowls.\nReturn the pho broth to a boil. Ladle the hot pho broth into each bowl, and serve.',
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())
