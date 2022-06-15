from recipe_scrapers.monsieurcuisine import MonsieurCuisine
from tests import ScraperTest


class TestMonsieurCuisineScraper(ScraperTest):

    scraper_class = MonsieurCuisine

    def test_host(self):
        self.assertEqual("monsieur-cuisine.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("© Monsieur Cuisine", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Guacamole", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(5, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.monsieur-cuisine.com/fileadmin/_processed_/e/8/csm_23055_Rezeptfoto_01_2fae43be2a.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "4 brins de coriandre",
                "100 g de tomates",
                "1 petit oignon",
                "2 avocats bien mûrs",
                "Jus de ½ citron vert",
                "1 c.c. de harissa (pâte de piment rouge)",
                "1 pincée de sel",
                "1 pincée de poivre",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Rincer et sécher la coriandre. Dans le bol mixeur, hacher finement les tiges entières avec la touche Turbo/7 secondes. Rincer les tomates, les couper en deux en ôtant le pédoncule et les épépiner. Les ajouter dans le bol mixeur et les hacher grossièrement 8 secondes/vitesse 5. Réserver dans un saladier.\nPeler l’oignon, le couper en deux, puis le hacher finement touche Turbo/7 secondes. Peler l’avocat et détacher la chair du noyau. L’ajouter avec le jus de citron vert, la harissa, le sel et le poivre. Puis mixer 8 secondes/vitesse 6. Ajouter enfin les tomates et mixer le tout avec le programme Sens inverse/10 secondes/vitesse 2.\nDresser le guacamole dans un saladier et servir.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.0, self.harvester_class.ratings())
