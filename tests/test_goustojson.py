from responses import GET

from recipe_scrapers.goustojson import GoustoJson
from tests import ScraperTest


class TestGoustoScraper(ScraperTest):

    scraper_class = GoustoJson

    @classmethod
    def expected_requests(cls):
        yield GET, "https://www.gousto.co.uk/cookbook/recipes/malaysian-style-coconut-meat-free-chicken-pickled-cucumber", "tests/test_data/gousto.testjson"
        yield GET, "https://production-api.gousto.co.uk/cmsreadbroker/v1/recipe/malaysian-style-coconut-meat-free-chicken-pickled-cucumber", "tests/test_data/gousto.testjson"

    def test_host(self):
        self.assertEqual("gousto.co.uk", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Malaysian-Style Coconut Meat-Free Chicken With Pickled Cucumber",
        )

    def test_description(self):
        self.assertEqual(
            self.harvester_class.description(),
            "Inspired by the fragrant flavours of the classic Malaysian chicken dish 'Ayam Percik'. Our spice paste blends lemongrass, almonds and ginger before adding coconut cream and meat-free chicken. Served with fluffy rice and quick-pickled cucumber.",
        )

    def test_image(self):
        self.assertEqual(
            "https://s3-eu-west-1.amazonaws.com/s3-gousto-production-media/cms/mood-image/1930--Malaysian-Coconut-Chicken--Pickled-Cucumber-1636110687600.jpg",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "50g solid creamed coconut",
                "15g fresh root ginger",
                "1 tsp ground turmeric",
                "2 shallots",
                "15ml soy sauce",
                "165g meat-free chicken bites",
                "130g basmati rice",
                "15g tamarind paste",
                "30ml rice vinegar",
                "1 red chilli",
                "1/2 cucumber",
                "3 garlic cloves",
                "25g blanched almonds",
                "1 fresh lemongrass",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions_list(self):
        return self.assertEqual(
            [
                "Add the basmati rice and 300ml [600ml] cold water to a pot with a lid and bring to the boil over a high heat\nOnce boiling, reduce the heat to very low and cook, covered, for 10-12 min or until all the water has absorbed and the rice is cooked\nOnce cooked, remove from the heat and keep covered until serving",
                "While the rice is cooking, bash the lemongrass stalk[s] with a rolling pin, cut down the middle lengthways, remove the tough outer layers and chop the softer inner core[s] finely\nPeel and roughly chop the shallots, garlic and ginger\nChop half of the red chilli[es] roughly, and finely slice the rest (save these for garnish!)\nPut everything into a food processor",
                "Add the blanched almonds and half the ground turmeric (you’ll use the rest later!) to the food processor with 2 tbsp [4 tbsp] vegetable oil\nAdd the soy sauce and a pinch of sugar\nPulse until you're left with a slightly chunky paste – this is your spice paste",
                "Boil a kettle, then heat a large wide-based pan (preferably non-stick with a matching lid), with a drizzle of vegetable oil over a medium-high heat\nCut the meat-free chicken into smaller, bite-sized pieces\nAdd the meat-free chicken pieces to the pan and sprinkle over the remaining ground turmeric and a pinch of salt and pepper\nCook for 2-3 min or until warmed through and starting to brown",
                "While the meat-free chicken is cooking, cut the cucumber[s] in half lengthways and then slice finely",
                "Add the sliced cucumber to a bowl with the rice vinegar, 1 tsp [2 tsp] sugar and a generous pinch of salt\nStir it all together and set aside until serving – this is your quick-pickled cucumber",
                "Add the spice paste to the meat-free chicken and cook for 2-3 min or until fragrant\nOnce fragrant, add the tamarind paste with 200ml [300ml] boiled water and cook for a further 2-3 min\nChop the creamed coconut roughly (if required!), then add it to the pan and cook for 1 min further – this is your Malaysian-style coconut meat-free chicken",
                "Serve the Malaysian-style coconut meat-free chicken with the cooked rice and quick-pickled cucumber to the side\nGarnish with the reserved sliced chilli rounds (can't handle the heat? Go easy!)\nEnjoy!",
            ],
            self.harvester_class.instructions_list(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Add the basmati rice and 300ml [600ml] cold water to a pot with a lid and bring to the boil over a high heat\nOnce boiling, reduce the heat to very low and cook, covered, for 10-12 min or until all the water has absorbed and the rice is cooked\nOnce cooked, remove from the heat and keep covered until serving\nWhile the rice is cooking, bash the lemongrass stalk[s] with a rolling pin, cut down the middle lengthways, remove the tough outer layers and chop the softer inner core[s] finely\nPeel and roughly chop the shallots, garlic and ginger\nChop half of the red chilli[es] roughly, and finely slice the rest (save these for garnish!)\nPut everything into a food processor\nAdd the blanched almonds and half the ground turmeric (you’ll use the rest later!) to the food processor with 2 tbsp [4 tbsp] vegetable oil\nAdd the soy sauce and a pinch of sugar\nPulse until you're left with a slightly chunky paste – this is your spice paste\nBoil a kettle, then heat a large wide-based pan (preferably non-stick with a matching lid), with a drizzle of vegetable oil over a medium-high heat\nCut the meat-free chicken into smaller, bite-sized pieces\nAdd the meat-free chicken pieces to the pan and sprinkle over the remaining ground turmeric and a pinch of salt and pepper\nCook for 2-3 min or until warmed through and starting to brown\nWhile the meat-free chicken is cooking, cut the cucumber[s] in half lengthways and then slice finely\nAdd the sliced cucumber to a bowl with the rice vinegar, 1 tsp [2 tsp] sugar and a generous pinch of salt\nStir it all together and set aside until serving – this is your quick-pickled cucumber\nAdd the spice paste to the meat-free chicken and cook for 2-3 min or until fragrant\nOnce fragrant, add the tamarind paste with 200ml [300ml] boiled water and cook for a further 2-3 min\nChop the creamed coconut roughly (if required!), then add it to the pan and cook for 1 min further – this is your Malaysian-style coconut meat-free chicken\nServe the Malaysian-style coconut meat-free chicken with the cooked rice and quick-pickled cucumber to the side\nGarnish with the reserved sliced chilli rounds (can't handle the heat? Go easy!)\nEnjoy!",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())
