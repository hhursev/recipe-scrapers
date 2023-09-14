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

    def test_description(self):
        self.assertEqual(
            "Okonomiyaki (meaning, 'grilled as you like it') is a Japanese dish, similar to the American omelette, but the main difference is the variation of ingredients. Typical okonomiyaki are made with eggs, and often include meat or fish. Making it without meat is simple enough, but without eggs? Back when we lived in Tokyo, our experience in cooking with plants was limited, but now we've been doing it long enough that we can think of alternatives with ease.\nThe key ingredient? Chickpea flour. We make chickpea pancakes, and scrambled chickpea flour (resembles scrambled eggs) at home all the time. Chickpea flour is a staple on Pino, and works very well for okonomiyaki.\nNagaimo: If you're in a place were nagaimo (or yamaimo) is available, we highly reccommend adding it to the dish. It makes a fluffier pancake. Although we've made okonomiyaki without nagaimo before, so if you can't find it know that it will work and be very delicious anyway. It imparts little flavor, all it does is add nutrition and texture. Nagaimo, unlike most potatoes, can be eaten raw. However, it is best to handle the nagaimo with gloves, or to soak the peeled tuber in a vinegar-water solution to neutralize irritant oxalate crystals found on their skin. Nagaimo are low-calorie, high in protein, and have potassium, zinc, vitamin C and more. The texture of grated nagaimo can be off-putting, it looks like a regular tuber when whole, but when grated it becomes slime, almost liquid. This sort of texture is well-liked in Japan and referred to as being 'neba neba' (slimy). This texture present in many other foods like okra and nattou. This texture makes it an ideal egg alternative, it can be used to make deserts when baking.\nAonori: Aonori is another obscure ingredient, but again, it can be omitted, although it tastes really amazing with it. We made okonomiyaki without it when we were in Majuro, because it simply wasn't available, so we used finely cut nori instead. Obviously, this isn't a perfect substitution, because aonori is sweet and tastes nothing like nori. However, nori is still very delicious and pairs well enough with the okonomiyaki.\nOkonomi sauce\nIn this recipe, we don't use true 'okonomi sauce'. Why? Because we don't use many pre-made sauces, we prefer to make my own. Okonomi sauce requires many ingredients, and honestly, the sauce we've made works really well in this recipe and makes a good okonomi sauce alternative.\nIf you want to make your own, you can mix 7g (1 1/2 tsp) sugar, 45g (3 tbsp) ketchup and 45g (3 tbsp) of vegan worcestershire sauce. If you are like us, and don't care to buy pre-made sauces but want to avoid buying both ketchup and worcestershire sauce, you can make these too:\nWorcestershire sauce: combine apple cider vinegar, water, soy sauce, sugar, mustard powder, onion powder, garlic powder, cinnamon and black pepper in pan, bring to a boil and cook for a minute, then let cool.\nKetchup: Using some fresh tomato sauce may be enough, otherwise add a bit of sugar and apple cider vinegar to it.",
            self.harvester_class.description(),
        )
