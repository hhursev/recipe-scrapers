from recipe_scrapers.bettybossi import BettyBossi
from tests import ScraperTest


class TestBettyBossiScraper(ScraperTest):

    scraper_class = BettyBossi

    def test_host(self):
        self.assertEqual("bettybossi.ch", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Betty Bossi", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Minicheesecakes", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(90, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.bettybossi.ch/rdbimg/bb_blub160501_0070a/bb_blub160501_0070a_r01_v005_x0010.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "120 g de biscuits au beurre (p. ex. petits-beurre)",
                "40 g de beurre, fondu, refroidi",
                "250 g de fromage frais double crème (p. ex. Philadelphia)",
                "250 g de mascarpone",
                "150 g de séré demi-gras",
                "3 œufs, battus",
                "120 g de sucre",
                "1 sachet de sucre vanillé",
                "1 citron bio, zeste râpé et 1 c.s. de jus",
                "2 c.s. de liqueur au cassis ou de sirop de cassis",
                "2 c.s. de farine",
                "250 g de myrtilles surgelées, dégelées",
                "2 c.s. de sucre",
                "1 c.s. de jus de citron",
                "2 c.s. de liqueur au cassis ou de sirop de cassis",
                "1 citron bio, zeste râpé",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Écraser les biscuits dans un sachet en plastique à l’aide d’un rouleau à pâtisserie, mélanger avec le beurre. Répartir sur le fond du moule préparé, bien tasser avec le dos d’une cuillère ou le fond d’un verre, réserver au frais.\nBien mélanger au fouet le fromage frais, le mascarpone et le séré. Incorporer les œufs et tous les ingrédients, farine comprise.\nBien égoutter les myrtilles et mixer les myrtilles avec le reste des ingrédients, étaler sur le fond de petits-beurre, répartir dessus l’appareil au fromage frais.\nCuisson: env. 50 min dans la moitié inférieure du four préchauffé à 180° C. Laisser tiédir ensuite env. 1 h dans le four éteint, en maintenant la porte entrouverte avec le manche d’une spatule en bois. Retirer, laisser refroidir sur une grille. Ôter le bord du moule.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual(
            "Dessert, Patisserie salée et sucrée", self.harvester_class.cuisine()
        )

    def test_description(self):
        self.assertEqual(
            "Ces larges biscuits cachent une crème composée de myrtilles avec un mélange de fromage frais, de séré et de mascarpone et n’attendent que vous pour les couper!",
            self.harvester_class.description(),
        )
