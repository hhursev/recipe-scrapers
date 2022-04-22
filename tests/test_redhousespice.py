from recipe_scrapers.redhousespice import RedHouseSpice
from tests import ScraperTest


class TestRedHouseSpiceScraper(ScraperTest):

    scraper_class = RedHouseSpice

    def test_host(self):
        self.assertEqual("redhousespice.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Wei Guo", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Easy Char Siu (Chinese BBQ pork, 叉烧)", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("3 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://redhousespice.com/wp-content/uploads/2020/05/Char-siu-Chinese-BBQ-pork-14-scaled.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 pork shoulder steaks (aka pork butt) (about 350g/12oz, see note 1)",
                "4 tbsp Char Siu sauce (see note 2)",
                "1 tbsp oyster sauce",
                "1/2 tbsp light soy sauce",
                "1/4 tsp Chinese five-spice powder",
                "4 cloves garlic, finely sliced",
                "5 slices ginger",
                "1/2 tsp chilli powder (optional, see note 4)",
                "2 tsp honey",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Marinate the meat\nPut pork steaks in a resealable plastic bag. Add all the ingredients for the marinade.\nSqueeze out air then seal the bag. Rub around for an even coating. Store in the fridge for at least 6 hours (ideally overnight).\nTake the meat out of the bag right before roasting. Keep the marinade for later use.\nPrepare for roasting\nPreheat the oven at 425°F/220°C/Fan 200°C.\nIf using a baking tray with a wire rack that fits inside, fill the tray with hot water (lower than the rack) and put the steak on the rack. Place the tray in the middle of the oven.\nAlternatively, place a large tray with hot water at the bottom of the oven. Then place the steak on the middle rack of the oven.\nRoast & brush (see note 5)\nLeave the meat to roast for 15 mins. Take out and flip it over. Brush some marinade then put back into the oven (Make sure there is always enough water in the tray).\nCook for a further 10 mins. While waiting, mix 2 teaspoons of honey with 2 teaspoons of the marinade.\nThen increase the oven temperature to 460°F/240°C/Fan 220°C. Take out the meat. Brush with the honey mixture.\nPut back into the oven for 5 mins. Then brush the other side with the honey mixture. Roast for a final 3 mins.\nServe\nLeave the meat to rest for 5 mins then slice and serve it in your preferred way.\nYou may also heat up the remaining marinade (remove the garlic & ginger) then serve it as a sauce, a soup base, or a noodle seasoning, etc.""",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
