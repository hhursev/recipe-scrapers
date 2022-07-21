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
            "https://streetkitchen.hu/hust-hussal/kapros-tejfolos-sajtos-csirke-rizzsel/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Kapros tejfölös sajtos csirke rizzsel"
        )

    def test_total_time(self):
        self.assertEqual(None, self.harvester_class.total_time())

    def test_ingredients(self):
        self.assertListEqual(
            [
                "250 g csirkemell",
                "só, bors",
                "2 db tojás",
                "100 g liszt",
                "150 g trappista sajt",
                "300 g tejföl",
                "50 ml víz",
                "1 csokor friss kapor",
                "2 gerezd fokhagyma",
                "100 g rizs",
                "200 ml meleg víz",
                "1 tk só",
                "1 ek olaj",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "A csirkemellet felszeleteljük, sózzuk, borsozzuk és bebundázzuk: először lisztbe, majd tojásba és a végén zsemlemorzsa helyett, finomra reszelt trappista sajtba forgatjuk és egy kb. 20×10-es tepsibe rakjuk.\n"
            + "A tejfölt kikeverjük a vízzel, sózzuk, borsozzuk, belereszeljük a fokhagymát, megszórjuk a felaprított kaporral és alaposan elkeverjük. Ráöntjük a húsra és 180 fokra előmelegített sütőben 15 percig sütjük. Ezután felvesszük 200 fokra a sütő hőmérsékletét és addig sütjük amíg kicsit aranybarna nem lesz a teteje.\n"
            + "A rizst az olajon 2 percig pirítjuk. Felöntjük forró vízzel, megsózzukk és lefedve felforraljuk. Ezután alacsony lángon készre főzzük. A végén a fedőt még 5 percig rajta hagyjuk. A tejfölös sajtos csirkét  a rizzsel tálaljuk.",
            self.harvester_class.instructions(),
        )

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://485744-1530733-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2019/03/kapros-tejfolos-csirke-talalasa.jpg",
            self.harvester_class.image(),
        )
