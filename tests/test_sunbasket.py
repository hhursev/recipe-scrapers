from recipe_scrapers.sunbasket import SunBasket
from tests import ScraperTest


class TestSunBasketScraper(ScraperTest):

    scraper_class = SunBasket

    def test_host(self):
        self.assertEqual("sunbasket.com", self.harvester_class.host())

    def test_host_domain(self):
        self.assertEqual("sunbasket.co.uk", self.harvester_class.host(domain="co.uk"))

    def test_title(self):
        self.assertEqual(
            "Lemongrass-turkey salad with rice noodles and pear",
            self.harvester_class.title(),
        )

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "5 ounces flat rice noodles",
                "Sun Basket lemongrass paste (lemongrass - extra virgin olive oil - garlic - ginger - turmeric)",
                "3 or 4 organic radishes (about ¼ pound total)",
                "1 organic Asian or other pear",
                "4 or 5 sprigs organic fresh mint",
                "Sun Basket Thai dressing base (maple syrup - lime juice - fish sauce)",
                "3 ounces organic baby kale or other leafy greens",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "1: Cook the rice noodles - Bring a medium [large] sauce pot of water to a boil. Add the rice noodles and cook until just tender, 6 to 8 minutes. Drain and rinse with cold water, then return to the pot and set aside. While the water is heating and the noodles are cooking, start preparing the rest of the meal.",
                    "2: Prep and cook your protein - Ground meat: Cut a small corner from the ground meat packaging and drain off any excess liquid. Transfer to a plate; pat dry with a paper towel. Shrimp: Rinse and drain the shrimp. Pat dry on a paper-towel-lined plate. Tofu: Pat the tofu dry with paper towels; cut into ½-inch cubes. Plant-based chick*n: Pat the chick*n dry with a paper towel. In a large frying pan over medium-high heat, warm 2 to 3 teaspoons oil until hot but not smoking. Add your protein and lemongrass paste, season lightly with salt and pepper, and cook, stirring occasionally and breaking up the ground meat if using, until the protein is lightly browned and cooked through, 2 to 4 minutes for regular shrimp; 4 to 6 minutes for jumbo shrimp, tofu, or plant-based chick*n; and 5 to 7 minutes for ground meat. Remove from the heat. Meanwhile, prepare the remaining ingredients.",
                    "3: Prep the remaining ingredients; assemble the salad - Cut the radishes in half, then cut the halves into thin half-moons. Peel the Asian pear, if desired; core and thinly slice. Strip the mint leaves from the stems; coarsely chop or tear the leaves. In a small bowl, stir together the Thai dressing base and 1 tablespoon [2 TBL] oil; season to taste with salt and pepper. In a large bowl, combine your protein, noodles, radishes, pear, mint, kale, and 2 to 3 tablespoons Thai dressing and toss to coat (set aside the remaining dressing for serving). Season to taste with salt and pepper.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_image(self):
        self.assertEqual(
            "//cdn.sunbasket.com/100408c8-f908-404e-a494-099fad9fed44.jpg",
            self.harvester_class.image(),
        )
