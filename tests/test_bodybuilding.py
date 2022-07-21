from recipe_scrapers.bodybuilding import Bodybuilding
from tests import ScraperTest


class TestBodybuildingScraper(ScraperTest):

    scraper_class = Bodybuilding

    def test_host(self):
        self.assertEqual("bodybuilding.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual(
            "Shannon Clark and Danielle Christine", self.harvester_class.author()
        )

    def test_title(self):
        self.assertEqual("Spicy Beans and Rice", self.harvester_class.title())

    def test_category(self):
        self.assertEqual(
            "Side Dishes,Vegetarian,High-Protein", self.harvester_class.category()
        )

    def test_total_time(self):
        self.assertEqual(75, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.bodybuilding.com/images/2021/october/spicy-beans-and-rice-header-960x540.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 tbsp olive oil",
                "2 clove garlic, minced",
                "1 red onion, diced",
                '1 stalk, medium (7-1/2" - 8" long) celery, peeled and chopped',
                "1 cup mushrooms, sliced",
                "1 15 oz. can red kidney beans",
                "1 tbsp hot sauce",
                "1 tsp paprika",
                "2½ cup low-sodium vegetable broth",
                "1 tsp vegetable bouillon",
                "1 cup wild rice, uncooked",
                "1 tbsp grass-fed butter",
                "1 tbsp green onion, chopped",
                "1 salt and pepper to taste",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """1. Dice the celery, red onion, and mushrooms.
2. Heat the butter in a skillet over medium heat. Add all of the vegetables and stir-fry for 3-4 minutes or until vegetables are tender. Set aside.
3. Bring broth to a boil in a large pot. Stir in wild rice, hot sauce, paprika, and bouillon and cook 45-60 minutes or until rice is tender.
4. Add olive oil and garlic to a skillet and quickly sauté. Remember that garlic burns quickly, so it is important to keep a close eye on it. Add in the cooked rice, beans, and cooked vegetables.
5. Stir-fry for 3-5 minutes to crisp up the rice and serve. Garnish with chopped green onion.
6. Optional: Add any other vegetables you prefer.""",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "This one-dish meal has it all—flavorful wild rice, protein-rich beans, heart-healthy vegetables, and just the perfect amount of spice to make you come back for more every time. This dish is also quick and easy to prepare, making it ideal for those who just don't have time to dedicate hours to preparing lunch or dinner.",
            self.harvester_class.description(),
        )
