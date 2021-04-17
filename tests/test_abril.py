from recipe_scrapers.abril import Abril
from tests import ScraperTest


class TestAbrilScraper(ScraperTest):

    scraper_class = Abril

    def test_host(self):
        self.assertEqual("claudia.abril.com.br", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://claudia.abril.com.br/receitas/estrogonofe-de-carne/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Estrogonofe de carne")

    def test_image(self):
        self.assertEqual(
            "https://claudia.abril.com.br/wp-content/uploads/2020/02/receita-estrogonofe-de-carne.jpg?quality=85&strip=info&w=620&h=372&crop=1",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 porções", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "500 gramas de alcatra cortada em tirinhas",
                "1/4 xícara (chá) de manteiga",
                "1 unidade de cebola picada",
                "1 colher (sobremesa) de mostarda",
                "1 colher (sopa) de ketchup (ou catchup)",
                "1 pitada de pimenta-do-reino",
                "1 unidade de tomate sem pele picado",
                "1 xícara (chá) de cogumelo variado | variados escorridos",
                "1 lata de creme de leite",
                "• sal a gosto",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Derreta a manteiga e refogue a cebola até ficar transparente.\nJunte a carne e tempere com o sal.\nMexa até a carne dourar de todos os lados.\nAcrescente a mostarda, o catchup, a pimenta-do-reino e o tomate picado.\nCozinhe até formar um molho espesso.\nSe necessário, adicione água quente aos poucos.\nQuando o molho estiver encorpado e a carne macia, adicione os cogumelos e o creme de leite.\nMexa por 1 minuto e retire do fogo.\nSirva imediatamente, acompanhado de arroz e batata palha.\nDica: Se juntar água ao refogar a carne, frite-a até todo o líquido evaporar.""",
            self.harvester_class.instructions(),
        )
