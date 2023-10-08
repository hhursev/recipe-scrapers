from recipe_scrapers.finedininglovers import FineDiningLovers
from tests import ScraperTest


class TestFineDiningLoversScraper(ScraperTest):

    scraper_class = FineDiningLovers

    def test_host(self):
        self.assertEqual("finedininglovers.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.finedininglovers.com/recipes/main-course/zucchini-raw-vegan-lasagna",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Zucchini Raw Vegan Lasagna")

    def test_total_time(self):
        self.assertEqual(50, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "Zucchini",
                "Basil",
                "Pine nuts",
                "Extra virgin olive oil",
                "Yeast Flakes",
                "Garlic",
                "Salt",
                "Tomatoes",
                "Sun dried tomatoes",
                "Extra virgin olive oil",
                "Salt",
                "Pepper",
                "Brown sugar",
                "Oregano",
                "Macadamia Nuts",
                "Yeast Flakes",
                "Salt",
                "Limes",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "For the macadamia cheese Pour all ingredients in a blender and mix until a thick cream. Set aside. For the tomato cream Pour all ingredients into a blender and mix until creamy. Set aside. For the basil pesto Pour all ingredients into a blender and mix until creamy. Set aside. Wash zucchini and cut them into very thin slices. Make the raw vegan lasagna alternating a layer of zucchini\na layer of macadamia cheese\na layer of zucchini\na layer of tomato sauce\na layer of zucchini\na layer of basil pesto. Keep the lasagna in the fridge and serve decorated with fresh basil and pine nuts.",
            self.harvester_class.instructions(),
        )

    def test_image(self):
        return self.assertEqual(
            "https://www.finedininglovers.com/sites/g/files/xknfdk626/files/Original_2242_zucchini-lasagna-raw-vegan.jpg",
            self.harvester_class.image(),
        )
