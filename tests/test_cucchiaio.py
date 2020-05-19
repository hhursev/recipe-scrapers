import os
import unittest

from recipe_scrapers import Cucchiaio


class TestCucchiaio(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                'test_data',
                'cucchiaio.testhtml'
        )) as file_opened:
            self.harvester_class = Cucchiaio(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'cucchiaio.it',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Penne all'arrabbiata"
        )

    def test_total_time(self):
        self.assertEqual(
            20,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '5 pomodori San Marzano maturi',
                '320 g di penne rigate',
                '1 peperoncino rosso',
                "1 spicchio d'aglio",
                'olio extravergine di oliva',
                'prezzemolo tritato',
                'pecorino romano',
                'sale'
            ]
            ,
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            "1 Realizzate il condimento delle penne all'arrabbiata mentre l'acqua bolle e la pasta cuoce. Mettete in una padella 2-3 cucchiai di olio, lo spicchio d'aglio schiacciato e il peperoncino tagliuzzato, dopo averne tolti tutti i semi. La fiamma dovrà essere moderata, l'olio deve insaporirsi ma non bruciare. Tagliate i pomodori a metà, eliminate i semi e quindi riduceteli a cubetti.\n2 Levate l'aglio dalla padella e versatevi i cubetti di pomodoro. Fateli scaldare per qualche minuto fino a quando otterrete una salsa leggera e ancora ben colorita. Una volta che le penne sono cotte al dente, scolatele e versatele direttamente sulla salsa.\n3 Mescolate bene in modo che la pasta sia condita in maniera uniforme quindi unite un giro d'olio crudo. Impiattate, completate con un po' di prezzemolo, pecorino grattugiato a piacere e servite subito le penne all'arrabbiata.",
            self.harvester_class.instructions()
        )
