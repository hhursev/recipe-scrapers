from tests import ScraperTest

from recipe_scrapers.jamieoliver import JamieOliver


class TestJamieOliverScraper(ScraperTest):

    scraper_class = JamieOliver

    def test_host(self):
        self.assertEqual("jamieoliver.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Bloomin' brilliant brownies")

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("20 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "jamieoliver_files/88_1_1441269331.jpg", self.harvester_class.image()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "250 g unsalted butter",
                "200 g good-quality dark chocolate (70% cocoa solids) , broken up",
                "75 g dried sour cherries , optional",
                "50 g chopped nuts , optional",
                "80 g cocoa powder , sifted",
                "65 g plain flour , sifted",
                "1 teaspoon baking powder",
                "360 g caster sugar",
                "4 large free-range eggs",
                "zest of 1 orange , optional",
                "250 ml crème fraîche , optional",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Preheat your oven to 180°C/350°F/gas 4. Line a 24cm square baking tin with greaseproof paper. In a large bowl over some simmering water, melt the butter and the chocolate and mix until smooth. Add the cherries and nuts, if you’re using them, and stir together. In a separate bowl, mix together the cocoa powder, flour, baking powder and sugar, then add this to the chocolate, cherry and nut mixture. Stir together well. Beat the eggs and mix in until you have a silky consistency. Pour your brownie mix into the baking tray, and place in the oven for around 25 minutes. You don’t want to overcook them so, unlike cakes, you don’t want a skewer to come out all clean. The brownies should be slightly springy on the outside but still gooey in the middle. Allow to cool in the tray, then carefully transfer to a large chopping board and cut into chunky squares. These make a fantastic dessert served with a dollop of crème fraîche mixed with some orange zest.",
            self.harvester_class.instructions(),
        )
