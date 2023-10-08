from recipe_scrapers.comidinhasdochef import ComidinhasDoChef
from tests import ScraperTest


class TestComidinhasDoChefScraper(ScraperTest):
    scraper_class = ComidinhasDoChef

    def test_host(self):
        self.assertEqual("comidinhasdochef.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Pedro Cavalcanti", self.harvester_class.author())

    def test_canonical_url(self):
        self.assertEqual(
            "https://comidinhasdochef.com/coxa-de-frango-na-fritadeira-eletrica/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            "Coxa de Frango na Fritadeira Elétrica", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("5 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://comidinhasdochef.com/wp-content/uploads/2022/01/Coxa-de-Frango-na-Fritadeira-Elétrica00.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "500 g de coxas de frango",
                "1 colher (sopa) de mostarda",
                "1 colher (sopa) de azeite",
                "2 colheres (sopa) de shoyo",
                "1 unidade de limões espremidos",
                "1 colher (sopa) de salsinha desidratada",
                "1 dente de alho",
                "0 e 1/2 colher (sopa) de colorau",
                "pimenta do reino a gosto",
                "sal a gosto",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Como preparar Coxa de Frango na Fritadeira Elétrica\nPasso 1\nEm uma tigela coloque as coxas de frango e adicione todos os ingredientes ( a mostarda, o azeite, o shoyu, o suco de limão, a salsa, o alho picado, o colorau, a pimenta do reino e o sal);\nPasso 2\nCom as mãos misture bem, massageando as coxas de frango para que o tempero pegue bem;\nPasso 3\nEm seguida tampe a tigela e reserve por 25-30 minutos;\nPasso 4\nPré aqueça sua fritadeira elétrica a 200º C por 5 minutos;\nPasso 5\nColoque as coxas de frango e deixe fritar por 10 minutos;\nPasso 6\nAbra a fritadeira, vire o frango e deixe por mais 10 minutos, mantendo sempre a temperatura de 200º C;\nPasso 7\nRetire as coxas de frango da fritadeira e sirva em seguida.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.8, self.harvester_class.ratings())
