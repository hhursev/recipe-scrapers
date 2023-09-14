# mypy: allow-untyped-defs

from recipe_scrapers.saboresanjinomoto import SaboresAnjinomoto
from tests import ScraperTest


class TestSaboresAnjinomotoScraper(ScraperTest):

    scraper_class = SaboresAnjinomoto
    test_file_name = "saboresanjinomoto_1"

    def test_host(self):
        self.assertEqual("saboresajinomoto.com.br", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("sabores ajinomoto", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Purê de batata com frango", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Verduras e Legumes", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("5 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.saboresajinomoto.com.br/uploads/images/recipes/pure-de-batata-com-frango.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "3 colheres (sopa) de margarina sem sal (45 g)",
            "1 filé de peito de frango (100 g)",
            "2 batatas médias, cozidas e espremidas (400 g)",
            "meia xícara (chá) de leite (100 ml)",
            "meia colher (chá) de sal",
            "meia colher (chá) de AJI-NO-MOTO®",
        ]

        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = [
            "Em uma panela média, derreta 1 colher (sopa) da margarina em fogo médio e frite o frango por cerca de 10 minutos, virando na metade do tempo, ou até dourar. Retire do fogo, desfie com o auxílio de um garfo e reserve aquecido.",
            "Na mesma panela, derreta a margarina restante, em fogo alto, junte a batata, o leite, o sal e o AJI-NO-MOTO®, e mexa até que fique homogêneo.",
            "Acrescente o frango, misture e retire do fogo. Sirva em seguida.",
        ]
        expected_instructions = "\n".join(expected_instructions)
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(4.0, self.harvester_class.ratings())

    def test_language(self):
        self.assertEqual("pt-br", self.harvester_class.language())
