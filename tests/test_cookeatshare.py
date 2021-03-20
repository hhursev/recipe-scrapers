from recipe_scrapers.cookeatshare import CookEatShare
from tests import ScraperTest


class TestCookEatShare(ScraperTest):

    scraper_class = CookEatShare

    def test_host(self):
        self.assertEqual("cookeatshare.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual("Pork Steak Vegetable Bake", self.harvester_class.title())

    def test_image(self):
        self.assertEqual(
            "https://assets.cookeatshare.com/assets/recipe-art/stock/3/full-f1e2882559f1146065432f8bdd182440.png",
            self.harvester_class.image(),
        )

    def test_total_time(self):
        self.assertEqual(None, self.harvester_class.total_time())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '4 med. potatoes, pared & cut lengthwise, in 1/4" slices',
                "1 lg. carrot, pared & sliced",
                '4 pork steaks, cut 1/2" thick',
                "1/2 c. water",
                "1 env. dry onion soup mix or possibly 1 can cream of onion soup",
                "2 tbsp. soy sauce",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            'Place potatoes and carrots in bottom of 11" x 7 1/2" x 1 3/4" baking dish. Trim fat from steaks. In large skillet, cook trimmings till about 2 Tbsp. oil accumulates; throw away trimmings.\nIn warm oil, brown steaks well on both sides. In small saucepan, bring to boil. Spoon 1/2 of onion soup mix over the potatoes and carrots; top with steaks. Spoon remaining soup mix over. Cover, bake in 350 degree oven for 1 hour. Uncover and bake 10 min more. Makes 4 servings.',
            self.harvester_class.instructions(),
        )
