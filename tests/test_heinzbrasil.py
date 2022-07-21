from recipe_scrapers.heinzbrasil import HeinzBrasil
from tests import ScraperTest


class TestHeinzBrasilScraper(ScraperTest):

    scraper_class = HeinzBrasil

    def test_host(self):
        self.assertEqual("heinzbrasil.com.br", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.heinzbrasil.com.br/recipe/100149100002/chili-com-carne",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Chili com carne")

    def test_image(self):
        self.assertEqual(
            "//d36rz30b5p7lsd.cloudfront.net/heinzbrasilbr/recipes/img/1e1fccb2d38d8b3e3611aa5c99706523.jpeg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 kg de carne moída",
                "1 cebola picada",
                "1 pimentão vermelho cortado em cubos",
                "1 pimentão verde cortado em cubos",
                "100 g de manteiga",
                "50 ml azeite",
                "20 g de especiarias mexicanas (pimentão, cominho, coentro...)",
                "100 ml de café forte",
                "150 g de milho crocante, escorrido",
                "200 g de feijão lavado e escorrido (feijão vermelho da América do Sul)",
                "2 tomates grandes cortados em cubos",
                "400 ml de Ketchup Heinz",
                "200 g de queijo gruyère ralado fininho",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Frite a carne, a cebola e os pimentões na manteiga com o azeite, mexendo bem. Despeje as especiarias mexicanas e o café. Adicione o milho, o feijão, os tomates picados e o Ketchup Heinz. Cozinhe por 5 minutos. Sirva com um bom pedaço de pão e gruyère.",
            self.harvester_class.instructions(),
        )
