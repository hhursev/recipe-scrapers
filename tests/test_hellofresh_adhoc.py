from recipe_scrapers.hellofresh import HelloFresh
from tests import ScraperTest


class TestHelloFreshScraperAdHoc(ScraperTest):

    scraper_class = HelloFresh
    test_file_name = "hellofresh_adhoc"

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.hellofresh.fr/recipes/chakchouka-au-fromage-de-chevre-5eb41aa7d5418a482a67b864",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            "Chakchouka au chèvre frais avec du piment, des œufs et du persil",
            self.harvester_class.title(),
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "HelloFresh")

    def test_total_time(self):
        self.assertEqual(65, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 pièce(s) Oignon",
                "2 pièce(s) Gousse d'ail",
                "½ pièce(s) Piment",
                "1 pièce(s) Poivron rouge",
                "4 pièce(s) Tomate",
                "5 g Persil",
                "4 pièce(s) Œuf",
                "75 g Fromage de chèvre frais",
                "2 pièce(s) Baguette",
                "1 cs Huile d'olive",
                "½ pièce(s) Cube de bouillon de légumes",
                "selon le goût Poivre et sel",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Préchauffez le four à 210 degrés. Hachez l'oignon et écrasez ou émincez l'ail. Épépinez le piment rouge et le poivron rouge et coupez-les en lanières. Coupez les tomates prunes en petits dés et ciselez finement le persil frisé.CONSEIL: LE SAVIEZ-VOUS ? Ce plat contient plus de 250 g de légumes, et plus de l'apport journalier recommandé en vitamine C grâce à la tomate et au poivron.\nFaites chauffer l’huile d’olive dans un wok ou une sauteuse avec couvercle et faites-y revenir l’oignon, l’ail et le piment rouge 2 minutes à feu moyen-vif. Puis, ajoutez le poivron, la tomate et la moitié du persil.\nAjoutez ensuite 30 ml d’eau par personne dans le wok ou la sauteuse, puis émiettez le cube de bouillon par-dessus. Portez à ébullition tout en remuant, puis laissez mijoter 5 minutes à couvert sur feu moyen-vif. Salez et poivrez.\nPour chaque œuf, faites un petit cratère dans le mélange de légumes, puis cassez-y les œufs. Saupoudrez-les de sel et de poivre. Disposez le chèvre frais émietté sur l’ensemble, couvrez et laissez les œufs cuire pendant 10 minutes (voir CONSEIL). Lors des 4 dernières minutes, retirez le couvercle, augmentez un peu le feu et laissez l’excédent d’eau s’évaporer.CONSEIL: CONSEIL : La cuisson de l’œuf dépend de la hauteur de votre poêle. Elle durera plus longtemps avec une poêle profonde à bord haut, contrairement à une poêle à bord bas ou un wok.\nPendant ce temps, enfournez les demi-baguettes 6 à 8 minutes ou jusqu’à ce qu’elles soient dorées.\nServez le chakchouka dans les assiettes. Garnissez du reste de persil et présentez les demi-baguettes en accompagnement.""",
            self.harvester_class.instructions(),
        )

    def test_nutrients(self):
        self.assertEqual(
            {
                "calories": "600 kcal",
                "fatContent": "8.98 g",
                "saturatedFatContent": "1.25 g",
                "carbohydrateContent": "107.89 g",
                "sugarContent": "13.27 g",
                "proteinContent": "16.52 g",
                "sodiumContent": "3.12 g",
                "servingSize": "484",
            },
            self.harvester_class.nutrients(),
        )

    def test_cuisine(self):
        self.assertEqual("Middle Eastern", self.harvester_class.cuisine())

    def test_category(self):
        self.assertEqual("Plat principal", self.harvester_class.category())
