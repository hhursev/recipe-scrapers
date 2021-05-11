from recipe_scrapers.kuchniadomowa import KuchniaDomowa
from tests import ScraperTest


class TestKuchniaDomowaScraper(ScraperTest):

    scraper_class = KuchniaDomowa

    def test_host(self):
        self.assertEqual("kuchnia-domowa.pl", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "http://www.kuchnia-domowa.pl/przepisy/dodatki-do-dan/548-mizeria",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Mizeria", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_language(self):
        self.assertEqual("pl-pl", self.harvester_class.language())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://static.kuchnia-domowa.pl/images/content/548/mizeria.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "600 g świeżych ogórków gruntowych (lub długich, szklarniowych)*",
                "300 g gęstej, kwaśnej śmietany 18% lub jogurtu typu greckiego",
                "1 łyżeczka soli",
                "1 łyżka soku z cytryny (lub niepełna łyżka octu jabłkowego)",
                "1 łyżeczka cukru",
                "czarny pieprz mielony",
                "1 łyżka drobno posiekanego koperku",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Ogórki umyć, osuszyć, obrać i pokroić w jak najcieńsze plasterki.\nPlasterki umieścić w misce i posypać 1 łyżeczką soli. Wymieszać i pozostawić na ok. 15 minut.\nW międzyczasie śmietanę przełożyć do miseczki. Przyprawić sokiem z cytryny, cukrem, pieprzem i posiekanym koperkiem. Wymieszać.\nPo 15 minutach odlać wodę, którą puściły ogórki. (Lekko je odcisnąć, ale nie za mocno, aby mizeria nie wyszła za sucha).\nDodać przygotowaną śmietanę i wymieszać.",
            self.harvester_class.instructions(),
        )
