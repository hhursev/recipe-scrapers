from recipe_scrapers.realfoodtesco import RealFoodTesco
from tests import ScraperTest


class TestRealFoodTescoScraper(ScraperTest):

    scraper_class = RealFoodTesco

    def test_host(self):
        self.assertEqual("realfood.tesco.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Tesco Real Food", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Roasted cauliflower tagine", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://realfood.tesco.com/media/images/1400x919-Roasted-cauliflower-tagine-d35191d9-d524-482a-8db8-11b122f4cbf0-0-1400x919.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 cauliflower, trimmed and broken into florets",
                "1 tbsp olive oil",
                "1 tbsp ras el hanout (or harissa seasoning)",
                "1 carrot, sliced on the diagonal",
                "2 red onions, thickly sliced",
                "3 garlic cloves, finely sliced",
                "400g tin chopped tomatoes",
                "400g tin chickpeas, drained and rinsed",
                "80g reduced-salt pitted green olives, halved",
                "200g wholewheat couscous",
                "½ reduced-salt vegetable stock cube, made up to 250ml",
                "120ml fat-free yogurt",
                "15g fresh parsley, roughly chopped",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Preheat the oven to gas 7, 220°C, fan 200°C. Toss the cauliflower with ½ tbsp oil and ½ tbsp ras el hanout in a baking dish, then roast for 20-25 mins until tender and golden.
Meanwhile, heat ½ tbsp oil in a large, lidded saucepan over a medium heat. Add the onions, carrot and garlic and cook for 5 mins, then stir in ½ tbsp ras el hanout and cook for 1 min. Add the tomatoes, chickpeas, olives and 200ml boiling water and bring to the boil. Reduce the heat to low, cover and simmer for 15-20 mins until the veg is cooked through and the sauce has thickened. Remove from the heat and stir in the cauliflower.
Put the couscous in a heatproof bowl, pour over the stock, cover and set aside for 5 mins, then fluff up with a fork. Divide between 4 plates and top with the tagine, yogurt and parsley to serve.""",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
