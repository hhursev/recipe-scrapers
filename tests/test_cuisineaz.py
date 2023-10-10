from recipe_scrapers.cuisineaz import CuisineAZ
from tests import ScraperTest


class CuisineAZScraper(ScraperTest):

    scraper_class = CuisineAZ

    def test_host(self):
        self.assertEqual("cuisineaz.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.cuisineaz.com/recettes/filet-de-saumon-au-four-63049.aspx",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Filet de saumon au four")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Cuisine AZ")

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://img.cuisineaz.com/660x660/2014/02/24/i78436-filet-de-saumon-au-four.jpeg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "600 g Filet de saumon",
                "30 ml Huile d'olive",
                "4 g Origan séché",
                "1 pincée(s) Sel",
                "1 pincée(s) Poivre",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Etape 1\nPréchauffez le four th.7 (210°C). Coupez le filet en pavés de saumon de même taille, correspondant au nombre de parts désirées, et déposez-les sur une plaque huilée ou dans un plat à four. Arrosez-les d'huile d'olive. Salez et poivrez à votre convenance et parsemez d'origan.\nEtape 2\nDisposez le plat ou la plaque au centre du four. Comptez environ 10 min pour un filet de 2 à 2,5 cm d'épaisseur. Le temps nécessaire à la bonne cuisson du saumon dépend non seulement de l'épaisseur des pavés mais aussi de la température réelle de votre four, c'est pourquoi il est important de vérifier régulièrement la cuisson du saumon à l'aide d'une fourchette.\nEtape 3\nLorsque vos pavés de saumon sont cuits, servez-les immédiatement, accompagnés d'une bonne salade bien assaisonnée, et éventuellement d'une belle timbale de riz basmati.",
            self.harvester_class.instructions(),
        )
