from recipe_scrapers.eatingbirdfood import EatingBirdFood
from tests import ScraperTest


class TestEatingBirdFoodScraper(ScraperTest):

    scraper_class = EatingBirdFood

    def test_host(self):
        self.assertEqual("eatingbirdfood.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Brittany Mullins", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Easy Shakshuka", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.eatingbirdfood.com/wp-content/uploads/2020/12/Shakshuka-in-pan-225x225.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 Tablespoons olive oil",
                "1 large onion, chopped",
                "1 orange bell pepper, chopped",
                "4 cloves garlic, minced",
                "1/2 teaspoon cumin",
                "1/2 teaspoon paprika",
                "1/4 teaspoon cayenne pepper",
                "1-2 teaspoons curry powder",
                "1/4 teaspoon turmeric",
                "1/2 teaspoon sea salt",
                "1/4 teaspoon ground pepper",
                "28 ounce can diced tomatoes",
                "4-5 eggs",
                "1/2 cup feta cheese",
                "fresh cilantro and parsley, for serving",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Heat oil in a large skillet over medium heat. Add onion, bell pepper and garlic to the skillet and cook until onions are soft and fragrant — about 5 to 10 minutes.\nAdd cumin, paprika, cayenne, curry, turmeric, salt and pepper. Give the mixture a stir and cook for about 1 minute more. Add diced tomatoes to the skillet and bring sauce to a boil. Reduce heat to a simmer and cook until the sauce thickens up a bit, about 10 minutes. Add feta cheese to the tomato mixture and stir.\nCrack eggs into tomato sauce. You should be able to fit 4-5 eggs in a large skillet. Cover and let the eggs cook for about 5 minutes, or until the egg whites are completely cooked through. Remove skillet from heat, uncover and let sit for a 1-2 minutes before serving.\nSpoon 1-2 eggs along with a big serving of tomato sauce on to each plate. Garnish with extra feta cheese and fresh cilantro and parsley. Serve with toast, veggies or over a whole grain like quinoa or brown rice for a complete meal.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
