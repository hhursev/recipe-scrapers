from recipe_scrapers.matprat import Matprat
from tests import ScraperTest


class TestMatprat(ScraperTest):

    scraper_class = Matprat

    def test_host(self):
        self.assertEqual("matprat.no", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.matprat.no/oppskrifter/gjester/butter-chicken---indisk-smorkylling/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Butter chicken - indisk smørkylling"
        )

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "Butter%20chicken%20|%20Oppskrift%20-%20MatPrat_files/large.jpeg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 stk kylling (ca. 1300 g)",
                "4 båter hvitløk",
                "½ ss revet frisk ingefær",
                "2 ss sitronsaft",
                "--- Marinade ---",
                "1 dl gresk yoghurt",
                "½ ss chilipulver (helst indisk)",
                "1 ss garam masala",
                "1 ss rapsolje eller sennepsolje",
                "--- Smør- og tomatcurry ---",
                "100 g cashewnøtter",
                "8 stk tomat",
                "2 ss olje",
                "4 båter finhakket hvitløk",
                "½ ss revet frisk ingefær",
                "½ ss chilipulver (helst indisk)",
                "2 stk hel kardemomme",
                "2 ts hel bukkehornkløver",
                "2 ss flytende honning",
                "1 stk grønn chili",
                "2 ss smør",
                "1 dl fløte",
                "½ potte frisk koriander",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            """Fjern skinnet på kyllingen og tørk den godt. Kutt dype snitt i kjøttet på hele kyllingen. Finhakk hvitløk og bland med revet ingefær og sitronsaft, og gni kyllingen godt inn med blandingen. Dryss over litt salt. Sett kaldt i 20 minutter.
Bland sammen chilipulver, garam masala, olje og yoghurt. Tørk kyllingen med litt kjøkkenpapir og gni den godt inn med yoghurtblandingen. Plasser kyllingen på et fat og sett den kaldt i minst 4-6 timer, helst over natten.
Stek kyllingen midt i stekeovnen ved 220 °C, eller grill den til den er gyllenbrun og gjennomstekt, ca. 1 time.
Avkjøl og plukk kjøttet av beina i store biter.
Lag smør- og tomatcurry: Bløtlegg cashewnøtter i litt lunkent vann i minst 30 minutter. Hell av vannet og mos nøttene i hurtigmikser eller med stavmikser. Sett til side.
Del tomater i biter. Varm en sauteringspanne med olje og fres tomater, hvitløk, ingefær, chilipulver, Kardemomme og bukkehornkløver på middels varme til tomatene er helt myke.
Tilsett cashewpuré og bruk stavmikser eller hurtigmikser til å finmose sausen. Sil gjerne sausen gjennom en grov sikt for å få ut rester av skall, hvis du vil ha den ekstra fin.
Ha sausen tilbake i kjelen og la den småkoke i i noen minutter. Smak til med honning, finhakket grønn chili, salt og pepper. Visp inn fløte og romtemperert smør i den varme sausen.
Legg kyllingbitene i sausen og la alt bli gjennomvarmt. Pynt med koriander.""",
            # 'Heat oven to 375°F. Spray bottom only of 13x9-inch pan with cooking spray.\n\nUnroll crescent dough; press in bottom of pan. Bake 12 to 14 minutes or until golden brown and baked through. Remove from oven to cooling rack; cool 20 minutes.\n\nIn medium bowl, beat dry pudding mixes and half-and-half with whisk about 2 minutes or until thick. Spread over cooled bar base.\n\nIn medium microwavable bowl, microwave chocolate chips and whipping cream uncovered on High 1 minute; stir. Microwave 30 seconds; stir until smooth. Carefully spread mixture on top of pudding layer. Refrigerate about 4 hours or until cooled completely.\n\nWhen ready to serve, using a sharp knife and up-and-down sawing motion for cleaner cuts, cut into 6 rows by 4 rows. Store covered in refrigerator.'
            # 'Stir together olive oil, garlic, and salt; toss with tomatoes, and allow to stand for 15 minutes. Preheat oven to 400 degrees F (200 degrees C).\nBrush each pizza crust with some of the tomato marinade. Sprinkle the pizzas evenly with Mozzarella and Fontina cheeses. Arrange tomatoes overtop, then sprinkle with shredded basil, Parmesan, and feta cheese.\nBake in preheated oven until the cheese is bubbly and golden brown, about 10 minutes.\n',
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(8, self.harvester_class.ratings())
