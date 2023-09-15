from recipe_scrapers.tudogostoso import TudoGostoso
from tests import ScraperTest


class TestTudoGostosoScraper(ScraperTest):

    scraper_class = TudoGostoso

    def test_host(self):
        self.assertEqual("tudogostoso.com.br", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Caipirinha - Original")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Daniela Belizario")

    def test_total_time(self):
        self.assertEqual(5, self.harvester_class.total_time())

    def test_ingredients(self):
        self.assertListEqual(
            ["1 limão grande", "2 colheres de açúcar", "gelo a gosto", "cachaça"],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Pegue o limão coloque-o na horizontal e retire as duas pontas, vire-o na vertical e corte-o ao meio, retire os meio (parte branca) do limão e fatie.",
                    "Coloque o limão fatiado e duas colheres bem cheias de açúcar dentro de um copo próprio para a bebida e com um socador esprema até que saia todo o suco do limão.",
                    "Coloque pedras de gelo até quase encher o copo (aproximadamente 12 pedras pequenas de gelo) e encha o copo com a cachaça.",
                    "Mexa bem com uma colher ou coloque em uma coqueteleira e sirva-se!",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_language(self):
        self.assertEqual("pt-br", self.harvester_class.language())
