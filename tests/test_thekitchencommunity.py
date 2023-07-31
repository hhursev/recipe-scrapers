# mypy: allow-untyped-defs

from recipe_scrapers.thekitchencommunity import TheKitchenCommunity
from tests import ScraperTest


class TestTheKitchenCommunityScraper(ScraperTest):

    scraper_class = TheKitchenCommunity

    def test_host(self):
        self.assertEqual("thekitchencommunity.org", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Cassie Marshall", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Our BEST Crock Pot Mac and Cheese Recipe", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Side Dish", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(125, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://thekitchencommunity.org/wp-content/uploads/2022/01/shutterstock_556523302-1200x801.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1 pound pasta",
            "2 1/3 cups of milk",
            "12 oz evaporated milk",
            "12 oz shredded sharp cheddar",
            "1 cup American cheese shredded",
            "1 1/4 teaspoon salt",
            "1/2 teaspoon pepper",
            "1/2 teaspoon dry ground mustard",
            "1/3 teaspoon garlic powder",
            "A sprinkle of cayenne pepper",
            "1/4 cup of butter",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = """Spray your crockpot with non-stick spray.
    Rinse your uncooked pasta in a strainer and drain out all the excess water.
    Add your uncooked pasta to your crockpot along with your milk, cheese, mustard, garlic, salt, pepper, and cayenne. Stir everything well so all the ingredients mix together and make sure the macaroni is in the liquid as much as possible.
    Add your cubed butter.
    Cover your crock pot and turn on the low heat and cook for 1 hour. Remove the lid and stir all your ingredients before replacing the lid. Check the consistency because your dish may be done or require an additional 1-2 hours.
    Check your dish every half hour if it is not done and remember to stir when checking your dish.
    You will know your mac and cheese is done if the pasta is tender and the liquid is thick and creamy. Once you remove the lid, keep in mind the sauce will thicken even more as the mac and cheese sits."""

        actual_instructions = self.harvester_class.instructions()
        expected_lines = [line.strip() for line in expected_instructions.splitlines()]
        actual_lines = [line.strip() for line in actual_instructions.splitlines()]

        self.assertSequenceEqual(expected_lines, actual_lines)

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        expected_description = "Simply the BEST Crockpot Mac and Cheese recipe out there. Give it a try!Don't cook the noodles for this recipe, just throw in your milk, cheese, and seasonings together in the slow cooker and you'll have a delicious family meal ready in no time!"
        self.assertEqual(expected_description, self.harvester_class.description())
