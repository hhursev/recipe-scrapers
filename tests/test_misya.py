from recipe_scrapers.misya import Misya
from tests import ScraperTest


class TestMisya(ScraperTest):

    scraper_class = Misya

    def test_host(self):
        self.assertEqual("misya.info", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.misya.info/ricetta/tortino-cuore-caldo.htm",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Tortino cuore caldo")

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.misya.info/wp-content/uploads/2016/02/Tortino-cuore-caldo1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 di uova",
                "2 di tuorli",
                "100 gr di zucchero",
                "110 gr di cioccolato bianco",
                "110 gr di burro",
                "50 gr di farina",
                "6 gr di cacao",
                "1 cucchiaino di essenza di vaniglia",
                "1 cucchiaino di colorante rosso",
                "zucchero a velo",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Montate i tuorli e le uova fino a renderle spumose.\nPoi aggiungete lo zucchero\nPoi unite il cioccolato ed il burro fuso.\nAggiungete adesso il cacao e la farina.\nQuindi aggiungete il colorante e la vaniglia e mescolate fino ad ottenere un impasto di un bel colore rosso.\nVersate l'impasto in 6 stampini imburrati ed infarinati meticolosamente.\nPoi infornate i tortini in forno già caldo a 190° e cuocete per 13-15 minuti circa.Vi accorgerete quando è il momento giusto quando vedrete una leggera crosticina sui bordi e la superficie ma muovendo lo stampino risulterà ancora morbido.Fate la prova con uno prima di tirarli via dal forno tutti e ricordatevi che ogni forno è diverso dall'altro.\nLasciate riposare un minuto, poi capovolgete su un piatto da dessert.\nServite il Tortino cuore caldo immediatamente spolverizzandolo con zucchero a velo.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.8, self.harvester_class.ratings())
