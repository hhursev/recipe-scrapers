from recipe_scrapers.bbcfood import BBCFood
from tests import ScraperTest


class TestBBCFoodScraper(ScraperTest):

    scraper_class = BBCFood

    def test_host(self):
        self.assertEqual("bbc.com", self.harvester_class.host())

    def test_host_domain(self):
        self.assertEqual("bbc.co.uk", self.harvester_class.host(domain="co.uk"))

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Rob Burns")

    def test_canonical_url(self):
        self.assertEqual(
            "http://www.bbc.co.uk/food/recipes/baileysandchocolatec_72293",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Irish cream and chocolate cheesecake"
        )

    def test_total_time(self):
        self.assertEqual(130, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("1 item(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://ichef.bbci.co.uk/food/ic/food_16x9_608/recipes/baileysandchocolatec_72293_16x9.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "100g/3½oz butter",
                "250g/8¾oz digestive biscuits, crushed",
                "600g/1lb 5oz cream cheese",
                "25ml/1fl oz Baileys or other Irish cream liqueur",
                "100ml/3½oz icing sugar",
                "300ml/10½oz double cream, whipped",
                "100g/3½oz grated chocolate",
                "200ml/7¼oz double cream, whipped",
                "cocoa powder, to dust",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Melt the butter in a pan and add the crushed digestive biscuits. Mix well until the biscuits have absorbed all the butter.\nRemove from the heat and press into the bottom of a lined 18cm/7in springform tin. Place in the refrigerator and allow to set for one hour.\nMeanwhile, prepare the filling. Lightly whip the cream cheese then beat in the Irish cream and icing sugar. Fold in the whipped cream and grated chocolate. When smooth, spoon evenly onto the biscuits.\nRefrigerate and allow to set for a further two hours. Once set, remove and decorate with whipped cream and cocoa powder dusted over the top. Serve.",
            self.harvester_class.instructions(),
        )
