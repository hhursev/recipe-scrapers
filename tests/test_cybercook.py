from recipe_scrapers.cybercook import Cybercook
from tests import ScraperTest


class TestCybercook(ScraperTest):

    scraper_class = Cybercook

    def test_host(self):
        self.assertEqual("cybercook.com.br", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://cybercook.com.br/receitas/aves/strogonoff-de-frango-16644",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Strogonoff de Frango")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Leticia Obo Andreghetti")

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://img.cybercook.com.br/receitas/644/strogonoff-de-frango-2.jpeg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "Molho de tomate 200 gramas",
                "Cebola 1 unidade",
                "Alho 2 dentes",
                "Creme de Leite 1 lata",
                "Peito de Frango 600 gramas",
                "Óleo de soja 2 colheres (sopa)",
                "Sal a gosto",
                "Pimenta-do-Reino Branca a gosto",
                "Champignon em conserva 100 gramas",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Primeiro corte o frango em cubinhos.\nEm uma panela média, coloque o óleo, o alho e a cebola e espere dourar.\nDepois coloque o frango e o sal e a pimenta a gosto, aqueça até o ponto de fritura.\nMexa bem e tampe meia panela para que crie água, espere.\nSumir a água e começar a fritura.\nQuando o frango já tiver dourado, acrescente o molho de tomate e o champignon.\nDepois coloque a lata de creme de leite e mexa até espalhar, com a mesma lata encha de água.\nMexa mais uma vez até misturar e deixe levantar fervura.\nO strogonoff está pronto para ser servido.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.0, self.harvester_class.ratings())
