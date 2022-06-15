from recipe_scrapers.kwestiasmaku import KwestiaSmaku
from tests import ScraperTest


class TestKwestiaSmakuScraper(ScraperTest):

    scraper_class = KwestiaSmaku

    def test_host(self):
        self.assertEqual("kwestiasmaku.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("kwestiasmaku", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Pieczony kalafior", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(None, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.kwestiasmaku.com/sites/v123.kwestiasmaku.com/files/pieczony-kalafior-01_0.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 kalafior",
                "4 łyżki oliwy z pierwszego tłoczenia",
                "świeżo zmielony pieprz",
                "1 i 1/2 łyżeczki kurkumy",
                "1 łyżeczka czarnuszki",
                "sól morska",
                "sos czosnkowy lub ser feta",
                "natka pietruszki",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Odciąć liście z kalafiora, przekroić na pół i wyciąć nadmiar głąba. Główkę kalafiora rozdzielić na różyczki lub pokroić na cząstki.\n"
            "Położyć na dużej blaszce (np. z wyposażenia piekarnika) wyłożonej papierem do pieczenia. Piekarnik nagrzać do 200 stopni C.\n"
            "Kalafiora polać oliwą, posypać pieprzem, kurkumą i czarnuszką, a następnie dokładnie wymieszać i rozłożyć na całej powierzchni blachy.\n"
            "Wstawić do nagrzanego piekarnika i piec przez 30 minut. Po upieczeniu doprawić solą i posiekaną natką pietruszki.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
