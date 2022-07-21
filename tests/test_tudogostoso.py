from recipe_scrapers.tudogostoso import TudoGostoso
from tests import ScraperTest


class TestTudoGostosoScraper(ScraperTest):

    scraper_class = TudoGostoso

    def test_host(self):
        self.assertEqual("tudogostoso.com.br", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.tudogostoso.com.br/receita/128825-caipirinha-original.html",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Caipirinha - Original")

    def test_total_time(self):
        self.assertEqual(5, self.harvester_class.total_time())

    def test_ingredients(self):
        self.assertListEqual(
            ["1 limão grande", "2 colheres de açúcar", "gelo a gosto", "cachaça"],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Pegue o limão coloque-o na horizontal e retire as duas pontas, vire-o na vertical e corte-o ao meio, retire os meio (parte branca) do limão e fatie.Coloque o limão fatiado e duas colheres bem cheias de açúcar dentro de um copo próprio para a bebida e com um socador esprema até que saia todo o suco do limão.Coloque pedras de gelo até quase encher o copo (aproximadamente 12 pedras pequenas de gelo) e encha o copo com a cachaça.Mexa bem com uma colher ou coloque em uma coqueteleira e sirva-se! Informações Adicionais Confira no TudoGostoso mais drinks deliciosos como batida de maracujá, mojito, licor caseiro, batida de morango e outras bebidas! Você sabia que existe mais de um tipo de caipirinha? É verdade! E aqui no TudoGostoso a gente te mostra e te ensina como preparar algumas delas. Confira e não deixe de fazer. Sabe qual a origem da caipirinha? Não? O TudoGostoso te mostra! Confira como essa e outros tipos de bebidas foram criados em uma matéria maravilhosa do blog. Veja também: Caipirinha perfeita: 4 dicas para arrasar nas festas Como fazer caipirinha de algodão-doce: confira esse e mais 2 drinques incríveis",
            self.harvester_class.instructions(),
        )
