import os
import unittest

from recipe_scrapers.allrecipesbr import AllRecipesBr


class TestAllRecipesBrScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'allrecipesbr.testhtml'
        )) as file_opened:
            self.harvester_class = AllRecipesBr(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'allrecipes.com.br',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Bolo de iogurte no liquidificador'
        )

    def test_total_time(self):
        self.assertEqual(
            40,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '1/2 copo (americano) de óleo',
                '1 copo (americano) de iogurte',
                '4 ovos',
                '2 copos (americanos) de açúcar',
                '2 copos (americanos) de farinha de trigo',
                '1 colher (sopa) de fermento'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Preaqueça o forno em temperatura média (180ºC) e unte e enfarinhe uma forma redonda com furo no meio.\nBata todos os ingredientes no liquidificador, começando pelos ingredientes líquidos e terminando com os ingredientes secos.\nDespeje a massa na forma preparada e leve ao forno até dourar. Espere esfriar um pouco para desenformar e servir.',
            self.harvester_class.instructions()
        )
