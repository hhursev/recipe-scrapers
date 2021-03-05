from recipe_scrapers.giallozafferano import GialloZafferano
from tests import ScraperTest


class TestGialloZafferanoScraper(ScraperTest):

    scraper_class = GialloZafferano

    def test_host(self):
        self.assertEqual("ricette.giallozafferano.it", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://ricette.giallozafferano.it/Bavarese-alle-fragole.html",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Bavarese alle fragole")

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("10 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "Latte intero 200 ml",
                "Tuorli 3",
                "Zucchero 105 g",
                "Baccello di vaniglia ½",
                "Limoni ½",
                "Sale fino 1 pizzico",
                "Fragole 1.1 kg",
                "Gelatina in fogli 18 g",
                "Panna fresca liquida 500 ml",
                "Panna fresca liquida 150 ml",
                "Zucchero a velo 30 g",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Per preparare la bavarese alle fragole, iniziate dalla crema inglese che è la base del dolce: incidete mezza bacca di vaniglia e raschiate con la punta di un coltellino per estrarre i semini 1 . Prelevate la scorza del limone facendo attenzione a non sbucciare anche la parte bianca 2 e unite i due aromi nel pentolino con il latte 3 : scaldate a fuoco dolce fino a sfiorare il bollore poi spegnete il fuoco.\nIntanto versate i tuorli in una ciotola capiente sbatteteli con la frusta poi aggiungete 65 g di zucchero semolato a pioggia continuando a mescolare 4 e aggiungete un pizzico di sale 5 . Lavorateli per qualche minuto, fino ad ottenere un composto omogeneo. Versate sulle uova sbattute il latte scaldato, filtrandolo con un colino a maglie strette 6 .\nMescolate con una spatola 7 e ponete la crema a cuocere a bagno maria a fuoco basso, sempre mescolando 8 ; la temperatura della crema non deve mai superare gli 85° (controllate con un termometro da cucina) 9 .\nQuando la crema sarà pronta versatela in una ciotola e ponete la ciotola in un'altra più capiente e piena di ghiaccio 10 : in questo modo rafferdderete immediatamente la crema senza che la consistenza ne risenta. Mescolate 11 poi togliete dal ghiaccio e coprite la crema con pellicola a contatto per farla raffreddare completamente. Mettete in ammollo i fogli di gelatina in acqua molto fredda 12 per almeno 10 minuti.\nLavate, scolate per bene e togliete il picciolo alle fragole, quindi tagliatele a pezzi 13 e cuocetele in padella con 40 g di zucchero semolato a fuoco dolce, coperte con un coperchio (14-15).\nFrullate le fragole cotte con lo zucchero 16 e setacciate la purea ottenuta 17 . Quindi trasferitela in un pentolino e rimettetela sul fuoco dolce 18 .\nScolate e strizzate i fogli di gelatina e scioglieteli nella coulis di fragole 19 , mescolate con una frusta per farli sciogliere completamente 20 . Fate intiepidire il composto, e unitelo alla crema inglese 21 e mescolate.\nPoi a parte montate 500 ml di panna fresca (non troppo ferma) 22 e unitela alla crema di fragole 23 e amalgamate bene il composto: dovrà risultare fluido, cremoso e omogeneo. Quindi prendete uno stampo da ciambella e bagnate l'interno con dell'acqua fredda. Versate delicatamente il composto ottenuto nello stampo di 22 cm di diametro e capienza 1,5 lt 24 .\nCopritelo con pellicola trasparente 25 e ponetelo in frigorifero per almeno 4-6 ore (meglio sarebbe prepararlo la sera prima). Preparate poi la panna montata con lo zucchero a velo 26 e ponetela in una sac-à-poche 27 e in frigorifero fino al momento dell'utilizzo.\nTrascorso il tempo necessario, estraete il bavarese dal frigorifero, immergete lo stampo fino al bordo in acqua calda per qualche secondo 28 e poi capovolgete delicatamente il bavarese su di un piatto da portata 29 . Decorate il bavarese a piacere con ciuffetti di panna tutto intorno 30 .\nCreate dei ciuffi anche sulla superficie 31 . Poi decorate con le fragole fresche e foglioline di menta a piacere (32-33).",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.0, self.harvester_class.ratings())
