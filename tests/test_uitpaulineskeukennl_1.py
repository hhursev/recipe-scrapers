# mypy: allow-untyped-defs

from recipe_scrapers.uitpaulineskeukennl import UitPaulinesKeukenNL
from tests import ScraperTest


class TestUitPaulinesKeukenNLScraper(ScraperTest):
    scraper_class = UitPaulinesKeukenNL
    test_file_name = "uitpaulineskeukennl_1"

    def test_host(self):
        self.assertEqual("uitpaulineskeuken.nl", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://uitpaulineskeuken.nl/recept/ravioli-met-salieboter",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Pauline", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Ravioli met salieboter", self.harvester_class.title())

    def test_category(self):
        self.assertEqual(
            "Makkelijke recepten, Pasta recepten, Snelle recepten, Ravioli, Italiaanse recepten, "
            "Notenvrije recepten, Kerst, Vegetarische recepten, Herfst recepten, Lente recepten, "
            "Winter recepten, Zomer recepten, Hoofdgerecht",
            self.harvester_class.category(),
        )

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://uitpaulineskeuken.nl/wp-content/uploads/2016/11/Ravioli-met-salieboter-LR-2-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "500 gr verse ravioli (bijvoorbeeld gevuld met ricotta en spinazie)",
                "100 gr Parmezaanse kaas",
                "75 gr roomboter",
                "10 gr verse salie",
                "1 citroen (biologisch)",
                "Peper en zout",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Kook de ravioli in ruim water met zout. Houd de kooktijd van de verpakking aan.",
                    "Laat de boter smelten in een koekenpan. Wrijf de salieblaadjes voorzichtig in je handen, zodat de "
                    "aroma’s vrijkomen. Voeg de salie bij de boter en voeg naar wens peper en zout toe. Laat dit op "
                    "een laag vuur staan.",
                    "Voeg twee eetlepels pastawater bij de boter, dit zorgt voor een saus. Giet de ravioli af en voeg "
                    "dit bij de boter.",
                    "Voeg de helft van de Parmezaanse kaas toe en zet het vuur iets hoger. Schud de pan heen en weer "
                    "zodat alle zijdes bedekt raken en er een iets gebonden saus ontstaat.",
                    "Verdeel de ravioli met salieboter over vier borden. Garneer de ravioli met citroenrasp en de "
                    "overgebleven Parmezaanse kaas.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(3.4, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Italiaanse recepten", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Ravioli met salieboter: lekker door haar eenvoud. Als je het hebt over fresh & easy dan is "
            "dit een receptje wat bovenaan hoort te staan. Super makkelijk om te maken. Slechts vijf "
            "ingrediënten heb je nodig. Daarom is het extra belangrijk dat die van goede kwaliteit zijn. "
            "Vers gemaakte ravioli, biologische citroen, want alleen daarvan is de rasp een "
            "smaakexplosie, een goede kwaliteit Parmezaanse kaas en verse salie. Veel meer heb je dan "
            "niet nodig!",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("nl-NL", self.harvester_class.language())
