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
            "https://www.latelierderoxane.com/blog/wp-content/uploads/img_7067-scaled.jpg",
            self.harvester_class.image(),
        )

    def test_title(self):
        self.assertEqual("Recette cake savane maison", self.harvester_class.title())

    def test_description(self):
        expected_description = "Je pense que nous avons déjà tous acheté, au moins une fois, un cake type Savane au supermarché ! Aujourd’hui, je te propose une recette facile et rapide pour réaliser un délicieux marbré au chocolat, moelleux à souhait au bon goût de vanille et cacao ! Réalise cette recette et tu n’achèteras plus l’industriel ! Découvre ma box de pâtisserie goûters faits maison"
        self.assertEqual(expected_description, self.harvester_class.description())

    def test_total_time(self):
        self.assertEqual(65.0, self.harvester_class.total_time())

    def test_prep_time(self):
        self.assertEqual(20, self.harvester_class.prep_time())

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
        expected_instructions = "\n".join(
            [
                "Préchauffe le four à 165°.",
                "Commence par fouetter les œufs et le sucre, à l’aide de ton robot ou batteur électrique, pendant 10 minutes : ton mélange doit s’éclaircir et doubler de volume !",
                "Ajoute le beurre fondu, la levure, la farine et fouette brièvement.",
                "Verse le lait et fouette jusqu’à l’obtention d’un mélange homogène.",
                "Sépare la préparation obtenue dans deux bols.",
                "Dans un des deux bols, ajoute l’arôme ou la poudre de vanille.",
                "Fais fondre ton chocolat, au bain-marie ou au micro-ondes et incorpore-le dans le second bol à l’aide d’une maryse.",
                "Récupère ton moule à cake et beurre-le généreusement.",
                "Verse, dans le fond de ton moule, la moitié de la pâte à la vanille puis la moitié de celle au chocolat.",
                "Répète l’opération une deuxième fois.",
                "Enfourne pendant 45 min.",
                "Tu peux vérifier la cuisson à l’aide d’un couteau, plante-le au centre de ton cake : ta lame doit ressortir sèche.",
                "À la sortie du four, laisse tiédir ton cake afin de faciliter son démoulage.",
                "À manger sans modération !",
            ]
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_site_name(self):
        self.assertEqual("L'Atelier de Roxane", self.harvester_class.site_name())
