from recipe_scrapers.greatbritishchefs import GreatBritishChefs
from tests import ScraperTest


class TestGreatBritishChefsScraper(ScraperTest):

    scraper_class = GreatBritishChefs
    test_file_name = "greatbritishchefs_2"

    def test_host(self):
        self.assertEqual("greatbritishchefs.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.greatbritishchefs.com/recipes/beef-mushroom-lasagne-recipe",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Beef and mushroom lasagne")

    def test_total_time(self):
        self.assertEqual(135, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "http:https://media-cdn.greatbritishchefs.com/media/mbqmodb5/img46675.jpg?mode=crop&width=768&height=512",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 lasagne pasta, packet",
                "50g of Parmesan",
                "oil",
                "2 onions, finely chopped",
                "700g of beef mince",
                "6 bacon rashers, diced",
                "3 tin of chopped tomatoes",
                "1 bay leaf",
                "250ml of red wine",
                "70g of butter",
                "50g of plain flour",
                "500ml of milk",
                "200g of chestnut mushrooms, sliced",
                "100g of button mushrooms, sliced",
                "100g of girolles, sliced",
                "1 handful of porcini mushroom",
                "6 sage leaves",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "In a large saucepan, cook the mince and bacon pieces until the mince is browned. Remove from the pan and set aside\nHeat 2 tbsp of oil in the pan and cook the onions until soft but not coloured. Add back the meat, then splash in the wine and cook for 10 minutes or so, stirring occasionally. Add the tomatoes, bay leaf and some salt and pepper\nPut a lid on the pan and allow to cook, stirring every now and then, for around 1 hour. After this time, remove the lid and allow to cook for another half an hour or so, until the ragu has thickened\nPour boiling water onto the dried porcini and allow to rehydrate for 20 minutes. Heat 2 tbsp of oil in a frying pan and cook the girolles, closed cup mushrooms and chestnut mushrooms until soft. Add the sage, cook a few minutes more then set aside\nDrain the porcini, reserving the water. Add the water to the ragu sauce, chop the porcini and add them to the other mushrooms\nTo make the béchamel, melt the butter and and add the flour to it. Cook, stirring all the time, until the flour mixture is a golden sandy colour\nIn a separate saucepan, heat the milk until almost boiling. Add it, a ladleful at a time, into the flour and butter mixture, whisking until smooth with each addition. Do this until all the milk is added, then bring the sauce to the boil and cook for around 5 minutes or so, until the sauce has thickened. Season with salt and pepper, then add the mushrooms and set aside\nPreheat the oven to 180°C/gas mark 4\nTo assemble the lasagne, add a layer of ragu, then add a layer of pasta sheets. Spread over a very scant layer of mushroom béchamel, then another layer of pasta sheets, then another of ragu\nAdd another very scant layer of béchamel, then pasta sheets, then continue repeating these steps until you get to the top. On the final layer of pasta sheets, add the remaining béchamel so that you have a nice thick layer. Grate the Parmesan cheese on top and bake for 30-40 minutes until golden and bubbling\nServe with a green salad dressed with a sharp vinaigrette",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "Helen Graves adds an extra special twist to her traditional lasagne recipe with a richly flavoured mushroom béchamel. Good quality mince and slowly cooking the ragu for an hour ensure this comfort food classic ticks all the boxes.",
            self.harvester_class.description(),
        )
