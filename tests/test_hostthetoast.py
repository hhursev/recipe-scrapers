from recipe_scrapers.hostthetoast import Hostthetoast
from tests import ScraperTest


class TestHostthetoastScraper(ScraperTest):

    scraper_class = Hostthetoast

    def test_host(self):
        self.assertEqual("hostthetoast.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://hostthetoast.com/homemade-garlic-naan/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Homemade Garlic Naan")

    def test_yields(self):
        self.assertEqual("12 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://hostthetoast.com/wp-content/uploads/2018/08/naan-202-320x320-1-225x225.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1/4 cup warm water",
                "1 tablespoon sugar",
                "1 package (2 1/4 teaspoons) active dry yeast",
                "3/4 cup warm milk",
                "3/4 cup plain yogurt",
                "4 cups all-purpose flour",
                "1 teaspoon Kosher salt",
                "1 stick melted butter, for brushing",
                "4 cloves minced garlic",
                "Fresh cilantro, to top",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "In a glass measuring cup, combine the yeast, sugar, and water and let sit until very foamy, about 10 minutes. Meanwhile, whisk the flour and salt together in a large bowl and create a well in the center.\nWhisk in the warm milk and plain yogurt into the yeast mixture until well-combined. Pour into the well in the dry ingredients. Stir until a dough is formed, then turn out onto a lightly-floured surface and knead until smooth, about 3-4 minutes. Transfer the dough to a large, lightly oiled bowl and cover loosely with a damp kitchen towel. Let rise at room temperature until doubled in size, about 1 hour.\nTurn the dough out onto a floured surface. Knead briefly into a disc and cut the dough into 12 equal-sized pieces. Roll each piece into a ball.\nHeat a large, heavy bottomed skillet over medium heat. Roll each dough ball out until it is about 1/4 inch thick and approximately 6 inches wide. Brush the dough lightly with butter and place one at a time onto the hot skillet. Cook until large bubbles form on the surface, about 2 minutes. Flip the dough and cook the other side until golden, about 1-2 more minutes. Stack the cooked flat bread on a plate and cover with a towel to keep warm as you cook the remaining pieces.\nAdd the minced garlic to the remaining melted butter. Loosely cover and microwave for 15 seconds. Brush the warm naan with the garlic butter (scooping out some of the garlic to sit on top) and sprinkle generously with cilantro. Serve warm.",
            self.harvester_class.instructions(),
        )
