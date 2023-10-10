import unittest

from recipe_scrapers.albertheijn import AlbertHeijn
from tests import ScraperTest


class TestAlbertHeijnScraper(ScraperTest):

    scraper_class = AlbertHeijn

    def test_host(self):
        self.assertEqual("ah.nl", self.harvester_class.host())

    @unittest.skip("canonical_url will not pass with testhtml (uses example.com)")
    def test_canonical_url(self):
        self.assertEqual(
            "https://www.ah.nl/allerhande/recept/R-R1198767/rijkgevulde-vegan-pastasalade",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Albert Heijn", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Rijkgevulde vegan pastasalade", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("hoofdgerecht", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "300 g fusilli",
                "1 teen knoflook",
                "2 aubergines",
                "2 el milde olijfolie",
                "1 el gedroogde oregano",
                "240 g biologische kalamata-olijven",
                "295 g semi-zongedroogde tomaten",
                "1 rode ui",
                "15 g verse basilicum",
                "1 el rodewijnazijn",
                "50 g gerookte amandelen",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Kook de pasta volgens de aanwijzingen op de verpakking. Spoel onder koud stromend water en laat uitlekken.",
                    "Snijd ondertussen de knoflook fijn en de aubergines in blokken van 2 cm. Verhit de olie in een koekenpan en roerbak de aubergine 10 min. op hoog vuur. Schep regelmatig om. Zet het vuur laag en meng de laatste minuut de helft van de oregano en de helft van de knoflook door de aubergine. Breng op smaak met peper.",
                    "Laat ondertussen de olijven en gedroogde tomaten uitlekken. Vang 2 el olie van de gedroogde tomaten (per 4 personen) op en snijd de tomaten doormidden. Snijd de ui in halve ringen. Pluk de blaadjes van de basilicum en snijd de steeltjes fijn. Meng de azijn met de apart gehouden zongedroogdetomaten-olie, de rest van de knoflook, de basilicumtakjes en de helft van de zongedroogde tomaten in de hakmolen tot een saus. Breng op smaak met peper en eventueel zout.",
                    "Hak de amandelen grof. Serveer de pasta over een serveerschaal en meng met de saus. Meng de aubergine, de rest van de zongedroogde tomaten, de olijven, de ui en de blaadjes basilicum erdoor. Garneer met de rest van de oregano en de amandelen.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Vul je pastasalade met semi-gedroogde tomaten, olijven en aubergine. Garneer met verse kruiden en gerookte amandelen voor extra smaakplezier.",
            self.harvester_class.description(),
        )
