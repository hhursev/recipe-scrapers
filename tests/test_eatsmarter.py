from recipe_scrapers.eatsmarter import Eatsmarter
from tests import ScraperTest


class TestEatSmarter(ScraperTest):

    scraper_class = Eatsmarter

    def test_host(self):
        self.assertEqual("eatsmarter.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://eatsmarter.com/recipes/pumpkin-black-bean-salad",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Pumpkin Black Bean Salad")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "EAT SMARTER")

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "22 ozs Hokkaido pumpkin",
                "0.25 oz ginger (1 piece)",
                "2 Tbsps olive oil",
                "salt",
                "peppers",
                "1 oz Baby spinach (1 lg handful)",
                "3 shallots",
                "2 garlic cloves",
                "8 ozs black Beans (can; drained)",
                "5 Tbsps Canola oil",
                "4 Tbsps lemon juice",
                "1 tsp honey",
                "1 Tbsp Hazelnut oil",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Clean pumpkin, wash, cut in half, remove seeds, cut flesh into narrow wedges. Peel the ginger and chop finely. Mix olive oil with salt, pepper and ginger. Brush the pumpkin wedges with it and place on a baking tray lined with baking paper and cook in a preheated oven at 180 °C / 350 °F for about 25 minutes.",
                    "Meanwhile, wash spinach and spin dry. Peel shallots and cut into wedges. Peel garlic and cut in half lengthwise. Rinse beans and drain in a sieve.",
                    "Heat 2 tablespoons of oil in a frying pan. Sauté shallots and garlic in it over medium heat for 2 minutes, then remove. Pour remaining oil and heat over high heat. Add drained beans and fry for 3-4 minutes until they pop.",
                    "Mix the lemon juice, salt, honey, pepper and nut oil to make a dressing. Arrange the pumpkin, beans, shallots and garlic on plates and drizzle with the dressing.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_cook_time(self):
        return self.assertEqual(None, self.harvester_class.cook_time())

    def test_prep_time(self):
        return self.assertEqual(None, self.harvester_class.prep_time())
