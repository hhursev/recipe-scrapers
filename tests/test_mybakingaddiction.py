from recipe_scrapers.mybakingaddiction import MyBakingAddiction
from tests import ScraperTest


class TestMyBakingAddictionScraper(ScraperTest):

    scraper_class = MyBakingAddiction

    def test_host(self):
        self.assertEqual("mybakingaddiction.com", self.harvester_class.host())

    def test_image(self):
        self.assertEqual(
            "https://www.mybakingaddiction.com/wp-content/uploads/2016/08/chocolate-coconut-zucchini-bread-1-of-11-1-720x720.jpg",
            self.harvester_class.image(),
        )

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.mybakingaddiction.com/chocolate-coconut-zucchini-bread/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Chocolate Coconut Zucchini Bread"
        )

    def test_ratings(self):
        self.assertEqual(self.harvester_class.ratings(), 4.4)

    def test_total_time(self):
        self.assertEqual(75, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 1/2 cups all-purpose flour",
                "1/2 cup unsweetened cocoa powder",
                "1 teaspoon salt",
                "1 teaspoon baking soda",
                "1/2 teaspoon baking powder",
                "1 teaspoon ground cinnamon",
                "1 cup CRISCO® Organic Refined Coconut Oil, melted",
                "2/3 cup granulated sugar",
                "2/3 cup light brown sugar",
                "1/2 cup sour cream",
                "3 large eggs",
                "2 teaspoons pure vanilla extract",
                "2 1/2 cups grated zucchini",
                "1 cup semi-sweet chocolate chips",
                "3/4 cup shredded sweetened coconut",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat oven to 350°F. Spray two 8x4-inch loaf pans with Pillsbury® Baking Spray with Flour.\nIn a medium bowl, sift together the flour, cocoa, salt, baking soda, baking powder and cinnamon.\nIn a large bowl with an electric mixer, mix the coconut oil and sugars until combined. Mix in the sour cream. Add in the eggs and vanilla and mix until thoroughly incorporated.\nSlowly add dry ingredients to wet ingredients and mix until just combined.\nAdd in the zucchini and mix for about 1 minute, or until the batter is moistened and the zucchini is evenly incorporated into the batter. Stir in the chocolate chips and shredded coconut.\nSpread the batter into the prepared pans and bake in preheated oven for 55-60 minutes, or until a toothpick inserted into the center comes out clean.\nCool bread in pan for 1/2 hour. Remove bread to a wire rack to cool completely.",
            self.harvester_class.instructions(),
        )
