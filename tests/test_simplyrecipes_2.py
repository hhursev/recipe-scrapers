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

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Isa Chandra Moskowitz")

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

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

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Roast the parsnips: Preheat the oven to 425°F (220°C). Line a large baking sheet with parchment paper. Drizzle the olive oil, salt, and pepper on the baking pan. Toss the parsnips in the oil to coat. Bake for about 20 minutes, flipping occasionally, until the parsnips are tender inside and golden brown in some spots. Let cool.",
                    "Make the dressing and assemble the salad: In a large mixing bowl, stir together the mayo, lemon juice, kelp powder, capers, chives, and salt. Fold in the celery and the cooled parsnips. Chill the salad for about 20 minutes.",
                    "Toast the buns: Preheat a large skillet, preferably cast-iron, over medium heat. Butter the outside of each hot dog bun. Place them in the skillet and toast until golden brown, about 2 minutes for each side.",
                    "Assemble: Fill the buns with salad. Sprinkle with paprika and additional chives. Serve with plenty of napkins.",
                ]
            ),
            self.harvester_class.instructions(),
        )
