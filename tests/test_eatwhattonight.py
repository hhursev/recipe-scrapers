from recipe_scrapers.eatwhattonight import EatWhatTonight
from tests import ScraperTest


class TestEatWhatTonight(ScraperTest):

    scraper_class = EatWhatTonight

    def test_host(self):
        self.assertEqual("eatwhattonight.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Eat What Tonight", self.harvester_class.author())

    def test_canonical_url(self):
        self.assertEqual(
            "http://eatwhattonight.com/2020/08/ginger-soya-chicken/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Ginger Soya Chicken")

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "http://eatwhattonight.com/wp-content/uploads/2020/08/DSC_0317-scaled.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "180g boneless chicken, diced (marinate with 2 tsp light soya sauce, 1/2 tsp sugar and pinch of pepper for 30mins)⁣",
                "1 thumb sized ginger, thinly sliced⁣",
                "Few sprigs of spring onion⁣",
                "1/2 tsp minced garlic⁣",
                "1 tbsp cooking oil⁣",
                "2 tsp shaoxing wine⁣",
                "1 tbsp oyster sauce⁣",
                "2 tbsp dark soya sauce⁣",
                "125ml water⁣",
                "1 tsp sugar⁣",
                "1 tsp sesame oil⁣",
                "2 tsp corn flour⁣",
                "2 tbsp water⁣",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Heat up oil and saute garlics, white parts of spring onion and ginger till fragrant.⁣\nAdd in marinated chicken with the light soya sauce and mix well.⁣\nAdd in water.\nFollowed by the rest of the seasoning and allow the sauce to cook on high heat.⁣\nAdd in green parts of spring onions.\nAdd in sauce thickening.\nWhen sauce has thickened, add in shaoxing wine and remove from heat.⁣Serve hot immediately with rice.",
            self.harvester_class.instructions(),
        )
