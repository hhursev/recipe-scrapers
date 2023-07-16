from recipe_scrapers.latelierderoxane import LAtelierDeRoxane
from tests import ScraperTest


class TestLAtelierDeRoxaneScraper(ScraperTest):

    scraper_class = LAtelierDeRoxane

    def test_host(self):
        self.assertEqual("latelierderoxane.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.latelierderoxane.com/blog/recette-cake-marbre/",
            self.harvester_class.canonical_url(),
        )

    def test_image(self):
        self.assertEqual(
            "https://www.latelierderoxane.com/blog/wp-content/uploads/cake-marbre..png",
            self.harvester_class.image(),
        )

    def test_title(self):
        self.assertEqual(
            "Recette cake marbré au chocolat facile", self.harvester_class.title()
        )

    def test_description(self):
        self.assertEqual(
            "Je pense que nous avons déjà tous acheté, au moins une fois, un cake Savane au supermarché ! Un délicieux marbré, moelleux à souhait au bon goût de vanille et cacao. Aujourd’hui, je te propose une recette facile et rapide pour réaliser ce fameux cake marbré maison ! Réalise cette recette et tu n’achèteras plus l’industriel 😉",
            self.harvester_class.description(),
        )

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_prep_time(self):
        self.assertEqual(15, self.harvester_class.prep_time())

    def test_cook_time(self):
        self.assertEqual(45, self.harvester_class.cook_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "3 œufs",
                "70 g de sucre",
                "70 g de beurre fondu",
                "1 sachet de levure chimique",
                "250 g de farine",
                "150 g de lait",
                "150 g de chocolat noir fondu",
                "1 càc d'arôme ou poudre de vanille",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Préchauffe le four à 165°.\nCommence par fouetter les œufs et le sucre, à l’aide de ton robot ou batteur électrique, pendant 5 minutes : ton mélange doit s’éclaircir et double de volume !\nAjoute le beurre fondu, la levure, la farine et fouette brièvement.\nVerse le lait et fouette jusqu’à l’obtention d’un mélange homogène.\nSépare la préparation obtenue dans deux bols différents.\nDans un des deux bols, ajoute l’arôme ou la poudre de vanille.\nFais fondre ton chocolat, au bain-marie ou au micro-onde, et incorpore-le à l’aide d’une maryse dans ton second bol.\nRécupère un moule à cake et beurre-le.\nVerse, dans le fond du moule, la moitié de la pâte à la vanille puis la moitié de celle au chocolat.\nRenouvèle la même opération une deuxième fois.\nEnfourne pendant 45 min.\nTu peux vérifier la cuisson à l’aide d’un couteau, plante-le au centre de ton cake : ta lame doit ressortir sèche.\nLaisse tiédir ton cake afin de faciliter son démoulage.",
            self.harvester_class.instructions(),
        )

    def test_site_name(self):
        self.assertEqual("L'Atelier de Roxane", self.harvester_class.site_name())
