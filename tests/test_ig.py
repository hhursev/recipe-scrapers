from recipe_scrapers.ig import IG
from tests import ScraperTest


class TestIGScraper(ScraperTest):

    scraper_class = IG

    def test_host(self):
        self.assertEqual("receitas.ig.com.br", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://receitas.ig.com.br/estrogonofe-de-cogumelos/4e7b634e7bb4e2ad5c000054.html",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Estrogonofe de cogumelos")

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://i0.statig.com.br/bancodeimagens/4y/4c/rs/4y4crseb7npraepfzuhc8iimy.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "3 colheres (sopa) de azeite",
                "1 cebola roxa cortada em cubos",
                "2 dentes de alho espremidos",
                "500 g de cogumelos variados (shiitake, shimeji, portobelo e champignons)",
                "2 colheres (sopa) de suco de limão",
                "1 colher (sopa) de catchup",
                "400 ml de caldo de legumes",
                "1 colher (sopa) de amido de milho dissolvido em água fria",
                "100 g de creme de leite",
                "½ xícara (chá) de iogurte desnatado",
                "3 colheres (sopa) de salsinha picada",
                "Arroz branco para acompanhar",
                "Batata palha",
                "",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Em uma panela com o azeite, refogue a cebola e o alho até que a cebola comece a murchar. Junte os cogumelos, o limão, e o catchup. Cozinhe por 5 a 10 minutos. Adicione o caldo e cozinhe por mais 5 minutos. Junte a maisena e deixe ferver até engrossar ligeiramente. Por último, adicione o creme de leite, tempere e junte a salsinha. Sirva com arroz e batata palha.",
            self.harvester_class.instructions(),
        )
