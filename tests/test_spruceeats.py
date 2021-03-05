from recipe_scrapers.spruceeats import SpruceEats
from tests import ScraperTest


class TestSpruceEatsScraper(ScraperTest):

    scraper_class = SpruceEats

    def test_host(self):
        self.assertEqual("thespruceeats.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Spaghetti Squash Alfredo")

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.thespruceeats.com/thmb/yiynAzw4XfwYb3ye0zKgyjzaIpU=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/spaghetti-squash-alfredo-4771024-hero-b9062b40b0184805bbf6ed5b223e3c44.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 (2 1/2-pound) spaghetti squash (halved lengthwise and seeds removed)",
                "1 tablespoon olive oil",
                "1/2 pound broccoli crowns (cut into bite-sized florets)",
                "6 tablespoons butter (cut into pieces)",
                "1/2 teaspoon garlic (about 1 large clove, finely grated)",
                "1/2 cup heavy cream",
                "1/2 cup whole milk",
                "2 1/2 cups Pecorino cheese (or Parmesan, finely grated)",
                "Salt and pepper (to taste)",
                "Flat-leaf parsley (chopped, for garnish)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Gather the ingredients.\nPreheat the oven to 425 F. Place the squash, cut-side down, on a parchment paper-lined rimmed baking sheet. Roast until the squash is very tender and easily pulls apart into strands when the cut side is scraped with a fork, about 40 minutes.\nRemove from the oven and let sit on the pan until cool enough to handle, about 15 minutes. Drag a fork through the squash to separate it into spaghetti-like strands.\nWhile the squash cools, heat the oil in a large skillet over medium-high. Add the broccoli and 2 tablespoons of water, cover, and cook until the broccoli is tender, 2 to 3 minutes. Transfer to a plate. Wipe out the skillet.\nMelt the butter in the same skillet over medium heat. Add the garlic and cook until fragrant, about 30 seconds. Add the cream and milk, and cook until mixture is heated through and little bubbles appear near edges of the pan (do not let it come to a rolling boil).\nRemove the skillet from the heat and whisk in cheese. Season with salt and pepper.\nAdd the squash to the skillet toss to combine with the alfredo sauce.\nServe in deep bowls topped with the broccoli and parsley.",
            self.harvester_class.instructions(),
        )
