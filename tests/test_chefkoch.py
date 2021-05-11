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
        self.assertEqual(self.harvester_class.title(), "Hackbraten supersaftig")

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://img.chefkoch-cdn.de/rezepte/1170311223132029/bilder/1158321/crop-960x540/hackbraten-supersaftig.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 ½ Semmel(n) , altbacken",
                "2 Gewürzgurke(n)",
                "2 kleine Zwiebel(n)",
                "1 kl. Bund Petersilie",
                "2 EL Zitronensaft",
                "50 g Butter",
                "600 g Hackfleisch , gemischt",
                "2 kleine Ei(er)",
                "125 ml Fleischbrühe",
                "125 ml Sahne",
                "1 EL Crème fraîche",
                "1 TL Paprikapulver , edelsüß",
                "Salz und Pfeffer , schwarzer",
                "Cayennepfeffer",
                "Fett für die Form",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Die Semmeln in Scheiben schneiden und mit Wasser \u00fcbergie\u00dfen, quellen lassen. Gut ausdr\u00fccken. Die Gew\u00fcrzgurken in sehr feine W\u00fcrfel schneiden. Zwiebeln ebenfalls in feine W\u00fcrfel schneiden.\n\n1 EL Butter erhitzen und die Zwiebeln glasig anschwitzen. Petersilie dazugeben. Zwiebel-Petersilienmischung in eine Sch\u00fcssel geben, Semmeln, Gew\u00fcrzgurken, Hackfleisch, Eier und Zitronensaft zuf\u00fcgen. Alles mit Salz, Cayennepfeffer und schwarzem Pfeffer w\u00fcrzen und kr\u00e4ftig durchkneten. \n\nDie restliche Butter schmelzen, eine Form fetten. Den Fleischteig zu einem Laib formen und in die Form legen. Auf der unteren Schiene 30 Minuten (Umluft 180\u00b0C) backen, dabei immer mit der fl\u00fcssigen Butter bestreichen. \n\nDie Fleischbr\u00fche erhitzen und mit der Sahne, der Cr\u00e8me fra\u00eeche und dem Paprikapulver verr\u00fchren. (Wer sehr viel So\u00dfe mag, kann die So\u00dfenmenge einfach verdoppeln). Die So\u00dfe \u00fcber den Hackbraten gie\u00dfen und weitere 10 - 15 Minuten garen. \n\nDazu passen hervorragend Salzkartoffeln.",
            self.harvester_class.instructions(),
        )
