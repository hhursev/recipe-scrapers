from recipe_scrapers.sallysblog import SallysBlog
from tests import ScraperTest


class TestSallysBlogScraper(ScraperTest):
    scraper_class = SallysBlog

    def test_host(self):
        self.assertEqual("sallys-blog.de", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://sallys-blog.de/rezepte/20-minuten-pasta-brokkoli-schinken-nudeln",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "20 Minuten Pasta / Brokkoli-Schinken-Nudeln / Sally und Murat kochen",
        )

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            self.harvester_class.image(),
            "https://img2.storyblok.com/950x650/f/130848/799x533/a857be2418/1840_27760_sally-brokkoli-schinken-nudeln-rezept_6.jpg",
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 Zwiebel",
                "1 Knoblauchzehe",
                "20 g Butter",
                "20 g Mehl",
                "300 g Gemüsebrühe",
                "200 g Milch",
                "500 g Brokkoli",
                "200 g Gorgonzola",
                "50 g Parmesan",
                "0,25 TL Salz",
                "0,25 TL Pfeffer",
                "100 g Schinken (z. B. Pute)",
                "150 g Erbsen (TK)",
                "500 g Nudeln (z. B. Orechiette)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Schäle die Zwiebel und Knoblauchzehe und schneide sie fein. Erhitze die Butter in einer großen Pfanne und gib das Mehl hinzu. Brate es etwa 1 Minute an. Füge die Knoblauch- und Zwiebelwürfel hinzu und brate sie auch etwa 2-3 Minuten an. Lasse in der Zwischenzeit Wasser für die Nudeln aufkochen und salze es gut.",
                    "Lösche die Mehlschwitze mit der Gemüsebrühe und Milch ab und lasse die Soße aufkochen. Teile die Röschen des Brokkolis auf, schäle und schneide den Strunk fein. Gib die Strunkwürfel und die beiden Käsesorten grob zerkleinert in die Soße, würze sie mit Salz und Pfeffer und lasse sie mit Deckel etwa 2 Minuten köcheln.",
                    "Schneide den Schinken in Würfel und gib ihn mit den Brokkoliröschen und den Erbsen in die Soße und lasse den Brokkoli etwa 3-4 Minuten in der Soße köcheln. Gib etwa 1 Schöpfkelle Nudelwasser in die Soße, gieße die Nudeln ab und vermische sie mit der Soße. Fertig ist das schnelle Nudelgericht. Viel Spaß beim Nachkochen, eure Sally!",
                ]
            ),
            self.harvester_class.instructions(),
        )
