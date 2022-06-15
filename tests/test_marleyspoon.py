import responses

from recipe_scrapers.marleyspoon import MarleySpoon

from tests import ScraperTest


class TestMarleySpoonScraper(ScraperTest):

    scraper_class = MarleySpoon

    @property
    def expected_requests(self):
        yield responses.GET, "https://marleyspoon.de/menu/113813-glasierte-veggie-burger-mit-roestkartoffeln-und-apfel-gurken-salat", "tests/test_data/marleyspoon.testhtml"
        yield responses.GET, "https://api.marleyspoon.com/recipes/113813?brand=ms&country=de&product_type=web", "tests/test_data/marleyspoon.testjson"

    def test__get_json_params(self):
        self.assertEqual(
            (
                "https://api.marleyspoon.com/recipes/113813?brand=ms&country=de&product_type=web",
                "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJtcyIsImNvdW50cnkiOiJkZSIsImJyYW5kIjoibXMiLCJ0cyI6MTY1Mzg4ODg3NiwicmFuZG9tX2lkIjoiMGY4YjZkIn0.quv6_xQk0EjwKmHn7u_CltqMkPuNen-N6kncGHTjcbg",
            ),
            self.harvester_class._get_json_params(),
        )

    def test_host(self):
        self.assertEqual("marleyspoon.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Glasierte Veggie-Burger mit Röstkartoffeln und Apfel-Gurken-Salat",
        )

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://marleyspoon.com/media/recipes/113813/main_photos/large/veggie_burger_mit_ahornsirupglasur-52496098c98adf7b4a82b8b38fdf14dc.jpeg",
            self.harvester_class.image(),
        )

    def test_nutrients(self):
        self.assertEqual(
            {
                "calories": "1143kcal",
                "carbs": "103.8g",
                "fat": "68.0g",
                "proteins": "27.8g",
            },
            self.harvester_class.nutrients(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "25g Erdnüsse, geröstet & gesalzen",
                "2 vegane Burgerpattys",
                "2 Burgerbrötchen mit Sesam",
                "1 Päckchen Sriracha-Sauce",
                "25ml Sojasauce",
                "2 Stangensellerie",
                "1 Minigurke",
                "1 Apfel",
                "1 Packung festkochende Kartoffeln",
                "2EL Mayonnaise",
                "2½TL Honig",
                "½TL Senf",
                "Salz",
                "Zucker",
                "Olivenöl",
                "Essig",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Den Backofen auf 240°C (220°C Umluft) vorheizen. Die Kartoffeln samt Schale in ca. 1cm breite Spalten schneiden und auf einem mit Backpapier ausgelegten Backblech mit 1EL Olivenöl sowie 1/2TL Salz vermengen. Die Kartoffeln im Ofen auf mittlerer Schiene 20–25Min. goldbraun rösten, zwischendurch einmal wenden.\n2EL Olivenöl, 1EL hellen Essig, 1/2TL Senf, 1/2TL Honig und 1 kräftige Prise Salz zu einem Dressing verrühren. Den Apfel vierteln, entkernen und in ca. 1cm große Würfel schneiden. Die 1/2 der Gurke ebenfalls in ca. 1cm große Würfel schneiden. Den Sellerie in dünne Scheiben schneiden. Die Apfel- und Gurkenwürfel und den Sellerie mit dem Dressing vermengen.\nDie restliche Gurke mit einem Sparschäler in breite Streifen schneiden. 1EL hellen Essig, 1TL Zucker und 1 kräftigen Prise Salz verrühren, bis sich Zucker und Salz aufgelöst haben. Mit den Gurkenstreifen vermengen und beiseitestellen.\nDie Sojasauce mit 2TL Honig und 1EL hellem Essig verrühren. Getrennt davon die Sriracha-Sauce mit 2EL Mayonnaise verrühren. Tipp: Wenn Kinder mitessen, ggf. weniger Sriracha-Sauce verwenden oder diese separat servieren. Die Burgerbrötchen auf einem Backrost 2–3Min. im Ofen aufbacken.\nDie Pattys in einer mittelgroßen Pfanne mit 1EL Olivenöl bei mittlerer Hitze auf jeder Seite 1–2Min. goldbraun braten. Die Soja-Würzsauce dazugeben, 1–2Min. köcheln lassen und die Pattys in der Glasur wenden, sodass sie vollständig damit bedeckt sind.\nDie Brötchen aufschneiden, mit dem Dip bestreichen und nach Geschmack mit den Pattys, den Gurkenstreifen und je ca. 1EL Apfel-Gurken-Salat belegen. Den restlichen Salat mit den Erdnüssen bestreuen und zu den Burgern, den Röstkartoffeln und ggf. übrigen Gurkenstreifen servieren. Ggf. übrigen Dip oder mehr Mayonnaise nach Geschmack dazu reichen.",
            self.harvester_class.instructions(),
        )

    def test_author(self):
        self.assertEqual("Lieke", self.harvester_class.author())

    def test_description(self):
        self.assertEqual(
            "Heute gibt’s Burgergenuss auf hohem Niveau: Die saftigen Pattys werden in einer würzig-süßen Glasur gebraten, ehe sie mit eingelegten Gurkenstreifen, pikantem Sriracha-Dip und knackigem Salat mit frisch-fruchtigem Apfel und würzigem Sellerie das Burgerbrötchen zieren. Der Salat fungiert übrigens – schick mit Erdnüssen bestreut – neben knusprigen Ofenkartoffeln auch noch zusätzlich als Beilage. Lass es dir schmecken!",
            self.harvester_class.description(),
        )

    def test_links(self):
        expected = "https://marleyspoon.com/media/pdf/recipe_cards/113813/R-113813_-_Glasierte_Veggie-Burger-CV.pdf"
        self.assertTrue(
            any(link["href"] == expected for link in self.harvester_class.links())
        )

    def test_language(self):
        self.assertEqual("de-DE", self.harvester_class.language())
