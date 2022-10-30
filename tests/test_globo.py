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
        self.assertEqual("Strogonoff de frango", self.harvester_class.title())

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Alm3")

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://s2.glbimg.com/hXxPtwuPHqQUp2w3pdklGQHBznM=/696x390/smart/filters:cover():strip_icc()/i.s3.glbimg.com/v1/AUTH_1f540e0b94d8437dbbc39d567a1dee68/internal_photos/bs/2022/8/O/xH9h1GSnW1LhMobyL7hQ/strogonoff-de-frango-receita.jpg",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(50, self.harvester_class.total_time())

    def test_ingredients(self):
        self.assertEqual(
            [
                "3 colheres de sopa de óleo",
                "1 tablete de caldo de galinha",
                "1 quilo de peito de frango em cubos",
                "2 colheres de sopa de molho de tomate",
                "2 colheres de sopa de mostarda",
                "2 colheres de sopa de ketchup",
                "Champignon a gosto",
                "1 lata de creme de leite sem soro",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "1 Em uma panela, coloque 3 colheres de sopa de óleo e 1 tablete de caldo de galinha. Espere aquecer para dissolver o tablete.\n2 Em seguida, adicione 1 quilo de peito de frango em cubos e deixe dourar.\n3 Depois, acrescente 2 colheres de sopa de molho de tomate, 2 colheres de sopa de mostarda, 2 colheres de sopa de ketchup e champignon a gosto. Misture.\n4 Desligue o fogo e acrescente 1 lata de creme de leite. Misture novamente.\n5 Sirva em seguida.",
            self.harvester_class.instructions(),
        )
