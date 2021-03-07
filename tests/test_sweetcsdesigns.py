from recipe_scrapers.sweetcsdesigns import SweetCsDesigns
from tests import ScraperTest


class SweetCsDesignsScraper(ScraperTest):

    scraper_class = SweetCsDesigns

    def test_host(self):
        self.assertEqual("sweetcsdesigns.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://sweetcsdesigns.com/the-best-easy-air-fryer-french-fries-recipe/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "The Best Easy Air Fryer French Fries Recipe"
        )

    def test_total_time(self):
        self.assertEqual(65, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://sweetcsdesigns.com/wp-content/uploads/2018/12/The-Best-French-Fries-from-an-Air-Fryer-Recipe-Picture-480x480.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "3 large russet potatoes",
                "2-3 tablespoons olive oil",
                "Sea salt and pepper, to taste",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Using a mandoline, slice the potatoes into fries. I don't worry too much about the size of fry I am making- some are bigger, and some are smaller. That's fine!\nNext, place your spuds in a nice cool water bath. Completely submerge the fries in water.\nLet fries sit one hour. This helps to remove excess starch and will help the fries crisp up more in the oven.\nPreheat air fryer to 375 degrees.\nAfter an hour, drain the water, and pat fries dry with a paper towel.\nToss with a couple tablespoons of olive oil, salt and pepper.\nAdd fries to bottom of air fryer basket, making sure they are all on the same level (don't stack them on top of each other.)\nCook 13 minutes, until crispy and golden brown.\nPlace on a baking sheet lined with paper towels and a cooling rack over it.\nPlace in warm oven (set to the minimum temperature, not over 250 degrees) and let rest while other batches of fries are cooking.\nServe hot and enjoy.",
            self.harvester_class.instructions(),
        )
