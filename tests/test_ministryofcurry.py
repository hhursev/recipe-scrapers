# mypy: allow-untyped-defs

from recipe_scrapers.ministryofcurry import MinistryOfCurry
from tests import ScraperTest


class TestMinistryOfCurryScraper(ScraperTest):

    scraper_class = MinistryOfCurry

    def test_host(self):
        self.assertEqual("ministryofcurry.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            "Slow Cooker EASY Chicken Tikka Masala", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("dinner,Entree", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(270, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://ministryofcurry.com/wp-content/uploads/2019/10/Pomi-Chicken-Tikka-Masala-1-2.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "2 pounds chicken breasts (skinless boneless)",
            "2½ teaspoons kosher salt",
            "1 tablespoon lemon juice",
            "3 tablespoons plain yogurt",
            "1 tablespoon kashmiri red chili powder",
            "½ teaspoon ground turmeric",
            "1½ teaspoon garam masala",
            "1 tablespoon ginger (grated)",
            "1 tablespoon garlic (minced)",
            "2 tablespoons oil",
            "2 medium yellow onions (finely diced)",
            "1½ cups tomato puree",
            "½ to ¾ cup heavy cream",
            "1 to 2 tablespoons tomato paste",
            "2 tablespoons dried fenugreek leaves (kasoori methi)",
            "½ cup cilantro (chopped)",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        expected_instructions = "Cut the chicken breasts into 2 to 3-inch cubes. Add 2 teaspoon salt and lemon juice and mix well. Add yogurt, red chili powder, turmeric, garam masala, ginger, and garlic. Mix well and allow to marinate while you prep the remaining ingredients.\nHeat oil in a medium pan. Add onions and 1/2 teaspoon of salt. Cook over medium heat for 5 minutes stirring frequently until the onions start to soften and turn translucent. Note: If you are using Instant Pot as a slow cooker, you can saute in the instant pot itself.\nAdd the cooked onions to the crockpot / slow cooker and spread it evenly. Evenly layer tomato puree over the onions. Line the marinated chicken over the tomato puree. Place the crockpot lid and set the cooking time to Slow Cook (Hi) and adjust the cooking time to 4 hours.\nAfter 4 hours, your kitchen will be filled with the beautiful aromas of the curry. Add heavy cream, crush the fenugreek leaves on the palm of your hands and add to the curry. Mix well, taste, and add tomato paste. Mix well and more cream if needed. Note: Optionally you can add 1 teaspoon of sugar to balance all the flavors. Garnish with cilantro and enjoy with basmati rice and naan.\nNotes:\nTo make chicken tikka masala without cream or dairy-free, you can either use unsweetened coconut cream (I love Trader Joe's) or homemade cashew cream. To make the cashew cream at home simply blend 1/2 cup of cashews in half a cup of warm water and make a smooth paste.\nI have tested this recipe using a Crockpot slow cooker, Instant Pot slow cooker function, and Instant Pot AURA Multi Cooker. The advantage with the Instant Pot models is that you can saute the onions in the same pot. With a crockpot slow cooker, you saute the onions in a separate pan on the stovetop.\nIf you do not have a good brand of tomato puree like the Pomi one, you can puree 3 fresh tomatoes in a blender and use that instead.\nI like to use chicken breasts in this recipe, but you can also use chicken thighs, simply cut each thigh into 2 pieces."
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(4.7, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Indian", self.harvester_class.cuisine())

    def test_description(self):
        expected_description = "Tender chicken marinated in aromatic spices is slow cooked in a delicious tomato-based curry for the best Indian meal."
        self.assertEqual(expected_description, self.harvester_class.description())
