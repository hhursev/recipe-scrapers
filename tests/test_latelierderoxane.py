from recipe_scrapers.latelierderoxane import LAtelierDeRoxane
from tests import ScraperTest

# test recipe's URL
# https://www.latelierderoxane.com/blog/recette-cake-marbre/


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
            "https://www.latelierderoxane.com/blog/wp-content/uploads/cake-marbre.-787x590.png",
            self.harvester_class.image(),
        )

    def test_title(self):
        self.assertEqual("Recette cake marbré", self.harvester_class.title())

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
                "70 g de beurre  fondu",
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
            "\n".join(
                [
                    "Préchauffe le four à 165°.",
                    "Dans le bol de ton robot, verse les œufs, le sucre et fouette pendant 5 minutes. Ton mélange doit s’éclaircir et doubler de volume. Tu peux également utiliser un batteur électrique.",
                    "Ajoute le beurre fondu, la levure, la farine et fouette le tout.",
                    "Verse le lait et fouette à nouveau jusqu’à l’obtention d’un mélange homogène.",
                    "Sépare la préparation dans deux bols différents de manière égale.",
                    "Ajoute l’arôme ou la poudre de vanille dans le premier bol et mélange le tout.",
                    "Verse le chocolat fondu dans le second bol et mélange à la maryse pour bien l’incorporer.",
                    "Beurre ton moule à cake.",
                    "Verse, dans le fond du moule, la moitié de la pâte à la vanille puis la moitié de la pâte au chocolat.",
                    "Renouvèle la même opération une deuxième fois.",
                    "Enfourne pendant 45 min. Vérifie la cuisson à l’aide d’un couteau, la lame doit ressortir sèche.",
                    "Laisse tiédir ton cake et démoule-le.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_site_name(self):
        self.assertEqual("L'Atelier de Roxane", self.harvester_class.site_name())
