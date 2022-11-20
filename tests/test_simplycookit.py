# mypy: disallow_untyped_defs=False

from recipe_scrapers.simplycookit import SimplyCookit
from tests import ScraperTest


class TestSimplyCookitScraper(ScraperTest):
    scraper_class = SimplyCookit

    def test_host(self):
        self.assertEqual("simply-cookit.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("simply-cookit.com", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Gnocchi mit Zuckerschoten und getrockneten Tomaten in Parmesansauce",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual("Vegetarisch", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(21, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.simply-cookit.com/sites/default/files/styles/square/public/assets/image/2021/03/gnocchi-mit-zuckerschoten-und-getrockneten-tomaten-in-parmesansosse_portrait.jpg?h=526df0cf&itok=wxxX6IM7",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "90 g Parmesan",
                "1 Zwiebel",
                "1 Knoblauchzehe",
                "0,5 TL Salz",
                "30 g Butter",
                "3 TL Weizenmehl, Type 405",
                "150 ml Gemüsefond",
                "250 ml Milch",
                "0,25 TL schwarzer Pfeffer, aus der Mühle",
                "800 g Gnocchi, aus dem Kühlregal",
                "100 g Tomaten, getrocknet, in Öl",
                "200 g Zuckerschoten",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Das Universalmesser einsetzen. Den Parmesan in ca. 3 cm großen Stücken in den Topf einwiegen. Den Deckel schließen, den Messbecher einsetzen und den Parmesan (Universalmesser | Stufe 18 | 20 Sek.) fein zerkleinern. Das Universalmesser entnehmen und das Lebensmittel mit dem Spatel abstreifen. Den Parmesan umfüllen und beiseitestellen.\nDas Universalmesser einsetzen. Die Zwiebel schälen, halbieren und in den Topf geben. Die Knoblauchzehe schälen und zugeben. Den Deckel schließen und die Zutaten (Universalmesser | Stufe 14 | 10 Sek.) zerkleinern. Das Universalmesser entnehmen und das Lebensmittel mit dem Spatel abstreifen. Die Zutaten mit dem Spatel nach unten schieben.\nIn einem Kochtopf reichlich Salzwasser zum Kochen bringen. In der Zwischenzeit den Zwillings-Rührbesen einsetzen. Die Butter in den Topf einwiegen.\nDen Deckel schließen, den Messbecher entnehmen und die Zwiebeln (Zwillings-Rührbesen | Stufe 3 | 120 °C | 4 Min.) andünsten. Das Mehl zugeben, den Deckel schließen und die Zutaten (Zwillings-Rührbesen | Stufe 3 | 120 °C | 3 Min.) anschwitzen. Den Gemüsefond und die Milch einwiegen sowie Salz und Pfeffer zugeben. Den Deckel schließen, den Messbecher einsetzen und die Zutaten (Zwillings-Rührbesen | Stufe 4 | 95 °C | 6 Min.) köcheln lassen.\nDie Gnocchi im Kochtopf nach Packungsangabe garen und anschließend abgießen. In der Zwischenzeit die getrockneten Tomaten in ca. 3 mm feine Stücke schneiden und in den Topf einwiegen. 60 g Parmesan einwiegen, den Deckel schließen und die Zutaten (Zwillings-Rührbesen | Stufe 4 | 100 °C | 1 Min.) vermengen. Den Zwillings-Rührbesen entnehmen. Die Zuckerschoten in ca. 2 cm große Stücke schneiden, einwiegen und mit dem Spatel unterheben.\nDie Sauce über die Gnocchi geben und mit dem restlichem Parmesan bestreut servieren.",
            self.harvester_class.instructions(),
        )

    def test_cuisine(self):
        self.assertEqual("Italien", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Ein besonders schnell zubereitetes Gericht - mit feiner Tomaten-Parmesansauce!",
            self.harvester_class.description(),
        )
