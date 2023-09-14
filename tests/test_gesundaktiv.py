# mypy: allow-untyped-defs

from recipe_scrapers.gesundaktiv import GesundAktiv
from tests import ScraperTest


class TestgesundaktivScraper(ScraperTest):

    scraper_class = GesundAktiv

    def test_host(self):
        self.assertEqual("gesund-aktiv.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual("Süße Spinat-Pancakes", self.harvester_class.title())

    def test_image(self):
        self.assertEqual(
            "https://www.gesund-aktiv.com/sites/default/files/2022-01/rezept_suesse_spinat-pancakes-a.png",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "80 g Spinat",
                "125 g Quark (Schaf)",
                "100 ml Milch (Schaf)",
                "100 g Dinkelmehl",
                "2 Stück Eier",
                "2 Esslöffel Joghurt (Schaf)",
                "50 g Blaubeeren",
                "2 Esslöffel Honig",
                "2 Esslöffel Rapsöl",
                "1 Prise Salz",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "1 Zu Beginn müssen der gefrorene Spinat und die gefrorenen Blaubeeren zum "
                    "Auftauen beiseite gelegt werden. Dies am besten eine Stunde vorher "
                    "erledigen. Dann aus dem aufgetauten Spinat das Wasser herauspressen. "
                    "Anschließend Spinat zusammen mit Milch und Quark zu einer feinen, grünen "
                    "Masse vermixen.",
                    "2 Nun die Eier unter die Spinat-Masse mischen uns salzen. Im Anschluss wird "
                    "das Dinkelmehl hinzugegeben und so lange verrührt bis ein klumpenfreier Teig "
                    "entsteht.",
                    "3 Etwas Rapsöl in einer beschichteten Pfanne auf mittlerer Stufe erhitzen. "
                    "Jeweils eine kleine Kelle Teig in die Pfanne geben. Von beiden Seiten etwas "
                    "anbraten lassen bis kleine Bläschen entstehen und je nach gewünschter Bräune "
                    "immer wieder wenden. Tipp: Mit kleinen, für die Pfanne geeigneten "
                    "Dessertringen lassen sich die Pancakes ganz einfach in Form halten.",
                    "4 Die fertigen Spinat-Pancakes mit zwei Esslöffeln Joghurt und ein wenig "
                    "Honig beträufeln. Anschließend mit den aufgetauten Blaubeeren servieren und "
                    "genießen.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "Tagesstart à la Popeye: Fluffige Spinat-Pfannkuchen "
            "mit süßem Topping aus Joghurt, Honig und Beeren.",
            self.harvester_class.description(),
        )
