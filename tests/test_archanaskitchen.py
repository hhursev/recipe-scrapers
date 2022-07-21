from recipe_scrapers.archanaskitchen import ArchanasKitchen
from tests import ScraperTest


class TestArchanasKitchenScraper(ScraperTest):

    scraper_class = ArchanasKitchen

    def test_host(self):
        self.assertEqual("archanaskitchen.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Archana's Kitchen", self.harvester_class.author())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.archanaskitchen.com/classic-greek-salad-recipe",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Classic Greek salad Recipe")

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 items", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.archanaskitchen.com/images/archanaskitchen/0-Archanas-Kitchen-Recipes/2018/May-2/Classic_Greek_Salad_With_Olives_And_Feta_Cheese-7.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "4 tablespoons Extra Virgin Olive Oil",
                "4 tablespoons Lemon juice",
                "Salt and Pepper, to taste",
                "1 cup Iceberg lettuce, washed thoroughly and drained",
                "2 Tomatoes, cut into chunks",
                "1 English Cucumber, chopped",
                "1 Red onion, sliced",
                "1/2 cup Kalmatta olives",
                "100 grams Feta Cheese, crumbled",
                "2 sprig Parsley leaves, chopped (optional)",
                "1/2 cup Kalmatta olives",
                "100 grams Feta Cheese, crumbled",
                "2 sprig Parsley leaves, chopped",
                "Salt and Pepper, to taste",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "We begin making the Classic Greek salad Recipe by washing the lettuce thoroughly and draining off any excess water. Tear them into bite size pieces and keep it aside.\nCut all the vegetables and keep it ready, add all the salad ingredients(lettuce,cucumber, tomatoes,red onion) except feta & olives into a large mixing bowl.\nIn another bowl whisk in the dressing ingredients till it combines. Drizzle this on top of the salad mixture and give it a toss.Check for salt and pepper and add if required.\nServe the salad on a flat plate topped up with some crumbled feta cheese and olives.\nServe the Classic Greek salad Recipe as a Party Appetizer followed by a Vegan Moussaka to relish a Greek Meal.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.9, self.harvester_class.ratings())
