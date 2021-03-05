from recipe_scrapers.bigoven import BigOven
from tests import ScraperTest


class TestBigOven(ScraperTest):

    scraper_class = BigOven

    def test_host(self):
        self.assertEqual("bigoven.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.bigoven.com/recipe/no-knead-herb-focaccia/2719857",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "No-Knead Herb Focaccia")

    def test_total_time(self):
        self.assertEqual(720, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("24 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://photos.bigoven.com/recipe/hero/no-knead-herb-focaccia-79674b.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 packet active dry yeast ; (or 2 ¼ teaspoons)",
                "2 cups warm water ; divided",
                "2 teaspoons granulated sugar",
                "5 ½ cups bread flour",
                "¼ cup extra-virgin olive oil ; (plus more to grease pans and dough)",
                "1 tablespoon sea salt (or kosher salt)",
                "flaky sea salt ; (like Maldon)",
                "¼ cup extra-virgin olive oil",
                "4 sprigs fresh rosemary leaves",
                "3 sprigs fresh thyme leaves",
                "2 sprigs fresh oregano ; (or various herbs of choice)",
                "¼ teaspoon crushed red pepper",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Herb Topping:",
                    "In a small bowl, combine olive oil, herbs, and crushed red pepper. Set aside until ready.",
                    "For the dough:",
                    "1. In a small saucepan, warm 1 cup water to a lukewarm temperature of 105°F to 110°F on an instant-read thermometer. Pour water into the bowl of a stand mixer and gently whisk in yeast and sugar to dissolve. Allow the yeast to bloom briefly, about 5-10 minutes.",
                    "2. Add remaining cup water, flour, and sea salt. With the dough hook attachment on lowest speed, mix until a loose, craggy dough forms and then increase speed to medium-high and mix until a smooth dough begins to wrap around the hook, about 5 to 7 minutes. Turn off the mixer, cover bowl with a damp towel, and allow dough to rest for 10 to 15 minutes. Resume mixing on medium-high for 10 to 15 minutes until dough becomes very elastic and begins tugging away from the sides of the bowl. Dough will be quite sticky, but resist the urge to add additional flour -- dough.",
                    "3. For the first rise, drizzle ¼ cup olive oil into the mixing bowl and swirl the sides of the bowl to coat as well as the surface of the dough. Cover and allow to rise in a warm place until doubled in size, about 90 to 120 minutes.",
                    "4. Use this time to prepare your herb oil and prep your decorative toppings, if using.",
                    "5. For the second rise, drizzle another ¼ cup olive oil on a half sheet pan (or two quarter sheet pans). Then, with well-oiled hands, gingerly raise the dough from the mixing bowl and allow its weight to stretch the dough down upon itself. Repeat this stretching technique 4 to 6 times to help encourage extra rise. Transfer the dough to the sheet pan and stretch in all directions to coax it into rectangular submission. It will likely not comply straight away. Cover with oiled plastic wrap and, after a brief rest (about 10 to 15 minutes), stretch the dough a second time.",
                    "6. If you plan to delay baking, now is the time to cover the sheet pan with oiled plastic wrap and place in the refrigerator for up to 24 hours. Bring to room temperature about an hour before baking so that the dough has doubled in height.",
                    "7. While the dough is doubling, preheat the oven to 450°F. Arrange the oven racks to both their highest and lowest positions.",
                    "8. Once risen and ready to bake, uncover the dough and, with well-oiled hands, dimple the dough by plunging fingers spread wide downward into the bottom of the pan. Bubbles are good, but especially large ones can be gently deflated.",
                    "9. Drizzle the focaccia as desired. We recommend a bare minimum of ¼ extra-virgin olive oil and a generous flurry of flaky sea salt, but encourage you to gild the lily here with herbs and garlic aplenty.",
                    "10. Place focaccia on the lowest rack and bake until the edges begin to pull away from the sides and corners of the pan, about 15 to 20 minutes. Transfer to the top rack and continue baking until the top is golden brown and bubbles are very well browned, about 5 minutes. Cool in the pan briefly then transfer to a cooling rack until completely cooled.",
                    "Possible toppings to decorate:",
                    "red onions",
                    "shallots",
                    "chives",
                    "fresh sage",
                    "fresh thyme",
                    "fresh oregano",
                    "fresh dill",
                    "fresh parsley",
                    "fresh basil",
                    "mix of mini sweet peppers",
                    "bell peppers",
                    "banana peppers",
                    "jalapeno peppers",
                    "cherry tomatoes",
                    "kalamata olives, pitted",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual({"count": 1, "rating": 5.0}, self.harvester_class.ratings())
