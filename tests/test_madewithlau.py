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
            "Egg Rolls (春捲)",
        )

    def test_description(self):
        self.assertEqual(
            "A customizable, vegetarian version of this crispy worldwide favorite!",
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
            "https://cdn.sanity.io/images/2r0kdewr/production/b4a1b1a373b898fe19bd894d1dfd041761eca5e6-1000x1000.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "0.5 oz dried shiitake mushroom",
                "2 oz vermicelli noodles",
                "0.25 oz cloud ear fungus",
                "8 oz cabbage",
                "4 oz celery",
                "3 oz carrot",
                "1 oz snow pea",
                "3 cloves garlic",
                "20 pieces egg roll wrapper",
                "16 oz oil",
                "2 tbsp flour",
                "2 tbsp water",
                "1 tbsp oil",
                "1 tsp salt",
                "1 tsp sugar",
                "1 tbsp Kikkoman® Vegetarian Oyster Sauce",
                "0.25 tsp white pepper",
                "1 tbsp Kikkoman® Sesame Oil",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Step 1 - Prepare dried ingredients\nSoak the vermicelli noodles (2 oz) in warm water to rehydrate for about 10 minutes.\nSoak the dried shiitake mushrooms (0.50 oz) in hot water for 10-15 minutes.\nSimilarly, soak the cloud ear fungus (0.25 oz) in hot water for 10-15 minutes.\nStep 2 - Cut ingredients\nFirst, prepare the cabbage (8 oz). Cut away and discard the hard stalk in the center, where it's very thick and dense. Stack the leaves and chop into very thin strips.\nCut the rehydrated cloud ear fungus and shiitake mushrooms into very thin strips as well.\nCut the celery (4 oz) into 2-inch segments first, then into thin strips.\nChop the snow peas (1 oz) into thin strips.\nStabilize the carrot (3 oz) by slicing off one side and creating a flat surface for it to lay on. If the carrot is long, cut it into 2-inch segments. Then, cut into thin slices, and then into thin strips.\nRoughly mince the garlic (3 clove).\nCreate glue\nIn a small bowl, mix together flour (2 tbsp) and water (2 tbsp).\nStep 3 - Stir-fry filling\nHeat your wok on high heat until it's hot, or about a minute.\nAdd oil (1 tbsp) and give it a swirl to coat the wok. Let it heat up for 30-40 seconds.\nAdd garlic, and fry it until it's aromatic.\nAdd the shiitake mushrooms, and cook for 20-30 seconds.\nAs you add each additional ingredient, mix them in thoroughly as they cook.\nAdd the celery and the cabbage. Cook for 30 seconds.\nAdd the carrot and cloud ear fungus. Cook for 30-40 seconds.\nUse scissors or kitchen shears to cut the vermicelli a few times. They will be added later.\nSeason the filling with salt (1 tsp), sugar (1 tsp), white pepper (0.25 tsp), and oyster sauce (1 tbsp).\nMix the seasoning in well to distribute, and then add the snow peas.\nFinally, push all the ingredients to the sides of the wok to make a small hole in the center. Add the cut-up vermicelli and mix it in the center to give it a good head start on soaking up the moisture, and then mix it in with the rest of the filling.\nAdd sesame oil (1 tbsp) and stir-fry for another 30-40 seconds, making sure everything is well-combined.\nTurn off the heat and plate the filling to help it cool down for the wrapping step.\nStep 4 - Wrap rolls\nPeel each individual wrapper apart and create a loose stack. Do this for the number of egg rolls you're making.\nGently put your stack of wrappers in a plastic bag or container. Take one wrapper out when you're ready to wrap it, and leave the rest covered.\nLay the wrapper with a corner pointing at you, like a diamond. Put 2 tbsp of filling in the wrapper, between the middle and the corner that's pointing to you.\nBring the wrapper corner that's closest to you and wrap it up and over the mound of filling, then tuck the tip under and firmly pull the covered section back towards yourself to tighten. Keep enough pressure on it to press out air pockets and keep the filling together, but be gentle as to not rip the wrapper.\nKeep the pressure pushing on the filling as you roll towards the middle. Be sure not to let the filling spread out too far horizontally.\nAt the halfway point, make a crease where the filling ends on the left, and fold that side of the wrapper up and over. Do the same crease and fold with the right.\nDab some of the flour-and-water glue on the top corner of the wrapper. As always, keep firm pressure on the roll as you roll it up to the end. The glue will seal the end of the roll.\nRepeat with the rest of the filling and wrappers until all your egg rolls have been wrapped up.\nStep 5 - Deep-fry rolls\nHeat oil (16 oz) in a deep pot over high heat. Let the oil reach 330°F (165°C), then turn the heat to low.\nAdd the egg rolls in batches of 6 as to not overcrowd the pot. As they cook, move them around and flip them so they fry evenly.\nFry on low heat for about a minute and a half, then turn the heat to high.\nFry at high heat for a minute and a half, until they're golden brown and crispy. Remove the cooked egg rolls from the oil.\nPlate the cooked egg rolls. Remember to lower the heat when you start the next batch.\nEnjoy quickly for maximum crunch!",
            self.harvester_class.instructions(),
        )

    def test_cuisine(self):
        self.assertEqual("Chinese", self.harvester_class.cuisine())

    def test_category(self):
        self.assertEqual("appetizer, snack", self.harvester_class.category())
