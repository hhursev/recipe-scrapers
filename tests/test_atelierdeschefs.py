from tests import ScraperTest

from recipe_scrapers.atelierdeschefs import AtelierDesChefs


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

    def test_instructions(self):
        return self.assertEqual(
            "1. POUR LA P\u00c2TE \u00c0 CR\u00caPES\nPour la p\u00e2te \u00e0 cr\u00eapes : dans un bol, r\u00e9unir les farines et le sel. Casser l'oeuf et m\u00e9langer grossi\u00e8rement, puis ajouter progressivement le lait tout en fouettant \u00e9nergiquement.\nFaire fondre le beurre, puis l'ajouter \u00e0 l'appareil. Laisser ensuite reposer au frais pendant 1 h.\nR\u00e9aliser les cr\u00eapes sur une cr\u00eapi\u00e8re chaude jusqu'\u00e0 \u00e9puisement de la p\u00e2te.\n2. POUR LA GARNITURE\nPr\u00e9chauffer le four \u00e0 180 °C (th. 6).\n\u00c9plucher les pommes de terre et les couper en rondelles. Les disposer ensuite dans une casserole avec le gros sel, puis les couvrir d'eau. Porter \u00e0 \u00e9bullition, puis cuire les pommes de terre pendant 5 min avant de les \u00e9goutter.\nDorer les lardons dans une po\u00eale chaude, puis les \u00e9goutter sur une feuille de papier absorbant.\nCouper le fromage en fines tranches.\nDans une po\u00eale chaude, faire fondre 10 g de beurre puis r\u00e9chauffer doucement une cr\u00eape. Disposer ensuite les rondelles de pommes de terre, puis les lardons. Ajouter la cr\u00e8me et une tranche de fromage, saler et poivrer. Enfourner \u00e0 180 °C (th. 6) jusqu'\u00e0 ce que le fromage ait fondu.\nRenouveler l'op\u00e9ration pour les 5 autres cr\u00eapes.\nServir aussit\u00f4t.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(3.7, self.harvester_class.ratings())
