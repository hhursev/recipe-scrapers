# mypy: allow-untyped-defs

from recipe_scrapers.fredriksfikaallas import FredriksFikaAllas
from tests import ScraperTest


class TestFredriksFikaAllasScraper(ScraperTest):

    scraper_class = FredriksFikaAllas

    def test_host(self):
        self.assertEqual("fredriksfika.allas.se", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Fredrik Nylén", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Ingredienser", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Fika", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual("https://files-aller-blogger-platform.aws.aller.com/uploads/sites/87/2015/08/10072015-_MG_0917-860x573.jpg?fit=crop&h=630&w=1200&ar=1.91:1", self.harvester_class.image())

    def test_ingredients(self):
        expected_ingredients = ['2 äpplen', '1 rulle färdig smördeg', '0,5 dl ljus sirap eller honung', 'kanel', 'råsocker eller strösocker', '1 ägg']
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = [
            'Sätt ugnen på 200 grader, klä en plåt med bakplåtspapper',
            'Kärna ur och skiva äpplena ganska tunt',
            'Klicka ut lite i 6 separata högar på bakplåtspapperet',
            'Strö över lite kanel och lägg äpplena omlott, strö lite socker på äpplena',
            'Skär smördegen lite större än äppelhögarna, lägg ovanpå äpplena och tryck till så det ligger tätt inpå äpplena så att de ligger lvar när du vänder upp dem',
            'Pensla smördegen med uppvispat ägg och baka mitt i ugnen 12-15 min tills de fått fin färg',
            'Låt svalna något och vänd sedan upp dem',
            'Servera gärna med vaniljglass eller vaniljsås',
        ]
        expected_instructions_str = '\n'.join(expected_instructions)

        actual_instructions = self.harvester_class.instructions()

        self.assertEqual(expected_instructions_str, actual_instructions)

    def test_ratings(self):
        self.assertEqual(3.4, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual("Enkel äppelpaj på färdig smördeg som du gör på ett kick!", self.harvester_class.description())
