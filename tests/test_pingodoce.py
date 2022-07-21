from recipe_scrapers.pingodoce import PingoDoce
from tests import ScraperTest


class TestPingoDoceScraper(ScraperTest):

    scraper_class = PingoDoce

    def test_host(self):
        self.assertEqual("pingodoce.pt", self.harvester_class.host())

    def test_title(self):
        self.assertEqual("Arroz de tamboril", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 q.b. hortelã",
                "1 kg tamboril",
                "100 ml azeite",
                "2 unid. cebola grande",
                "5 dente alho",
                "1 q.b. coentros",
                "1 unid. pimento",
                "4 unid. tomate maduro",
                "1 unid. malagueta pequena",
                "3 c. de sopa polpa de tomate",
                "300 g arroz carolino",
                "2 c. de chá sal",
                "1 q.b. pimenta branca",
                "400 g miolo de camarão",
                "40 g manteiga",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Coza o tamboril já cortado em cubos. Reserve a água de cozedura.\nNum tacho largo refogue em azeite as cebolas, os alhos e os coentros picados.\nQuando a cebola estiver translúcida, junte ao refogado o pimento em tiras, o tomate em cubos e a malagueta picada, envolvendo bem os ingredientes.\nDilua a polpa de tomate na água de cozedura do tamboril e vá acrescentando, aos poucos, ao refogado.\nDepois de lavado, junte o arroz e tempere de sal e pimenta.\nA meio da cozedura do arroz, adicione o tamboril, previamente cozido, e o miolo de camarão.\nPor fim, envolva a manteiga, polvilhe com a hortelã picada.\nSirva o seu arroz de tamboril com fatias de pão torrado.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(2.0, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "Malandrinho, como se quer, saboroso e fresco, graças aos coentros e à hortelã, este arroz de tamboril vai deliciá-lo. Siga a receita e impressione lá em casa.",
            self.harvester_class.description(),
        )
