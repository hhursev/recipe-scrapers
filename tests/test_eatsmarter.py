from recipe_scrapers.eatsmarter import Eatsmarter
from tests import ScraperTest


class TestClosetCooking(ScraperTest):

    scraper_class = Eatsmarter

    def test_host(self):
        self.assertEqual("eatsmarter.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://eatsmarter.com/recipes/citrus-avocado-salad-with-almonds",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Citrus Avocado Salad with Almonds"
        )

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 tablespoons Sliced almonds",
                "2 stalks Celery",
                "2 ounces green Olives (pitted)",
                "3 Oranges",
                "1 pink Grapefruit",
                "1 Belgian endive",
                "1 Avocado",
                "2 tablespoons Olive oil",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Toast almonds in a dry pan until golden and fragrant. Place into a bowl to cool. Rinse and thinly slice celery. Cut olives into slices. Squeeze orange juice from one orange. Peel remaining oranges well and fillet, cut fillets into pieces. Repeat the same steps with grapefruit. Separate endive into individual leaves, rinse and spin dry, cut into strips. Peel and pit avocado, cut pulp into small cubes. Combine avocado cubes with orange juice in a bowl. Add all remaining prepared salad ingredients, drizzle with oil and toss salad carefully. Arrange on plates and serve.",
            self.harvester_class.instructions(),
        )
