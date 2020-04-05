import os
import unittest

from recipe_scrapers.cybercook import Cybercook


class TestCybercook(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'cybercook.testhtml'
        )) as file_opened:
            self.harvester_class = Cybercook(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'cybercook.com.br',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Strogonoff de Frango'
        )

    def test_total_time(self):
        self.assertEqual(
            30,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        self.assertEqual("4 porções", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            'https://img.cybercook.com.br/imagens/receitas/644/strogonoff-de-frango-1.jpg',
            self.harvester_class.image()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '200 gr de molho de tomate',
                '1 unidade de cebola picada',
                '2 dentes de alho',
                '1 lata de creme de leite sem soro',
                '600 gr de peito de frango sem osso',
                '2 colheres (sopa) de óleo de soja',
                'sal a gosto',
                'pimenta-do-reino branca a gosto',
                '100 gr de champignon em conserva'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Primeiro corte o frango em cubinhos.\nEm uma panela média, coloque o óleo, a cebola e espere dourar.\nDepois coloque o frango o tablete de caldo de galinha e o sal a gosto, aqueça até o ponto de fritura.\nMexa bem e tampe meia panela para que crie água, espere.\nSumir a água e começar a fritura.\nQuando o frango já tiver dourado, acrescente o molho de tomate.\nDepois coloque a lata de creme de leite e mexa até espalhar, com a mesma lata encha de água.\nMexa mais uma vez até misturar e deixe levantar fervura.\nAcrescente o oregano e pronto.\nO strogonoff está pronto para ser servido.',
            self.harvester_class.instructions()
        )

    def test_ratings(self):
        self.assertEqual(
            4.0,
            self.harvester_class.ratings()
        )
