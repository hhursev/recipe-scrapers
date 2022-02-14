from recipe_scrapers.valdemarsro import Valdemarsro
from tests import ScraperTest


class TestWoolworthsScraper(ScraperTest):

    scraper_class = Valdemarsro

    def test_host(self):
        self.assertEqual("valdemarsro.dk", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            "Madpandekager",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual("Nem Hverdagsmad,Opskrifter,Opskrifter til børn - Hverdagsfavoritter små børn,Tilbehør Aftensmad,Vegetar", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_cook_time(self):
        self.assertEqual(20, self.harvester_class.cook_time())

    def test_yields(self):
        self.assertEqual("10 stk.", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.valdemarsro.dk/wp-content/2020/10/madpandekager.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                '4 æg',
                '4 dl mælk',
                '1 nip salt',
                '125 g hvedemel',
                '50 g grahamsmel',
                '1 spsk smør, til stegning'
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Pisk æg og mælk sammen med salt, grahamsmel og hvedemel.
            
            Smelt lidt smør eller kom lidt olie på en pande og steg 10 madpandekager en ad gangen, på begge sider, til de er flotte lysebrune.""",
            self.harvester_class.instructions(),
        )

    def test_author(self):
        self.assertEqual("Ann-Christine Hellerup Brandt", self.harvester_class.author())

    def test_description(self):
        self.assertEqual("""Klassiske madpandekager er nemme og lækre til at fylde med alverdens gode sager og kan nydes til både frokost og aftensmad.

Man kan både fylde madpandekager ved bordet ala wraps eller man kan fylde dem med gode sager, rulle dem sammen og komme dem i et fad. Fordel lidt god friskrevet ost over og gratiner dem i ovnen. De er skønne at spise med en salat og dip til.

Jeg deler en masse ekstra tips til min opskrift på madpandekager under opskriften

----------

dejen kan holde sig i køleskab i 2-3 dage. Pisk den blot hurtigt op med et piskeris, så er der klar til endnu en omgang pandekager. Hvis man laver en dobbeltportion, så kan dejen også strækkes til fx to forskellige retter med forskelligt fyld.

Kom alt fra stegte krydrede kyllingestykker, falafler og andre grønne deller i. En krydret omgang hakket oksekød eller bagte rodfrugter skåret i små tern. Drys gerne med lidt ost og server med cremede dips, som fx guacamole eller hummus.

De færdige pandekager kan fryses. Pak dem ind i madpapir og en stor frysepose og lad dem tø langsomt op. Lun dem i en forvarmet ovn ved 125 grader, mellem to tallerkener og gerne med damp, hvis du har en ovn med dampfunktion.""", self.harvester_class.decription())

    def test_language(self):
        self.assertEqual("da", self.harvester_class.language())

    def test_site_name(self):
        self.assertEqual(
            "Valdemarsro", self.harvester_class.site_name()
        )
