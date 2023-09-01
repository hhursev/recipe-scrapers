# mypy: allow-untyped-defs

from recipe_scrapers.omnivorescookbook import OmnivoresCookbook
from tests import ScraperTest


class TestOmnivoresCookbookScraper(ScraperTest):

    scraper_class = OmnivoresCookbook
    test_file_name = "omnivorescookbook_multiple_ingredient_groups"

    def test_ingredients(self):
        self.assertEqual(
            [
                "8 oz (225 g) flank steak (or skirt steak) , thinly sliced against the grain",
                "8 oz (225 g) fresh Hong Kong pan fry noodles (or other type of thin noodles) (Footnote 1)",
                "2 tablespoons Shaoxing wine (or dry sherry)",
                "2 teaspoons cornstarch",
                "1/4 teaspoon salt",
                "1 cup low-sodium beef broth",
                "2 tablespoons soy sauce (*Footnote 2)",
                "2 tablespoons oyster sauce",
                "1 tablespoon Shaoxing wine (or dry sherry)",
                "2 tablespoons cornstarch",
                "1 teaspoon sugar",
                "1/4 teaspoon Chinkiang vinegar",
                "1/4 teaspoon white pepper",
                "4 tablespoons peanut oil , divided",
                "4 heads baby bok choy , quartered",
                "4 cloves garlic , minced",
                "1 inch (2.5 cm) ginger , minced",
                "1/2 yellow onion , sliced",
                "1/2 carrot , sliced into strips",
            ],
            self.harvester_class.ingredients(),
        )
