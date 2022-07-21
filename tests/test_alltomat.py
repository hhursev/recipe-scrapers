from recipe_scrapers.alltomat import AllTomat
from tests import ScraperTest


class TestAllTomatScraper(ScraperTest):

    scraper_class = AllTomat

    def test_host(self):
        self.assertEqual("alltommat.se", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("gunilla von heland", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Brioche-hamburgerbröd", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cached-images.bonnier.news/bnl01/standard-article/ec93ddbf-20de-46db-a563-3b88881f0e71/89ad5fc0-7218-4e14-b9be-dafb51ae221a/16x9/0/original.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2.5 dl vatten",
                "0.5 dl mjölk",
                "25 g jäst",
                "2.5 msk strösocker",
                "1 tsk salt",
                "1 ägg",
                "7.5 dl vetemjöl",
                "50 g smör",
                "1 ägg",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Värm vatten och mjölk till 37°. Rör ut jästen med lite av vätskan och tillsätt socker, salt, ägg och mjöl, spara ca 1/2 dl till utbakning. Arbeta degen i maskin ca 5 min. Klicka ner smöret mot slutet. Låt jäsa övertäckt ca 1 timme.\nArbeta degen lätt i maskinen. Ta upp på mjölad arbetsbänk. Dela degen i 12 bitar. Forma bitarna till runda bullar och platta ut dem lätt. Lägg dem på en plåt med bakplåtspapper. Låt jäsa övertäckta ytterligare ca 1 timme. Sätt ugnen på 200°.\nPensla bröden med uppvispat ägg och grädda mitt i ugnen ca 15 min. Låt svalna på galler.""",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(3.9, self.harvester_class.ratings())
