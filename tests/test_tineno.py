from recipe_scrapers.tineno import TineNo
from tests import ScraperTest


class TestTineNoScraper(ScraperTest):
    scraper_class = TineNo

    def test_host(self):
        self.assertEqual("tine.no", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.tine.no/oppskrifter/middag-og-hovedretter/kylling-og-fjarkre/rask-kylling-tikka-masala",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("TINE", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Rask kylling tikka masala", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("middag", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.tine.no/_/recipeimage/w_2880%2Ch_1620%2Cc_fill%2Cx_764%2Cy_430%2Cg_xy_center/recipeimage/yshftxnhdmojzhelrupo.png",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "4 dl basmatiris",
                "400 g kyllingfileter",
                "1 ss TINE® Meierismør til steking",
                "1 stk paprika",
                "0.5 dl chili",
                "3 stk vårløk",
                "1 ts hvitløksfedd",
                "1 ss hakket, frisk ingefær",
                "0.5 dl hakket, frisk koriander",
                "2 ts garam masala",
                "3 dl TINE® Lett Crème Fraîche 18 %",
                "3 ss tomatpuré",
                "0.5 ts salt",
                "0.25 ts pepper",
                "0.5 dl slangeagurk",
                "3 dl TINE® Yoghurt Naturell",
                "0.5 dl frisk mynte",
                "1 ts hvitløksfedd",
                "0.5 ts salt",
                "0.25 ts pepper",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Kok ris etter anvisningen på pakken.\nTikka masala:\nDel kylling i biter. Brun kyllingen i smør i en stekepanne på middels varme.\nRens og hakk paprika, chili, vårløk og hvitløk og ha det i stekepannen sammen med kyllingen. Rens og finhakk ingefær og frisk koriander. Krydre med garam masala, koriander og ingefær.\nHell i crème fraîche og tomatpuré, og la småkoke i 5 minutter. Smak til med salt og pepper.\nRaita:\nRiv agurk og bland den med yoghurt. Hakk mynte og hvitløk og bland det i. Smak til med salt og pepper.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(3.9, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("indisk", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "En god og rask oppskrift på en kylling tikka masala. Dette er en rett med små smakseksplosjoner som sender tankene til India.",
            self.harvester_class.description(),
        )
