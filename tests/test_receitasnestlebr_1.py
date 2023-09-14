# mypy: allow-untyped-defs

from recipe_scrapers.receitasnestlebr import ReceitasNestleBR
from tests import ScraperTest


class TestReceitasNestleBRScraper(ScraperTest):

    scraper_class = ReceitasNestleBR
    test_file_name = "receitasnestlebr_1"

    def test_host(self):
        self.assertEqual("receitasnestle.com.br", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Monalisa Campos", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Receita de Costelinha de Porco com Batatas Salteadas no Alecrim",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual("Meal set", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("5 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.receitasnestle.com.br/sites/default/files/srh_recipes/ef9051b4a2b476e658b5f8b6ef18bd24.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "500g de costelinha de porco",
                "3 batatas grandes",
                "2 dentes de alho",
                "meia colher (sopa) de chimichurri seco",
                "1 ramo de alecrim",
                "1 colher (chá) de sal",
                "2 xícaras (chá) de água",
                "meia colher (sopa) de azeite",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        expected_instructions = [
            "Leve uma panela para esquentar e acrescente o azeite. Em seguida, acrescente a costelinha de porco e deixe fritar, sem mexer.",
            "Quando estiver dourada, vire e acrescente o sal e o chimichurri. Deixe fritar.",
            "Quando começar a ficar seco, adicione meia xícara (chá) de água e deixe cozinhar em fogo alto até secar.",
            "Quando a carne estiver douradinha, adicione o alho e as batatas já descascadas cortadas em cubos grandes.",
            "Adicione o restante da água e deixe cozinhar em fogo baixo.",
            "Depois, acrescente o alecrim e refogue mais um pouco.",
            "Sirva quente.",
        ]
        expected_instructions = "\n".join(expected_instructions)
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(0, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "Receita de Costelinha de Porco com Batatas Salteadas no Alecrim suculenta feita com costelinha de porco, batata, chimichurri, alho e alecrim",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("pt-br", self.harvester_class.language())
