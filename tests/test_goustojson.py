from recipe_scrapers.goustojson import GoustoJson
from tests import ScraperTest


class TestGoustoScraper(ScraperTest):

    scraper_class = GoustoJson
    test_file_name = "gousto"
    test_file_extension = "testjson"

    def test_host(self):
        self.assertEqual("gousto.co.uk", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Malaysian-Style Coconut Meat-Free Chicken With Pickled Cucumber",
        )

    def test_image(self):
        self.assertEqual(
            "https://s3-eu-west-1.amazonaws.com/s3-gousto-production-media/cms/mood-image/1930--Malaysian-Coconut-Chicken--Pickled-Cucumber-1636110687600.jpg",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

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

    def test_instructions(self):
        return self.assertEqual(
            "Add the basmati rice and 300ml [600ml] cold water to a pot with a lid and bring to the boil over a high heatOnce boiling, reduce the heat to very low and cook, covered, for 10-12 min or until all the water has absorbed and the rice is cookedOnce cooked, remove from the heat and keep covered until serving\nWhile the rice is cooking, bash the lemongrass stalk[s] with a rolling pin, cut down the middle lengthways, remove the tough outer layers and chop the softer inner core[s] finelyPeel and roughly chop the shallots, garlic and gingerChop half of the red chilli[es] roughly, and finely slice the rest (save these for garnish!)Put everything into a food processor\nAdd the blanched almonds and half the ground turmeric (you’ll use the rest later!) to the food processor with 2 tbsp [4 tbsp] vegetable oilAdd the soy sauce and a pinch of sugarPulse until you're left with a slightly chunky paste – this is your spice paste\nBoil a kettle, then heat a large wide-based pan (preferably non-stick with a matching lid), with a drizzle of vegetable oil over a medium-high heatCut the meat-free chicken into smaller, bite-sized piecesAdd the meat-free chicken pieces to the pan and sprinkle over the remaining ground turmeric and a pinch of salt and pepperCook for 2-3 min or until warmed through and starting to brown\nWhile the meat-free chicken is cooking, cut the cucumber[s] in half lengthways and then slice finely\nAdd the sliced cucumber to a bowl with the rice vinegar, 1 tsp [2 tsp] sugar and a generous pinch of saltStir it all together and set aside until serving – this is your quick-pickled cucumber\nAdd the spice paste to the meat-free chicken and cook for 2-3 min or until fragrantOnce fragrant, add the tamarind paste with 200ml [300ml] boiled water and cook for a further 2-3 minChop the creamed coconut roughly (if required!), then add it to the pan and cook for 1 min further – this is your Malaysian-style coconut meat-free chicken\nServe the Malaysian-style coconut meat-free chicken with the cooked rice and quick-pickled cucumber to the sideGarnish with the reserved sliced chilli rounds (can't handle the heat? Go easy!)Enjoy!",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())
