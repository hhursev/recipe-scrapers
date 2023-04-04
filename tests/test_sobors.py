from recipe_scrapers.sobors import SoBors
from tests import ScraperTest


class TestSoBorsScraper(ScraperTest):

    scraper_class = SoBors

    def test_host(self):
        self.assertEqual("sobors.hu", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://sobors.hu/receptek/piskotatekercs-parizsi-kremmel-recept/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Piskótatekercs párizsi krémmel")

    def test_total_time(self):
        self.assertEqual(105, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://kep.cdn.index.hu/1/0/4789/47897/478976/47897666_b1b9c0144433ad82534842ea54d4500f_wm.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "6 darab tojás",
                "6 evőkanál cukor",
                "6 evőkanál finomliszt",
                "1 dl habtejszín",
                "20 dkg cukor",
                "3 evőkanál kakaó (cukrozatlan)",
                "20 dkg vaj",
                "1 dl mascarpone",
                "1 evőkanál rum",
                "kakaó a szóráshoz",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Piskóta:\n"
            "A tojásokat válasszuk szét, majd a sárgáját keverjük fehéredésig a cukorral.\n"
            "A tojásfehérjét verjük kemény habbá, majd forgassuk a sárgájához, ezután a lisztet szitáljuk hozzá, és óvatosan keverjük egybe a tojásos keverékkel.\n"
            "A piskótát simítsuk sütőpapírral bélelt tepsire (24x18 centiméter), majd toljuk 180 fokosra előmelegített sütőbe, és 10-15 perc alatt süssük készre.\n"
            "A piskótát még melegen tekerjük fel, és tegyük félre.\n"
            "Krém:\n"
            "A habtejszínt öntsük lábasba és melegítsük fel a cukorral együtt, addig, amíg a cukor elolvad. Ezután keverjük hozzá a kakaót is, majd tegyük félre, és hűtsük ki.\n"
            "A kihűlt főzött krémhez keverjük hozzá a vajat, mascarponét és a rumot.\n"
            "A piskótát terítsük ki, és kenjük meg a krémmel, majd tekerjük fel. A rolád tetejét szórjuk meg kakaóval, és tálalásig tartsuk hűtőben.",
            self.harvester_class.instructions(),
        )

    def test_cook_time(self):
        return self.assertEqual(15, self.harvester_class.cook_time())

    def test_prep_time(self):
        return self.assertEqual(90, self.harvester_class.prep_time())

    def test_author(self):
        return self.assertEqual("Botos Claudia", self.harvester_class.author())

    def test_description(self):
        return self.assertEqual(
            "A puha piskóta édes párizsi krémmel töltve készül, melyben a rum zamata is érződik, ettől lesz különleges.",
            self.harvester_class.description(),
        )
