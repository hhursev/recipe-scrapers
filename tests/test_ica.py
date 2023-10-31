from recipe_scrapers.ica import Ica
from tests import ScraperTest


class TestIcaScraper(ScraperTest):
    scraper_class = Ica

    def test_host(self):
        self.assertEqual("ica.se", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.ica.se/recept/lysande-gul-fiskgryta-1677/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("ICA Köket", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Lysande gul fiskgryta", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Huvudrätt,Middag", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://assets.icanet.se/t_ICAseAbsoluteUrl/imagevaultfiles/id_243155/cf_259/lysande_gul_fiskgryta.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "400 g torskfilé, sej eller hoki",
                "300 g laxfilé",
                "1/2 purjolök (1/2 purjolök motsvarar ca 150 g)",
                "1/2 gul lök",
                "1 msk smör eller olivolja",
                "1 vitlöksklyfta",
                "1 1/2 tsk tomatpuré",
                "1 tsk torkad timjan",
                "1 tsk torkad basilika",
                "2 1/2 dl torrt vitt vin",
                "1 1/2 fiskbuljongtärning",
                "2 - 2 1/2 dl Oatly iMat eller vispgrädde",
                "1 dl Oatly iMat Fraiche eller crème fraiche",
                "2 dl vatten",
                "1 pkt saffran (à 0,5 g)",
                "1 tsk salt",
                "300 g räkor med skal",
                "1 burk musslor (à 150 g)",
                "ev. bröd och vitlöksmajonnäs",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Tina fisken (om fryst används). Skölj, ansa och strimla purjon. Skala och hacka löken.\n"
            "Smält smöret i en stor gryta eller tjockbottnad kastrull. Fräs löken och purjolöken (spara lite till servering) ett par minuter tills de blivit glansiga och genomskinliga. Pressa i vitlök. Rör ner tomatpuré, timjan och basilika. Låt detta fräsa med en kort stund.\n"
            "Tillsätt vin och buljongtärning. Koka ett par minuter. Rör ner grädde, fraiche, vatten och saffran. Sjud i 15 minuter. Smaka av med salt.\n"
            "Skär fisken i munsbitar, lägg i grytan och sjud i ytterligare 7 minuter.\n"
            "Skala räkorna. Tillsätt dem och de avrunna musslorna. Toppa soppan med purjolöksstrimlor.\n"
            "Serveringsförslag: Hetta upp och servera genast, gärna med bröd och vitlöksmajonnäs.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.5, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Denna fiskgryta får sin lysande solgula färg och ljuvliga smak av saffran, vitl"
            "ök och tomatpuré. Grytan blir matig och mättande med lax, torsk, räkor och muss"
            "lor och passar perfekt att bjuda på till en lite festligare middag med eller ut"
            "an gäster.",
            self.harvester_class.description(),
        )
