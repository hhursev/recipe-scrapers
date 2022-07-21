from recipe_scrapers.comidinhasdochef import ComidinhasDoChef
from tests import ScraperTest


class TestComidinhasDoChefScraper(ScraperTest):
    scraper_class = ComidinhasDoChef

    def test_host(self):
        self.assertEqual("comidinhasdochef.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Pedro Cavalcanti", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Pernil de Cordeiro com Vinho", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(105, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 porções", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://comidinhasdochef.com/wp-content/uploads/2021/08/Pernil-de-Cordeiro-com-Vinho.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1 pernil de cordeiro",
            "600 ml de vinho branco",
            "4 batatas descascadas e fatiadas",
            "3 cebolas picadas",
            "30 g de folhas de hortelã",
            "30 g de tomilho fresco",
            "2 cabeças de alho cortadas ao meio",
            "30 g de alecrim",
            "1 colher (sopa) de suco de limão",
            "2 colheres (sopa) de sal",
            "1 colher (sopa) de pimenta do reino",
            "½ colher (sopa) de raspas de limão siciliano",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = (
            "Limpe bem o pernil e faça furos com uma faca para que o tempero penetre bem;\n"
            "Em seguida acomode o perfil em um saco próprio para alimentos e coloque o suco de limão siciliano por cima do pernil;\n"
            "Adicione as raspas de limão, a cebola picada, as cabeças de alho, a pimenta do reino, o sal, as hortelãs, o alecrim, o tomilho e o vinho branco;\n"
            "Amarre o saco e vá misturando bem;\n"
            "Deixe o pernil para marinar de um dia para o outro;\n"
            "Dica : Na metade desse tempo vire o pernil para que fique bem temperado;\n"
            "No dia seguinte com o pernil já bem temperado pegue uma forma, forre com papel alumínio e acomode as batatas cortadas em rodelas por toda a forma;\n"
            "Coloque o pernil em cima das batatas e coloque as cabeças de alho também na forma;\n"
            "Use um pouco do tempero para regar o pernil, fazendo com que ele fique ainda mais suculento;\n"
            "Em seguida cubra a forma com papel alumínio e leve para assar em forno pré aquecido a 220º C por cerca de 01 hora e meia;\n"
            "Após esse tempo retire o papel alumínio e leve novamente para assar até dourar bem o pernil;\n"
            "Em seguida retire do forno e prontinho, já pode servir."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
