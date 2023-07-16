from recipe_scrapers.afghankitchenrecipes import AfghanKitchenRecipes
from tests import ScraperTest


class TestafghankitchenrecipesScraper(ScraperTest):

    scraper_class = AfghanKitchenRecipes

    def test_host(self):
        self.assertEqual("afghankitchenrecipes.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("nash", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Mantu (Beef Dumplings)", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(75, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "http://www.afghankitchenrecipes.com/wp-content/uploads/2014/04/manto4-250x212.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 cups of Onions",
                "1 pound of Ground Beef/Lamb",
                "½ tsp. Garlic",
                "2 tsp. Coriander Powder",
                "½ tsp. Salt",
                "½ tsp. Black Pepper Powder (freshly ground)",
                "1 cup Chana Lentils",
                "½ pound Ground Beef/Lamb",
                "1 medium Onion (finely chopped)",
                "½ tsp. Garlic",
                "½ tsp. Salt",
                "½ tsp. Black Pepper Powder (freshly ground)",
                "2 tsp. Tomato Paste",
                "30 ml. Cooking Oil",
                "1 tsp. Dried Mint Leaves",
                "½ tsp. Garlic",
                "½ tsp. Salt",
                "500 ml. Plain Yogurt",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Heat pan over a medium heat and add garlic, ground beef and salt and coriander. Cook until the meat is half-way cooked for about 15 to 20 minutes.",
                    "Add black pepper and remove from heat.",
                    "Combine one cup of raw chopped onions to the meat and let it cool down to room temperature",
                    "Soak split peas for 2–3 hours or overnight.",
                    "Heat oil in a frying pan and cook onion and garlic until lightly browned.",
                    "Add tomato and tomato paste. Add split peas and ¾ cup water and cook for 30–45 minutes until soft.",
                    "Season with salt and pepper and set aside.",
                    "Combine all of the ingredients for dip in a bowl and mix well.",
                    "Place flour in a large mixing bowl and gradually add water, mixing with hands until it becomes doughy.",
                    "Leave the dough to settle for 15–20 minutes or until it becomes firm.",
                    "Separate dough into small handfuls and roll into individual ball shapes.",
                    "Scatter some flour on the bench surface and using a small rolling pin, roll the balls into circular shapes.",
                    "Roll the dough ball into a very thin (1/16-inch) strips using a pasta machine. Cut the strips into 2-inch squares.",
                    "Place approximately one tablespoon of the cooled ground beef and onion mixture onto each wrap. To make the wraps stick together easily, wet the edges with water (you may use your fingers or a basting brush).",
                    "Fold over first two opposite ends of the egg roll wrap and followed by other two ends to enclose dumplings. Press the edges tightly to seal together. Continue with the remaining wraps.",
                    "Take the racks out of the steamer dish. Add water to the dish, cover and bring to boil.",
                    "Oil the base of steamer to prevent sticking and place dumplings carefully across oil.",
                    "Cover lid and cook for approximately 40 minutes.",
                    "When the dumplings have cooked, add a thin layer of the yogurt mixture to a large serving plate. Place the steamed dumplings on top.",
                    "Pour some more of the yogurt mixture on top of the dumplings and coat everything with the the topping sauce.",
                    "Garnish with dried mint and a little bit of cayenne pepper.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(3.5, self.harvester_class.ratings())
