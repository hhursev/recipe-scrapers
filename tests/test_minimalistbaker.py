from recipe_scrapers.minimalistbaker import Minimalistbaker
from tests import ScraperTest


class TestMinimalistbakerScraper(ScraperTest):

    scraper_class = Minimalistbaker

    def test_host(self):
        self.assertEqual("minimalistbaker.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://minimalistbaker.com/vegan-cashew-ricotta-cheese-soy-free-fast-easy/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Cashew Ricotta Cheese (Soy-Free, Fast, Easy!)",
        )

    def test_yields(self):
        self.assertEqual("8 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://minimalistbaker.com/wp-content/uploads/2020/05/Cashew-Ricotta-Cheese-sQUARE.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 \u00bc cup raw cashews",
                "1 Tbsp lemon juice",
                "1 Tbsp nutritional yeast, plus more to taste",
                "1/2 tsp garlic powder",
                "1/4-1/2 tsp sea salt ((plus more to taste))",
                "4-6 Tbsp water",
                "1/4 cup fresh chopped parsley or cilantro",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            'Soak cashews in very hot water for 30 minutes to 1 hour, or overnight (or 6 hours) in cool water. Then drain, rinse, and set aside.\nAdd soaked, drained cashews to a food processor (or a high-speed blender) along with lemon juice, nutritional yeast, garlic powder, sea salt, and lesser amount of water (4 Tbsp or 60 ml as original recipe is written // adjust if altering batch size). Mix/blend, scraping down sides as needed. Then add more water 1 Tbsp (15 ml) at a time until a thick paste forms. I find I get the best texture results with a food processor, but in a pinch, a blender can work too. It just generally requires more scraping and more liquid.\nTaste and adjust flavor as needed, adding more nutritional yeast for cheesy flavor, salt to taste, lemon juice for acidity, or garlic powder for garlic flavor. Blend again to combine.\nAt this point, the "cheese" is ready to enjoy! The flavors continue to develop and thicken when chilled. Delicious on things like pizza, pasta, lasagna, salads, and more.\nBest when fresh. Store leftover nut "cheese" in the refrigerator for up to 5-7 days or in the freezer up to 1 month (let thaw at room temperature or in the refrigerator before serving).',
            self.harvester_class.instructions(),
        )
