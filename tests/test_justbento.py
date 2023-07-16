from recipe_scrapers.justbento import JustBento
from tests import ScraperTest


class TestJustBentoScraper(ScraperTest):

    scraper_class = JustBento

    def test_host(self):
        self.assertEqual("justbento.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://justbento.com/handbook/recipes-sides-and-fillers/bento-filler-orange-juice-carrots",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Bento Filler: Orange Juice Carrots"
        )

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("1", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "http://justbento.com/files/bento/images/orangecarrots1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "The thick end of 3 large carrots",
                "Orange juice (freshly squeezed is best but from a carton or concentrate is fine)",
                "1/4 tsp. salt",
                "1 whole red chili pepper",
                "1 Tbs. soy sauce",
                "1/2 Tbs. maple syrup",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Cut the top half of the carrots. Reserve the thin ends for another dish. Peel the parts you will use, and cut into fairly thick rounds. Cut out shapes at this point if you like.",
                    "Put the carrots and chili pepper in a pan, and add enough orange juice to cover. Add the salt. Bring up to a boil, and cook until the carrot slices crisp-tender, about 10 minutes. Add a little water if it looks like the pan will dry out before the carrots are cooked.",
                    "When the carrots are cooked, take out the whole chili pepper. Add the soy sauce and maple syrup, and rapidly boil until the juice is almost gone. Cool off before putting into your bento.",
                    "This will keep for about 3-4 days, well covered in the refrigerator.",
                ]
            ),
            self.harvester_class.instructions(),
        )
