from recipe_scrapers.allrecipes import AllRecipes
from tests import ScraperTest


class TestAllRecipesScraper(ScraperTest):

    scraper_class = AllRecipes

    def test_host(self):
        self.assertEqual("allrecipes.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Michelle", self.harvester_class.author())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.allrecipes.com/recipe/133948/four-cheese-margherita-pizza/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Four Cheese Margherita Pizza")

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F694708.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "¼ cup olive oil",
                "1 tablespoon minced garlic",
                "½ teaspoon sea salt",
                "8 Roma tomatoes, sliced",
                "2 (12 inch) pre-baked pizza crusts",
                "8 ounces shredded Mozzarella cheese",
                "4 ounces shredded Fontina cheese",
                "10 fresh basil leaves, washed, dried",
                "½ cup freshly grated Parmesan cheese",
                "½ cup crumbled feta cheese",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Stir together olive oil, garlic, and salt; toss with tomatoes, and allow to stand for 15 minutes. Preheat oven to 400 degrees F (200 degrees C).\nBrush each pizza crust with some of the tomato marinade. Sprinkle the pizzas evenly with Mozzarella and Fontina cheeses. Arrange tomatoes overtop, then sprinkle with shredded basil, Parmesan, and feta cheese.\nBake in preheated oven until the cheese is bubbly and golden brown, about 10 minutes.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.8, self.harvester_class.ratings())
