from recipe_scrapers.sallysblog import SallysBlog
from tests import ScraperTest


class TestSallysBlogScraper(ScraperTest):

    scraper_class = SallysBlog

    def test_host(self):
        self.assertEqual("sallys-blog.de", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://sallys-blog.de/chili-con-carne-vom-grill-mit-brotsticks-und-gerostetem-knoblauch",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Chili con Carne vom Grill mit Brotsticks und geröstetem Knoblauch",
        )

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 Person", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://sallys-blog.de/media/image/21/2f/04/sallly-grill-chili-con-carne-rezept_1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 Sally Brotvormischung #6",
                "21 g Hefe",
                "480 g Wasser",
                "50 g Hartweizengrieß",
                "2 Zwiebeln",
                "2 Knoblauchzehen",
                "2 rote Paprikaschoten",
                "1 Chilischote",
                "50 g Olivenöl",
                "800 g Hackfleisch (Rind)",
                "1200 g Tomaten (Dose)",
                "700 g Wasser",
                "0,25 TL Zimt",
                "2 TL Kreuzkümmel",
                "2 TL Salz",
                "1 TL Pfeffer",
                "800 g Kidneybohnen (Dose)",
                "600 g Mais (Dose)",
                "40 g Zartbitterschokolade",
                "3 Knollen Knoblauch",
                "3 Esslöffel Olivenöl",
                "0,25 TL Salz",
                "1 Pr. Pfeffer",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Heize den Grill auf 200°C ein.\nVerrühre die Brotmischung nach Packungsanleitung mit Hefe und Wasser in etwa 10 Minuten zu einem geschmeidigen Teig und lasse ihn abgedeckt aufgehen.\nTipp: Du kannst auch eine andere Brotsorte wählen (Wassermenge beachten) oder statt einer fertigen Brotvormischung auch ein anderes Brot-Rezept aus meinem Blog zubereiten.\nSchäle die Zwiebeln und Knoblauchzehen und schneide sie in feine Würfel. Schneide auch die Paprika- und Chilischoten in kleine Würfel. Stelle einen Gusseisentopf auf einen Rost über die Flamme des Grills und erhitze darin das Olivenöl. Brate das Hackfleisch darin krümelig an, füge die Zwiebel-, Knoblauch-, Paprika- und Chiliwürfel hinzu und brate sie für etwa 5 Minuten mit an. Lösche alles mit den Tomaten aus der Dose und dem Wasser ab und füge die Gewürze, Kidneybohnen und Mais hinzu. Lasse das Chili etwa 1 Stunde bei indirekter Hitze köcheln.\nGib die Knoblauchknollen ungeschält in einen Mini-Gusseisentopf, füge das Olivenöl hinzu und stelle den Topf mit verschlossenem Deckel mit auf den Grill, während das Chili köchelt, so entsteht ein einzigartiges Aroma. Entferne nach einer Stunde Garzeit die Schale des Knoblauchs, zerdrücke ihn und würze ihn mit Salz und Pfeffer.\nGib den Hartweizengrieß auf ein Schneidebrett oder deine Arbeitsfläche. Reiße etwa golfballgroße Stücke vom Teig ab und rolle sie im Grieß jeweils zu einem langen Strang. Drücke sie zu Brotsticks flach und backe sie im Grill, auf einem Pizzastein bei 180°C für etwa 10 Minuten, wende sie hierbei einmal.\nTipp: Du kannst die Brotsticks auch in einer Pfanne ohne Fett oder im Backofen backen.\nRühre die Schokolade ein, schmecke das Chili ab und serviere es mit den Brotsticks. Nach Belieben kannst du noch Sauerrahm dazu servieren. Viel Spaß beim Nachmachen, eure Sally!\nTipp: Wenn du es etwas schärfer möchtest kannst du mehr Chilischoten oder etwas Cayennepfeffer hinzugeben.\nZubereitung auf dem Herd Erhitze das Olivenöl in einem Gusseisentopf auf dem Herd, brate das Hackfleisch und alle gewürfelten Zutaten darin an, lösche das Chili mit Tomaten und Wasser ab, füge die restlichen Zutaten hinzu und lasse es 1 Stunde auf dem Herd köcheln oder im Backofen schmoren.",
            self.harvester_class.instructions(),
        )
