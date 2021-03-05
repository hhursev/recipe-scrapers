from recipe_scrapers.globo import Globo
from tests import ScraperTest


class TestGloboScraper(ScraperTest):

    scraper_class = Globo

    def test_host(self):
        self.assertEqual("receitas.globo.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://receitas.globo.com/strogonoff-de-frango-simples-4fbe8cc656ec5b3c9801b7e5.ghtml",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Strogonoff de Frango Simples", self.harvester_class.title())

    def test_yields(self):
        self.assertEqual("8 porções", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://s2.glbimg.com/idlMgKR80VkIYBguqV_c2gOTHCQ=/696x390/smart/filters:cover():strip_icc()/i.s3.glbimg.com/v1/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2020/4/r/9xz2kyQHKWlgkAthy9tA/estrogonofe-de-frango.jpg",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(50, self.harvester_class.total_time())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 quilo de peito de frango sem pele",
                "1 tablete de caldo de galinha",
                "3 colheres de sopa de óleo",
                "2 latas de creme de leite sem soro",
                "2 colheres de sopa de molho de tomate",
                "2 colheres de sopa de ketchup",
                "2 colheres de sopa de mostarda",
                "Champignon",
                "Batata palha e arroz branco para acompanhar",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "1. Em uma panela a fogo médio, acrescente o óleo e o caldo de galinha e, dissolva o caldo. Logo em seguida coloque o frango picado em cubos na panela e deixe cozinhar, sempre dando uma olhadinha para não queimar.\n2. Assim que o frango estiver bem cozido, acrescente o molho de tomate, o ketchup, a mostarda e champignon a gosto.\n3. Abaixe o fogo e coloque o creme de leite e mexa bem até se tornar um creme homogêneo.\n4. Está pronto para servir.",
            self.harvester_class.instructions(),
        )
