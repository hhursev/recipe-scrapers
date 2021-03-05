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

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Rask kylling tikka masala")

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.tine.no/_/recipeimage/w_2880%2Ch_1620%2Cc_fill%2Cx_764%2Cy_430%2Cg_xy_center/recipeimage/yshftxnhdmojzhelrupo.png",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "Ris:",
                "4 dl basmatiris",
                "Tikka masala:",
                "400 g kyllingfileter",
                "1 ss TINE Meierismørtil steking",
                "1 stk paprika",
                "½ dl chili",
                "3 stk vårløk",
                "1 ts hvitløksfedd",
                "1 ss hakket, friskingefær",
                "½ dl hakket, friskkoriander",
                "2 ts garam masala",
                "3 dl TINE Lett Crème Fraîche 18 %",
                "3 ss tomatpuré",
                "½ ts salt",
                "¼ ts pepper",
                "Raita:",
                "½ dl slangeagurk",
                "3 dl TINE Yoghurt Naturell",
                "½ dl friskmynte",
                "1 ts hvitløksfedd",
                "½ ts salt",
                "¼ ts pepper",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Kok ris etter anvisningen på pakken.\nTikka masala: Del kylling i biter. Brun kyllingen i smør i en stekepanne på middels varme. Rens og hakk paprika, chili, vårløk og hvitløk og ha det i stekepannen sammen med kyllingen. Rens og finhakk ingefær og frisk koriander. Krydre med garam masala, koriander og ingefær. Hell i crème fraîche og tomatpuré, og la småkoke i 5 minutter. Smak til med salt og pepper.\nRaita: Riv agurk og bland den med yoghurt. Hakk mynte og hvitløk og bland det i. Smak til med salt og pepper.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(3.9, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "En god og rask oppskrift på en kylling tikka masala. Dette er en rett med små smakseksplosjoner som sender tankene til India.",
            self.harvester_class.description(),
        )
