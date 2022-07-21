from recipe_scrapers.panelinha import Panelinha
from tests import ScraperTest


class TestPanelinhaScraper(ScraperTest):

    scraper_class = Panelinha

    @property
    def test_file_name(self):
        return "{}_1".format(self.scraper_class.__name__.lower())

    def test_host(self):
        self.assertEqual("panelinha.com.br", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Rosbife")

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("Até 4 porções", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 peça de filé mignon para rosbife (cerca de 750 g)",
                "1 colher (chá) de mostarda amarela em pó",
                "1 colher (chá) de páprica defumada",
                "azeite a gosto",
                "sal e pimenta-do-reino moída na hora a gosto",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preaqueça o forno a 220 ºC (temperatura alta). Retire a peça de filé mignon da geladeira e deixe em temperatura ambiente por 15 minutos, enquanto o forno aquece.\nNuma tigela pequena, misture a páprica com a mostarda em pó. Disponha a peça de filé mignon na tábua e tempere com sal, pimenta e a mistura de mostarda com páprica. Regue com ½ colher (sopa) de azeite e espalhe bem com as mãos por toda a superfície da carne.\nTransfira o filé mignon para uma assadeira grande e leve ao forno para assar por 15 minutos. Após esse tempo, diminua a temperatura para 180 ºC (temperatura média) e deixe o rosbife no forno por mais 10 minutos para assar a carne com o interior bem vermelhinho (mal passada). Se quiser ao ponto, deixe assar por mais 5 minutos.\nRetire a assadeira do forno e deixe o rosbife descansar por 10 minutos antes de cortar e servir – nesse período os sucos se redistribuem, deixando a carne mais suculenta.",
            self.harvester_class.instructions(),
        )
