from recipe_scrapers.marmiton import Marmiton
from tests import ScraperTest


class TestMarmitonScraper(ScraperTest):

    scraper_class = Marmiton

    def test_host(self):
        self.assertEqual("marmiton.org", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.marmiton.org/recettes/recette_ratatouille_23223.aspx",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Ratatouille")

    def test_total_time(self):
        self.assertEqual(80, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 personnes", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "350 g d'aubergine",
                "350 g de courgette",
                "350 g de poivron de couleur rouge et vert",
                "350 g d'oignon",
                "500 g de tomate bien mûres",
                "3 gousses d'ail",
                "6 cuillères à soupe d'huile d'olive",
                "1 brin de thym",
                "1 feuille de laurier",
                "poivre",
                "sel",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Coupez les tomates pelées en quartiers,\n"
            "les aubergines et les courgettes en rondelles.\n"
            "Emincez les poivrons en lamelles\n"
            "et l'oignon en rouelles.\n"
            "Chauffez 2 cuillères à soupe d'huile dans une poêle\n"
            "et faites-y fondre les oignons et les poivrons.\n"
            "Lorsqu'ils sont tendres, ajoutez les tomates, l'ail haché, le thym et le laurier.\n"
            "Salez, poivrez et laissez mijoter doucement à couvert durant 45 minutes.\n"
            "Pendant ce temps, préparez les aubergines et les courgettes. "
            "Faites les cuire séparemment ou non dans l'huile d'olive pendant 15 minutes.\n"
            "Vérifiez la cuisson des légumes pour qu'ils ne soient plus fermes. "
            "Ajoutez les alors au mélange de tomates et prolongez la cuisson sur tout petit feu pendant 10 min.\n"
            "Salez et poivrez si besoin.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.8, self.harvester_class.ratings())
