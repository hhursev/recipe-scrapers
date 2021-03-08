from recipe_scrapers.watchwhatueat import WatchWhatUEat
from tests import ScraperTest


class TestWatchWhatUEatScraper(ScraperTest):

    scraper_class = WatchWhatUEat

    def test_host(self):
        self.assertEqual("watchwhatueat.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.watchwhatueat.com/healthy-instant-pot-cauliflower-head/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Garlic And Herb Instant Pot Cauliflower With Delicious Gravy",
        )

    def test_yields(self):
        self.assertEqual("5 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.watchwhatueat.com/wp-content/uploads/2018/10/Instant-Pot-Whole-Cauliflower-6.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 large cauliflower head",
                "3-4 garlic cloves finely chopped",
                "1 tbsp fresh thyme (or 1 tsp dried)",
                "1 tbsp fresh parsley finely chopped",
                "1/2 tbsp olive oil",
                "1 tbsp lemon juice",
                "1 tsp smoked paprika",
                "salt and pepper",
                "1 onion cut into large pieces",
                "1 tsp oil",
                "2-3 garlic cloves whole",
                "1 1/2 cup vegetable stock",
                "1/2 tsp thyme (or more if fresh)",
                "1/2 tbsp lemon juice",
                "1 tbsp whole wheat flour",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "In a small bowl combine all the ingredients listed under marinade.\nCut leaves from the bottom of the cauliflower head. Carefully trim the stem flush without cutting the florets. It will help the cauliflower to sit flat on the trivet.\nRub the prepared garlic-herb marinade on the cauliflower head evenly.\nFor the gravy heat oil in saute mode of the Instant Pot. Add onion and whole garlic cloves; cook until translucent.\nThen add vegetable stock, thyme and lemon juice. Place the trivet into the Instant Pot.\nPut the whole cauliflower head on the trivet. Cook for 3 min on manual high-pressure mode. Allow pressure to release naturally for 5 min and then quick release the remaining pressure.\nCarefully transfer the cauliflower to an oven-safe dish or tray. Optionally, broil it 3-4 min in the oven to get a nice crust.\nTurn on the saute mode in the Instant Pot. Add flour to the gravy base and blend everything using a hand blender until it gets to a smooth consistency. Add salt and pepper according to taste.\nCook the gravy for 3-4 min and serve warm with the cooked cauliflower.",
            self.harvester_class.instructions(),
        )
