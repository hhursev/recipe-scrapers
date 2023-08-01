# mypy: allow-untyped-defs

from recipe_scrapers.therecipecritic import Therecipecritic
from tests import ScraperTest


class TestTherecipecriticScraper(ScraperTest):

    scraper_class = Therecipecritic

    def test_host(self):
        self.assertEqual("therecipecritic.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("The Recipe Critic", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Burrata Appetizer", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Appetizer,Side Dish", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://therecipecritic.com/wp-content/uploads/2023/07/burrata-appetizer.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 tablespoons olive oil",
                "1 shallot, (minced)",
                "2 cloves garlic, (minced)",
                "2 teaspoons fresh thyme",
                "2 cups cherry tomatoes, (halved)",
                "½ cup dried figs, (quartered)",
                "½ teaspoon kosher salt",
                "½ teaspoon pepper",
                "¼ cup balsamic vinegar",
                "16 ounces burrata cheese",
                "fresh basil, (coarsely chopped)",
                "additional kosher salt, to taste",
                "1 baguette, (sliced and toasted for serving)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "In a large skillet, heat the olive oil over medium-high heat.\nAdd the shallot and saute for 4-5 minutes. Add the garlic and thyme, and saute for an additional minute.\nAdd the tomatoes, figs, salt, and pepper. Cover and saute for about 10-12 minutes undisturbed.\nRemove the lid, add the balsamic vinegar, then stir. Reduce heat to medium and continue to saute until any excess liquid has cooked off, stirring occasionally.\nRemove the skillet from heat and let the tomatoes and figs rest for about 8-10 minutes to cool the skillet slightly.\nPlace the burrata on top of the tomatoes and figs. Garnish with fresh basil and kosher salt.\nServe with toasted baguette, sourdough, or your favorite dipping bread!",
            self.harvester_class.instructions(),
        )

    def test_cuisine(self):
        self.assertEqual("Italian,Italian American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "This burrata appetizer is a flavor bomb made with juicy cherry tomatoes, sweet dried figs, and a tangy balsamic kick. Topped with creamy burrata cheese, it's pure indulgence. Perfect for parties or whenever you want to treat yourself to something special!",
            self.harvester_class.description(),
        )
