from recipe_scrapers.arla import Arla
from tests import ScraperTest


class TestArlaScraper(ScraperTest):

    scraper_class = Arla

    def test_host(self):
        self.assertEqual("arla.se", self.harvester_class.host())

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
            "https://cdn-rdb.arla.com/Files/arla-se/235235459/f96b874a-5b9c-4936-b3e2-5071e76136c0.jpg?mode=crop&w=1200&h=630&scale=both&format=jpg&quality=80&ak=f525e733&hm=35af1404",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "200 g kokt rimmad oxbringa, eller corned beef",
                "1 dl surkål",
                "1 dl riven Arla Präst® ost",
                "8 skivor surdegsbröd",
                "50 g Arla® Svenskt Smör, smält",
                "2 saltgurkor",
                "½ gul paprika",
                "1 schalottenlök",
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
            "Dressing:\nBörja med dressingen. Finhacka paprika och lök. Blanda med övr"
            "iga ingredienser och ställ åt sidan.\nSkär köttet i tunna skivor. Låt sur"
            "kålen rinna av ordentligt och blanda med osten.\nPensla bröden med smör p"
            "å båda sidor. Lägg surkål och ost på hälften av bröden. Lägg på köttet. K"
            "licka dressingen över köttet och lägg på resterande bröd.\nGrilla på båda"
            " sidor i en het grillpanna eller smörgåsgrill.\nDela grillspett på mitten"
            " och trä genom mackorna. Skär saltgurkorna på längden och fäst på grillsp"
            "etten.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.5, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Amerikansk", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "En reuben sandwich är en amerikansk macka, vanligtvis med pastrami - men "
            "vi använder svensk oxbringa, saltgurka och så kallad rysk dressing.",
            self.harvester_class.description(),
        )
