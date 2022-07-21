from recipe_scrapers.budgetbytes import BudgetBytes
from tests import ScraperTest


class TestBudgetBytesScraper(ScraperTest):

    scraper_class = BudgetBytes

    def test_host(self):
        self.assertEqual("budgetbytes.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.budgetbytes.com/creamy-coconut-curry-lentils-with-spinach/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Creamy Coconut Curry Lentils with Spinach"
        )

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 items", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 Tbsp olive oil ($0.24)",
                "2 cloves garlic ($0.16)",
                "1 tsp grated fresh ginger ($0.10)",
                "1 small yellow onion ($0.21)",
                "1 Tbsp curry powder* ($0.30)",
                "1 cup brown lentils (dry) ($0.67)",
                "2 cups vegetable broth** ($0.26)",
                "1 13oz. can coconut milk ($1.99)",
                "3 cups fresh baby spinach ($1.61)",
                "4 cups cooked rice ($0.60)",
                "1/4 cup chopped fresh cilantro ($0.15)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Mince the garlic, grate the ginger, and dice the onion. Add the olive oil, garlic, and ginger to a deep skillet, Dutch oven, or soup pot. Sauté the garlic and ginger over medium heat for 1 minute, or just until the garlic becomes soft and fragrant.\nAdd the diced onion to the skillet and continue to sauté over medium until the onion is soft and translucent. Add the curry powder and continue to sauté for about one minute more to toast the spices.\nAdd the dry lentils and vegetable broth to the skillet. Stir to dissolve any browned bits from the bottom of the skillet. Place a lid on top, turn the heat up to medium-high, and bring the broth to a boil. Once boiling, turn the heat down to low, and let it simmer for 20 minutes, stirring occasionally.\nAfter simmering for 20 minutes the lentils should be tender and most of the broth absorbed. Add the can of coconut milk and stir to combine. Turn the heat back up to medium and allow the skillet to come back up to a simmer. Let it simmer without a lid for an additional 10 minutes, stirring often, to thicken the mixture.\nOnce thickened, turn the heat off. Add the fresh spinach and stir gently until the spinach has wilted. Taste the mixture and adjust the salt or curry powder to your liking, if needed.\nServe over a bowl of rice, and top with chopped cilantro if desired.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
