import os

from recipe_scrapers._exceptions import SchemaOrgException
from recipe_scrapers.southernliving import SouthernLiving
from tests import ScraperTest


class TestSouthernLiving(ScraperTest):

    scraper_class = SouthernLiving

    def test_host(self):
        self.assertEqual("southernliving.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.southernliving.com/recipes/spicy-sausage-cheddar-kolaches-recipe",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Spicy Sausage-and-Cheddar Kolaches Recipe"
        )

    def test_total_time(self):
        self.assertEqual(180, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("22 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F24%2F2015%2F09%2F2546801_bread_02_1_0_1_0_0_0-2000.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 cup whole milk",
                "3/4 cup salted butter, divided",
                "1/2 cup warm water (100°F to 110°F)",
                "1 (1⁄4-oz.) envelope active dry yeast",
                "1/3 cup plus 1 tsp. granulated sugar, divided",
                "2 large eggs, beaten",
                "3/4 teaspoon salt",
                "5 1/4 - 6 cups bread flour, divided, plus more for dusting",
                "1 1/4 pounds Conecuh sausage or spicy smoked sausage",
                "4 ounces sharp Cheddar cheese, shredded (about 1 cup)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Combine whole milk and 1⁄2 cup of the butter in a small saucepan. Cook over medium-low, stirring occasionally, until butter melts, about 5 minutes. Transfer mixture to a medium bowl, and cool slightly to 100°F to 110°F, about 10 minutes.",
                    "Stir together warm water, active dry yeast, and 1 teaspoon of the granulated sugar in a small bowl. Let stand until foamy, about 5 minutes.",
                    "Combine eggs, salt, and remaining 1⁄3 cup granulated sugar in the bowl of a heavy-duty electric stand mixer fitted with a dough hook attachment. Beat on medium-low speed just until combined. Stir in milk mixture and yeast mixture. Gradually add 4 1⁄2 cups of the bread flour, beating just until incorporated. With mixer running on low speed, gradually add up to 3⁄4 cup more flour, 1⁄4 cup at a time, just until dough pulls away from sides of bowl.",
                    "Turn dough out onto a lightly floured work surface. Knead until smooth and elastic, about 10 minutes, adding up to 3⁄4 cup flour, in very small amounts, if necessary to keep dough workable. Place dough in a lightly greased bowl, turning to coat all sides. Cover and let stand in a warm place until dough doubles in size, about 1 hour.",
                    "Cut sausage into 20 to 22 (2-inch-long) straight pieces, reserving curved pieces for another use. Divide dough into 20 to 22 (2-ounce) balls (a little larger than a golf ball). Roll each ball into a 4-inch-wide circle on a lightly floured surface. (Keep remaining dough balls covered while working.) Place about 1 tablespoon of the cheese on lower third of each dough circle, and top with 1 sausage piece. Fold dough over filling, folding in sides; pinch to seal. Place kolaches, seam side down, on 2 baking sheets lined with parchment paper, leaving 1 inch between them. Keep covered while working. Cover loosely with plastic wrap, and let stand in a warm place until dough doubles in size, about 45 minutes.",
                    "Preheat oven to 375°F. Microwave remaining 1⁄4 cup butter in a small microwavable bowl on HIGH until melted, about 45 seconds. Brush kolaches with half of melted butter. Bake in preheated oven until golden brown, 14 to 16 minutes. Brush with remaining melted butter, and serve hot.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings_exception_handling(self):
        self.assertEqual(None, self.harvester_class.ratings())

    def test_ratings_raises_exception(self):
        os.environ["RECIPE_SCRAPERS_SETTINGS"] = "recipe_scrapers.settings.default"
        with self.assertRaises(SchemaOrgException):
            self.assertEqual(None, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "Kolaches are beloved in Texas, but we believe they deserve more widespread attention. Our savory spin on this classic Czech pastry is filled with a combo of smoky Conecuh sausage and sharp Cheddar cheese. Serve with coffee and a fruit salad for a simple yet satisfying breakfast. Leftover kolaches can be reheated in the microwave, but they're best when served fresh out of the oven and still warm.",
            self.harvester_class.description(),
        )
