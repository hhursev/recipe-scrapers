from recipe_scrapers.steamykitchen import SteamyKitchen
from tests import ScraperTest


class TestSteamyKitchenScraper(ScraperTest):
    scraper_class = SteamyKitchen
    test_file_name = "steamykitchen_2"

    def test_host(self):
        self.assertEqual("steamykitchen.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Jaden", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Hungarian Pork Stew Recipe", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(120, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://steamykitchen.com/wp-content/uploads/2012/10/pork-paprikash-recipe-9514.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "8 medium yellow onions, chopped to medium dice",
                "1/3 cup canola/vegetable oil, plus more for frying",
                "9 3/4-inch thick boneless center cut loin pork chops, trimmed of fat, sliced in half length-wise, pounded 1/4 inch thin (if you’re lucky enough to find the thin loin chops, you’ll only have to pound them thin)",
                "1 tablespoon salt",
                "1 tablespoon pepper",
                "flour for dredging",
                "3 tablespoons sweet Hungarian paprika",
                "6-8 cups water, or enough to fully immerse all ingredients in the pot",
                "Vegeta to taste, approximately 1 tablespoon (but if you can’t find it, just use vegetable/chicken soup seasoning packets)",
                "1 cup sour cream",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "In a large pot (6 qt) over medium to medium-high heat, add onions and canola oil. Saute onions until they are translucent, but not browned. Add more oil when necessary to keep them slick in the process. When the onions have finished cooking, turn down heat to low, add paprika to mixture and stir to mix well.\nSeason each side of the pork slices generously with salt and pepper. Dredge the slices in flour on each side.\nIn a frying pan over medium-high to high heat, heat about an inch of canola or vegetable oil. Fry each slice of pork until just barely golden brown around the edges, about 1-2 minutes, flipping halfway through. If they are thin enough, this will be enough to cook them fully. Lay them between sheets of paper towel on a plate to catch excess oil.\nCut each of the pork slices in half and place them back in the pot with the onions. Add enough water to the pot to cover the pork and onions. Cover pot and simmer on medium heat for 45 minutes to 1 hour. Stir occasionally.\nWhen the stew is thickened up a bit from the flour and the onions are starting to disappear, it is ready for the final seasoning. Add salt, pepper and Vegeta seasoning to taste. Add sour cream and stir until the stew is a rich, thick consistency.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())
