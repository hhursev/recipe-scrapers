import os
import unittest

from recipe_scrapers.mindmegette import Mindmegette


class TestMindmegetteScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
                os.getcwd(),
                'recipe_scrapers',
                'tests',
                'test_data',
                'mindmegette.testhtml'
        )) as file_opened:
            self.harvester_class = Mindmegette(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'mindmegette.hu',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Jókai-bableves'
        )

    def test_total_time(self):
        self.assertEqual(
            90,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                '18 dkg szárazbab (vagy 30 dkg friss fejtett bab)',
                '1 db füstölt sertéscsülök',
                '8 dkg petrezselyemgyökér',
                '10 dkg sárgarépa',
                '1 db babérlevél',
                '1 gerezd fokhagyma',
                '15 dkg zöldpaprika',
                '7 dkg friss paradicsom',
                'só',
                '30 dkg kolbász',
                '4 dkg zsír',
                '3 dkg liszt',
                '3 dkg vöröshagyma',
                '1/2 dkg fűszerpaprika',
                '1/2-1 csokor petrezselyem zöldje',
                '1,5 dl tejföl (+ a tálaláshoz)',
                '3 dkg liszt',
                'csipetke'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            "A szárazbabot jól megmossuk és előző este beáztatjuk. (Fejtett bab esetén erre nincs szükség.) " +
            "A csülköt kb. 1 1/2 l vízben vajpuhára főzzük.\n" +
            "Másnap a karikára vágott gyökérzöldséget a főzőlé tetején megfagyott s arról villával leszedett zsírján " +
            "megpirítjuk. Ha barnulni kezd, az áztatólével együtt hozzáöntjük a babot, és felöntjük a füstölt ízű " +
            "lével. Hozzáadjuk a babérlevelet, az összezúzott fokhagymát, a kis kockára vágott zöldpaprikát és " +
            "paradicsomot. A csülöklé sótartalmától függően kevés sóval ízesítjük, és puhára főzzük.\n" +
            "Közben a kolbászt a zsíron megsütjük, majd kivesszük, és vékony karikákra vágjuk. Ha a bab megpuhult, " +
            "a kolbászzsírral és a liszttel világos rántást készítünk az apróra vágott vöröshagymával. " +
            "Az utolsó pillanatban meghintjük a fűszerpaprikával és aprított petrezselyemzölddel.\n" +
            "Ha a leves a rántással felforrt, a tejföllel behabarjuk. Végül csipetkét főzünk bele, és a " +
            "kolbászkarikákkal együtt felforraljuk. Tálalás előtt apró kockákra vágjuk a csülökhúst, és rámerjük " +
            "a forró levest. Egy kevés tejföllel díszítve kínáljuk.",
            self.harvester_class.instructions()
        )

    def test_yields(self):
        self.assertEqual(
            "4 serving(s)",
            self.harvester_class.yields()
        )

    def test_image(self):
        self.assertEqual(
            'http://mindmegette.hu/images/163/O/crop_201609051236_jokai_bableves.jpg',
            self.harvester_class.image()
        )
