import responses

from recipe_scrapers.quitoque import QuiToque
from tests.legacy import ScraperTest


class TestQuiToqueScraper(ScraperTest):
    scraper_class = QuiToque

    @classmethod
    def expected_requests(cls):
        yield responses.GET, "https://www.quitoque.fr/recette/12519/hot-dog-sauce-quitoque", "tests/legacy/test_data/quitoque.testhtml"
        yield responses.GET, "https://mgs.quitoque.fr/graphql?operationName=getRecipe&variables={%22id%22:%2212519%22}&extensions={%22persistedQuery%22:{%22version%22:1,%22sha256Hash%22:%2204af4d1a48fd536a67292733e23a2afcf6d0da9770ab07055c59b754eec9bd6d%22}}", "tests/legacy/test_data/quitoque.testjson"

    def test_host(self):
        self.assertEqual("quitoque.fr", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            "Hot-dog de saucisse au piment chipotle et sauce fra\u00eeche au persil",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual(
            "Porc, Pimenté, Viande, Express, Découverte, Familial, Gourmand, Express, Américain, Printemps, Été, Automne, Hiver, Recettes à base de pains : tartines, croques monsieurs, bruschetta, Pimenté, Américain / anglo-saxons, Je mange de tout",
            self.harvester_class.category(),
        )

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 portions", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://s3.eu-central-1.amazonaws.com/media.quitoque.fr/recipe_w1536_h1024/recipes/images/hot-dog-sauce-quitoque/hot-dog-sauce-quitoque-43.jpg",
            self.harvester_class.image(),
        )

    def test_description(self):
        self.assertEqual(
            "En 20 min, dégustez le roi de la street food revisité avec nos délicieuses saucisses, une sauce fraîche au persil et des oignons frits !",
            self.harvester_class.description(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "100 g Fromage blanc",
                "0.5 Gousse d'ail",
                "1 Oignon jaune",
                "0.5 Oignons frits (sachet)",
                "2 Pains \u00e0 hot dog - Maison Salesse (2x90g)",
                "qq brins Persil plat",
                "1 Piment Chipotle (pinc\u00e9e)",
                "50 g Pousses d'\u00e9pinards",
                "2 Saucisses natures - Vall\u00e9grain (2x120g)",
                "Sel",
                "Poivre",
                "Huile d'olive",
                "2 cc Sucre",
                "Vinaigre de votre choix",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Préchauffez votre four à 200°C en chaleur tournante !\nPendant ce temps, dans une sauteuse, faites chauffer un filet d'huile d'olive à feu moyen à vif.\nFaites cuire les saucisses 7 min environ. Retournez-les régulièrement.\nAu bout des 7 min de cuisson, ajoutez un fond d'eau et le piment Chipotle. Poursuivez la cuisson 7 min. Salez, poivrez.\nPendant ce temps, préparez l'oignon confit.Émincez l'oignon.\nDans une petite casserole, faites chauffer un filet d'huile d'olive à feu moyen à vif.\nFaites revenir l'oignon et le sucre 12 min environ jusqu'à ce que l'oignon soit confit. Remuez régulièrement. \nEn parallèle, préparez la sauce.Dans un bol, déposez les ingrédients suivants : \nPressez ou hachez l'ail.\nEffeuillez et ciselez le persil.\nAjoutez le fromage blanc. Salez, poivrez et mélangez bien.\nGoûtez et rectifiez l'assaisonnement si nécessaire.Ouvrez les pains à hot-dog en deux et passez-les au four 5 min pour les dorer. \nDéposez une saucisse et un peu d'oignon confit dans chaque pain à hot-dog. Nappez le tout de sauce fraîche au persil. \nParsemez-les d'oignons frits.\nAssaisonnez les pousses d'épinards d'un filet d'huile d'olive et de vinaigre.Dégustez sans attendre votre hot-dog de saucisse au piment Chipotle et sauce fraîche au persil accompagné de la salade !",
            self.harvester_class.instructions(),
        )

    def test_nutrients(self):
        self.assertEqual(
            {
                "calories": "601.84 calories",
                "fatContent": "29.81 grammes",
                "saturatedFatContent": "13.41 grammes",
                "carbohydrateContent": "49.64 grammes",
                "sugarContent": "6.31 grammes",
                "fiberContent": "4.26 grammes",
                "proteinContent": "31.31 grammes",
                "sodiumContent": "3.22 grammes",
            },
            self.harvester_class.nutrients(),
        )

    def test_equipment(self):
        self.assertEqual(
            ["petite casserole", "sauteuse", "four"], self.harvester_class.equipment()
        )
