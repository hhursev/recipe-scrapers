from recipe_scrapers.farmhouseonboone import FarmhouseOnBoone
from tests import ScraperTest


class TestFarmhouseOnBoone(ScraperTest):
    scraper_class = FarmhouseOnBoone

    def test_host(self):
        self.assertEqual("farmhouseonboone.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.farmhouseonboone.com/sourdough-croissants",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Sourdough Croissants")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Lisa")

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_total_time(self):
        self.assertEqual(900, self.harvester_class.total_time())

    def test_image(self):
        self.assertEqual(
            "https://www.farmhouseonboone.com/wp-content/uploads/2022/09/sourdough-croissants-11-2-scaled-720x720.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1/4 cup butter",
                "3 1/2 cups flour",
                "1/4 cup sugar",
                "2 teaspoons salt",
                "1 1/4 cup milk",
                "1/2 cup sourdough starter, active and bubbly",
                "1.5 cups unsalted butter",
                "1 egg yolk",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Knead dough. Add everything (except the 1.5 cups butter and the egg yolk) to a stand mixer and allow it to knead until it pulls away from the sides of the bowl and is glossy and stretchy. About 10 minutes on medium/low speed) should do.",
                    "Transfer the dough to a lightly greased bowl and cover tightly, using a lid, plastic wrap, or beeswax wraps.",
                    "Allow to sit at room temperature overnight or 8 hours. This is the bulk ferment to get all of those sourdough benefits.",
                    "Chill the dough for 1 hour so that it is easier to work with.",
                    "Roll out dough to 10” by 16”.",
                    "Chill for 4 hours, or overnight.",
                    "Cut the sticks of butter in about fourths vertically, and lay them out on parchment paper, creating an 8” by 10” rectangle. I like to place the parchment paper onto my work surface and, using a ruler and pencil, make that size of rectangle as a template.",
                    "Fold the sides of the parchment up around the butter, creating a little 8” by 10” packet. Fold the parchment all around.",
                    "Using a rolling pin, roll on top of it so that the butter fills the area. You want a 8 by 10 inch rectangle of butter.",
                    "Chill for 15-30 minutes. You want the butter to be about the same consistency as the dough, not super hard. If it is harder than the dough it will break up as opposed to creating a nice layer between the dough (see troubleshooting). If the dough chills for several hours, and the butter for about 20 minutes, they should be about the same consistency.",
                    "Peel the butter off of the parchment paper and put the butter in the middle of the dough and fold the sides over so that you basically create an envelope for the butter. Pinch the edges down. You shouldn’t see the butter at all, as it should be entirely encased in the croissant dough.",
                    "Roll out to 10” by 16” rectangle. If the dough springs back or resists at all, put it in the fridge and allow the gluten to relax a bit. You don’t want to press the butter in too much so that it actually incorporates into the dough. You are trying to create layers!",
                    "Fold the dough/butter into thirds.",
                    "Tap the dough with the rolling pin so the butter is pliable yet not melted.",
                    "Roll out to 10 by 16 again and fold in thirds again. *Big key during the lamination is for the dough to never get too warm. If it does, the butter will just melt into the dough. So at this point, you’ll want to refrigerate for 30 minutes to get it cool again.",
                    "Roll out 10 by 16 one more time.",
                    "Fold in thirds one more time (for 3 times total).",
                    "Put the dough back in the fridge for 4 hours.",
                    "Roll out the dough into 10 by 20 inch rectangle.",
                    "Measure every 4” down one long side. Then measure 4” down the other side, starting off set from the 4” on the other side (so that the marks are in the middle of the 4” on the other side).",
                    "Cut diagonally from a mark on one side to one on the other, to create a triangle.",
                    "Start at large end and tightly roll.",
                    "Allow to rise for 2 hours at room temp, or until puffy.",
                    "Place in the fridge for an hour. This is optional, but I found that they hold their shape better during baking.",
                    "Preheat oven to 375 degrees.",
                    "Brush with egg wash.",
                    "Bake for 30 minutes until golden.",
                ]
            ),
            self.harvester_class.instructions(),
        )
