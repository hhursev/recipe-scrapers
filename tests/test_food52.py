from recipe_scrapers.food52 import Food52
from tests import ScraperTest


class TestFood52(ScraperTest):

    scraper_class = Food52

    def test_host(self):
        self.assertEqual("food52.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://food52.com/recipes/84961-pomegranate-chicken-wings-recipe",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Sticky Pomegranate & Black Pepper Chicken Wings",
        )

    def test_total_time(self):
        self.assertEqual(1520, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 to 2 1/4 pounds chicken wings",
                "1 tablespoon kosher salt",
                "1 tablespoon granulated sugar",
                "2 teaspoons baking powder",
                "1/2 teaspoon MSG (optional)",
                "2 tablespoons neutral oil, such as grapeseed or canola",
                "1/4 cup granulated sugar",
                "1/2 cup pomegranate molasses",
                "2 tablespoons freshly ground black pepper",
                "2 teaspoons kosher salt",
                "2 teaspoons ground cinnamon",
                "1 teaspoon freshly ground nutmeg",
                "1/2 teaspoon toasted walnut halves, roughly chopped",
                "Flaky salt (optional)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Line a sheet pan with foil (for easy cleanup) and set an ovenproof wire rack inside.",
                    "Brine the wings: Pat the wings dry with a paper towel and place in a large bowl. In a small bowl, stir together the kosher salt, sugar, baking powder, and MSG (if using). Sprinkle this mixture over the wings and toss until evenly coated. Arrange the wings on the wire rack and refrigerate uncovered at least 6 hours or preferably overnight, flipping the wings halfway through. (Wash the bowl and keep it handy—we’ll be using it again.)",
                    "When you’re ready to roast, heat the oven to 350°F.",
                    "The first roast: Transfer the wings to the big bowl, toss with the oil until evenly coated, then return them to the wire rack. Roast the wings, flipping them once halfway through, until the skin is lightly browned, the flesh of the drumettes is starting to pull away from the bones, and the fat from the skin has mostly rendered, about 1 hour.",
                    "Meanwhile, prepare the glaze: Wash the large bowl. Add the sugar and pour 2 tablespoons of boiling water on top, whisking until the sugar dissolves. Add the pomegranate molasses, black pepper, salt, cinnamon, and nutmeg, whisking until combined.",
                    "The second roast: Remove the wings from the oven and increase the temperature to 375°F. Transfer the wings to the bowl with the glaze and toss to coat. Use tongs to return the wings to the rack, reserving any remaining glaze in the bowl, and roast until lightly charred and glossy, about 20 minutes.",
                    "Once the wings are out of the oven, transfer them to the bowl and toss again in the remaining glaze. Transfer the wings to a platter and garnish with the walnuts. Sprinkle with flaky salt if desired.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
