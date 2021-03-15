from recipe_scrapers._factory import SchemaScraperFactory
from tests import ScraperTest


class TestWildMode(ScraperTest):

    scraper_class = SchemaScraperFactory

    def setUp(self):
        with open("tests/test_data/wild_mode.testhtml", encoding="utf-8") as testfile:
            self.harvester_class = self.scraper_class.generate(testfile)

    def test_host(self):
        # let this one pass
        pass

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.feastingathome.com/tomato-risotto/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Summer Tomato Risotto with Saffron"
        )

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.feastingathome.com/wp-content/uploads/2020/07/Tomato-Risotto_-20-225x225.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 lb cherry or grape tomatoes",
                "1 tablespoon olive oil",
                "1 white or yellow onion, diced",
                "2 tablespoons olive oil",
                "4-6 cloves garlic, rough chopped",
                "1 teaspoon dried thyme (or 1 tablespoon fresh)",
                "1 1/2 cups arborio rice or Spanish short-grain rice",
                "pinch saffron",
                "1/2 teaspoon salt",
                "1/2 teaspoon pepper",
                "1/4 teaspoon smoked paprika",
                "6-8 cups veggie stock or chicken stock, warmed",
                "1 tablespoon butter",
                "1/4 cup grated parmesan",
                "16 ounces large shrimp -raw, peeled, deveined (or sub a white fish)",
                "1 tablespoon cumin",
                "1 tablespoon smoked paprika",
                "2 teaspoons granulated garlic",
                "1 teaspoon salt",
                "oil for searing",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            """BLISTER TOMATOES\nIn a large skillet, heat oil over medium-high heat. Add tomatoes (whole) and sear, stirring occasionally, until they burst and soften, about 7 minutes. Turn heat off. Chop if extra-large.\nMAKE RISOTTO\nAt the same time, in a large heavy-bottomed pot or dutch oven, heat the olive oil over medium heat and add the onions. Saute until golden about 10-12 minutes. Add garlic and thyme, saute 2 more minutes until fragrant.\nAdd the rice, saute 1 minute, stirring. Add 2 cups warm stock (enough to cover the rice), saffron and smoked paprika, stir and bring to a simmer. Simmer until most of the liquid is absorbed. Add 1 cup broth and the tomatoes and all their juices. Stir until all the liquid is absorbed. Continue adding broth 1 cup at a time, letting the rice absorb it slowly, stirring often over med-low heat, until the rice is plumped, slightly al dente, yet creamy, about 20-25 minutes. You may not need all 8 cups. ( I used 6 3/4).\nStir in the butter and parmesan. Season generously with salt, pepper, and optional chili flakes. Taste, adjust salt. If bland, it probably needs more salt.\nServe\nas a flavorful side or vegetarian main, garnishing with fresh parsley and lemon zest.\nOptional Seared Prawns:\nIf adding the prawns, mix spices and salt in a bowl. Coat shrimp with the spices. Heat 2-3 tablespoons oil in a skillet (you may need to do this in batches) over medium-high heat, sear each side 2-3 minutes or until cooked through. Top the risotto with the seared prawns.""",
            self.harvester_class.instructions(),
        )
