from recipe_scrapers.madewithlau import MadeWithLau
from tests import ScraperTest


class TestMadeWithLauScraper(ScraperTest):

    scraper_class = MadeWithLau

    def test_host(self):
        self.assertEqual("madewithlau.com", self.harvester_class.host())

    def test_author(self):
        print(self.harvester_class.host())
        self.assertEqual("Made With Lau", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Salt & Pepper Tofu (椒鹽豆腐)",
        )

    def test_description(self):
        self.assertEqual(
            "Fragrant deep-fried tofu that'll disappear from the table before you know it!",
            self.harvester_class.description(),
        )

    def cook_time(self):
        self.assertEqual(20, self.harvester_class.cook_time())

    def prep_time(self):
        self.assertEqual(40, self.harvester_class.prep_time())

    def total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cdn.sanity.io/images/2r0kdewr/production/3172f1134f6ad9f09fafa7770328db9066b7215a-500x500.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "16 oz firm tofu",
                "3 stalks green onion",
                "2 oz mini bell pepper",
                "2 cloves garlic",
                "4 cups boiling water",
                "1 tsp salt",
                "0.5 egg",
                "6 tbsp cornstarch",
                "16 oz oil",
                "2 tbsp oil",
                "1 tbsp garlic salt",
                "0.25 tsp white pepper",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Step 1 - Cut ingredients\nFirst, cut to separate the green and the white parts of the green onions (3 stalks). You're only using the firmer, more pungent whites for this dish. Dice the green onion whites.\nHalve the bell peppers (2 oz) and discard the core and seeds. Cut into strips, and then dice them.\nSmash, peel, and finely mince the garlic (2 clove).\nStep 2 - Cut tofu\nDrain and rinse the firm tofu (16 oz). Cut the tofu into cubes.\n\nStep 3 - Boil tofu\nBoil hot water (4 cup) in a pot with the heat on high. Add salt (1 tsp) and stir to dissolve. When water is boiling, add the tofu cubes. Use chopsticks to shift the tofu around so they’re all fully submerged.\nCook for 3 minutes with the lid on, and then lower the heat to low and uncover the pot. Cook for another 2 minutes.\nCarefully pour the tofu into a colander to drain the water out. Let it start to cool.\nStep 4 - Dry & coat tofu\nLine a plate with a paper towel or a clean kitchen towel. Transfer the tofu cubes onto the lined plate in an even layer. Lay another towel on top and gently press to remove excess moisture.\nSpread a layer of cornstarch (4.8 tbsp) on a separate, large plate. Transfer the tofu into a bowl and add the beaten egg (0.50 ). Gently mix to evenly coat the tofu.\nTransfer the egg-covered tofu cubes to the cornstarch plate to begin coating them.\nSprinkle more cornstarch (1.2 tbsp) over the top of the tofu. Use chopsticks to flip and mix the tofu until all the pieces are evenly coated in cornstarch.\nStep 5 - Fry tofu\nAdd oil (16 oz) to a large pot and set the heat on high.\nAs the oil heats, mix together garlic salt (1 tbsp) and white pepper (0.25 tsp) in a separate bowl.\nPrepare a batch of dredged tofu in a spider strainer.\nWhen the oil reaches 400°F (or 200°C), carefully set the tofu in the oil. At the beginning, let the tofu cook undisturbed so that the crust can set.\nWhen the tofu has started to set and the oil has started to recover from the temperature drop, you can add the rest of the tofu. Set them down along the sides of the pot so they don't stick to the other pieces. Gently mix the pieces around so they fry evenly.\nWhen the tofu is golden brown, or after about 5 minutes of frying at 360°-380°F (180-190°C), turn off the heat and carefully remove the tofu. Let the excess oil drain from the tofu.\nStep 6 - Stir-fry everything\nHeat a wok on high. Add oil (2 tbsp) (take this from the deep-frying oil). Before the oil gets too hot (before it starts to shimmer or smoke), add the dried chili and stir immediately. Fry for just 8 seconds to extract the flavor, and then remove them.\nAdd the minced garlic and fry it for 15 seconds, stirring the entire time.\nAdd the diced bell peppers and green onion whites. Fry for 20-25 seconds, still stirring constantly.\nAdd the fried tofu and stir-fry for 10 seconds.\nWhile stirring constantly, sprinkle just enough of the garlic salt+white pepper seasoning mix over all the ingredients in the wok to evenly coat the tofu cubes.\nStep 7 - Plate & serve\nTurn off the heat and plate. Make sure to scoop up all the little bits of vegetables; they're delicious. Enjoy!",
            self.harvester_class.instructions(),
        )

    def test_cuisine(self):
        self.assertEqual("Chinese", self.harvester_class.cuisine())

    def test_category(self):
        self.assertEqual("side dish", self.harvester_class.category())
