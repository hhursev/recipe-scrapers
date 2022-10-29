# mypy: allow-untyped-defs

from recipe_scrapers.weightwatcherspublic import WeightWatchersPublic
from tests import ScraperTest


class TestweightwatchersPublicScraper(ScraperTest):

    scraper_class = WeightWatchersPublic

    # Test-Url:
    # https://www.weightwatchers.com/de/rezept/kartoffelgulasch/562a9b02873e1afb2a3c4c13

    def test_host(self):
        self.assertEqual("www.weightwatchers.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("WeightWatchers", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Kartoffelgulasch")

    def test_category(self):
        self.assertEqual("WeightWatchers", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_cook_time(self):
        self.assertEqual(0, self.harvester_class.cook_time())

    def test_prep_time(self):
        self.assertEqual(40, self.harvester_class.prep_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cmx.weightwatchers.com/assets-proxy/weight-watchers/image/upload/q_auto/h7wo0hbnwcleucj30sbw.jpg?auto=webp",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "800 g Kartoffeln; vorwiegend festkochend",
                "2 Stück Zwiebel/n; mittelgroß",
                "2 Stück Paprika; rot",
                "2 Stück Paprika; grün",
                "1 EL Petersilie; gehackt",
                "2 Stück Paprika; gelb",
                "250 g Tomaten, frisch",
                "4 Stück Wiener Würstchen",
                "2 TL Pflanzenöl, Rapsöl/Sonnenblumenöl",
                "2 EL Tomatenmark",
                "250 ml Gemüsebouillon/Gemüsebrühe, zubereitet; (1 TL Instantpulver)",
                "1 TL Oregano; gehackt",
                "1 TL Paprikapulver",
                "1 Prise(n) Salz/Jodsalz",
                "1 Prise(n) Pfeffer",
                "2 EL Schmand, 24 % Fett",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredientsCount(self):
        self.assertEqual(16, len(self.harvester_class.ingredients()))

    def test_instructions(self):
        self.assertEqual(
            "Kartoffeln und Zwiebeln schälen. Kartoffeln würfeln und Zwiebeln in Streifen schneiden. Paprika waschen, entkernen und in Stücke schneiden. Tomaten waschen und in Spalten schneiden. Würstchen in Scheiben schneiden.\nÖl in einem Topf erhitzen, Kartoffelwürfel und Zwiebelstreifen darin ca. 5 Minuten anbraten. Paprikastücke zufügen, Tomatenmark einrühren und kurz mitbraten. Mit Brühe ablöschen und zugedeckt ca. 15 Minuten garen.\nKartoffelgulasch mit Oregano, Paprikapulver, Salz und Pfeffer würzen. Würstchenscheiben und Tomatenspalten zufügen und weitere ca. 5 Minuten garen. Kartoffelgulasch mit Salz und Pfeffer abschmecken. Mit einem Klecks Schmand und Petersilie bestreut servieren.",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "Das Rezept zaubert ein saftiges, würziges Gericht auf den Tisch und schmeckt garantiert.",
            self.harvester_class.description(),
        )

    def test_difficulty(self):
        self.assertEqual("Leicht", self.harvester_class.difficulty())

    def test_nutrients(self):
        expected_nutrients = {
            "points": "10 bis 13 PersonalPoints",
        }
        self.assertEqual(self.harvester_class.nutrients(), expected_nutrients)
