# mypy: allow-untyped-defs

from recipe_scrapers.rutgerbakt import RutgerBakt
from tests import ScraperTest


class TestRutgerBaktScraper(ScraperTest):
    scraper_class = RutgerBakt
    test_file_name = "rutgerbakt_3"

    def test_host(self):
        self.assertEqual("rutgerbakt.nl", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Rutger van den Broek", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Banketstaaf", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual(None, self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://rutgerbakt.nl/wp-content/uploads/2016/11/banketstaaf-1-e1478017268526-1920x1080-c-default.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "400 gr amandelspijs, gekocht of zelfgemaakt",
                "1 rol Tante Fanny vers bladerdeeg 270 gr",
                "½ ei, losgeklopt",
                "½ ei, losgeklopt, om te bestrijken",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Verwarm de oven voor op 220 ⁰C en bekleed een bakplaat met bakpapier. Kneed het amandelspijs kort door en voeg vervolgens een half ei toe om het amandelspijs iets soepeler te maken. Maak twee rollen van het amandelspijs van zo’n 32-34 centimeter lang.\nRol het bladerdeeg uit en snijd het deeg in de lengte doormidden. Leg op het midden van ieder stuk bladerdeeg een rol amandelspijs en vouw de twee korte uiteinden van het deeg over het amandelspijs. Bestrijk deze twee uiteinden licht met water. Vouw één lange kant van het deeg over het amandelspijs en maak ook deze licht vochtig. Vouw tot slot de andere kant van het deeg over de rol amandelspijs en druk dit goed vast. Leg de banketstaven met de deegnaad naar beneden op de bakplaat en laat ze 20 minuten rusten in de koelkast.\nBestrijk de banketstaven met het losgeklopte ei en bak ze in 25 tot 35 minuten goudbruin. Laat de banketstaven afkoelen op een rooster.\n\n\nDit bericht is gesponsord door Tante Fanny.\n",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.0, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "Rondom Sinterklaas wordt er volop gebakken voor het ‘heerlijk avondje’! Een lekkernij die zeker niet mag ontbreken is de banketstaaf. Als kind (en nu eigenlijk nog steeds wel) wilde ik altijd het liefst het kontje van de banketstaaf. Er is niks lekkerder dan eerst het spijs eruit te lepelen en dan als laatste het bladerdeeg op te eten. Heerlijk!",
            self.harvester_class.description(),
        )
