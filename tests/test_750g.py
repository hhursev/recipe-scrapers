from recipe_scrapers.g750g import G750g
from tests import ScraperTest


class TestG750gScraper(ScraperTest):

    scraper_class = G750g

    def test_host(self):
        self.assertEqual("750g.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Salade de carottes cuites et crues à l'orange",
        )

    def test_yields(self):
        self.assertEqual("6 personnes", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://static.750g.com/images/600-600/72dcbbdc4c59e14ea2e93632904fc482/salade-de-carottes-cuites-et-crues-a-l-orange.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "500g de carottes",
                "3 jus d'orange",
                "1 c.c de coriandre en grain",
                "1 branche de thym",
                "30g d'huile d'olive",
                "2 oranges",
                "1 fenouil",
                "10 cl de vinaigrette citron",
                "500 g de carottes",
                "1/4 de botte de coriandre hachée",
                "Sel",
                "Piment d'Espelette",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            """Étape 1 : Cuisson des carottes\nDécoupez les carottes en rondelles et faites-les revenir à feu moyen à l'huile d'olive avec les graines de coriandre grossièrement concassées.
\nDéglacez au jus d'orange.
\nAjoutez la branche de thym ainsi que l'assaisonnement.
\nLaissez cuire avec un couvercle une dizaine de minutes puis laissez refroidir. Étape 2 : Préparation de la salade\nRâpez les carottes.
\nDans un saladier, mélangez les carottes râpées, les carottes cuites, le fenouil et les oranges en cubes.
\nAjoutez la vinaigrette et mélangez.
\nAjoutez la coriandre ciselée et le piment d'espelette.""",
            self.harvester_class.instructions(),
        )
