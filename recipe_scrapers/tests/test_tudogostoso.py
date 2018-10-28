import os
import unittest

from recipe_scrapers.tudogostoso import TudoGostoso


class TestTudoGostosoScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'tudogostoso.testhtml'
        )) as file_opened:
            self.harvester_class = TudoGostoso(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'tudogostoso.com.br',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Brigadeiro'
        )

    def test_total_time(self):
        self.assertEqual(
            25,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '1 caixa de leite condensado',
                '1 colher (sopa) de margarina sem sal',
                '7 colheres (sopa) de achocolatado ou 4 colheres (sopa) de chocolate em pó',
                'chocolate granulado'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Em uma panela funda, acrescente o leite condensado, a margarina e o chocolate em pó\nCozinhe em fogo médio e mexa até que o brigadeiro comece a desgrudar da panela\nDeixe esfriar e faça pequenas bolas com a mão passando a massa no chocolate granulado',
            self.harvester_class.instructions()
        )
