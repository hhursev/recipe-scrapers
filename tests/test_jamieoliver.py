from recipe_scrapers.jamieoliver import JamieOliver
from tests import ScraperTest


class TestJamieOliverScraper(ScraperTest):

    scraper_class = JamieOliver

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.jamieoliver.com/recipes/chocolate-recipes/bloomin-brilliant-brownies/",
            self.harvester_class.canonical_url(),
        )

    def test_host(self):
        self.assertEqual("jamieoliver.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Bloomin' brilliant brownies")

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("20 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://img.jamieoliver.com/jamieoliver/recipe-database/oldImages/large/88_1_1441269331.jpg?tr=w-800,h-1066",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "200 g quality dark chocolate (70%)",
                "250 g unsalted butter",
                "75 g dried sour cherries , optional",
                "50 g chopped nuts , optional",
                "80 g quality cocoa powder",
                "65 g plain flour",
                "1 teaspoon baking powder",
                "360 g caster sugar",
                "4 large free-range eggs",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Preheat the oven to 180°C/350°F/gas 4. Line a 24cm square baking tin with greaseproof paper.",
                    "Snap the chocolate into a large bowl, add the butter and place over a pan of simmering water, until melted, stirring regularly. Stir through the cherries and nuts (if using).",
                    "Sift the cocoa powder and flour into a separate bowl, add the baking powder and sugar, then mix together.",
                    "Add the dry ingredients to the chocolate, cherry and nut mixture and stir together well. Beat the eggs, then mix in until you have a silky consistency.",
                    "Pour the brownie mix into the baking tin, and place in the oven for around 25 minutes. You don’t want to overcook them so, unlike cakes, you don’t want a skewer to come out clean – the brownies should be slightly springy on the outside but still gooey in the middle.",
                    "Allow to cool in the tray, then carefully transfer to a large chopping board and cut into chunky squares. Delicious served with a dollop of crème fraîche or yoghurt mixed with some orange zest.",
                ]
            ),
            self.harvester_class.instructions(),
        )
