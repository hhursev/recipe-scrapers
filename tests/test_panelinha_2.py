from recipe_scrapers.panelinha import Panelinha
from tests import ScraperTest


class TestPanelinhaScraper(ScraperTest):
    scraper_class = Panelinha

    @property
    def test_file_name(self):
        return "{}_2".format(self.scraper_class.__name__.lower())

    def test_host(self):
        self.assertEqual("panelinha.com.br", self.harvester_class.host())

    def test_title(self):
        self.assertEqual("Arroz sírio com frango", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(0, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("Até 2 porções", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cdn.panelinha.com.br/receita/1433732400000-Arroz-sirio-com-frango.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 bifes de filé de peito de frango (cerca de 240 g)",
                "⅓ de xícara (chá) de arroz",
                "⅔ de xícara (chá) de lentilha",
                "1 cebola",
                "1 dente de alho",
                "2 xícaras (chá) de água",
                "1 ½ colher (sopa) de azeite",
                "½ colher (chá) de pimenta síria",
                "1 colher (chá) de sal",
                "1 pitada de açúcar",
                "¼ de xícara (chá) de nozes picadas",
                "⅓ de xícara (chá) de iogurte natural",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        expected_instructions = (
            "Coloque a lentilha numa tigela funda e cubra com 1 xícara (chá) de água fervente. Deixe de molho enquanto prepara os outros ingredientes.\n"
            "Descasque e fatie a cebola em meias-luas médias. Descasque e pique fino o alho. Corte os bifes de frango em tirinhas de cerca de 1 cm x 7 cm.\n"
            "Leve ao fogo médio uma panela média. Quando aquecer, junte 1 colher (sopa) de azeite e a cebola fatiada. Tempere com uma pitada de sal e de açúcar e abaixe o fogo. Deixe cozinhar por cerca de 10 minutos, mexendo de vez enquanto, até a cebola ficar bem dourada - não aumente o fogo para acelerar o processo, caso contrário, a cebola pode queimar em vez de caramelizar.\n"
            "Transfira a cebola para uma tigela e aumente o fogo para médio. Acrescente o restante do azeite e doure as tirinhas de frango aos poucos - se colocar todas ao mesmo tempo, elas vão soltar o próprio líquido e cozinhar no vapor, em vez de dourar. Tempere com uma pitada de sal e mexa aos poucos para dourar por igual.\n"
            "Junte a cebola dourada e o alho e misture por apenas 1 minuto. Acrescente o arroz, 1 colher (chá) de sal e a pimenta síria. Mexa bem para envolver os grãos nos temperos.\n"
            "Numa peneira, escorra a lentilha e junte à panela. Cubra com 2 xícaras (chá) de água, misture e deixe cozinhar. Assim que começar a ferver, diminua o fogo e deixe cozinhar com a tampa entreaberta até a água secar, por cerca de 20 minutos.\n"
            "Desligue o fogo e mantenha a panela tampada por 5 minutos antes de servir, para que os grãos terminem de cozinhar no próprio vapor. Divida o arroz em dois pratos e salpique com as nozes. Sirva a seguir com iogurte natural."
        )

        return self.assertEqual(
            expected_instructions,
            self.harvester_class.instructions(),
        )
