from tests import ScraperTest

from recipe_scrapers.smaker import Smaker


class TestSmakerScraper(ScraperTest):
    scraper_class = Smaker

    def test_host(self):
        self.assertEqual("smaker.pl", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("KORAL", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Ciasto \"Słoneczko\" bez blaszki", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "//static.smaker.pl/photos/d/9/6/d96d1e3fbc676d8c4e597e0c7c2c119f_367480_5fff1aa8d1776_wm.jpg",
            self.harvester_class.image())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "Ciasto: mąka pszenna 250 g",
                "drożdże 15 g",
                "cukier 33 g",
                "mleko 65-75 ml",
                "1 mniejsze jajko",
                "roztopione masło lub margaryna 25 g",
                "Nadzienie : twaróg półtłusty 250 g",
                "cukier puder 1 łyżka",
                "1 żółtko",
                "1-2 łyżki powideł śliwkowych",
                "ew. trochę suszonej żurawiny",
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join([
                "Talerz obwód 20 cm. Ciasto. Mąkę przesiać do miski, w środku zrobić dołek, wkruszyć drożdże, posypać łyżką cukru, dodać 3 łyżki letniego mleka. Odstawić na 10 minut do wyrośnięcia. W tym czasie jajko utrzeć z pozostałym cukrem. Gdy drożdże wyrosną, dodać do miski resztę składników i dokładnie wyrobić gładkie ciasto. Masa powinna być lekko luźna ale zwarta, w trakcie wyrabiania można dodać trochę mleka. Ciasto przykrywamy ściereczką i odstawiamy w ciepłe miejsce do wyrośnięcia ( 0,5 -1 godziny ). Nadzienie. Twaróg rozgniatamy widelcem, mieszamy z cukrem i żółtkiem . Blachę od piekarnika przykrywamy papierem do pieczenia. Wyrośnięte ciasto przekładamy centralnie na blachę i formujemy okrąg minimum 26 cm. No środku koła kładziemy talerz a wokół niego wycinamy paski 36 sztuk. Po 3 paski na jeden płatek. Środkowy pasek skręcamy dwa razy i podwijamy do środka, dwa wokół niego łączymy ze sobą. Po zrobieniu wszystkich płatków zdejmujemy talerz i ręcznie spłaszczamy ciasto tworząc niewielką górkę wokół płatków. Wgłębienie smarujemy cienką warstwą powideł, potem nakładamy twaróg.",
                "Ciasto pieczemy w 180 C około 15-20 minut. Po wyjęciu płatki smarujemy rozrzedzonymi powidłami.",
            ]),
            self.harvester_class.instructions()
        )

    def test_description(self):
        self.assertEqual(
            "Słowiańskie ciasto drożdżowe bez użycia blaszek, tortownic. To jest wersja z twarogiem i powidłami.",
            self.harvester_class.description(),
        )
