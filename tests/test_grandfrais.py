# mypy: allow-untyped-defs

from recipe_scrapers.grandfrais import GrandFrais
from tests import ScraperTest


class TestGrandFraisScraper(ScraperTest):
    scraper_class = GrandFrais

    def test_host(self):
        self.assertEqual("grandfrais.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            "Gratinée à l'emmental et aux poireaux", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual(None, self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(85, self.harvester_class.total_time())

    def test_cook_time(self):
        self.assertEqual(70, self.harvester_class.cook_time())

    def test_prep_time(self):
        self.assertEqual(15, self.harvester_class.prep_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.grandfrais.com/images/institBackoffice/recette/desktop/63d92727777fd_300x300-gratin.webp",
            self.harvester_class.image(),
        )

    def test_nutrients(self):
        self.assertEqual(None, self.harvester_class.nutrients())

    def test_ingredients(self):
        self.assertEqual(
            [
                "300 g d'emmental",
                "0.5 L de bouillon de boeuf",
                "80 g de beurre",
                "20 cl de vin blanc sec",
                "1 kg d'oignons",
                "20 cl de vin blanc sec",
                "500 g de poireaux",
                "50 g de farine",
                "1 baguette",
                "Sel et poivre",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Épluchez les oignons et les poireaux et émincez-les.\n"
            "Faites revenir à feu doux les oignons dans le beurre et laissez- les colorer, ajoutez la farine et déglacez avec le vin blanc.\n"
            "Ajoutez les poireaux, arrosez de bouillon et laissez cuire 1h à feu doux.\n"
            "Coupez le pain et préparez des croûtons que vous ferez griller au four.\n"
            "Versez la soupe dans des bols allant au four sur laquelle vous rajouterez les croûtons.\n"
            "Râpez l'emmental et disposez-le dans les bols.\n"
            "Faites gratiner 6 min sous le grill jusqu'à ce que le râpé soit bien fondu.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())

    def test_author(self):
        self.assertEqual("Grand Frais", self.harvester_class.author())

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(None, self.harvester_class.description())
