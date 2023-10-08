from recipe_scrapers.arla import Arla
from tests import ScraperTest


class TestArlaScraper(ScraperTest):

    scraper_class = Arla

    def test_host(self):
        self.assertEqual("arla.se", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.arla.se/recept/reuben-sandwich/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Arla Mat", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Reuben sandwich", self.harvester_class.title())

    def test_category(self):
        self.assertEqual(
            "Brunch, Förrätt, Huvudrätt, Mellanmål", self.harvester_class.category()
        )

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://images.arla.com/recordid/FB2425A1-47CE-4EFB-8D47570F80762F18/reuben-sandwich.jpg?format=jpg&width=1300&height=525",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "200 g kokt rimmad oxbringa, eller corned beef",
                "1 dl surkål",
                "1 dl riven Arla Präst® ost",
                "8 skivor surdegsbröd",
                "50 g Svenskt Smör från Arla®, smält",
                "4 saltgurkor",
                "½ grön paprika",
                "1 dl majonnäs",
                "1 msk chilisås",
                "1 tsk paprikapulver",
                "1 tsk dijonsenap",
                "½ krm tabasco",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Dressing:\nBörja med dressingen. Finhacka paprika och lök. Blanda med övriga ingredienser och ställ åt sidan.\nSista instruktionen\nSkär köttet i tunna skivor. Låt surkålen rinna av ordentligt och blanda med osten.\nPensla bröden med smör på båda sidor. Lägg surkål och ost på hälften av bröden. Lägg på köttet. Klicka dressingen över köttet och lägg på resterande bröd.\nGrilla på båda sidor i en het grillpanna eller smörgåsgrill.\nDela grillspett på mitten och trä genom mackorna. Skär saltgurkorna på längden och fäst på grillspetten.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.2, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Amerikansk", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Reuben sandwich är en amerikansk macka med mycket pastrami, saltgurka och så kallad rysk dressing. Bröden fylls med alla godsaker fär att sedan smörstekas. En riktig mack-klassiker som är perfekt att bjuda på till brunch!",
            self.harvester_class.description(),
        )
