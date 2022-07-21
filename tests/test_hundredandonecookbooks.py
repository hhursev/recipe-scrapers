from recipe_scrapers.hundredandonecookbooks import HundredAndOneCookbooks
from tests import ScraperTest


class TestHundredAndOneCookbooksScraper(ScraperTest):

    scraper_class = HundredAndOneCookbooks

    def test_host(self):
        self.assertEqual("101cookbooks.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.101cookbooks.com/blood-orange-gin-sparkler/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Blood Orange Gin Sparkler")

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("1 serving", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://images.101cookbooks.com/gin_sparkler.jpg?w=680&auto=format",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 cups / 480 ml water",
                "1 cup / 6.5 oz / 185 g sugar",
                "4 tablespoons (~2 sprigs-worth) fresh rosemary leaves",
                "1 bay leaf (optional)",
                "blood oranges",
                "gin",
                "ice cubes",
                "tonic water (or sparkling water)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Combine the water, sugar, rosemary, and bay in a small saucepan over medium heat. Bring to a simmer for 3-5 minutes, or long enough for the sugar to dissolve, stirring occasionally. Remove from the heat and let infuse for 10 minutes. Strain into a jar to cool completely.\nIn the meantime, juice and strain your oranges, you'll need 3 tablespoons / 1.5 ounces of juice for each drink.\nTo make each drink you're going to combine equal parts gin, juice, and tonic water with a bit of syrup and ice. So, its 3 tablespoons / 1 1/2 oz gin, 3 tablespoons / 1 1/2 oz freshly squeezed blood orange juice, and 1-2 teaspoons of the rosemary syrup in each tall glass (I used kolsch glasses here). Stir to combine, fill each glass 2/3 full with ice and top off with 3 tablespoons / 1 1/2 oz tonic water. Stir again and you're set.",
            self.harvester_class.instructions(),
        )
