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
            "Chakchouka au fromage de chèvre avec du piment, des œufs et du persil",
            self.harvester_class.title(),
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "HelloFresh")

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 * ¼ pièce Cube de bouillon de légumes",
                "2 * ½ pièce Oignon jaune",
                "2 * 1 pièce Gousse d'ail",
                "2 * ¼ pièce Piment rouge",
                "2 * ½ pièce Poivron rouge",
                "2 * 2 pièce Tomate allongée",
                "2 * 2 pièce Œuf de poule élevée en plein air",
                "2 * 50 g Fromage de chèvre frais",
                "2 * 2.5 g Persil plat",
                "2 * 1 pièce Demi-baguette",
                "2 * 1 cs Huile d'olive",
                "2 * selon le goût Poivre et sel",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Préchauffez le four à 210 degrés. Hachez l'oignon et écrasez ou émincez l'ail. Épépinez le piment rouge et le poivron rouge et coupez-les en lanières. Coupez les tomates prunes en petits dés et ciselez finement le persil frisé.\nFaites chauffer l’huile d’olive dans un wok ou une sauteuse avec couvercle et faites-y revenir l’oignon, l’ail et le piment rouge 2 minutes à feu moyen-vif. Puis, ajoutez le poivron, la tomate et la moitié du persil.\nAjoutez ensuite 30 ml d’eau par personne dans le wok ou la sauteuse, puis émiettez le cube de bouillon par-dessus. Portez à ébullition tout en remuant, puis laissez mijoter 5 minutes à couvert sur feu moyen-vif. Salez et poivrez.\nPour chaque œuf, faites un petit cratère dans le mélange de légumes, puis cassez-y les œufs. Saupoudrez-les de sel et de poivre. Disposez le chèvre frais émietté sur l’ensemble, couvrez et laissez les œufs cuire pendant 10 minutes. Lors des 4 dernières minutes, retirez le couvercle, augmentez un peu le feu et laissez l’excédent d’eau s’évaporer.\nPendant ce temps, enfournez les demi-baguettes 6 à 8 minutes ou jusqu’à ce qu’elles soient dorées.\nServez le chakchouka dans les assiettes. Garnissez du reste de persil et présentez les demi-baguettes en accompagnement.""",
            self.harvester_class.instructions(),
        )

    def test_nutrients(self):
        self.assertEqual(
            {
                "calories": "857 kcal",
                "fatContent": "28 g",
                "saturatedFatContent": "10 g",
                "carbohydrateContent": "109 g",
                "sugarContent": "15 g",
                "proteinContent": "35 g",
                "sodiumContent": "4 g",
                "servingSize": "654",
            },
            self.harvester_class.nutrients(),
        )

    def test_cuisine(self):
        self.assertEqual("Middle Eastern", self.harvester_class.cuisine())

    def test_category(self):
        self.assertEqual("main course", self.harvester_class.category())
