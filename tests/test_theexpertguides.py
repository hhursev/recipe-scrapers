from recipe_scrapers.theexpertguides import TheExpertGuides
from tests import ScraperTest


class TestTheExpertGuidesScraper(ScraperTest):
    scraper_class = TheExpertGuides

    def test_host(self):
        self.assertEqual("theexpertguides.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            "Coconut Milk Pasta Sauce Recipe", self.harvester_class.title()
        )

    def test_author(self):
        self.assertEqual("Anne Maxwell", self.harvester_class.author())

    def test_category(self):
        self.assertEqual("Main Course", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(28, self.harvester_class.total_time())

    def test_prep_time(self):
        self.assertEqual(15, self.harvester_class.prep_time())

    def test_cook_time(self):
        self.assertEqual(15, self.harvester_class.cook_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://theexpertguides.com/wp-content/uploads/2022/08/pexels-photo-1487511-1.webp",
            self.harvester_class.image(),
        )

    def test_language(self):
        self.assertEqual("en-US", self.harvester_class.language())

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 lb pasta of your choice",
                "4-5 garlic cloves (minced )",
                "1 can chopped tomatoes",
                "1 can coconut milk",
                "1/2 cup vegetable stock",
                "Fresh basil and oregano",
                "2 tbsp olive oil",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        test_instructions = """In a large pan bring water to a boil. When it starts boiling, add a generous amount of salt (2 tbsp) and cook the pasta according to the instructions on the package.
When cooked, drain the pasta and keep it aside.
Take a saucepan to make the coconut milk pasta sauce.
In the saucepan, heat olive oil and add minced garlic. Stire for 30 seconds and make sure it doesn't burn.
Add chopped tomatoes and stir for 2-3 minutes.
Pour in the vegetable broth and coconut milk.
Bring the sauce to a boil and cook for 10 minutes on medium heat without the lid. Cook the sauce until its creamy and thickened.
Add chopped basil and dried oregano with salt and pepper to taste.
Combine the cooked pasta in the sauce, and serve hot."""
        self.assertEqual(test_instructions, self.harvester_class.instructions())

    def test_cuisine(self):
        self.assertEqual("Italian", self.harvester_class.cuisine())

    def test_nutrients(self):
        self.assertEqual(
            {
                "calories": "638 kcal",
                "servingSize": "1 serving",
            },
            self.harvester_class.nutrients(),
        )

    def test_description(self):
        self.assertEqual(
            "Coconut milk pasta sauce is a super easy vegan pasta recipe that's creamy, flavourful, and just the perfect sauce for pasta ready in 15 minutes.",
            self.harvester_class.description(),
        )
