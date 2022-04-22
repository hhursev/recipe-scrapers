from recipe_scrapers.meljoulwan import Meljoulwan
from tests import ScraperTest


class TestMeljoulwanScraper(ScraperTest):

    scraper_class = Meljoulwan

    def test_host(self):
        self.assertEqual("meljoulwan.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Melissa Joulwan", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Chicken Pesto Meatballs in Marinara Sauce", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Poultry,Recipes,Whole30", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://meljoulwan.com/wp-content/uploads/2014/03/pestochicken.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1/2 cup (packed) fresh basil leaves",
                "1/4 cup fresh parsley leaves",
                "1/4 cup walnuts",
                "1 clove garlic, smashed and peeled",
                "1 tablespoon extra-virgin olive oil",
                "3/4 teaspoon salt",
                "1/4 teaspoon ground black pepper",
                "dash crushed red pepper flakes",
                "1 pound ground chicken",
                "2 tablespoons warm water",
                "1/2 teaspoon cream of tartar",
                "1/4 teaspoon baking soda",
                "1 teaspoon extra-virgin olive oil",
                "1-2 cloves garlic, minced",
                "1 (14.5 ounce) can crushed tomatoes",
                "1 \xa0(8 ounce) can tomato sauce",
                "1/2 teaspoon salt",
                "1/4 teaspoon ground black pepper",
                "10 large fresh basil leaves, slivered",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "1. Place the basil, parsley, walnuts, garlic, olive oil, salt, pepper, and red pepper flakes in the bowl of a food processor and purée until it forms a uniform paste. You may need to scrape down the sides a few times to get it to the right texture.",
                    "2. Place the ground chicken in a large bowl, then add the pesto. In a small bowl or measuring cup, mix the water with the cream of tartar and baking soda \xa0— it will fizz a little. Add to the bowl with the chicken and mix until all ingredients are evenly distributed. Cover and refrigerate at least 20 minutes and up to overnight.",
                    "3. While the meat is chilling, start the sauce. Heat a large non-stick skillet over low heat and add the olive oil. When the oil is warm, about 2 minutes, add the crushed garlic and when it’s fragrant, about 30 seconds, add the tomatoes. Stir to combine and bring to a very low simmer.",
                    "4. Remove the chicken dough from the fridge. Moisten your hands with cold water and shake to remove excess. Measure a rounded tablespoon of chicken and roll into a ball between your palms. Place gently in the tomato sauce. Repeat until all the balls are nestled into the sauce. It’s OK if they touch each other and aren’t completely submerged.",
                    "5. Cook the meatballs in the tomato sauce, covered, about 25 minutes. Remove the lid from the pan and allow to cook another 5-10 minutes to allow the sauce to thicken a little. Add the fresh basil leaves, stir, and serve on spaghetti squash or zucchini noodles. Bonus if you drizzle with a little extra-virgin olive oil.",
                ]
            ),
            self.harvester_class.instructions(),
        )
