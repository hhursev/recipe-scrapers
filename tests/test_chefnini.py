# mypy: allow-untyped-defs

from recipe_scrapers.chefnini import Chefnini
from tests import ScraperTest


class TestChefniniScraper(ScraperTest):
    scraper_class = Chefnini

    def test_host(self):
        self.assertEqual("chefnini.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.chefnini.com/tagliatelles-carbonara/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("chefNini", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Tagliatelles carbonara", self.harvester_class.title())

    def test_category(self):
        self.assertEqual(None, self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(None, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://static.chefnini.com/wp-content/uploads/2013/09/tagliatelle-carbonara10.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "250 g de tagliatelles",
                "100 g de lardons fumés ou de pancetta",
                "1 oeuf",
                "1 jaune d’oeuf",
                "4 cs de parmesan fraîchement râpé",
                "1 gousse d’ail",
                "1 peu de noix de muscade (facultatif)",
                "poivre du moulin",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "1- Versez l’œuf et le jaune dans un bol et battez-les à la fourchette.\n2- Ajoutez le parmesan et mélangez.\n3- Épluchez la gousse d’ail, dégermez-la et hachez-la.\n4- Portez une grande casserole d’eau salée à ébullition et mettez à cuire les pâtes en comptant 2 minutes de moins que le temps du paquet. Une fois cuites, égouttez-les mais gardez 2 louches d’eau de cuisson.\n5- Pendant ce temps, faites dorer les lardons dans une poêle, sans matière grasse.\n6- Ajoutez la gousse d’ail et laissez cuire en mélangeant régulièrement.\n7- Lorsque les pâtes sont cuites, versez-les dans les lardons et mélangez.\n8- Versez la préparation œuf / parmesan et une petite louche d’eau de cuisson. Mettez sur feu moyen et mélangez délicatement.\n9- Stoppez la cuisson lorsque la sauce est encore sirupeuse – trop tard, les pâtes seront sèches. Dosez l’eau de cuisson pour obtenir la consistance de sauce désirée.\n10- Servez aussitôt, poivrez et ajoutez un peu de noix de muscade râpée.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "En France, les pâtes carbonara sont très souvent cuisinées avec des oignons et de la crème liquide. C’est d’ailleurs de cette manière que je les ai découvertes. J’aimais bien mais j’ai toujours trouvé ça un peu écœurant et lourd.",
            self.harvester_class.description(),
        )
