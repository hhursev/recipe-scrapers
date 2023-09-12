from recipe_scrapers.redhousespice import RedHouseSpice
from tests import ScraperTest


class TestRedHouseSpiceScraper(ScraperTest):
    scraper_class = RedHouseSpice
    test_file_name = "redhousespice_2"

    def test_host(self):
        self.assertEqual("redhousespice.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Wei Guo", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Smashed Cucumber Salad (拍黄瓜)", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(15, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://redhousespice.com/wp-content/uploads/2022/06/chinese-smashed-cucumber-scaled.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 large cucumber (or 2 small ones (about 350g/12oz))",
                "¼ tsp salt",
                "2 cloves garlic (minced)",
                "1 tbsp light soy sauce",
                "½ tbsp black rice vinegar (e.g. Chikiang vinegar)",
                "1 tsp sesame oil",
                "1 pinch sugar",
                "Chinese chilli oil (to taste)",
                "Sichuan pepper oil (optional)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Place cucumber onto a chopping board. Use the side of a cleaver, or a rolling pin/a meat pounder, to smash it. Make sure the pressure is enough to crack it open by one stroke, instead of pounding it multiple times on one spot. Then cut it crosswise into bite-sized pieces.\nTransfer the cucumber to a bowl. Sprinkle evenly with salt. Leave to rest for 10 minutes or so. Then drain away the water extracted by the salt (see note).\nAdd light soy sauce, black rice vinegar, sesame oil, sugar, minced garlic, chilli oil and Sichuan pepper oil if using. Toss very well to evenly distribute the seasonings.\nEnjoy it right away or let it sit for 2 minutes before serving (The flavour will penetrate further into the cucumber).""",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
