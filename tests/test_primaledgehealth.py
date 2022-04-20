from recipe_scrapers.primaledgehealth import PrimalEdgeHealth
from tests import ScraperTest


class TestPrimalEdgeHealthScraper(ScraperTest):

    scraper_class = PrimalEdgeHealth

    def test_host(self):
        self.assertEqual("primaledgehealth.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.primaledgehealth.com/no-bake-custard/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "No Bake Custard (Keto & Carnivore-Friendly)"
        )

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.primaledgehealth.com/wp-content/uploads/2021/02/no-bake-custard-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 tablespoon grass-fed beef gelatin",
                "1¼ cups half and half",
                "1 tablespoon sweetener (optional, see note)",
                "½ teaspoon vanilla extract",
                "2 raw egg yolks",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Sprinkle the gelatin over 2 tablespoons of water in a wide, shallow dish. The more surface area to cover, the better. Set aside to thicken.\nIf sweetening: Warm the cream over low heat in a small saucepan on the stovetop. Add the sweetener and stir until it dissolves. Then stir in vanilla.If not sweetening: Add vanilla to half and half in a bowl without heating.\nWhisk egg yolks into the half and half.\nMix in the gelatin. Gently warm liquid over low heat until gelatin dissolves if needed.\nDivide into individual ramekins or use one single serving dish. Chill in the refrigerator for at least 1 hour until set. Serve cold.",
            self.harvester_class.instructions(),
        )
