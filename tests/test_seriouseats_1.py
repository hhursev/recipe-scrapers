from recipe_scrapers.seriouseats import SeriousEats
from tests import ScraperTest


class TestSeriousEats(ScraperTest):

    scraper_class = SeriousEats

    @property
    def test_file_name(self):
        return "{}_1".format(self.scraper_class.__name__.lower())

    def test_host(self):
        self.assertEqual("seriouseats.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.seriouseats.com/old-fashioned-flaky-pie-dough-recipe",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Stella Parks")

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Buttery, Flaky Pie Crust Recipe"
        )

    def test_total_time(self):
        self.assertEqual(150, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("20 servings", self.harvester_class.yields())

    def test_image(self):
        # image has hash keys in it so the full url isn't consistent
        # i.e. https://www.seriouseats.com/thmb/gnvQg8_1sB7B1moyDaadHT3pQJo=/960x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__recipes__images__2015__07__20150727-horseradish-vicky-wasik-14-2819caaee55a40cfab06ef8cd257094d.jpg
        self.assertTrue(
            "decorative-pie-crust-vicky-wasik" in self.harvester_class.image()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "8 ounces low-protein all-purpose flour, such as Gold Medal Blue Label (1 2/3 cups; 225g), plus more for dusting",
                "1/2 ounce sugar (1 tablespoon; 15g)",
                "1 teaspoon (4g) Diamond Crystal kosher salt; for table salt, use half as much by volume or use the same weight",
                "8 ounces unsalted, American-style butter, straight from the fridge (2 sticks; 225g), cold",
                "4 ounces cold tap water (1/2 cup; 115g)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "For the Dough: Whisk flour, sugar, and salt together in a medium bowl. Cut butter into cubes no smaller than 1/2 inch, and toss with flour mixture to break up the pieces. With your fingertips, smash each cube flat—that's it! No rubbing or cutting. Stir in water, then knead dough against sides of the bowl until it comes together in a shaggy ball. Dough temperature should register between 65 and 70°F (18 and 21°C); if not, refrigerate briefly before rolling and folding (see note).\nMake the Layers: On a generously floured work surface, roll dough into a roughly 10- by 15-inch rectangle. Fold the 10-inch sides to the center, then close the newly formed packet like a book. Fold in half once more, bringing the short sides together to create a thick block. Divide in half with a sharp knife or bench scraper. Dough temperature should still be somewhere between 65 and 70°F (18 and 21°C); if not, refrigerate briefly before proceeding (see note).\nFor Single-Crusted Pies: Using as much flour as needed, roll one piece into a 14-inch circle; this size allows ample room to line pie plate, with enough overhang to form a generous border. At smaller sizes, dough will fall short, making it difficult to shape edges, and thicker dough will not crisp as intended. Transfer to 9-inch pie plate; dough should be easy to handle, and will not require any special procedures to move. Dust off excess flour with a pastry brush, using it to nestle dough into corners of pan. With scissors or kitchen shears, trim edge so that it overhangs by 1 1/4 inches. Fold overhang over itself to create thick border that sits on top edge of pie plate, not below. Crimp or shape crust as desired. Repeat with remaining dough. Wrap with plastic and refrigerate at least 2 hours and up to overnight. Use as directed in your favorite recipe.\nFor a Double-Crusted Pie: Using as much flour as needed, roll one piece into a 14-inch circle; this size allows ample room to line pie plate, with enough overhang to form a generous border. At smaller sizes, dough will fall short, making it difficult to shape edges, and thicker dough will not crisp as intended. Transfer to 9-inch pie plate; dough should be easy to handle, and will not require any special procedures to move. Dust off excess flour with a pastry brush, using it to nestle dough into corners of pan. With scissors or kitchen shears, trim edge so that it overhangs by 1 1/4 inches. For solid top crust, roll remaining dough as before; for lattice-top pie, roll into a 9- by 15-inch rectangle instead. Transfer to a baking sheet or parchment-lined cutting board. (The parchment will prevent dough from absorbing any savory odors from the board.) Wrap both portions in plastic and refrigerate at least 2 hours and up to overnight. Use as directed in your favorite recipe; after filling pie and sealing crusts together, refrigerate 30 minutes before baking.\nFor a Blind-Baked Pie : Adjust oven rack to lower-middle position and preheat to 350°F (180°C). Line pie shell that has been chilled for at least 2 hours (as outlined in Step 3) with large sheet of aluminum foil, pressing so it conforms to curves of plate. (A second sheet of foil may be needed for full coverage.) Fill to brim with sugar, transfer to a half sheet pan, and bake until fully set and golden around the edges, 60 to 75 minutes. Fold long sides of foil toward middle, gather short sides, and use both hands to carefully transfer sugar to heat-safe bowl. Let sugar cool to room temperature. If needed, continue baking crust a few minutes more to brown along the bottom.",
            self.harvester_class.instructions(),
        )
