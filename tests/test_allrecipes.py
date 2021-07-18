from recipe_scrapers.allrecipes import AllRecipes
from tests import ScraperTest


class TestAllRecipesScraper(ScraperTest):

    scraper_class = AllRecipes

    def test_host(self):
        self.assertEqual("allrecipes.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Michelle", self.harvester_class.author())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.allrecipes.com/recipe/133948/four-cheese-margherita-pizza/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Four Cheese Margherita Pizza")

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F694708.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "¼ cup olive oil",
                "1 tablespoon minced garlic",
                "½ teaspoon sea salt",
                "8 Roma tomatoes, sliced",
                "2 (12 inch) pre-baked pizza crusts",
                "8 ounces shredded Mozzarella cheese",
                "4 ounces shredded Fontina cheese",
                "10 fresh basil leaves, washed, dried",
                "½ cup freshly grated Parmesan cheese",
                "½ cup crumbled feta cheese",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Stir together olive oil, garlic, and salt; toss with tomatoes, and allow to stand for 15 minutes. Preheat oven to 400 degrees F (200 degrees C).\nBrush each pizza crust with some of the tomato marinade. Sprinkle the pizzas evenly with Mozzarella and Fontina cheeses. Arrange tomatoes overtop, then sprinkle with shredded basil, Parmesan, and feta cheese.\nBake in preheated oven until the cheese is bubbly and golden brown, about 10 minutes.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.8, self.harvester_class.ratings())

    def test_nutrients(self):
        nutes = self.harvester_class.nutrients()
        self.assertEqual(nutes, {
             "calcium": "424.5mg",
             "calcium%": "43",
             "calories": "551.4 calories",
             "carbohydrateContent": "54.4 g",
             "carbohydrates": "54.4g",
             "carbohydrates%": "18",
             "cholesterol": "58.4mg",
             "cholesterol%": "20",
             "cholesterolContent": "58.4 mg",
             "dietary fiber": "2.8g",
             "dietary fiber%": "11",
             "fat": "25.6g",
             "fat%": "39",
             "fatContent": "25.6 g",
             "fiberContent": "2.8 g",
             "folate": "16.8mcg",
             "folate%": "4",
             "iron": "1.8mg",
             "iron%": "10",
             "magnesium": "21.9mg",
             "magnesium%": "8",
             "niacin equivalents": "3.6mg",
             "niacin equivalents%": "28",
             "potassium": "200.5mg",
             "potassium%": "6",
             "protein": "28.9g",
             "protein%": "58",
             "proteinContent": "28.9 g",
             "saturated fat": "11g",
             "saturated fat%": "55",
             "saturatedFatContent": "11 g",
             "sodium": "1182.5mg",
             "sodium%": "47",
             "sodiumContent": "1182.5 mg",
             "thiamin": "0.1mg",
             "thiamin%": "6",
             "vitamin a iu": "882.5IU",
             "vitamin a iu%": "18",
             "vitamin b6": "0.1mg",
             "vitamin b6%": "9",
             "vitamin c": "8.3mg",
             "vitamin c%": "14",
         })

    def test_nutrients_unitized(self):
        nutes_ext = self.harvester_class.nutrients_unitized()
        self.assertEqual(nutes_ext, {
            "calcium": (424.5, "mg"),
            "calcium%": (43.0, "RDA"),
            "calories": (551.4, "calories"),
            "carbohydrateContent": (54.4, "g"),
            "carbohydrates": (54.4, "g"),
            "carbohydrates%": (18.0, "RDA"),
            "cholesterol": (58.4, "mg"),
            "cholesterol%": (20.0, "RDA"),
            "cholesterolContent": (58.4, "mg"),
            "dietary fiber": (2.8, "g"),
            "dietary fiber%": (11.0, "RDA"),
            "fat": (25.6, "g"),
            "fat%": (39.0, "RDA"),
            "fatContent": (25.6, "g"),
            "fiberContent": (2.8, "g"),
            "folate": (16.8, "mcg"),
            "folate%": (4.0, "RDA"),
            "iron": (1.8, "mg"),
            "iron%": (10.0, "RDA"),
            "magnesium": (21.9, "mg"),
            "magnesium%": (8.0, "RDA"),
            "niacin equivalents": (3.6, "mg"),
            "niacin equivalents%": (28.0, "RDA"),
            "potassium": (200.5, "mg"),
            "potassium%": (6.0, "RDA"),
            "protein": (28.9, "g"),
            "protein%": (58.0, "RDA"),
            "proteinContent": (28.9, "g"),
            "saturated fat": (11.0, "g"),
            "saturated fat%": (55.0, "RDA"),
            "saturatedFatContent": (11.0, "g"),
            "sodium": (1182.5, "mg"),
            "sodium%": (47.0, "RDA"),
            "sodiumContent": (1182.5, "mg"),
            "thiamin": (0.1, "mg"),
            "thiamin%": (6.0, "RDA"),
            "vitamin a iu": (882.5, "IU"),
            "vitamin a iu%": (18.0, "RDA"),
            "vitamin b6": (0.1, "mg"),
            "vitamin b6%": (9.0, "RDA"),
            "vitamin c": (8.3, "mg"),
            "vitamin c%": (14.0, "RDA"),
        })
