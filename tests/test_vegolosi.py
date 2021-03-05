from recipe_scrapers.vegolosi import Vegolosi
from tests import ScraperTest


class TestVegolosiScraper(ScraperTest):

    scraper_class = Vegolosi

    def test_host(self):
        self.assertEqual("vegolosi.it", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.vegolosi.it/ricette-vegane/polpette-di-tofu-e-piselli-salsa-allo-zafferano/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Polpette di tofu e piselli con salsa allo zafferano",
        )

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "250 g tofu al naturale",
                "150 g piselli lessati",
                "100 g cous cous",
                "100 ml acqua bollente",
                "20 g di mandorle",
                "20 g di olio extravergine di oliva",
                "basilico",
                "sale e pepe",
                "250 ml latte di soia senza zucchero ( oppure brodo vegetale o latte di avena o farro)",
                "15 g amido di mais o fecola di patate",
                "1 bustina zafferano in polvere",
                "Sale",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Si cucina! Dopo aver messo il cous cous in una ciotola capiente o in una pentola, versateci sopra l’acqua bollente e lasciate riposate il tempo necessario affinché quest’ultimo assorba tutto il liquido. Dopo qualche minuto con i rebbi di una forchetta sgranatelo per bene e lasciatelo da parte. Formiamo le polpettine Nel robot da cucina aggiungete il tofu spezzettato grossolanamente, il basilico, i piselli, metà del cous cous cotto, l’olio extravergine di oliva, il sale e il pepe. Tritate tutti gli ingredienti sino a ottenere un composto che potrete lavorare con le mani, quindi versatelo in una ciotola insieme al cous cous rimanente e mescolate. Correggete di sale, se ce ne fosse bisogno, e se il composto risultasse troppo asciutto, aggiungeteci ancora un filo di olio extravergine di oliva. In forno Con le mani umide formate con l’impasto dei bocconcini: la grandezza dovrà essere, più o meno, quella di una noce. Passateli poi in un trito fine di mandorle, che potrete realizzare sia al coltello che con un tritatutto. Procedete adagiando le polpette di tofu su una leccarda ricoperta da carta da forno. Infornate a 180 gradi per circa 15 minuti. Negli ultimi minuti utilizzate la funzione grill del forno per creare una giusta doratura delle vostre polpette vegane. Prepariamo la crema Nel frattempo, preparate la crema allo zafferano unendo tutti gli ingredienti, quindi il latte di soia, l’amido di mais, lo zafferano e il sale in un pentolino. Cuocete fino a raggiungere al consistenza desiderata. Servite le polpette vegan ben calde e con la loro salsa come accompagnamento.",
            self.harvester_class.instructions(),
        )
