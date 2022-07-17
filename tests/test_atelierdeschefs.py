from recipe_scrapers.atelierdeschefs import AtelierDesChefs
from tests import ScraperTest


class TestAtelierDesChefsScraper(ScraperTest):

    scraper_class = AtelierDesChefs

    def test_host(self):
        self.assertEqual("atelierdeschefs.fr", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("L'atelier des Chefs", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Cr\u00eape savoyarde")

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 Servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.atelierdeschefs.com/media/recette-e16689-crepe-savoyarde.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "Lait 1/2 \u00e9cr\u00e9m\u00e9 : 25 cl",
                "Beurre doux : 120 g",
                "Oeuf(s) : 1 pi\u00e8ce(s)",
                "Farine de bl\u00e9 : 70 g",
                "Farine de sarrasin (bl\u00e9 noir) : 55 g",
                "Sel fin : 8 pinc\u00e9e(s)",
                "Pomme(s) de terre \u00e0 chair ferme : 300 g",
                "Gros sel : 5 g",
                "Raclette au lait cru : 50 g",
                "Lardon(s) fum\u00e9(s) : 100 g",
                "Cr\u00e8me fra\u00eeche \u00e9paisse : 50 g",
                "Moulin \u00e0 poivre : 6 tour(s)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions_list(self):
        return self.assertEqual(
            [
                "Pour la pâte à crêpes",
                "Pour la pâte à crêpes : dans un bol, réunir les farines et le sel.",
                "Casser l’œuf et mélanger grossièrement, puis ajouter progressivement le lait tout en fouettant énergiquement.",
                "Faire fondre le beurre, puis l'ajouter à l'appareil.",
                "Laisser ensuite reposer au frais pendant 1 h.",
                "Réaliser les crêpes sur une crêpière chaude jusqu'à épuisement de la pâte.",
                "Pour la garniture",
                "Préchauffer le four à 180 °C (th.",
                "6).",
                "Éplucher les pommes de terre et les couper en rondelles.",
                "Les disposer ensuite dans une casserole avec le gros sel, puis les couvrir d'eau.",
                "Porter à ébullition, puis cuire les pommes de terre pendant 5 min avant de les égoutter.",
                "Dorer les lardons dans une poêle chaude, puis les égoutter sur une feuille de papier absorbant.",
                "Couper le fromage en fines tranches.",
                "Dans une poêle chaude, faire fondre 10 g de beurre puis réchauffer doucement une crêpe.",
                "Disposer ensuite les rondelles de pommes de terre, puis les lardons.",
                "Ajouter la crème et une tranche de fromage, saler et poivrer.",
                "Enfourner à 180 °C (th.",
                "6) jusqu'à ce que le fromage ait fondu.",
                "Renouveler l'opération pour les 5 autres crêpes.",
                "Servir aussitôt.",
            ],
            self.harvester_class.instructions_list(),
        )

    def test_ratings(self):
        self.assertEqual(3.7, self.harvester_class.ratings())
