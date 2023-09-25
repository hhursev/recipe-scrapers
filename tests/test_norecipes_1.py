# mypy: allow-untyped-defs

from recipe_scrapers.norecipes import NoRecipes
from tests import ScraperTest


class TestNoRecipesScraper(ScraperTest):

    scraper_class = NoRecipes
    test_file_name = "norecipes_1"

    def test_host(self):
        self.assertEqual("norecipes.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Marc", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Best Burnt Basque Cheesecake", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Dessert", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(27, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://norecipes.com/wp-content/uploads/2020/01/basque-cheesecake-011.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "226 grams cream cheese (cold)",
                "1 cup heavy cream (cold)",
                "100 grams granulated sugar",
                "2 large eggs (cold)",
                "15 grams cake flour",
                "1/2 teaspoon vanilla extract",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        expected_instructions = [
            "Preheat the oven to the 450 degrees F* (230 C). See the section above in the headnotes about how long to bake it.",
            "Line a 6-inch cake pan with 2.5-inch sides with parchment paper. If the pan has a removable bottom, you can use the bottom to press the paper into the pan. Then you can use your hands to crease the sides to hold its shape. Once the paper is molded to the pan, you can remove the bottom and the paper and then reattach the bottom to the pan, placing the paper on top.",
            "Add all of the ingredients to a blender and blend until smooth. I usually let this mixture rest for about 20 minutes to give the air bubbles in the batter a chance to settle, but you can bake it right away if you're in a rush.",
            "Pour the mixture into the prepared pan and then drop the pan a few times onto a kitchen towel to coax any remaining bubbles out of the batter.",
            "Bake the cheesecake until the top is just shy of turning black. This takes 22 minutes in my oven. The cake should still be very jiggly in the center when you remove it from the oven.",
            "Let the burnt cheesecake cool on a cooling rack and then place it in a sealable bag and refrigerate overnight.",
            "To slice the Basque Cheesecake, prepare a long sharp knife along with a pot of boiling water. Clean and heat the knife with the hot water between each slice. This ensures you get nice clean slices.",
        ]

        self.assertEqual(
            "\n".join(expected_instructions), self.harvester_class.instructions()
        )

    def test_ratings(self):
        self.assertEqual(4.45, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual(["Best,Spanish"], [self.harvester_class.cuisine()])

    def test_description(self):
        self.assertEqual(
            "With a caramelized top that borders on burnt and a jiggly custardy center, Basque Cheesecake is a mind-blowingly delicious combination of textures and tastes that comes together from a handful of ingredients with almost no effort.",
            self.harvester_class.description(),
        )
