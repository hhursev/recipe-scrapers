from tests import ScraperTest

from recipe_scrapers.kwestiasmaku import KwestiaSmaku


class TestKwestiaSmakuScraper(ScraperTest):
    scraper_class = KwestiaSmaku

    def test_host(self):
        self.assertEqual('kwestiasmaku.com', self.harvester_class.host())

    def test_title(self):
        self.assertEqual('Krajanka piernikowa', self.harvester_class.title())

    def test_yields(self):
        self.assertEqual("3 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual('https://www.kwestiasmaku.com/sites/v123.kwestiasmaku.com/files/krajanka-piernikowa.jpg',
                         self.harvester_class.image())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "Ciasto piernikowe",
                "500 g mąki pszennej",
                "1 łyżeczka sody oczyszczonej",
                "1 łyżeczka proszku do pieczenia",
                "1/2 szklanki drobno posiekanych orzechów",
                "100 g masła",
                "1 szklanka cukru",
                "1/2 szklanki miodu",
                "2 łyżki przyprawy piernikowej (gotowej lub domowej)",
                "1 jajko",
                "Masa marcepanowa",
                "200 g masy marcepanowej",
                "50 g (1/3 szklanki) mąki pszennej",
                "1 jajko",
                "1 łyżka likieru Amaretto lub soku z cytryny",
                "Oraz",
                "280 g (słoiczek) powideł śliwkowych",
                "1/2 szklanki cukru pudru",
                "2 łyżki likieru Amaretto lub soku z cytryny",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.maxDiff = None
        self.assertEqual(
            "\n".join([
                "Ciasto piernikowe",
                "Mąkę wymieszać z sodą oczyszczoną, proszkiem do pieczenia oraz drobno posiekanymi orzechami.",
                "Do dużego garnka włożyć masło, cukier, miód oraz przyprawę piernikową. Mieszając podgrzewa aż składniki się roztopią i będą gorące (nie zagotowywać).",
                "Dodawać stopniowo mąkę ciągle mieszając aż składniki się połączą. Odstawić z ognia i przestudzić (ok. 5 minut).",
                "Wyłożyć na stolnicę podsypaną mąką, dodać jajko i chwilę wyrobić, w razie potrzeby delikatnie podsypać mąką.",
                "Ciasto podzielić na 2 części, każdą rozwałkować na placek o wymiarach nieco większych niż 20 x 30 cm.",
                "Piekarnik nagrzać do 175 stopni C.",
                "Masa marcepanowa",
                "Masę marcepanową pokroić na kawałki i zmiksować na pastę z dodatkiem mąki jajka i likieru lub soku z cytryny (użyłam rozdrabniacza - melaksera).",
                "Pieczenie",
                "Jeden placek piernikowego ciasta położyć na papierze do pieczenia. Na cieście rozsmarować masę marcepanową zostawiając wolne brzegi na zlepienie ciasta.",
                "Następnie wyłożyć powidła i przykryć drugim plackiem ciasta. Dokładnie zlepić brzegi ciasta i umieścić całość w blaszce ok. 20 x 30 cm lub położyć na innej większej blaszce.",
                "Wstawić do piekarnika i piec przez ok. 30 minut. Wyjąć z piekarnika i ostudzić (ciasto stwardnieje po upieczeniu, z czasem będzie dojrzewało i miękło). Należy je szczelnie przykryć lub włożyć do pojemnika i odłożyć na kilka - kilkanaście dni.",
                "Przed podaniem lub kilka dni wcześniej polać lukrem (utarty cukier puder z likierem lub sokiem z cytryny). Pokroić na małe kwadraciki i przechowywać w zamkniętym pojemniku.",
            ]),
            self.harvester_class.instructions()
        )

    def test_description(self):
        self.assertEqual(
            "Ciasto w stylu piernika dojrzewającego. Robimy je z wyprzedzeniem (1 - 4 tygodnie wcześniej), aby dojrzało i zmiękło. Można je przechowywać przez kilka tygodni (całe lub już pokrojone).",
            self.harvester_class.description(),
        )
