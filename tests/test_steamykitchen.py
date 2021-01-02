from tests import ScraperTest

from recipe_scrapers.steamykitchen import SteamyKitchen


class TestSteamyKitchenScraper(ScraperTest):

    scraper_class = SteamyKitchen

    def test_host(self):
        self.assertEqual("steamykitchen.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://steamykitchen.com/23936-hungarian-pork-stew-recipe-video.html",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Hungarian Pork Stew Recipe")

    def test_total_time(self):
        self.assertEqual(120, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("10 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://steamykitchen.com/wp-content/uploads/2012/11/pork-paprikash-recipe-featured-9514-180x220.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertListEqual(
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
        return self.assertEqual(
            "1. In a large pot (6 qt) over medium to medium-high heat, add onions and canola oil. Saute onions until they are translucent, but not browned. Add more oil when necessary to keep them slick in the process. When the onions have finished cooking, turn down heat to low, add paprika to mixture and stir to mix well.\n2. Season each side of the pork slices generously with salt and pepper. Dredge the slices in flour on each side.\n3. In a frying pan over medium-high to high heat, heat about an inch of canola or vegetable oil. Fry each slice of pork until just barely golden brown around the edges, about 1-2 minutes, flipping halfway through. If they are thin enough, this will be enough to cook them fully. Lay them between sheets of paper towel on a plate to catch excess oil.\n4. Cut each of the pork slices in half and place them back in the pot with the onions. Add enough water to the pot to cover the pork and onions. Cover pot and simmer on medium heat for 45 minutes to 1 hour. Stir occasionally.\n5. When the stew is thickened up a bit from the flour and the onions are starting to disappear, it is ready for the final seasoning. Add salt, pepper and Vegeta seasoning to taste. Add sour cream and stir until the stew is a rich, thick consistency.",
            self.harvester_class.instructions(),
        )
