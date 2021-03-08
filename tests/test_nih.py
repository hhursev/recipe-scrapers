from recipe_scrapers.nihhealthyeating import NIHHealthyEating
from tests import ScraperTest

# test recipe's URL
# https://healthyeating.nhlbi.nih.gov/recipedetail.aspx?linkId=17&cId=10&rId=247


class TestNIHHealthyEatingRecipesScraper(ScraperTest):

    scraper_class = NIHHealthyEating

    def test_host(self):
        self.assertEqual("healthyeating.nhlbi.nih.gov", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Vietnamese Fresh Spring Rolls (Gỏi Cuốn)"
        )

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 C carrots, cut into long, thin strips",
                "2 C bean sprouts",
                "2 C cucumber, seeded and cut into long, thin strips",
                "1 C minced scallions",
                "½ C chopped fresh cilantro",
                "¼ C chopped fresh mint",
                "8 rice paper wrappers",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Toss first six ingredients in a large bowl.\nSoak one rice paper wrapper in warm water until soft (1 to 2 minutes). Shake off excess water.\nPlace vegetable filling off-center on rice paper, and fold like an egg roll (tuck in the sides to keep the filling inside).\nRepeat with remaining vegetable filling and rice paper wrappers.\nOnce you have assembled all of the spring rolls, serve immediately.",
            self.harvester_class.instructions(),
        )
