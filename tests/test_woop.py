from recipe_scrapers.woop import Woop
from tests import ScraperTest


class TestWoopScraper(ScraperTest):
    scraper_class = Woop

    def test_host(self):
        self.assertEqual("woop.co.nz", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Pan-seared beef",
        )

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 pack of beef sirloin",
                "1 pack of steamed brown rice",
                "1 pot of Korean seasoning",
                "1 pot of sesame drizzle",
                "1 pot of kimchi",
                "1 sachet of sesame sprinkle",
                "1 pot of edamame and peas",
                "1 capsicum",
                "1 bag of bok choy",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            """1. TO PREPARE THE VEGETABLES: Slice the capsicum into ½ cm slices. Cut the root end off the bok choy, discard and slice into 1 cm slices. Finely slice the kimchi.
2. TO COOK THE KIMCHI RICE: Spray a non-stick frying pan with oil and place over a medium-high heat. Once hot add the sliced capsicum and cook for 2-3 mins stirring occasionally to create a char. Open the bag of steamed brown rice, squeezing gently on the bag to break up any large clumps and add to the pan with the bok choy, edamame and peas and cook for 1-2 mins. Pour in the Korean seasoning and add half the kimchi, stir and cook for 1-2 mins. Season with salt to taste, remove from the pan and cover to keep warm.
3. TO COOK THE BEEF SIRLOIN: Remove the beef sirloin from its packaging and pat dry with a paper towel. Respray the pan with oil and place over a high heat. Season the beef with salt and pepper and place in the hot pan. Cook for 2-3 mins each side for medium-rare, a little longer for well done. Rest for 1-2 mins before slicing.
TO SERVE: Spoon kimchi fried rice onto plates and top with sliced beef sirloin. Dollop with sesame drizzle and sprinkle remaining kimchi and sesame sprinkle on top.""",
            self.harvester_class.instructions(),
        )

    def test_nutrients(self):
        return self.assertEqual(
            {
                "Energy": "2322kj (554Kcal)",
                "Protein": "43g",
                "Carbohydrate": "43g",
                "Fat": "23g",
                "Contains": "Soy, Sesame, Gluten, Milk, Egg",
            },
            self.harvester_class.nutrients(),
        )

    def test_image(self):
        self.assertEqual(
            "https://woop.co.nz/media/catalog/product/cache/f4f005ad5960ef8c7b8a08a9a3fc244e/b/-/b-pan-seared-beef_s64dydtpoves1rbu.jpg",
            self.harvester_class.image(),
        )
