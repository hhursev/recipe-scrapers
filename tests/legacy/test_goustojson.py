from responses import GET

from recipe_scrapers.goustojson import GoustoJson
from tests.legacy import ScraperTest


class TestGoustoScraper(ScraperTest):
    scraper_class = GoustoJson

    @classmethod
    def expected_requests(cls):
        yield GET, "https://www.gousto.co.uk/cookbook/vegetarian-recipes/3-cheese-veg-packed-pasta-bake", "tests/legacy/test_data/gousto.testjson"
        yield GET, "https://production-api.gousto.co.uk/cmsreadbroker/v1/recipe/3-cheese-veg-packed-pasta-bake", "tests/legacy/test_data/gousto.testjson"

    def test_host(self):
        self.assertEqual("gousto.co.uk", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.gousto.co.uk/cookbook/vegetarian-recipes/3-cheese-veg-packed-pasta-bake",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "3 Cheese Veg-Packed Pasta Bake",
        )

    def test_description(self):
        self.assertEqual(
            self.harvester_class.description(),
            "This hearty pasta dish doesn't just have a rich tomato sauce, it's layered with mozzarella, cheddar cheese and Italian hard cheese for a tasty and wholesome midweek bake.",
        )

    def test_image(self):
        self.assertEqual(
            "https://production-media.gousto.co.uk/cms/mood-image/2023---3-Cheese-Veg-Packed-Pasta-Bake-7065-1579799730289.jpg",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "10g parsley",
                "40g cheddar cheese",
                "200g finely chopped tomatoes",
                "1 tsp dried basil",
                "20g Italian hard cheese",
                "11g vegetable stock mix",
                "16g tomato paste",
                "125g mozzarella",
                "2 garlic cloves",
                "1 courgette",
                "125g cherry tomatoes",
                "15ml balsamic vinegar",
                "200g tortiglioni",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions_list(self):
        return self.assertEqual(
            [
                "Preheat the oven to 240ºC/ 220ºC (fan)/ gas 9\nBoil a kettle\nPeel and finely chop (or grate) the garlic",
                "Add the tortiglioni to a pot of boiled water with a pinch of salt, bring to the boil over a high heat and cook for 8-10 min or until cooked with a slight bite\nOnce cooked, drain the tortiglioni\nReboil half a kettle",
                "While the pasta is cooking, top, tail and chop the courgette[s] into quarters lengthways, then slice finely\nHeat a large, wide-based pan (preferably non-stick) with a drizzle of olive oil over a medium-high heat\nOnce hot, add the sliced courgette with a pinch of salt and cook for 4 min or until beginning to soften",
                "Meanwhile, dissolve the vegetable stock mix, dried basil, balsamic vinegar, tomato paste and 1 tsp [2 tsp] sugar in 100ml [150ml] boiled water – this is your stock\nChop the cherry tomatoes roughly",
                "Once the courgette is beginning to soften, add the chopped garlic to the pan and cook for 30 secs\nAdd the stock with the chopped cherry tomatoes and the chopped tomatoes and bring to the boil over a high heat\nSeason with a generous grind of black pepper and cook for 3-4 min further",
                "Grate the cheddar cheese\nGrate the Italian hard cheese\nDrain the mozzarella, then pat and squeeze as much liquid out as you can with kitchen paper\nTear the drained mozzarella into rough, bite-sized pieces\nChop the parsley finely, including the stalks",
                "Add the drained tortiglioni to the sauce with the chopped parsley (save some for garnish!) and mix it up\nAdd half the pasta mixture to an oven-proof dish, then top with the grated cheddar cheese\nTop with the remaining pasta mixture, torn mozzarella and grated Italian hard cheese and put the dish in the oven for 5-10 min or until all the cheese has melted – this is your 3 cheese veg-packed pasta bake",
                "Serve the 3 cheese veg-packed pasta bake topped with the reserved chopped parsley and a grind of black pepper and enjoy!\nLoved this recipe? Us too! That’s why it’s one of our Everyday Favourites, available every week.",
            ],
            self.harvester_class.instructions_list(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat the oven to 240ºC/ 220ºC (fan)/ gas 9\nBoil a kettle\nPeel and finely chop (or grate) the garlic\nAdd the tortiglioni to a pot of boiled water with a pinch of salt, bring to the boil over a high heat and cook for 8-10 min or until cooked with a slight bite\nOnce cooked, drain the tortiglioni\nReboil half a kettle\nWhile the pasta is cooking, top, tail and chop the courgette[s] into quarters lengthways, then slice finely\nHeat a large, wide-based pan (preferably non-stick) with a drizzle of olive oil over a medium-high heat\nOnce hot, add the sliced courgette with a pinch of salt and cook for 4 min or until beginning to soften\nMeanwhile, dissolve the vegetable stock mix, dried basil, balsamic vinegar, tomato paste and 1 tsp [2 tsp] sugar in 100ml [150ml] boiled water – this is your stock\nChop the cherry tomatoes roughly\nOnce the courgette is beginning to soften, add the chopped garlic to the pan and cook for 30 secs\nAdd the stock with the chopped cherry tomatoes and the chopped tomatoes and bring to the boil over a high heat\nSeason with a generous grind of black pepper and cook for 3-4 min further\nGrate the cheddar cheese\nGrate the Italian hard cheese\nDrain the mozzarella, then pat and squeeze as much liquid out as you can with kitchen paper\nTear the drained mozzarella into rough, bite-sized pieces\nChop the parsley finely, including the stalks\nAdd the drained tortiglioni to the sauce with the chopped parsley (save some for garnish!) and mix it up\nAdd half the pasta mixture to an oven-proof dish, then top with the grated cheddar cheese\nTop with the remaining pasta mixture, torn mozzarella and grated Italian hard cheese and put the dish in the oven for 5-10 min or until all the cheese has melted – this is your 3 cheese veg-packed pasta bake\nServe the 3 cheese veg-packed pasta bake topped with the reserved chopped parsley and a grind of black pepper and enjoy!\nLoved this recipe? Us too! That’s why it’s one of our Everyday Favourites, available every week.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())
