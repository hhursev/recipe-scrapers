from recipe_scrapers.livelytable import LivelyTable
from tests import ScraperTest


class TestLivelyTableScraper(ScraperTest):

    scraper_class = LivelyTable
    test_file_name = "livelytable_1"

    def test_host(self):
        self.assertEqual("livelytable.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://livelytable.com/parmesan-zucchini-casserole/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Parmesan Zucchini Casserole")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "LINDSAY DELK")

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://livelytable.com/wp-content/uploads/2023/01/Parmesan-zucchini-casserole-1-225x225.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 small zucchini",
                "2 eggs",
                "1 cup grated parmesan cheese + ½ cup parmesan cut in thin strips",
                "½ cup grated breadcrumbs with garlic powder and dried parsley",
                "1 white onion",
                "1 garlic clove",
                "2 tablespoons olive oil",
                "1 ½ teaspoons salt",
                "1 teaspoon dried rosemary",
                "½ teaspoon black pepper",
                "1 bunch of fresh thyme",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat the oven to 395F.\nWash the zucchinis (alternatively you can also peel them) and chop the ends.\nIn a big bowl place the box grater and grate the zucchini in the biggest hole setting.\nDice thinly the onion and mince the garlic clove.\nAdd a bit of salt to the bowl with the grated zucchini, this will help them to lose their water. Let rest while you cook the rest of the ingredients.\nIn a pan add the olive oil and minced garlic and chopped onion. Season with a bit of salt, pepper, rosemary, and thyme. Cook until soft and fragrant.\nDrain the zucchinis squeezing them with your hands.\nTransfer the cooked onion and garlic into the bowl with the drained zucchini.\nAdd the eggs and beat them, once beaten ad the grated parmesan cheese to the mixture, rest of the seasonings, and mix well.\nTransfer the mixture to a baking dish and spread evenly.\nCover with the breadcrumbs and add a final layer of parmesan strips. Add a bit more thyme on top.\nCook in the oven for 20 minutes.",
            self.harvester_class.instructions(),
        )
