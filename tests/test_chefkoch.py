from recipe_scrapers.chefkoch import Chefkoch
from tests import ScraperTest


class TestChefkochScraper(ScraperTest):

    scraper_class = Chefkoch

    def test_host(self):
        self.assertEqual("chefkoch.de", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.chefkoch.de/rezepte/1170311223132029/Hackbraten-supersaftig.html",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Saftiger Hackbraten im Ofen")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Delphinella")

    def test_description(self):
        self.assertEqual(
            self.harvester_class.description(),
            "Hackbraten supersaftig - klassischer saftiger Hackbraten mit viel Soße. Über 1347 Bewertungen und für lecker befunden. Mit ► Portionsrechner ► Kochbuch ► Video-Tipps!",
        )

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://img.chefkoch-cdn.de/rezepte/1170311223132029/bilder/1508325/crop-960x540/hackbraten-supersaftig.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 ½ Semmel(n) , altbacken",
                "2 Gewürzgurke(n)",
                "2 kleine Zwiebel(n)",
                "1 kl. Bund Petersilie",
                "2 EL Zitronensaft",
                "50 g Butter",
                "600 g Hackfleisch, gemischtes",
                "2 kleine Ei(er)",
                "125 ml Fleischbrühe",
                "125 ml Sahne",
                "1 EL Crème fraîche",
                "1 TL Paprikapulver, edelsüßes",
                "Salz und Pfeffer, schwarzer",
                "Cayennepfeffer",
                "Fett für die Form",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Die Semmeln in Scheiben schneiden und mit Wasser übergießen, quellen lassen. Gut ausdrücken. Die Gewürzgurken in sehr feine Würfel schneiden. Zwiebeln ebenfalls in feine Würfel schneiden.\n\n1 EL Butter erhitzen und die Zwiebeln glasig anschwitzen. Petersilie dazugeben. \n\nZwiebel-Petersilienmischung in eine Schüssel geben. Semmeln, Gewürzgurken, Hackfleisch, Eier und Zitronensaft zufügen. Alles mit Salz, Cayennepfeffer und schwarzem Pfeffer würzen und kräftig durchkneten. \n\nDie restliche Butter schmelzen, eine Form fetten. Den Fleischteig zu einem Laib formen und in die Form legen. Auf der unteren Schiene 30 Minuten (Umluft 180 °C) backen, dabei immer mit der flüssigen Butter bestreichen. \n\nDie Fleischbrühe erhitzen und mit der Sahne, der Crème fraîche und dem Paprikapulver verrühren. (wer sehr viel Soße mag, kann die Soßenmenge einfach verdoppeln). Die Soße über den Hackbraten gießen und weitere 10 - 15 Minuten garen. \n\nDazu passen hervorragend Salzkartoffeln.",
            self.harvester_class.instructions(),
        )

    def test_total_time(self):
        return self.assertEqual(85.0, self.harvester_class.total_time())

    def test_cook_time(self):
        return self.assertEqual(45.0, self.harvester_class.cook_time())

    def test_prep_time(self):
        return self.assertEqual(40.0, self.harvester_class.prep_time())
