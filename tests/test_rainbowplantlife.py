from recipe_scrapers.rainbowplantlife import RainbowPlantLife
from tests import ScraperTest


class TestRainbowPlantLifeScraper(ScraperTest):

    scraper_class = RainbowPlantLife

    def test_host(self):
        self.assertEqual("rainbowplantlife.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Nisha Vora", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Vegan Brown Butter Peach Cobbler", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("10 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://rainbowplantlife.com/wp-content/uploads/2020/11/peachblueberrrycobbler286of1029.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 pound (454g) ripe but relatively firm peaches",
                "1/2 cup (75-85g) fresh blueberries",
                "1/3 cup (45g) coconut sugar (or brown sugar)",
                "1 teaspoon ground cinnamon",
                "1/4 teaspoon nutmeg ((I recommend freshly grated nutmeg))",
                "Scant 1/2 teaspoon ground ginger",
                "2 pinches of ground cardamom ((optional))",
                "10 tablespoons (140g) Country Crock Plant Butter",
                "1 1/2 cups (180g) all-purpose flour",
                "Scant 2/3 cup ((60g) old-fashioned rolled oats)",
                "1 cup (200g) organic cane sugar",
                "1/4 - 1/2 teaspoon kosher salt",
                "2 teaspoons baking powder",
                "1 1/3 cups (320 mL) full-fat oat milk (I used Oatly)",
                "1 1/2 teaspoons pure vanilla extract",
                "1/4 - 1/2 teaspoon pure almond extract ((optional))",
                "For serving: vegan vanilla ice cream ((optional))",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Arrange a rack in the middle of your oven and preheat it to 375°F/190°C.",
                    "Cut the peaches in half and remove the pits, then cut the peaches into 1/4-1/2 inch thick slices (3/4 cm - 1 1/4 cm). Transfer the peaches to a medium or large bowl. Add the blueberries, coconut sugar, cinnamon, nutmeg, ginger, and cardamom (if using), and toss gently to combine. Set aside for 30 minutes to allow the fruit to absorb the flavors.",
                    "Heat a skillet over medium heat, then add the Plant Butter. Once the butter is melted, stir it often and swirl the pan to ensure even browning and cooking, until it foams and then eventually browns. You might want to stand back to avoid splatter. The browning process should take 5-8 minutes. Take the browned butter off the heat and immediately pour brown into a 2-quart/2-liter baking pan. See note below on alternative pan sizes.*",
                    "In a medium or large bowl, combine the flour, oats, cane sugar, salt, and baking powder. Whisk in the oat milk and vanilla extract and almond extract (if using) until well combined. Using a ladle or measuring cup, ladle the batter on top of the brown butter. Ladling, instead of pouring all of the batter on top at once, helps the butter swirl and mix into batter. Top the cobbler with the peach-blueberry mixture.",
                    "Bake the cobbler for 45-50 minutes, rotating the pan 180° halfway through to ensure even browning, until the top is deeply golden brown and bubbling. Mine took exactly 45 minutes.",
                    "Allow the cobbler to cool slightly before serving. Serve warm and, if desired, with vegan vanilla ice cream on top.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.96, self.harvester_class.ratings())
