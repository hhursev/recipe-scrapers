from recipe_scrapers.yemek import Yemek
from tests import ScraperTest


class TestYemekScraper(ScraperTest):

    scraper_class = Yemek

    def test_host(self):
        self.assertEqual("yemek.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Yasemin Gürsürer", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Köri Soslu Tavuklu Patates Topları", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(85, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cdn.yemek.com/mncrop/300/200/uploads/2020/06/kori-soslu-tavuklu-patates-toplari-yemekcom.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 yemek kaşığı sıvı yağ",
                "1 kilogram tavuk",
                "1 adet soğan",
                "1 adet kapya biber",
                "300 gram mantar",
                "1,5 çay kaşığı tuz",
                "1 çay kaşığı karabiber",
                "1 çay kaşığı toz kırmızı biber",
                "1 çay bardağı su",
                "5 adet patates",
                "2 yemek kaşığı tereyağı",
                "2 çay kaşığı tuz",
                "2 yemek kaşığı tereyağı",
                "1 tatlı kaşığı sıvı yağ",
                "2 yemek kaşığı un",
                "2,5 su bardağı süt",
                "1 tatlı kaşığı köri",
                "1/2 çay kaşığı tuz",
                "100 gram rendelenmiş mozarella peyniri",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Patatesleri bir tencerede haşlayın. Haşlandıktan sonra suyunu süzüp tereyağı ve tuzla tatlandırıp püre haline getirin. Kişi sayısına göre eşit parçalara bölüp top haline getirin.\nTavukları pişireceğiniz tavayı ısıtın ve sıvı yağ ekleyip tavukları suyunu salıp çekene dek pişirin.\nSoğanları da tavukların üzerine ekleyip 2-3 dakika soteleyin. Ardından kapya biberi de ilave edip kavurun ve mantarları ekleyip suyunu salıp çekmesini bekleyin. Ara ara karıştırın.\nTuz, karabiber ve kırmızı biberi de ilave edip karıştırın ve son olarak suyunu ilave edip kısık ateşte 10 dakika kadar pişirin.\nSos için, tereyağını bir sos tenceresinde eritin ve sıvı yağ ekleyin. Üzerine un ve köriyi ilave edip 2-3 dakika kavurun. Sütü de yavaş yavaş ilave edip sürekli olarak karıştırın. Kaynamaya ve kıvamı koyulaşmaya başladıktan sonra altını kısıp 5 dakika daha pişirip ocaktan alın. Beklerken çok koyulaşırsa su veya sütle açın.\nFırını 200 dereceye ayarlayın.\nBorcama pişirdiğiniz sebzeli tavuğu yayın. Üzerine hazırladığınız patates toplarını, aralarında boşluk olacak şekilde dizin. Her bir patates topunun üzerine köri sosundan eşit miktarda dökün. Son olarak üzerlerine rendelenmiş mozarella ilave edip 200 derece fırında üzerleri kızarana dek 15 dakika pişirin.""",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.5, self.harvester_class.ratings())
