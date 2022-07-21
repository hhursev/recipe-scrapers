from recipe_scrapers.fredriksfikaallas import FredriksFikaAllas
from tests import ScraperTest


class TestFredriksFikaAllasScraper(ScraperTest):

    scraper_class = FredriksFikaAllas

    def test_host(self):
        self.assertEqual("fredriksfika.allas.se", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Fredrik Nylén", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Mormors bästa tekakor", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Fredriks bröd", self.harvester_class.category())

    def test_image(self):
        self.assertEqual(
            "https://files.allas.se/uploads/sites/25/2015/08/10072015-_MG_0917-860x573.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 dl havregryn",
                "5 dl vatten",
                "50 g smör",
                "0,5 dl ljus sirap",
                "2 tsk salt",
                "50 g jäst",
                "9-12 dl rågsikt",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """1. Koka en gröt på havregryn och 2,5 dl vatten.
2. Smält smöret i gröten, samt blanda i resten av vattnet, sirapen och saltet.
3. Smula jästen i en bunke, ha i grötblandningen och rör tills jästen löst upp sig.
4. Blanda i mjölet och arbeta degen ihop till en deg, mjölmängden varierar på hur länge man kokat gröten så därav kan det variera. Degen ska gå att ta på utan att den klibbar på fingrarna.
5. Låt jäsa 30 minuter.
6. Ha upp degen på ett bakbord och knåda den lite. Kavla ut degen ca 0,5 cm hög. Stansa ut rundlar och lägg på bakplåtspapperklädd plåt. Nagga tekakorna med en gaffel.
7. Låt jäsa under en handduk ca 30 minuter. Sätt ugnen på 225 grader.
8. Baka mitt i ugnen i 6-8 minuter tills de får en gyllene färg.Ett bra tips att använda som utstickare när du gör tekakor är en innerkruka som är väl rengjord såklart. Perfekt tekakestorlek!""",
            self.harvester_class.instructions(),
        )
