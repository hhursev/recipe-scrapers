from recipe_scrapers.tasty import Tasty
from tests import ScraperTest


class TestTastyScraper(ScraperTest):

    scraper_class = Tasty

    def test_host(self):
        self.assertEqual("tasty.co", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://tasty.co/recipe/red-wine-braised-short-ribs-with-cashew-cauliflower-mash",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Red Wine-Braised Short Ribs With Cashew Cauliflower Mash Recipe by Tasty",
        )

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://img.buzzfeed.com/thumbnailer-prod-us-east-1/video-api/assets/236025.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "3 lb bone in beef short ribs, cut into 2-inch pieces",
                "1 tablespoon kosher salt",
                "2 teaspoons kosher salt",
                "1 ½ teaspoons freshly ground black pepper",
                "2 tablespoons avocado oil, divided",
                "1 large white onion, cut into 1 inch (2.5 cm) pieces",
                "4 celery stalks, cut into 1/2 inch (1 1/4 cm) diagonal pieces",
                "2 tablespoons tomato paste",
                "2 tablespoons all purpose flour",
                "2 cups dry red wine, such as cabernet sauvignon",
                "1 head garlic, halved crosswise",
                "6 small rainbow carrots, peeled and ends trimmed",
                "10 sprigs fresh thyme",
                "2 cups low sodium beef broth",
                "2 lb cauliflower, cut into florets",
                "1 cup raw cashews",
                "1 teaspoon garlic",
                "¼ cup fresh parsley, chopped, for garnish",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Liberally season the short ribs on all sides with 1 tablespoon of salt and the pepper.\nHeat 2 tablespoons of avocado oil in a 5-quart (5 liter) ceramic pot over medium-high heat until shimmering. Working in batches, add 6-7 pieces of short rib at a time to the pot and sear without disturbing for 2-3 minutes, until a golden brown crust forms. Turn the pieces and continue cooking until seared well on all sides. Remove the short ribs from the pan and set aside, adding another tablespoon of avocado oil to the pot if needed, and repeat with the remaining short ribs.\nReduce the heat to medium and add the onion, celery, and the remaining ½ teaspoon of salt. Sauté for 3-4 minutes, until the vegetables begin to soften and release moisture.\nAdd the tomato paste and stir to coat the vegetables, then cook for 2 minutes. Add the flour and stir to coat the vegetables, then cook for 2-3 minutes more, until deep red in color. Pour in the wine and stir to release any browned bits from the bottom of the pot.\nNestle the short ribs on top of the vegetables in the pot. Bring to a boil, then reduce the heat to medium-low and simmer until the liquid is reduced by about half, 15-20 minutes.\nPreheat the oven to 350˚F (180°C).\nNestle the garlic between the short ribs, then place the carrots and thyme sprigs on top. Pour in the beef stock.\nCover the pot and transfer to the oven. Bake for 2½ hours, until the meat is falling off the bone and fork tender.\nWhile the short ribs are in the oven, make the cauliflower mash: Fill a medium pot with about an inch of water and set a steamer basket inside. Cover and bring the water to a simmer over medium-high heat. Add the cauliflower to the basket and steam for 12-15 minutes, until mashable with the back of a fork, but not overcooked.\nWorking in batches, transfer the steamed cauliflower to a fine-mesh strainer set over a bowl. Using another bowl that is slightly smaller than the strainer, press the bowl into the cauliflower to press excess liquid from the cauliflower. Repeat with remaining cauliflower. Discard the liquid and set the cauliflower aside.\nAdd the cashews to the bowl of a food processor. Blend on high speed for 2-3 minutes, until the cashews are completely broken down and can be mashed into a paste between your fingers, scraping down the sides of the bowl as necessary.\nAdd the strained cauliflower, garlic powder, and salt. Blend until smooth and well combined with the cashew paste.\nTransfer to a serving bowl and serve warm.\nServe the braised short ribs and carrots with the cauliflower mash and garnish with parsley.\nEnjoy!",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(
            93,
            self.harvester_class.ratings(),
        )
