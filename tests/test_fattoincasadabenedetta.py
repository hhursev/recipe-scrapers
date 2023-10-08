# mypy: allow-untyped-defs

from recipe_scrapers.fattoincasadabenedetta import FattoInCasaDaBenedetta
from tests import ScraperTest


class TestFattoInCasaDaBenedettaScraper(ScraperTest):

    scraper_class = FattoInCasaDaBenedetta

    def test_host(self):
        self.assertEqual("fattoincasadabenedetta.it", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.fattoincasadabenedetta.it/ricetta/torta-fredda-al-limone/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Benedetta Rossi", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Torta fredda al limone", self.harvester_class.title())

    def test_category(self):
        self.assertEqual(
            "Al cucchiaio,Alla frutta,Dolci,Torte,Torte fredde",
            self.harvester_class.category(),
        )

    def test_total_time(self):
        self.assertEqual(45.0, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.fattoincasadabenedetta.it/wp-content/uploads/2018/07/copertina-YT.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "limoni 4 il succo di 3 limoni per la crema e di 1 per la panna allo yogurt + fettine di limone q.b. per decorare",
            "zucchero 130 g",
            "amido di mais 45 g",
            "aroma limone 2 ml di cui 1 ml per la crema e 1 ml per la panna allo yogurt",
            "colorante giallo",
            "limoncino 30 ml oppure succo di arancia o di limone",
            "acqua 200 ml + q.b. per crema",
            "savoiardi 12",
            "gelatina in fogli 10 g",
            "panna zuccherata 750 ml ben fredda, di cui 500 ml per la panna allo yogurt e 250 ml per la decorazione",
            "yogurt al limone 250 g",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = [
            "Iniziamo preparando la crema al limone per il ripieno. Spremiamo il succo di 3 limoni e versiamolo in un bicchiere graduato. Aggiungiamo acqua fino a raggiungere un totale di 400 ml.",
            "In un pentolino versiamo lo zucchero e l’amido di mais, mescoliamoli con una frusta. Continuando a mescolare versiamo succo di limone e acqua e aggiungiamo mezza fialetta di aroma al limone e qualche goccia di colorante alimentare giallo. Pubblicità",
            "Portiamo sul fuoco e continuiamo a mescolare fino a quando il composto si addensa e diventa una crema. Ci vorranno 5 minuti circa.",
            "La crema al limone è pronta, teniamola da parte per farla raffreddare completamente.",
            "Per preparare la bagna mescoliamo in una ciotola un bicchierino di limoncino e 1 bicchiere di acqua. In alternativa Per una bagna analcolica possiamo mescolare acqua e succo di limone, oppure acqua e succo d'arancia. Pubblicità",
            "Prepariamo un bel piatto rotondo e una tortiera apribile da 24 cm di diametro. Della tortiera ci servirà solo il cerchio apribile senza il fondo che sistemiamo al centro del piatto.",
            "Bagniamo leggermente i savoiardi nella bagna e posizioniamoli per formare la base della torta. In alternativa Se non abbiamo i savoiardi possiamo usare un disco sottile di pan di Spagna, oppure usare un altro tipo di biscotto da sbriciolare e mescolare con il burro, come per la base della cheesecake.",
            "Mettiamo in ammollo in acqua fredda la gelatina in fogli.",
            "In una ciotola capiente versiamo la panna già zuccherata, due vasetti di yogurt, mezza fialetta di aroma al limone e il succo di un limone. Montiamo a neve con lo sbattitore elettrico. Pubblicità",
            "Strizziamo la gelatina e mettiamola in un pentolino assieme a 3 cucchiaini di acqua, facciamo sciogliere sul fuoco mescolando, ci vorranno pochi secondi. Aggiungiamola subito alla crema e mescoliamo con le fruste per incorporarla.",
            "Per assemblare la torta versiamo metà del composto di panna e yogurt appena ottenuta sulla base e mettiamo in freezer per 20 minuti. Quindi versiamo la crema al limone ormai fredda e livelliamola bene sulla torta. Ricopriamo con il resto della panna. Livelliamo la superficie e mettiamo in freezer per 2 ore o in frigo per 4 ore.",
            "Trascorso il tempo togliamo la torta dallo stampo, per aiutarci passiamo un coltello sui bordi e poi apriamo delicatamente la tortiera.",
            "Per la decorazione montiamo a neve 250 ml di panna già zuccherata e aggiungiamo qualche goccia di colorante alimentare giallo. Riempiamo una sac à poche e iniziamo a decorare. Facciamo tanti piccoli ciuffetti in superficie. Affettiamo un limone e sistemiamo le fettine lungo tutto il bordo della torta. La torta al limone è pronta, teniamo in frigo fino al momento di servire.",
        ]
        expected_instructions = "\n".join(expected_instructions)
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(3.8, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "Un dessert estivo fresco e delicato, con una decorazione elegante e un sapore unico.",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("it-IT", self.harvester_class.language())
