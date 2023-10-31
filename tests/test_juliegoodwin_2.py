from recipe_scrapers.juliegoodwin import JulieGoodwin
from tests import ScraperTest


class TestJudyGoodwinScraper(ScraperTest):
    scraper_class = JulieGoodwin
    test_file_name = "juliegoodwin_2"

    def test_host(self):
        self.assertEqual("juliegoodwin.com.au", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://juliegoodwin.com.au/butter-chicken-recipe/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Butter Chicken", self.harvester_class.title())

    def test_author(self):
        self.assertEqual("Julie Goodwin", self.harvester_class.author())

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("Serves 6", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://juliegoodwin.com.au/wordpress/wp-content/uploads/2015/09/800-butter-chicken-2.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 tablespoons olive oil",
                "50g butter",
                "1.6kg chicken thighs, trimmed and cut into thirds",
                "2 tablespoons fresh ginger, grated",
                "2 cloves garlic, finely chopped",
                "3 teaspoons ground coriander seed",
                "3 teaspoons ground cumin",
                "1 teaspoon ground cardamom",
                "½ teaspoon ground allspice",
                "½ teaspoon chilli powder",
                "4 tablespoons tomato paste",
                "1 ½ cups tomato puree",
                "2/3 cup natural yoghurt",
                "1 cup thickened cream",
                "salt",
                "coriander leaves and extra yoghurt",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "In a large non-stick chef’s pan, heat ¼ the oil and a ¼ of the butter over medium-high heat. Brown ¼ of chicken pieces for about 3 minutes, then remove from the pan and set aside. Repeat with the rest of the oil, butter and chicken.",
                    "Reduce the heat to medium-low. In the oil left in the pan, saute the ginger and garlic for a minute or two, then add the ground spices and cook for a further minute. Add tomato paste to the mixture and cook for another minute.",
                    "Return chicken to the pan, along with tomato puree, yoghurt and cream. Simmer for 10 minutes or until chicken has cooked through. Taste and add a pinch of salt if necessary.",
                    "Serve with basmati rice topped with extra yoghurt and scattered with coriander leaves.",
                ]
            ),
            self.harvester_class.instructions(),
        )
