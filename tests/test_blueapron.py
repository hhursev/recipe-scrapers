from recipe_scrapers.blueapron import BlueApron
from tests import ScraperTest


class TestBlueApronScraper(ScraperTest):

    scraper_class = BlueApron

    def test_host(self):
        self.assertEqual("blueapron.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.blueapron.com/recipes/bbq-chickpeas-farro-with-corn-cucumbers-hard-boiled-eggs-3",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            "BBQ Chickpeas & Farro with Corn, Cucumbers & Hard-Boiled Eggs",
            self.harvester_class.title(),
        )

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://media.blueapron.com/recipes/24483/c_main_dish_images/1593115477-32-0038-5165/0819_2PV2_BBQ-Chickpea_4449_CropRight_Web_high_feature.jpg",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 Pasture-Raised Eggs",
                "1 15.5 -Ounce Can Chickpeas",
                "½ cup Semi-Pearled Farro",
                "2 ears Of Corn",
                "2 Persian Cucumbers",
                "1 bunch Chives",
                "¼ cup Barbecue Sauce",
                "1 Tbsp Apple Cider Vinegar",
                "1 oz Sliced Pickled Jalapeño Pepper",
                "1 Tbsp Barbecue Spice Blend (Smoked Paprika, Sweet Paprika, Ground Fennel Seeds, Ground Coriander, Garlic Powder & Light Brown Sugar)",
                "2 tsps Honey",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "1 Cook the farro Remove the honey from the refrigerator to bring to room temperature. Fill a medium pot 3/4 of the way up with salted water; cover and heat to boiling on high. Fill a separate, small pot 3/4 of the way up with salted water; cover and heat to boiling on high. Once the medium pot is boiling, add the farro. Cook, uncovered, 18 to 20 minutes, or until tender. Turn off the heat. Drain thoroughly and return to the pot.\n2 Prepare the ingredients & make the vinaigrette Meanwhile, wash and dry the fresh produce. Remove the husks and silks from the corn; cut the kernels off the cobs. Drain and rinse the chickpeas. Halve the cucumbers lengthwise; thinly slice crosswise. Roughly chop the pepper; thoroughly wash your hands immediately after handing. In a bowl, combine the sliced cucumbers, a drizzle of olive oil, and as much of the chopped pepper as you’d like, depending on how spicy you’d like the dish to be; season with salt and pepper. Set aside to marinate, stirring occasionally, at least 10 minutes. Taste, then season with salt and pepper if desired.Thinly slice the chives. In a separate bowl, whisk together the honey (kneading the packet before opening), vinegar, and 1 tablespoon of olive oil; season with salt and pepper.\n3 Cook & slice the eggs While the cucumbers marinate, carefully add the eggs to the small pot of boiling water. Cook 9 minutes for hard-boiled. Drain and rinse under cold water 30 seconds to 1 minute to stop the cooking process. When cool enough to handle, peel the cooked eggs; thinly slice. Season with salt and pepper.\n4 Char the corn In a large pan (nonstick, if you have one), heat 2 teaspoons of olive oil on medium-high until hot. Add the corn kernels in an even layer; season with salt and pepper. Cook, without stirring, 3 to 4 minutes, or until charred (be careful, as the corn may pop as it cooks). Continue to cook, stirring occasionally, 1 to 2 minutes, or until softened. Transfer to a bowl. Wipe out the pan.\n5 Cook the chickpeas & serve your dish In the same pan, heat 2 teaspoons of olive oil on medium-high until hot. Add the drained chickpeas and half the spice blend (you will have extra). Cook, stirring occasionally, 2 to 3 minutes, or until slightly softened. Add the barbecue sauce (carefully, as the liquid may splatter) and 1/4 cup of water. Cook, stirring occasionally, 2 to 3 minutes, or until the sauce is thickened. Turn off the heat. Taste, then season with salt and pepper if desired. To the pot of cooked farro, add the vinaigrette; stir to combine. Taste, then season with salt and pepper if desired. Serve the finished farro topped with the sliced eggs, marinated cucumbers, cooked chickpeas, and charred corn. Garnish with the sliced chives. Enjoy!\n1 Cook the farro Remove the honey from the refrigerator to bring to room temperature. Fill a medium pot 3/4 of the way up with salted water; cover and heat to boiling on high. Fill a separate, small pot 3/4 of the way up with salted water; cover and heat to boiling on high. Once the medium pot is boiling, add the farro. Cook, uncovered, 18 to 20 minutes, or until tender. Turn off the heat. Drain thoroughly and return to the pot.\n2 Prepare the ingredients & make the vinaigrette Meanwhile, wash and dry the fresh produce. Remove the husks and silks from the corn; cut the kernels off the cobs. Drain and rinse the chickpeas. Halve the cucumbers lengthwise; thinly slice crosswise. Roughly chop the pepper; thoroughly wash your hands immediately after handing. In a bowl, combine the sliced cucumbers, a drizzle of olive oil, and as much of the chopped pepper as you’d like, depending on how spicy you’d like the dish to be; season with salt and pepper. Set aside to marinate, stirring occasionally, at least 10 minutes. Taste, then season with salt and pepper if desired.Thinly slice the chives. In a separate bowl, whisk together the honey (kneading the packet before opening), vinegar, and 1 tablespoon of olive oil; season with salt and pepper.\n3 Cook & slice the eggs While the cucumbers marinate, carefully add the eggs to the small pot of boiling water. Cook 9 minutes for hard-boiled. Drain and rinse under cold water 30 seconds to 1 minute to stop the cooking process. When cool enough to handle, peel the cooked eggs; thinly slice. Season with salt and pepper.\n4 Char the corn In a large pan (nonstick, if you have one), heat 2 teaspoons of olive oil on medium-high until hot. Add the corn kernels in an even layer; season with salt and pepper. Cook, without stirring, 3 to 4 minutes, or until charred (be careful, as the corn may pop as it cooks). Continue to cook, stirring occasionally, 1 to 2 minutes, or until softened. Transfer to a bowl. Wipe out the pan.\n5 Cook the chickpeas & serve your dish In the same pan, heat 2 teaspoons of olive oil on medium-high until hot. Add the drained chickpeas and half the spice blend (you will have extra). Cook, stirring occasionally, 2 to 3 minutes, or until slightly softened. Add the barbecue sauce (carefully, as the liquid may splatter) and 1/4 cup of water. Cook, stirring occasionally, 2 to 3 minutes, or until the sauce is thickened. Turn off the heat. Taste, then season with salt and pepper if desired. To the pot of cooked farro, add the vinaigrette; stir to combine. Taste, then season with salt and pepper if desired. Serve the finished farro topped with the sliced eggs, marinated cucumbers, cooked chickpeas, and charred corn. Garnish with the sliced chives. Enjoy!",
            self.harvester_class.instructions(),
        )
