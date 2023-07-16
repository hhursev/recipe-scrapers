from recipe_scrapers.nosalty import NoSalty
from tests import ScraperTest


class TestNoSaltyScraper(ScraperTest):

    scraper_class = NoSalty

    def test_host(self):
        self.assertEqual("nosalty.hu", self.harvester_class.host())

    def test_language(self):
        self.assertEqual("hu", self.harvester_class.language())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.nosalty.hu/recept/aranygaluska-ahogy-nagymamam-kesziti",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Aranygaluska ahogy a nagymamám készíti"
        )

    def test_total_time(self):
        self.assertEqual(90, self.harvester_class.total_time())

    def test_ingredients(self):
        self.assertListEqual(
            [
                "50 dkg Finomliszt",
                "2 dkg Friss élesztő",
                "7 dkg Vaj",
                "3 dl Tej",
                "1 púpozott ek Cukor",
                "2 db Tojássárgája",
                "1 ek Vaj a forma kikenéséhez",
                "30 dkg Dió darált",
                "15 dkg Cukor ízlés szerint",
                "10 dkg Vaj",
                "7 dl Tej",
                "4 db Tojássárgája",
                "1 db Vanília kikapart magja",
                "6 dkg Cukor",
                "1 púpozott ek Finomliszt",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "A szobahőmérsékletű lisztet tálba szitáljuk.\n"
            "A tejet meglangyosítjuk, elmorzsoljuk benne az élesztőt, hozzáadjuk a cukrot, és felfuttatjuk.\n"
            "A vajat megolvasztjuk, a tojássárgákkal és a felfuttatott élesztővel együtt a liszthez adjuk, és kemény munkával hólyagosra gyúrjuk. Tetejét meglisztezzük, letakarjuk, és duplájára kelesztjük.\n"
            "Ha kész, ujjnyi vastagra nyújtjuk, és picipogácsaszaggatóval kiszaggatjuk.\n"
            "Egy kapcsos tortaformát vastagon kivajazunk, a vajat megolvasztjuk, a diót és a cukrot kikeverjük.\n"
            "Fogjuk a pogácsákat, beleforgatjuk az olvasztott vajba, meghempergetjük a cukros dióban, és a formába sorakoztatjuk őket.\n"
            "Ha az egész kész, előmelegített sütőbe toljuk letakarva (a dió könnyen odakap).\n"
            "Amíg sül, elkészítjük a sodót: A tejet a vaníliarúd kikapart magjával felforraljuk, majd levesszük a tűzről.\n"
            "Egy másik lábosban kikeverjük a tojássárgákat a cukorral és a liszttel.\n"
            "Apránként hozzáadva a vaníliás tejet, kis lángon sűrűre főzzük (nem nagyon sűrűre, nem puding!).\n"
            "Megvárjuk, míg a kész aranygaluska is hűl egy kicsit, majd széttépjük (nem vágjuk), és nyakon öntjük a sodóval.",
            self.harvester_class.instructions(),
        )

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://image-api.nosalty.hu/nosalty/images/recipes/Am/SZ/aranygaluska-ahogy-nagymamam-kesziti.jpeg?w=1200&h=1200&s=78e81357b434b48faaac2ca43c8321f5",
            self.harvester_class.image(),
        )
