from recipe_scrapers.realsimple import RealSimple
from tests import ScraperTest


class TestRealSimpleScraper(ScraperTest):

    scraper_class = RealSimple

    def test_host(self):
        self.assertEqual("realsimple.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.realsimple.com/food-recipes/browse-all-recipes/classic-cheesecake-recipe",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Classic Cheesecake")

    def test_image(self):
        self.assertEqual(
            "https://www.realsimple.com/thmb/EFNZU3tZG_O0FvomS1ExHzse4qI=/300x300/smart/filters:no_upscale()/classic-cheesecake_300-70617627cf5f4f5eae7f1a11018713ec.jpg",
            self.harvester_class.image(),
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Dawn Perry")

    def test_total_time(self):
        self.assertEqual(270, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("10 servings", self.harvester_class.yields())

    def test_ingredients(self):
        expected_ingredients = [
            "Cake:",
            "18 graham crackers (2 sleeves)",
            "½ cup (1 stick) unsalted butter, melted",
            "¼ teaspoon kosher salt",
            "1 cup plus 4 tablespoons sugar",
            "3 8-ounce packages cream cheese, at room temperature",
            "2 cups sour cream, at room temperature",
            "1 ½ teaspoons pure vanilla extract",
            "3 large eggs, at room temperature",
            "Cherry sauce:",
            "1 10-ounce bag frozen cherries",
            "½ cup sugar",
            "¼ teaspoon kosher salt",
            "1 tablespoons cornstarch",
            "2 tablespoons fresh lemon juice",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        self.assertEqual(
            "Make the cake: Heat oven to 325° F. In a food processor, pulse the graham crackers until fine crumbs form. Add the butter, salt, and 2 tablespoons of the sugar and pulse to combine. Using a straight-sided dry measuring cup, press the mixture into the bottom and 2 inches up the sides of a 9-inch springform pan.\nUsing an electric mixer, beat the cream cheese and 1 cup of the remaining sugar on medium speed until smooth. Add 1 cup of the sour cream and 1 teaspoon of the vanilla and beat to combine. Beat in the eggs one at a time. Pour the mixture into the crust and bake until just set (the center will be slightly wobbly), 50 to 60 minutes.\nIn a small bowl, combine the remaining 1 cup of sour cream, 2 tablespoons of sugar, and ½ teaspoon of vanilla. Spread over the hot cheesecake, then bake until set, 3 to 5 minutes more. Let cool to room temperature in the pan, then refrigerate for at least 2 hours. Run a knife around the edge of the cheesecake before unmolding.\nM ake the cherry sauce: In a large skillet, combine the cherries, sugar, salt, and 2 tablespoons water. Cook over medium-high heat, stirring often, until the mixture begins to thicken, 4 to 6 minutes.\nIn a small bowl, stir together the cornstarch and 2 tablespoons water. Add to the cherries in the skillet and cook, stirring, until the mixture is thick and syrupy, 1 to 2 minutes. Stir in the lemon juice. Let cool completely. Serve with the cheesecake.",
            self.harvester_class.instructions(),
        )
