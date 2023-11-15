from recipe_scrapers.lekkerensimpel import LekkerEnSimpel
from tests import ScraperTest


class TestLekkerEnSimpelScraper2(ScraperTest):
    scraper_class = LekkerEnSimpel
    test_file_name = "lekkerensimpel_2"

    def test_host(self):
        self.assertEqual("lekkerensimpel.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual("American pancakes", self.harvester_class.title())

    def test_image(self):
        self.assertEqual(
            "https://www.lekkerensimpel.com/wp-content/uploads/2016/08/IMG_7654.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 eieren",
                "250 ml melk",
                "snufje kaneel",
                "125 gr zelfrijzend bakmeel",
                "boter",
                "1 tl suiker",
                "scheut melk",
                "4 el Nutella",
                "Fruit zoals banaan en aardbei",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertIn(
            "Bereidingswijze:\nSplits de eieren. Klop in een kom de eidooiers met de melk, kaneel, suiker en zelfrijzend bakmeel goed door elkaar. In een andere kom klop je de eiwitten stijf. Vind je het lastig om eieren te scheiden? Zelf doen wij het heel gemakkelijk door een ei in tweeën te breken en vervolgens het eiwit door onze handen de laten glijden in een kom. Uiteindelijk houd je de eidooier in je hand over en die kun je in een andere kom doen. Schep de stijfgeklopte eiwitten door de rest van het beslag. Let op: mix dit niet door elkaar maar schep het geheel voorzichtig door elkaar.\n\nSmelt een blokje boter in een pan en schep met een soeplepel 2-3 kleine pannenkoekjes in de pan.\n\nBak de pannenkoekjes circa 2 minuten per kant. Ondertussen verwarm de Nutella en melk in een pannetje. Meng even goed door elkaar en zodra je een mooi glad sausje hebt, is het klaar. Serveer de American pancakes met wat gesmolten nutella en wat vers fruit.",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "Wil je iemand (of jezelf) verwennen met een heel lekker ontbijtje? Bekijk dan dit recept voor American Pancakes met Nutella en fruit!",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("nl-NL", self.harvester_class.language())
