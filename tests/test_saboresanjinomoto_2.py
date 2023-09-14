# mypy: allow-untyped-defs

from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.saboresanjinomoto import SaboresAnjinomoto
from tests import ScraperTest


class TestSaboresAnjinomotoScraper(ScraperTest):

    scraper_class = SaboresAnjinomoto
    test_file_name = "saboresanjinomoto_2"

    def test_host(self):
        self.assertEqual("saboresajinomoto.com.br", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("sabores ajinomoto", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Crepioca com brócolis e frango", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Ovos", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.saboresajinomoto.com.br/uploads/images/recipes/crepioca_de_brocolis_e_frango.webp",
            self.harvester_class.image(),
        )

    def test_consistent_ingredient_list(self):
        expected_ingredients = [
            "1 e meia colher (sopa) Azeite de Oliva Extra Virgem TERRANO®",
            "3 filés de peito de frango (300 g)",
            "1 tomate pequeno, com pele e sem sementes, picado",
            "1 sachê de Caldo SAZÓN® Lev Galinha",
            "3 colheres (sopa) de requeijão cremoso",
            "6 ovos",
            "6 colheres (sopa) de goma para tapioca",
            "3 colheres (sopa) de leite desnatado",
            "meia xícara (chá) de floretes de brócolis picadinhos",
        ]

        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        expected_groups = [
            IngredientGroup(
                ingredients=[
                    "1 e meia colher (sopa) Azeite de Oliva Extra Virgem TERRANO®",
                    "3 filés de peito de frango (300 g)",
                    "1 tomate pequeno, com pele e sem sementes, picado",
                    "1 sachê de Caldo SAZÓN® Lev Galinha",
                    "3 colheres (sopa) de requeijão cremoso",
                ],
                purpose="Recheio",
            ),
            IngredientGroup(
                ingredients=[
                    "6 ovos",
                    "6 colheres (sopa) de goma para tapioca",
                    "3 colheres (sopa) de leite desnatado",
                    "meia xícara (chá) de floretes de brócolis picadinhos",
                ],
                purpose="Massa",
            ),
        ]

        actual_groups = self.harvester_class.ingredient_groups()

        self.assertEqual(expected_groups, actual_groups)

    def test_instructions(self):
        expected_instructions = [
            "Faça o recheio: em uma frigideira média, aqueça meia colher (sopa) do Azeite TERRANO® e frite os filés de frango por 4 minutos de cada lado, ou até dourarem. Retire da frigideira e desfie o frango.",
            "Volte o frango para a frigideira e leve ao fogo médio. Junte o tomate e metade do Caldo SAZÓN®, e refogue por 2 minutos, ou até o tomate desmanchar parcialmente. Adicione o requeijão e misture. Retire da frigideira e reserve aquecido.",
            "Prepare a massa: em uma tigela média, coloque os ovos, a goma para tapioca, o leite e o Caldo SAZÓN® restante, e misture até ficar homogêneo. Junte os brócolis e misture.",
            "Em uma frigideira média (26 cm de diâmetro), untada com um fio do Azeite TERRANO®, coloque 1 concha da massa e cozinhe por 1 minuto. Vire, disponha parte do recheio e dobre a crepioca ao meio. Tampe e deixe por 2 minutos de cada lado. Repita o processo com a massa e recheio restantes, repondo o Azeite TERRANO® quando necessário. Sirva em seguida.",
        ]
        expected_instructions = "\n".join(expected_instructions)
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(3.0, self.harvester_class.ratings())

    def test_language(self):
        self.assertEqual("pt-br", self.harvester_class.language())
