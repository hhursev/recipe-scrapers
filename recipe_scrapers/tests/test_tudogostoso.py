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
            'Caipirinha - Original'
        )

    def test_total_time(self):
        self.assertEqual(
            5,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                '1 limão grande'
                '1 limão grande'
                '2 colheres de açúcar'
                'gelo a gosto'
                'cachaça'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
	    "Pegue o limão coloque-o na horizontal e retire as duas pontas, vire-o na vertical e corte-o ao meio, retire os meio (parte branca) do limão e fatie.Coloque o limão fatiado e duas colheres bem cheias de açúcar dentro de um copo próprio para a bebida e com um socador esprema até que saia todo o suco do limão.Coloque pedras de gelo até quase encher o copo (aproximadamente 12 pedras pequenas de gelo) e encha o copo com a cachaça.Mexa bem com uma colher ou coloque em uma coqueteleira e sirva-se!",
            self.harvester_class.instructions()
        )
