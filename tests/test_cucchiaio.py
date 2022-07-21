from recipe_scrapers.cucchiaio import Cucchiaio
from tests import ScraperTest


class TestCucchiaioScraper(ScraperTest):

    scraper_class = Cucchiaio

    def test_host(self):
        self.assertEqual("cucchiaio.it", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Il Cucchiaio d'Argento", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Pesce spada al miele millefiori, pomodorini e patatine novelle",
            self.harvester_class.title(),
        )

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 items", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://statics.cucchiaio.it/content/cucchiaio/it/ricette/2017/10/pesce-spada-al-miele-millefiori-pomodorini-e-patatine-novelle/jcr:content/header-par/image-single.img10.jpg/1610381008015.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "4 fette di pesce spada di circa 200 g l'una",
                "20 patatine novelle",
                "1 spicchio d'aglio",
                "1 grappolo di pomodorini",
                "2 cucchiai di pinoli tostati",
                "4-5 cucchiaini di miele millefiori",
                "1 bicchiere di aceto di vino",
                "foglioline di mirto",
                "prezzemolo",
                "erba cipollina",
                "olio extravergine di oliva",
                "sale",
                "pepe",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "1. Iniziate la preparazione del pesce spada al miele millefiori, pomodorini e patatine novelle mettendo a marinare le fette di pesce. Poggiatele su un piatto, aggiungete alcune foglie di mirto, l'aglio a fettine, un giro d'olio e lasciatele marinare per dieci minuti. In un tegame scaldate tre cucchiai d'olio, adagiatevi le fette di pesce spada e cuocetele per circa 2 minuti per lato o comunque fino a quando si forma una crosticina. Trasferitele su una teglia e passatele per circa 5 minuti in forno a 200°. Sfornatele e fatele riposare al caldo per una decina di minuti.\n2. Intanto tagliate a cubetti i pomodorini, cospargeteli con un po' di sale, un pizzico di pepe, prezzemolo ed erba cipollina tritati finemente. Preparate la salsina al miele: in una casseruola scaldate l'aceto facendolo ridurre di un quarto, aggiungete il miele millefiori e assaggiate per controllarne il sapore, se troppo agro aggiungete altro miele. Lasciate raffreddare.\n3. Infine, incorporate il tutto ai pomodori, mescolate bene, aggiungete olio, pinoli, regolate di sale e fate riposare. Sbollentate le patatine in acqua salata, asciugatele e insaporitele in una padella con un filo d’olio.\n4. Disponete le fette di pesce spada sul piatto da portata: completate con le patatine e cospargete su tutto la salsina al miele.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())
