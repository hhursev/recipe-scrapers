from recipe_scrapers.rezeptwelt import Rezeptwelt
from tests import ScraperTest


class TestRezeptweltScraper(ScraperTest):

    scraper_class = Rezeptwelt

    def test_host(self):
        self.assertEqual("rezeptwelt.de", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Thermomix Rezeptentwicklung", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Nudelsalat", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("sonstige Hauptgerichte", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://de.rc-cdn.community.thermomix.com/recipeimage/mbc1phgz-e2d56-160794-cfcd2-x6yic6yp/69b775cf-693a-443e-b61e-990e025b3ef5/main/nudelsalat.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "100 g Käse",
                "2 Möhren, in Stücken",
                "100 g Weißkohl, in Stücken",
                "1 Paprika, rot, geviertelt",
                "500 g Nudeln, gekocht, z. B.Spiral",
                "50 g Gemüsebrühe",
                "Salz",
                "Pfeffer",
                "300 g Knoblauch, aioli",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        expected = "Käse und Gemüse in den Mixtopf geben, 5 Sek./Stufe 5 zerkleinern (auf das laufende Messer fallen lassen, Stufe 5) und in eine Schüssel umfüllen.\nGekochte Nudeln, Gemüsebrühe und als Salatsauce Knoblauchaioli unterheben, durchziehen lassen und vor dem Servieren abschmecken.\n"
        self.assertEqual(expected, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(4.04, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Deutsch", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Nudelsalat, ein Rezept der Kategorie sonstige Hauptgerichte.",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("de_DE", self.harvester_class.language())
