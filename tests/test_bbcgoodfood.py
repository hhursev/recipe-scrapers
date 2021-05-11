from recipe_scrapers.bbcgoodfood import BBCGoodFood
from tests import ScraperTest


class TestBBCGoodFoodScraper(ScraperTest):

    scraper_class = BBCGoodFood

    def test_host(self):
        self.assertEqual("bbcgoodfood.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.bbcgoodfood.com/recipes/monster-cupcakes",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Monster cupcakes")

    def test_total_time(self):
        self.assertEqual(50, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 item(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/recipe-image-legacy-id-405483_12-cee017a.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "250g self-raising flour",
                "25g cocoa powder",
                "175g light muscovado sugar",
                "85g unsalted butter, melted",
                "5 tbsp vegetable or sunflower oil",
                "150g pot fat-free natural yogurt",
                "1 tsp vanilla extract",
                "3 large eggs",
                "85g unsalted butter, softened",
                "1 tbsp milk",
                "½ tsp vanilla extract",
                "200g icing sugar, sifted",
                "food colourings(optional)",
                "sweetsand sprinkles, to decorate",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Heat oven to 190C/170C fan/gas 5 and line a 12-hole muffin tin with deep cake cases. Put all the cake ingredients into a large bowl and beat together with electric hand beaters until smooth. Spoon the mix into the cases, then bake for 20 mins until risen and a skewer inserted into the middle comes out dry. Cool completely on a rack. Can be made up to 3 days ahead and kept in an airtight container, or frozen for up to 1 month.\nFor the frosting, work the butter, milk and vanilla into the icing sugar until creamy and pale. Colour with food colouring, if using, then create your own gruesome monster faces using sweets and sprinkles.",
            self.harvester_class.instructions(),
        )
