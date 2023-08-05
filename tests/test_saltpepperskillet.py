# mypy: allow-untyped-defs

from recipe_scrapers.saltpepperskillet import SaltPepperSkillet
from tests import ScraperTest


class TestSaltPepperSkilletScraper(ScraperTest):

    scraper_class = SaltPepperSkillet

    def test_host(self):
        self.assertEqual("saltpepperskillet.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Justin", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Smoked Whole Chicken Recipe", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Main", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(435, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://saltpepperskillet.com/wp-content/uploads/smoked-whole-chicken-horizontal-head-on.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 (4 to 5 lb) Chicken",
                "3 tbsp Chicken Dry Rub ((omit the salt if brining the chicken))",
                "Apple or Cherry Wood for Smoke",
                "4 quarts Water",
                "1 cup Diamond Kosher Salt ((Use 3/4 cup if using Morton Kosher Salt))",
                "3/4 cup Sugar",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "To Brine the Chicken (optional but recommended)\nIn a large bowl or container large enough to easily fit the chicken, whisk the salt and sugar with the water until it is dissolved. Submerge the chicken in the brine, then cover and refrigerate for 3 to 6 hours.\nThoroughly rinse and pat the chicken dry with paper towels and discard the brine. Let the chicken sit out on the counter to come up to temperature while you set up your smoker.\nTo Smoke the Chicken\nPrep the smoker for indirect heat cooking and bring the temperature between 225° and 275* F 250° F *see note. Add wood chunks or pellets according to the manufacturer's instructions and place a drip pan filled with water below where the chicken will smoke.\nApply a light slather (canola oil, mustard or hot sauce) all over the skin of the chicken to help the spice rub stick. Sprinkle about 2 to 3 tablespoons of dry rub with a shaker for even distribution all over the skin. Do the presentation side (breasts) last.\nPlace the chicken in the smoker and cook until the internal temperature of the breasts reaches 160° F and thighs the are around 180° F. This will take between 3 and 4 hours. Use a probe thermometer to verify. The temperature will continue to rise about 5 degrees once removed from the heat.\nRest the chicken on a cutting board for 15 minutes before carving and serving.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Brined, dry rubbed and applewood smoked with a little kick and sweetness. Making a whole chicken in the smoker is the perfect way to feed a crowd or feast for days on succulent yardbird.",
            self.harvester_class.description(),
        )
