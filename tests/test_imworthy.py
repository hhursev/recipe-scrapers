from recipe_scrapers.imworthy import ImWorthy
from tests import ScraperTest


class TestImWorthyScraper(ScraperTest):

    scraper_class = ImWorthy

    def test_host(self):
        self.assertEqual("im-worthy.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Shana Thomas", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Vegan Almond Flour Pancakes (Fluffy & Gluten-free)",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual(
            "Breakfast,Brunch,Main Course", self.harvester_class.category()
        )

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.im-worthy.com/wp-content/uploads/2020/11/Almond-Flour-Pancakes_Blog4.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        ingredients = [
            "1/2 cup almond flour",
            "1 cup oat flour (or all-purpose flour)",
            "1/2-1 cup non-dairy milk (plus more, if needed)",
            "2 tsp baking powder",
            "1/2 tsp cinnamon (optional) (can sub for vanilla extract)",
            "pinch of salt",
            "1 tbsp unsweetened apple sauce or maple syrup (optional)",
            "1 tsp grapeseed oil (for cooking. Add more, if needed. can sub for coconut or avocado oil)",
        ]
        self.assertEqual(ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        self.assertEqual(
            "In separate bowls: mix the wet & dry ingredients.\nAdd the wet ingredients to the dry ingredients and stir until combined. Let the pancake batter rest for 5 minutes to thicken while you heat the pan according the next steps below.\nAdd the oil to a nonstick pan over medium heat. Once the pan is hot pour the batter into the pan using a 1/4 measuring cup (for easy clean up). Cook on each side for about 2-5 minutes (depends on your pan) or until you see little bubbles form on top, then flip and let them cook for another couple of minutes.\nServe with your favorite toppings. Some suggestions include maple syrup, coconut whip cream, fresh berries, or vegan butter.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "These almond flour pancakes are sweet, fluffy and easy to make. They're vegan, gluten-free and can easily be made keto-friendly. Serve with fresh fruit or maple syrup.",
            self.harvester_class.description(),
        )
