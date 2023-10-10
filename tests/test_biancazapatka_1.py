from recipe_scrapers.biancazapatka import BiancaZapatka
from tests import ScraperTest


class TestBiancaZapatkaScraper(ScraperTest):

    scraper_class = BiancaZapatka
    test_file_name = "biancazapatka_1"

    def test_host(self):
        self.assertEqual("biancazapatka.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://biancazapatka.com/en/tempeh-rice-noodle-bowl-in-peanut-sauce/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Bianca Zapatka", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Rice Noodle Salad with Tempeh and Peanut Sauce",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual(
            "Lunch &amp; Dinner,Main Course", self.harvester_class.category()
        )

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://biancazapatka.com/wp-content/uploads/2022/07/buddha-bowl-sauce.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "7 oz Tempeh (oder Tofu)",
                "2 garlic cloves (pressed)",
                "3 piece of ginger (grated)",
                "3 tbsp tamari (or soy sauce)",
                "1 tbsp sesame oil (or peanut oil + more for frying)",
                "1 tbsp rice vinegar (or other vinegar or lemon/lime juice)",
                "1 tbsp maple syrup (or other syrup)",
                "1 tsp sriracha (or chili paste optional to taste)",
                "7 oz rice noodles (or other noodles or rice or quinoa)",
                "6 radishes (finely sliced)",
                "4 mini cucumbers (finely sliced)",
                "1 red bell pepper (finely sliced)",
                "2 large carrots (finely sliced)",
                "2 cups fresh baby spinach",
                "3-4 spring onions (cut into fine rings)",
                "1 recipe peanut sauce (or tahini sauce, if nut-free)",
                "2 tbsp sesame seeds",
                "4 tbsp roasted peanuts",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Marinated Tempeh\nFor the marinade, pour tamari, sesame oil, rice vinegar, maple syrup, and Sriracha into a sealable container. Press in the garlic, grate in the ginger, and stir everything together.\nCut the tempeh into cubes and add them to the marinade. Seal the container and shake well until the tempeh is completely marinated. Then let it marinate for at least 20 minutes (or overnight in the refrigerator).\nNoodles & Veggies\nMeanwhile, prepare and chop the vegetables. Cover the rice noodles with boiling water and set aside, covered, for 10 minutes (or according to package directions). Then drain and rinse with fresh water.\nCook and assemble\nOnce the tempeh is marinated, heat about 1-2 tbsp of oil in a frying pan (or wok). Remove the tempeh from the marinade (you can use the remaining marinade to make the peanut sauce) and cook until golden brown from all sides.\nAssemble the rice noodles and vegetables in bowls, as shown in the recipe video. Add the tempeh on top and drizzle with peanut sauce. Lastly, garnish with scallions, sesame seeds, and peanuts, and serve with fresh limes on the side.\nEnjoy!",
            self.harvester_class.instructions(),
        )

    def test_cuisine(self):
        self.assertEqual("Asian", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "This colorful Tempeh Rice Noodle Salad Bowl recipe is quick and easy to make, super healthy, and incredibly delicious! A vegan banquet of perfectly marinated tempeh with gluten-free rice noodles, crunchy fresh veggies, and the best peanut sauce ever! It’s the perfect bowl of happiness for anyone who’s looking to combine healthy eating with indulgence!",
            self.harvester_class.description(),
        )
