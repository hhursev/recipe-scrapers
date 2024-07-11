import responses

from recipe_scrapers.monsieurcuisine import MonsieurCuisine
from tests.legacy import ScraperTest


class TestMonsieurCuisineScraper(ScraperTest):
    scraper_class = MonsieurCuisine

    @classmethod
    def expected_requests(cls):
        yield responses.GET, "https://www.monsieur-cuisine.com/de/recipe/paprika-nudel-auflauf-mit-hackfleisch", "tests/legacy/test_data/monsieurcuisine.testhtml"
        expected_headers = {"Accept-Language": "de-DE", "Device-Type": "web"}
        yield responses.GET, "https://mc-api.tecpal.com/api/v2/recipes/1741327", "tests/legacy/test_data/monsieurcuisine.testjson", expected_headers

    def test_host(self):
        self.assertEqual("monsieur-cuisine.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Monsieur Cuisine Official", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Paprika-Nudel-Auflauf mit Hackfleisch", self.harvester_class.title()
        )

    def test_prep_time(self):
        self.assertEqual(70, self.harvester_class.prep_time())

    def test_cook_time(self):
        self.assertEqual(0, self.harvester_class.cook_time())

    def test_total_time(self):
        self.assertEqual(70, self.harvester_class.total_time())

    def test_language(self):
        self.assertEqual("de-DE", self.harvester_class.language())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://mc-web-content-cdn.tecpal.com/wp-content/uploads/2022/08/29214717/paprika-nudelauflauf-mit-hackfleisch-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "20 g Olivenöl",
                "400 g Fusilli",
                "200 g Emmentaler am Stück (45 % Fett)",
                "400 g Hackfleisch, gemischt",
                "85 g Zwiebeln",
                "1 Stück Knoblauchzehen",
                "155 g Paprikaschoten, rot",
                "155 g Paprikaschoten, gelb",
                "20 g Tomatenmark",
                "1 Tl Paprikapulver, edelsüß",
                "1/2 Tl Salz",
                "1/2 Tl Pfeffer, schwarz, gemahlen",
                "200 g Sahne (30 % Fett)",
                "800 g Tomaten, stückig aus der Dose/Glas",
                "10 g Gemüse-Gewürzpaste",
                "2 Tl Kräuter, getrocknet nach Wahl",
                "250 g Erbsen (TK)",
                "1 Stück Auflaufform (20 x 30 cm)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "1. Den Backofen auf 200 °C Ober-/Unterhitze vorheizen und eine Auflaufform mit etwas Öl einfetten. Die Nudeln nach Packungsangabe bissfest garen und abtropfen lassen.\n2. Emmentaler, in Stücken, in den Mixbehälter einwiegen, 12 Sek. | Stufe 8 zerkleinern und umfüllen.\n3. Zwiebel halbieren und mit Knoblauch in den Mixbehälter geben, 5 Sek. | Stufe 8 zerkleinern und mit dem Spatel nach unten schieben. Olivenöl zufügen, ohne Messbecher 2 Min. | Anbraten andünsten. Hackfleisch zugeben, 4 Min. | Anbraten andünsten. Paprikaschoten würfeln und in den Mixbehälter geben. Tomatenmark und Paprikapulver hinzufügen, einmal mit dem Spatel durchrühren und weitere 3 Min. | Anbraten andünsten.\n4. Salz, Pfeffer, Sahne, stückige Tomaten, 1 TL Gemüse-Gewürzpaste sowie Kräuter hinzufügen, den Messbecher einsetzen 10 Min. | Linkslauf | Stufe 1 | 100 °C aufkochen.\n5. Erbsen und Nudeln in die Auflaufform geben. Die Hackmischung dazugeben und mit dem Spatel vermengen. Den Auflauf mit Käse bestreuen und im vorgeheizten Backofen 30 Min. backen. Portionsweise auf Teller verteilen und servieren.\nTIPP: Für eine vegane Variante des Auflaufs mit pflanzlichem Hack bereitet die vegane Hackfleisch-Alternative zunächst nach Packungsanleitung vor, so dass ihr 400 g Hackmasse zur Verfügung habt. In Schritt 3 anstelle des Hackfleischs die pflanzliche Alternative zugeben. In Schritt 4 könnt ihr statt Sahne 200 g Soja-Cuisine an die Tomatensoße geben.",
            self.harvester_class.instructions(),
        )

    def test_instructions_list(self):
        self.assertEqual(
            [
                "1. Den Backofen auf 200 °C Ober-/Unterhitze vorheizen und eine Auflaufform mit etwas Öl einfetten. Die Nudeln nach Packungsangabe bissfest garen und abtropfen lassen.",
                "2. Emmentaler, in Stücken, in den Mixbehälter einwiegen, 12 Sek. | Stufe 8 zerkleinern und umfüllen.",
                "3. Zwiebel halbieren und mit Knoblauch in den Mixbehälter geben, 5 Sek. | Stufe 8 zerkleinern und mit dem Spatel nach unten schieben. Olivenöl zufügen, ohne Messbecher 2 Min. | Anbraten andünsten. Hackfleisch zugeben, 4 Min. | Anbraten andünsten. Paprikaschoten würfeln und in den Mixbehälter geben. Tomatenmark und Paprikapulver hinzufügen, einmal mit dem Spatel durchrühren und weitere 3 Min. | Anbraten andünsten.",
                "4. Salz, Pfeffer, Sahne, stückige Tomaten, 1 TL Gemüse-Gewürzpaste sowie Kräuter hinzufügen, den Messbecher einsetzen 10 Min. | Linkslauf | Stufe 1 | 100 °C aufkochen.",
                "5. Erbsen und Nudeln in die Auflaufform geben. Die Hackmischung dazugeben und mit dem Spatel vermengen. Den Auflauf mit Käse bestreuen und im vorgeheizten Backofen 30 Min. backen. Portionsweise auf Teller verteilen und servieren.",
                "TIPP: Für eine vegane Variante des Auflaufs mit pflanzlichem Hack bereitet die vegane Hackfleisch-Alternative zunächst nach Packungsanleitung vor, so dass ihr 400 g Hackmasse zur Verfügung habt. In Schritt 3 anstelle des Hackfleischs die pflanzliche Alternative zugeben. In Schritt 4 könnt ihr statt Sahne 200 g Soja-Cuisine an die Tomatensoße geben.",
            ],
            self.harvester_class.instructions_list(),
        )

    def test_ratings(self):
        self.assertEqual(4.5, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_site_name(self):
        self.assertEqual("Monsieur Cuisine", self.harvester_class.site_name())

    def test_category(self):
        self.assertEqual(
            "Snacks, Backen, Abendessen, ZauberTopf", self.harvester_class.category()
        )

    def test_nutrients(self):
        expected_nutrients = {
            "calories": "873 kcal",
            "carbohydrateContent": "56 g",
            "fatContent": "54 g",
            "proteinContent": "44 g",
        }
        self.assertEqual(expected_nutrients, self.harvester_class.nutrients())
