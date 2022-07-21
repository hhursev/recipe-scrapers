from recipe_scrapers.finedininglovers import FineDiningLovers
from tests import ScraperTest


class TestFineDiningLoversScraper(ScraperTest):

    scraper_class = FineDiningLovers

    @property
    def test_file_name(self):
        return "{}_1".format(self.scraper_class.__name__.lower())

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
        self.assertCountEqual(
            [
                "Zucchini 4 each, large",
                "Basil 20 g, fresh",
                "Pine nuts 70 g",
                "Extra virgin olive oil 120 ml",
                "Yeast Flakes 6 g",
                "Garlic 1/2 clove",
                "Salt 1 pinch",
                "Tomatoes 200 g",
                "Sun Dried Tomatoes 4 each",
                "Extra virgin olive oil 30 ml",
                "Salt 1 pinch",
                "Pepper 1 pinch",
                "Brown sugar 1 pinch",
                "Oregano to taste",
                "Macadamia Nuts 150 g (not roasted, unsalted)",
                "Yeast Flakes 6 g",
                "Salt 1 pinch",
                "Limes 1 (juice only, filtered)",
                "50 ml (filtered)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "For the macadamia cheese Pour all ingredients in a blender and mix until a thick cream. Set aside.\nFor the tomato cream Pour all ingredients into a blender and mix until creamy. Set aside.\nFor the basil pesto Pour all ingredients into a blender and mix until creamy. Set aside. Wash zucchini and cut them into very thin slices. Make the raw vegan lasagna alternating a layer of zucchini, a layer of macadamia cheese, a layer of zucchini, a layer of tomato sauce, a layer of zucchini, a layer of basil pesto. Keep the lasagna in the fridge and serve decorated with fresh basil and pine nuts.",
            self.harvester_class.instructions(),
        )

    def test_image(self):
        return self.assertEqual(
            "https://www.finedininglovers.com/sites/g/files/xknfdk626/files/styles/recipes_1200_800_fallback/public/Original_2242_zucchini-lasagna-raw-vegan.jpg",
            self.harvester_class.image(),
        )
