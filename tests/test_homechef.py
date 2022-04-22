from recipe_scrapers.homechef import HomeChef
from tests import ScraperTest


class TestHomeChefScraper(ScraperTest):

    scraper_class = HomeChef

    def test_host(self):
        self.assertEqual("homechef.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Chef\n\nPatrick Le Beau", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Prosciutto and Mushroom Carbonara with Asiago and peas",
            self.harvester_class.title(),
        )

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://homechef.imgix.net/https%3A%2F%2Fasset.homechef.com%2Fuploads%2Fmeal%2Fplated%2F18612%2F5846ProsciuttoandAsiagoCarbonara_Ecomm__1_of_1_-7e576bca3e38185a1acfd06570476d88-7e576bca3e38185a1acfd06570476d88.jpg?ixlib=rails-1.1.0&w=600&auto=format&s=8ffa167fc61e45d14b773a3e06cddaf4",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "3 oz. Peas",
                "2 oz. Prosciutto",
                "Info 1 oz. Shredded Asiago Cheese",
                "Info 2 oz. Sour Cream",
                "Info ⅓ oz. Butter",
                "1 Lemon",
                "4 oz. Cremini Mushrooms",
                "Info 6 oz. Linguine",
                "2 Garlic Cloves",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Cook the Pasta\n\nOnce water in medium pot is boiling, add pasta and cook until al dente, 10-12 minutes.\n\nReserve 1/2 cup pasta cooking water. Drain pasta in a colander and set aside.\n\nWhile pasta cooks, prepare ingredients.\nPrepare the Ingredients\n\nCut mushrooms into 1/4" slices.\n\nHalve and juice lemon.\n\nMince garlic.\nCrisp the Prosciutto\n\nRemove prosciutto from refrigerator. Line a plate with a paper towel.\n\nPlace a large non-stick pan over medium heat and add 1/2 tsp. olive oil. Working in batches, add prosciutto to hot pan in a single layer. Cook until crispy, 1-2 minutes per side.\n\nTransfer prosciutto to towel-lined plate. When cool enough to handle, break into bite-sized pieces. Reserve pan; no need to wipe clean.\nCook the Mushrooms\n\nReturn pan used to crisp prosciutto to medium-high heat and add 1 tsp. olive oil.\n\nAdd mushrooms and a pinch of salt and pepper to hot pan. Stir occasionally until beginning to brown, 3-4 minutes.\n\nAdd garlic and stir constantly until aromatic, 30-60 seconds.\nMake Sauce and Finish Dish\n\nStir pasta, butter, a pinch of salt, and half the reserved pasta cooking water into hot pan until butter is melted. Stir in peas and half the cheese (reserve remaining for garnish) until cheese melts, 30-60 seconds.\n\nRemove from burner and stir in sour cream, 2 tsp. lemon juice, half the prosciutto (reserve remaining for garnish), 1/4 tsp. salt, and a pinch of pepper. If sauce is too thick, add additional pasta cooking water, 1 Tbsp. at a time, until desired consistency is reached.\n\nPlate dish as pictured on front of card, garnishing with remaining prosciutto and remaining cheese. Bon appétit!""",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            """This meal could go by another name: “A cured meat and umami bomb of flavor, all tangled with pasta.” But that's too long a name to go on the recipe card and besides, you already know what we mean when we say “prosciutto” and “mushrooms.” But this pasta also has a creamy lemon-y sauce, not to mention butter and cheese… now we're talking paragraphs, not meal titles.""",
            self.harvester_class.description(),
        )
