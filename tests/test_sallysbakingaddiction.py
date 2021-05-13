from recipe_scrapers.sallysbakingaddiction import SallysBakingAddiction
from tests import ScraperTest


class TestSallysBakingAddictionScraper(ScraperTest):

    scraper_class = SallysBakingAddiction

    def test_host(self):
        self.assertEqual("sallysbakingaddiction.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://sallysbakingaddiction.com/rosemary-garlic-pull-apart-bread/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Rosemary Garlic Pull Apart Bread"
        )

    def test_yields(self):
        self.assertEqual("1 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cdn.sallysbakingaddiction.com/wp-content/uploads/2020/12/garlic-rosemary-pull-apart-bread-225x225.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 teaspoons Platinum Yeast by Red Star*",
                "1 Tablespoon granulated sugar",
                "3/4 cup (180ml) whole milk",
                "3 Tablespoons (45g) unsalted butter, softened to room temperature",
                "1 large egg",
                "2 and 1/3 cups (291g) all-purpose flour (spoon & leveled), plus more as needed*",
                "1 teaspoon salt",
                "1 teaspoon garlic powder",
                "1 Tablespoon finely chopped fresh rosemary (or 2 teaspoons dried)",
                "5 Tablespoons (75g) unsalted butter, extra soft (see note)",
                "1 Tablespoon finely chopped fresh rosemary (or 2 teaspoons dried)",
                "1 Tablespoon finely chopped fresh parsley (or 2 teaspoons dried)",
                "2 garlic cloves, minced or 1/2 teaspoon garlic powder",
                "1/4 teaspoon salt",
                "3/4 cup (95g) shredded parmesan, mozzarella, or white cheddar cheese (or your favorite shredded cheese)",
                "1 Tablespoon unsalted butter, melted",
                "flaky/coarse sea salt for sprinkling",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Make the dough\nPlace the yeast and sugar in the bowl of a stand mixer fitted with a dough hook or paddle attachment. Or, if you do not own a stand mixer, a regular large mixing bowl. Heat the milk on the stove or in the microwave until warm to touch, about 110°F (43°C). Pour warm milk on top of yeast/sugar. Whisk gently to combine, then loosely cover with a clean kitchen towel and allow to sit for 5-10 minutes. The mixture will be frothy after 5-10 minutes.\nIf you do not have a mixer, you can mix the dough together with a wooden spoon or rubber spatula in this step\nAdd the butter, egg, flour, salt, garlic powder, and rosemary. Beat on low speed for 3 minutes. Dough will be soft. Transfer it to a lightly floured work surface. Using lightly floured hands, knead it for 1 minute. If the dough is too sticky to handle, add 1-3 more Tablespoons of flour, but you want a very soft dough. Shape into a ball.\nPlace the dough in a greased bowl (I use nonstick spray to grease) and cover with plastic wrap or aluminum foil. Place in a slightly warm environment to rise until doubled in size, around 60-90 minutes. (If desired, use my warm oven trick for rising. See my answer to Where Should Dough Rise? in my Baking with Yeast Guide.)\nAs the dough rises, prepare the filling in the next step and grease a 9×5 inch loaf pan.\nMake the filling\nIn a medium bowl, mix the soft butter, rosemary, parsley, garlic, and salt together. If the butter is soft enough, you can just mix it all together with a spoon or fork. You can use an electric mixer if that’s easier too. Cover tightly and set aside until ready to use. (Don’t refrigerate unless making well in advance. It’s easiest to spread on the dough when at room temperature. If refrigerated, let it come to room temperature before spreading on dough pieces.)\nAssemble the bread:\nPunch down the dough to release the air. Place dough on a lightly floured work surface. Divide it into 12 equal pieces, each about 1/4 cup of dough and a little larger than a golf ball. Using lightly floured hands, flatten each into a circle that’s about 4 inches in diameter. The circle doesn’t have to be perfectly round. I do not use a rolling pan to flatten, but you certainly can if you want. Spread 1-2 teaspoons of filling mixture onto each. Sprinkle each with 1 Tablespoon of cheese. Fold circles in half and line in prepared baking pan, round side up. See photos above for a visual.\nCover with plastic wrap or aluminum foil and allow to rise once again in a slightly warm environment until puffy, about 45 minutes.\nAdjust the oven rack to the lower third position then preheat oven to 350°F (177°C).\nBake until golden brown, about 50 minutes. If you find the top of the loaf is browning too quickly, tent with aluminum foil. (Don’t be alarmed if there’s melted butter around the sides of the bread as it bakes, it will seep into the bread before it finishes.) Remove from the oven and place the pan on a wire rack. If desired, brush with melted butter for topping and sprinkle with sea salt.\nCool for 10 minutes in the pan, then remove from the pan and serve warm.\nCover and store leftovers at room temperature for up to 2 days or in the refrigerator for up to 1 week. Since the bread is extra crispy on the exterior, it will become a little hard after day 1. Reheat in a 300°F (149°C) oven for 10-15 minutes until interior is soft again or warm in the microwave.",
            self.harvester_class.instructions(),
        )
