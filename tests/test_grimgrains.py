# mypy: allow-untyped-defs

from recipe_scrapers.grimgrains import GrimGrains
from tests import ScraperTest


class TestGrimGrainsScraper(ScraperTest):
    scraper_class = GrimGrains

    def test_host(self):
        self.assertEqual("grimgrains.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Hundred Rabbits", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("okonomiyaki", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.harvester_class.url = "https://grimgrains.com/site/okonomiyaki.html"
        self.assertEqual(
            "https://grimgrains.com/media/recipes/okonomiyaki.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "nagaimo: 160 g, grated",
                "green cabbage: 500 g, minced",
                "chickpea flour: 85 g",
                "nutritional yeast: 15 g",
                "salt: 1.25 g",
                "shiitake: 6",
                "water: 320 ml",
                "sesame oil: 10 ml",
                "soy sauce: 60 ml",
                "mirin: 60 ml",
                "granulated sugar: 15 g",
                "arrowroot starch: 15 g",
                "ao nori: 30 g",
                "beni shouga: to taste",
                "scallions: 4 stalks",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            (
                "\n".join(
                    [
                        "Peel the nagaimo, then soak it in a water and vinegar solution (doing this helps to remove irritants). Dry the nagaimo, then grate 160 g (6-8cm) of nagaimo with a fine grater. Do this over a bowl, as the grated nagaimo is very slimy. Keep aside.",
                        "Mince 500 g (1 small head) green cabbage, keep aside.",
                        "In a bowl, mix 85 g (1 cup) of chickpea flour, 15 g (1/4 cup) nutritional yeast, the grated nagaimo, the minced green cabbage and 1.25g (1/4 tsp) of salt. Then, add 320 ml (1 1/4 cup) of water, or shiitake dashi. (for shiitake dashi, soak 5-6 shiitake in 320 ml of hot water for 15 minutes, or overnight in cold water.)",
                        "Heat a non-stick pan at high heat, add 5 ml (1 tsp) of sesame oil. If you throw some water on and it starts to sizzle, the pan is hot and you can add 1/4 of the batter. Alternatively, you can add 1/2, although this makes two very large portions.",
                        "Let okonomiyaki cook for 5 minutes, shaking the pan every now and then so the batter doesn't stick.",
                        "After 5 minutes, it's time to give the other side some grilling time. Put a plate on top of the pancake, keep your hand on the plate and flip the pan so that the pancake ends up cooked side up on the plate. Then, slide the pancake back into the pan (cooked side up). You can also just flip it with a spatula, but we rather like the plate method :).",
                        "Cook for another 5 minutes, then slide onto a plate, repeat process for the rest of the batter.",
                        "In a small bowl, mix 60 ml (4 tbsp) of soy sauce, 60 ml (4 tbsp) of mirin, 15 g (1 tbsp) of sugar and 15 g (1 tbsp) of arrowroot starch. Stir well.",
                        "Heat a pan at high heat, when hot, add sauce and cook for 2-3 minutes until it thickens. Then, divide onto your okonomiyaki.",
                        "First, add about 15 g (1 tbsp) (per okonomiyaki) of aonori on top of the sauce.",
                        "Then, add some beni shouga (pickled red ginger).",
                        "Finally, top off with some finely chopped scallions.",
                    ]
                )
            ),
            self.harvester_class.instructions(),
        )
