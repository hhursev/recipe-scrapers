from recipe_scrapers.dr import Dr
from tests import ScraperTest


class TestDrMeScraper(ScraperTest):

    scraper_class = Dr

    def test_host(self):
        self.assertEqual("dr.dk", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            self.harvester_class.canonical_url(),
            "https://www.dr.dk/mad/opskrift/millionaires-shortbread",
        )

    def test_title(self):
        self.assertEqual("Millionaires’ Shortbread", self.harvester_class.title())

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Brdr. Price")

    def test_image(self):
        self.assertEqual(
            "https://asset.dr.dk/imagescaler01/https%3A%2F%2Fwww.dr.dk%2Fimages%2Fother%2F2023%2F07%2F06%2Fmillionaires-shortbread-jpg-1597218581.png&w=700",
            self.harvester_class.image(),
        )

    def test_language(self):
        self.assertEqual("da-DK", self.harvester_class.language())

    def test_ingredients(self):
        self.assertEqual(
            [
                "130 g mel",
                "50 g farin",
                "2 tsk. maizena",
                "Et nip salt",
                "120 g smør",
                "1 spsk. koldt vand",
                "1 æggeblomme",
                "1 dåse sød kondenseret mælk",
                "100 g farin",
                "100 g smør",
                "2 spsk. lys sirup",
                "1 tsk. vanilje ekstrakt",
                "Et nip salt",
                "170 g mørk chokolade",
                "1 stor spsk. smør",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        expected_instructions = "\n".join(
            [
                "Opskriften giver cirka 16 styks, afhængig af størrelsen.",
                "I en foodprocessor kommes mel, farin, maizena og salt. Kør til alt er blandet.",
                "Kom smørret ved og kør til det ligner brødkrummer. Tilsæt koldt vand og æggeblomme og kør til dejen lige samler sig.",
                "Kom dejen ud på et melet bord og saml den hurtigt. Kom køkkenfilm omkring den og lad den hvile i køleskabet i en times tid.",
                "Rul den derpå ud på et melet bord og placer den i bunden af en firkantet bageform (24 x 24 cm.) der er foret med bagepapir. Prik dejen med en gaffel og bag den i en 180 grader varm ovn i ca. 20 minutter.",
                "Til karamellen kommes den kondenserede mælk i en gryde sammen med farin, smør, sirup, vanille og salt. Bring massen i kog og lad den koge roligt til den når 110 grader på et sukkertermometer - eller til massen er tyk og gyldenbrun. Hæld karamellem over den stadig lune kagebund.",
                "Lad derpå kagen køle helt af.",
                "Smelt chokoladen i et vandbad sammen med smørret, bland godt og hæld så chokoladen ovenpå karamellen. Jævn ud med en spatel. Sæt kagen på køl.",
                "Tag kagen ud af formen og fjern bagepapiret. Skær kagen i små firkanter som opbevares på køl til de skal serveres.",
            ]
        )

        return self.assertEqual(
            expected_instructions, self.harvester_class.instructions()
        )
