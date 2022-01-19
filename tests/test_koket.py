from recipe_scrapers.koket import Koket
from tests import ScraperTest


class TestKoketScraper(ScraperTest):

    scraper_class = Koket

    def test_host(self):
        self.assertEqual("koket.se", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Agnes Fredriksson", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Blommande äpple med salt kolasås", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://img.koket.se/standard-mega/blommande-apple-med-salt-kolasas.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):

        json_data = [
            {
                "id": None,
                "name": "Blommande äpple",
                "plural": None,
                "type": "header",
                "preparation": None,
                "comment": None,
                "alternative_amount": None,
                "unit": None,
                "amount_info": None,
            },
            {
                "id": 9515,
                "name": "äpple",
                "plural": "äpplen",
                "type": "ingredient",
                "preparation": None,
                "comment": "fast sort",
                "alternative_amount": None,
                "unit": None,
                "amount_info": {
                    "to": None,
                    "from": 4,
                    "approximate": None,
                    "optional": None,
                },
            },
            {
                "id": 9873,
                "name": "gräddkola",
                "plural": "gräddkolor",
                "type": "ingredient",
                "preparation": None,
                "comment": "Werthers",
                "alternative_amount": None,
                "unit": None,
                "amount_info": {
                    "to": None,
                    "from": 4,
                    "approximate": None,
                    "optional": None,
                },
            },
            {
                "id": 10709,
                "name": "smör",
                "plural": None,
                "type": "ingredient",
                "preparation": None,
                "comment": None,
                "alternative_amount": None,
                "unit": "g",
                "amount_info": {
                    "to": None,
                    "from": 50,
                    "approximate": None,
                    "optional": None,
                },
            },
            {
                "id": 10658,
                "name": "salt",
                "plural": None,
                "type": "ingredient",
                "preparation": None,
                "comment": None,
                "alternative_amount": None,
                "unit": "krm",
                "amount_info": {
                    "to": None,
                    "from": 1,
                    "approximate": True,
                    "optional": None,
                },
            },
            {
                "id": 10290,
                "name": "malen kanel",
                "plural": None,
                "type": "ingredient",
                "preparation": None,
                "comment": None,
                "alternative_amount": None,
                "unit": "tsk",
                "amount_info": {
                    "to": None,
                    "from": 2,
                    "approximate": None,
                    "optional": None,
                },
            },
            {
                "id": 10620,
                "name": "rörsocker",
                "plural": None,
                "type": "ingredient",
                "preparation": None,
                "comment": None,
                "alternative_amount": None,
                "unit": "msk",
                "amount_info": {
                    "to": None,
                    "from": 4,
                    "approximate": None,
                    "optional": None,
                },
            },
            {
                "id": 10878,
                "name": "valnötter",
                "plural": None,
                "type": "ingredient",
                "preparation": None,
                "comment": None,
                "alternative_amount": None,
                "unit": None,
                "amount_info": {
                    "to": None,
                    "from": 10,
                    "approximate": True,
                    "optional": None,
                },
            },
            {
                "id": 10882,
                "name": "vaniljglass",
                "plural": None,
                "type": "ingredient",
                "preparation": None,
                "comment": None,
                "alternative_amount": None,
                "unit": None,
                "amount_info": None,
            },
            {
                "id": None,
                "name": "Kolasås",
                "plural": None,
                "type": "header",
                "preparation": None,
                "comment": None,
                "alternative_amount": None,
                "unit": None,
                "amount_info": None,
            },
            {
                "id": 10919,
                "name": "vispgrädde",
                "plural": None,
                "type": "ingredient",
                "preparation": None,
                "comment": None,
                "alternative_amount": None,
                "unit": "dl",
                "amount_info": {
                    "to": None,
                    "from": 2.5,
                    "approximate": None,
                    "optional": None,
                },
            },
            {
                "id": 10767,
                "name": "strösocker",
                "plural": None,
                "type": "ingredient",
                "preparation": None,
                "comment": None,
                "alternative_amount": None,
                "unit": "msk",
                "amount_info": {
                    "to": None,
                    "from": 3,
                    "approximate": None,
                    "optional": None,
                },
            },
            {
                "id": 10692,
                "name": "sirap",
                "plural": None,
                "type": "ingredient",
                "preparation": None,
                "comment": None,
                "alternative_amount": None,
                "unit": "dl",
                "amount_info": {
                    "to": None,
                    "from": 0.5,
                    "approximate": None,
                    "optional": None,
                },
            },
            {
                "id": 10658,
                "name": "salt",
                "plural": None,
                "type": "ingredient",
                "preparation": None,
                "comment": None,
                "alternative_amount": None,
                "unit": "tsk",
                "amount_info": {
                    "to": None,
                    "from": 1,
                    "approximate": None,
                    "optional": None,
                },
            },
            {
                "id": 10709,
                "name": "smör",
                "plural": None,
                "type": "ingredient",
                "preparation": None,
                "comment": None,
                "alternative_amount": None,
                "unit": "msk",
                "amount_info": {
                    "to": None,
                    "from": 1,
                    "approximate": None,
                    "optional": None,
                },
            },
        ]
        self.assertEqual(
            [str(json_element) for json_element in json_data],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        json_data = [
            {"type": "header", "name": "Blommande äpplen"},
            {"type": "instruction", "name": "\nSätt ugnen på 220 grader."},
            {
                "type": "instruction",
                "name": "Skär av toppen på äpplena och gröp ur kärnhuset uppifrån, utan att göra hål i botten. Skär två cirklar runt hålet.",
            },
            {
                "type": "instruction",
                "name": "Lägg äpplet upp och ner och skär snitt uppifrån och ner. ",
            },
            {
                "type": "instruction",
                "name": "Lägg äpplena i en ugnsfast form med botten neråt.",
            },
            {"type": "instruction", "name": "Lägg i en kola i varje äpple."},
            {
                "type": "instruction",
                "name": "Smält smöret och blanda ihop med salt, kanel och rörsocker.",
            },
            {
                "type": "instruction",
                "name": "Pensla äpplena med smörblandningen och sätt in i ugnen. Efter ca 20 minuter är de klara och har slagit ut som en blomma.",
            },
            {
                "type": "instruction",
                "name": "Under tiden så grovhacka nötterna och rosta i en torr panna tillsammans med salt. Det går fort så ha koll! ",
            },
            {
                "type": "instruction",
                "name": "Servera de varma äpplena med en kula vaniljglass, kolasås (se recept nedan) och strö över de rostade nötterna.",
            },
            {"type": "header", "name": "Kolsås"},
            {"type": "instruction", "name": "Blanda alla ingredienser i en kastrull."},
            {
                "type": "instruction",
                "name": "Låt koka under omrörning tills den har en gyllene färg.",
            },
            {
                "type": "instruction",
                "name": "Låt den svalna lite och servera!\xa0Förvara inte i kylen. Då stelnar den.",
            },
        ]

        self.assertEqual(
            [str(json_element) for json_element in json_data],
            self.harvester_class.instructions(),
        )

        def test_ratings(self):
            rating_dict = self.harvester_class.ratings()
            self.assertEqual(
                [4.7, 14], [rating_dict["rating_value"], rating_dict["rating_count"]]
            )
