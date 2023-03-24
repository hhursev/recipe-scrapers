from recipe_scrapers.streetkitchen import StreetKitchen
from tests import ScraperTest


class TestStreetKitchenScraper(ScraperTest):

    scraper_class = StreetKitchen

    def test_host(self):
        self.assertEqual("streetkitchen.hu", self.harvester_class.host())

    def test_language(self):
        self.assertEqual("hu", self.harvester_class.language())

    def test_canonical_url(self):
        self.assertEqual(
            "https://streetkitchen.hu/husvet/husveti-fofogasok/sertesszuz-cukorborsos-ujburgonya-salataval/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Sertésszűz cukorborsós újburgonya-salátával"
        )

    def test_total_time(self):
        self.assertEqual(None, self.harvester_class.total_time())

    def test_ingredients(self):
        self.assertListEqual(
            [
                "500 g újburgonya",
                "2 ek olaj",
                "200 g cukorborsó",
                "só, bors",
                "2 gerezd fokhagyma",
                "50 g vaj",
                "½ db citrom leve",
                "2 - 3 ek tejföl",
                "1 tk ecetes torma (üveges)",
                "1 kis csokor petrezselyem",
                "1 kis csokor snidling",
                "400 g sertésszűz",
                "só, bors",
                "2 ek olaj",
                "2 gerezd fokhagyma (héjastul)",
                "2 - 3 ág rozmaring",
                "50 g vaj",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "A burgonyát félbevágjuk, sós vízben puhára főzzük, majd leszűrjük.\n"
            "A húst sózzuk, borsozzuk, és egy serpenyőben 2 kanál olajon, nagyon magas hőfokon kérgesítjük, a vége előtt pár perccel hozzáadunk 2 gerezd héjas fokhagymát, 2 ág rozmaringot és 50 gramm vajat, majd a vaj barnulásáig pirítjuk tovább.\n"
            "Egy tepsire tesszük, és 170 fokra előmelegített sütőbe helyezzük 10-15 percre. Amikor készre sült a hús, kivesszük, és 5-10 percig pihentetjük.\n"
            "A megfőtt burgonyát 2 evőkanál olajon, magas hőfokon lepirítjuk, majd mikor már kapott egy kis piros színt, rádobjuk a cukorborsót, sózzuk, borsozzuk, majd mehet rá 2 gerezd szeletelt fokhagyma, 50 "
            "gramm vaj, fél citrom leve, és további kb. 3 percig pirítjuk. Jöhet rá 2-3 evőkanál tejföl, az ecetes torma, illetve a finomra aprított petrezselyem és snidling.\n"
            "Tálalásnál, ha szeretnénk, adhatunk még hozzá tejfölt. A sertésszűz mellé kínáljuk.",
            self.harvester_class.instructions(),
        )

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://streetkitchen.hu/wp-content/uploads/2021/03/sertesszuz-cukorborsos-ujburgonya-salataval-1.jpg",
            self.harvester_class.image(),
        )
