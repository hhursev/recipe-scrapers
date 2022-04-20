from recipe_scrapers.nytimes import NYTimes
from tests import ScraperTest


class TestNYTimesScraper(ScraperTest):

    scraper_class = NYTimes

    def test_host(self):
        self.assertEqual("cooking.nytimes.com", self.harvester_class.host())

    def test_image(self):
        self.assertEqual(
            "https://static01.nyt.com/images/2020/05/28/dining/lp-cacio-e-pepe-crackers/merlin_172657737_693784a8-529d-4496-9e60-3ff2af3c7735-articleLarge.jpg",
            self.harvester_class.image(),
        )

    def test_canonical_url(self):
        self.assertEqual(
            "https://cooking.nytimes.com/recipes/1021128-cacio-e-pepe-crackers",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Cacio e Pepe Crackers")

    def test_ratings(self):
        self.assertEqual(self.harvester_class.ratings(), 4.0)

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("160 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 1/2 cups/190 grams unbleached all-purpose flour (see Tip)",
                "1 tablespoon freshly ground black pepper, plus more for finishing",
                "1/2 teaspoon kosher salt",
                "1/2 teaspoon onion powder (optional)",
                "1/2 teaspoon ground mustard (optional)",
                "1/8 teaspoon garlic powder (optional)",
                "5 ounces/145 grams white Cheddar, roughly grated (about 1 1/4 cups packed)",
                "3 ounces/85 grams Asiago cheese, roughly grated (about 3/4 cup)",
                "5 tablespoons/70 grams unsalted butter, cold and cubed",
                "1/4 cup/25 grams finely ground Pecorino Romano cheese (or Parmigiano-Reggiano or more Asiago), for sprinkling",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "In the bowl of a food processor, add the flour, pepper, salt and spices (if using), and pulse to combine.\nAdd the Cheddar, Asiago and butter, and pulse several times, then let the mixer run until the dough comes mostly together around the blade, 1 to 3 minutes. It’s OK if the dough is a little pebbly, but it should clump easily when you squeeze it. (You can also prepare this dough by hand, though you’ll need to bring the butter to room temperature first. Mix all your dry ingredients in a medium bowl. Then, in a large bowl, mix Cheddar, Asiago and butter to form a paste. Add the flour mixture and knead the dough together.)\nPull your dough out of your bowl onto a flat surface and gently knead it into a smooth ball. Split your dough in half and shape each half into a rectangle. Using a rolling pin, roll each piece until about 1/2-inch thick, dusting a tiny bit of flour on your pin, if needed, to prevent the dough from sticking. (If you don’t want to bake all the crackers now, you can freeze dough in 1/2-inch-thick blocks.)\nPlace a piece of dough in the center of an 18-inch-long piece of parchment paper. Roll the dough on the parchment paper, working from the center outward. (You want the dough to adhere to the bottom layer of parchment, but if your rolling pin sticks to the surface, lightly dust it with flour.) When your dough is about 1/4-inch thick, lay another piece of parchment, plastic wrap, or a silicone baking mat over the surface of your dough. Continue to roll the dough out 1/8- to 1/16-inch thick, as thin as your arms will allow, pressing together any cracks that may form. (You can also use an etching motion, moving your pin from the center out toward the edges across your dough.) Rotate the parchment in front of you with every few strokes to ensure you are rolling the dough evenly.\nPeel back the top layer of parchment and sprinkle the surface with half the Pecorino Romano and a dozen or so grinds of black pepper across the surface. Lightly roll over once more with your rolling pin so the cheese and pepper adheres to the cracker dough. Transfer this sheeted dough onto a baking sheet and chill in the fridge or freezer until firm, about 15 minutes. (If you let it chill longer, just pull it out and let it temper a bit before proceeding.) Repeat with the second piece of dough.\nWhen the dough is nearly chilled, arrange the racks in the upper and lower third of the oven and heat to 325 degrees. Remove one sheet of dough from the tray and place on a work surface.\nUsing a pastry wheel (fluted is nice), pizza cutter or a sharp knife and a ruler, cut 1-inch squares across the surface of the dough. (A 1-inch-thick ruler or tracer made from card stock or cardboard comes in handy here.) Transfer crackers to parchment-lined baking sheets with 1/2-inch space in between. (They will not spread much.) If your dough warms up or is difficult to peel and place, just slip it back into the freezer still attached to your parchment paper and let it firm up, then proceed.\nBake the crackers in the center of your oven for 14 to 20 minutes (depending on thickness), rotating trays midway through baking to ensure they color evenly. Crackers will be just golden at the edges and the surface should be firm to the touch. You want them to dry crisp. (Test by pulling one cracker off the tray, let it quickly cool and break it in half to see how it snaps.) Remove from the oven and cool on trays.\nOnce fully cooled, store crackers in a tin or covered container for up to 4 weeks.",
            self.harvester_class.instructions(),
        )


# https://cooking.nytimes.com/recipes/1021128-cacio-e-pepe-crackers
