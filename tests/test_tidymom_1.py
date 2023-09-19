# mypy: allow-untyped-defs

from recipe_scrapers.tidymom import TidyMom
from tests import ScraperTest


class TestTidyMomScraper(ScraperTest):

    scraper_class = TidyMom
    test_file_name = "tidymom_1"

    def test_host(self):
        self.assertEqual("tidymom.net", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("TidyMom", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Chicken Bacon Ranch Pizza", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Main Dish", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://tidymom.net/blog/wp-content/uploads/2021/04/chicken-bacon-ranch-pizza-pic-480x480.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1 pizza crust",
            "1 teaspoon olive oil",
            "1-2 teaspoons Italian seasoning",
            "1 teaspoon garlic powder",
            "2/3 cup ranch dressing",
            "1 tomato, sliced and diced",
            "1/4 cups green onion, chopped",
            "1½ cup shredded mozzarella cheese *(see notes)",
            "1½ cups shredded cheddar cheese *(see notes)",
            "1/4 cup Parmesan cheese",
            "1½ cup chopped or shredded cooked chicken *(see notes)",
            "4 slices of bacon, cooked and crumbled *(see notes)",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = (
            "Preheat oven to 425° F\n"
            "Put the pizza crust on a pizza pan or pizza peel. Using a pastry brush, lightly brush the entire crust with olive oil and season with Italian seasoning and garlic powder.\n"
            "Evenly spread ranch dressing over the crust.\n"
            "Sprinkle with cheese then top with chicken, tomatoes, green onions, and bacon crumbs.\n"
            "Place the pizza* in the oven for 15-20 minutes or until cheese is melted and crust is golden. Let rest for several minutes, then cut and serve."
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        expected_description = "Chicken, smokey bacon, creamy ranch, and lots of gooey melted cheese are the perfect combo to pile on a pizza crust!"
        self.assertEqual(expected_description, self.harvester_class.description())
