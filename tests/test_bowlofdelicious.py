from recipe_scrapers.bowlofdelicious import BowlOfDelicious
from tests import ScraperTest


class TestBowlOfDeliciousScraper(ScraperTest):

    scraper_class = BowlOfDelicious

    def test_host(self):
        self.assertEqual("bowlofdelicious.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.bowlofdelicious.com/six-minute-seared-ahi-tuna-steaks/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Six-Minute Seared Ahi Tuna Steaks"
        )

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.bowlofdelicious.com/wp-content/uploads/2019/09/Ahi-Tuna-Steaks-square.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '2 ahi tuna (yellowfin tuna) steaks ((about 4 oz. each, at least 1.5" thick))',
                "2 tablespoons soy sauce",
                "1 tablespoon toasted sesame oil (see notes)",
                "1 tablespoon honey (see notes)",
                "1/2 teaspoon kosher salt",
                "1/4 teaspoon black pepper (to taste)",
                "1/4 teaspoon cayenne pepper ((optional))",
                "1 tablespoon canola oil (or olive oil)",
                "green onions, toasted sesame seeds, and lime wedges (for serving (optional))",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Pat the ahi tuna steaks dry with a paper towel. Place on a plate or inside a plastic bag.\nMix the soy sauce (2 tablespoons), toasted sesame oil (1 tablespoon), honey (1 tablespoon) kosher salt (1/2 teaspoon- OMIT if marinating for more than a couple hours, see notes), pepper (1/4 teaspoon), and cayenne pepper (1/4 teaspoon) until honey is fully dissolved. Pour over the ahi tuna steaks and turn over to coat completely. Optional: allow to marinate for at least 10 minutes, or up to overnight in the refrigerator. Also optional: Reserve a spoonful or two of the marinade before coating the fish for drizzling on top after you've cooked it.\nHeat a medium skillet (preferably non-stick or a well-seasoned cast iron skillet) on medium-high to high until very hot ( or medium medium-high for nonstick). I recommend giving cast iron 3-5 minutes to get hot and nonstick about 1 minute, depending on how thick it is.\nAdd the canola oil (1 tablespoon) to the hot pan. Sear the tuna for 2 minutes on each side for medium rare (1.5 minutes on each side for rare; 3 on each side for medium). (Note: different burners get hotter depending on your stove. Use your best judgement whether you use medium, medium-high, or high heat, as the marinade may burn if too high heat is used)\nRemove to a cutting board and allow to rest for at least 3 minutes. Slice into 1/2 inch slices and serve garnished with green onions, toasted sesame seeds, and a squeeze of fresh lime juice, if desired.",
            self.harvester_class.instructions(),
        )
