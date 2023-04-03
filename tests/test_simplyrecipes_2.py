from recipe_scrapers.simplyrecipes import SimplyRecipes
from tests import ScraperTest


class TestSimplyRecipes2(ScraperTest):
    """
    Scrape simplyrecipes.com recipe with multiple ingredient sections.
    """

    scraper_class = SimplyRecipes
    test_file_name = "simplyrecipes_2"

    def test_host(self):
        self.assertEqual("simplyrecipes.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.simplyrecipes.com/parsnip-lobster-rolls-recipe-6944750",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Parsnip Lobster Rolls")

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 tablespoons olive oil",
                "1 teaspoon kosher salt",
                "1/2 teaspoon ground black pepper",
                "2 pounds (910g) parsnips, peeled, cut into 1 1/2-inch (4 cm) chunks (see Recipe Note)",
                "1/2 cup (120 ml) vegan mayo, prepared or homemade",
                "2 tablespoons fresh lemon juice",
                "1 teaspoon kelp powder",
                "3 tablespoons capers, drained and rinsed",
                "1/3 cup (15g) chives, thinly sliced chives, plus extra for garnish",
                "1/2 teaspoon salt",
                "2 stalks celery, thinly sliced",
                "Large split-top hot dog buns",
                "Vegan butter, softened",
                "Sweet paprika",
                "1/4 cup (11 g) thickly sliced chives",
            ],
            self.harvester_class.ingredients(),
        )
