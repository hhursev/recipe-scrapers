from recipe_scrapers.cucchiaio import Cucchiaio
from tests import ScraperTest


class TestCucchiaioScraper(ScraperTest):

    scraper_class = Cucchiaio

    def test_host(self):
        self.assertEqual("cucchiaio.it", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Il Cucchiaio d'Argento", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Riso al latte di cocco", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(0, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 item(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://statics.cucchiaio.it/content/cucchiaio/it/ricette/2021/02/riso-al-latte-di-cocco/jcr:content/header-par/image-single.img10.jpg/1613547033182.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            ["300 g di riso basmati", "1 bicchiere di latte di cocco"],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "1. Per preparare il riso al latte di cocco cominciate facendo cuocere il riso. Versatelo in una pentola coperto da due dita di acqua. Il riso cuocerà e assorbirà l'acqua. Il riso è pronto quando si disfa e raggiunge una consistenza simile a quella della nostra 'polenta'. Se l'acqua si assorbe ma il riso non risulta ancora ben cotto potete aggiungere acqua calda per proseguire la cottura. 10 minuti prima di toglierlo dal fuoco (deve essere già in parte 'disfatto') aggiungete il latte di cocco e proseguite la cottura.\n2. Una volta terminata la cottura, stendete il riso in una teglia, livellatelo e lasciate che raffreddi completamente.\n3. Una volta raffreddato, tagliate il riso al latte a quadrotti della dimensione che preferite e servitelo con il condimento che più vi piace.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())
