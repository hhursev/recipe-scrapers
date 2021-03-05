from recipe_scrapers.whatsgabycooking import WhatsGabyCooking
from tests import ScraperTest


class TestWhatsGabyCookingScraper(ScraperTest):

    scraper_class = WhatsGabyCooking

    def test_host(self):
        self.assertEqual("whatsgabycooking.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://whatsgabycooking.com/vegetarian-quinoa-bake/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Vegetarian Quinoa Bake")

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_image(self):
        self.assertEqual(
            "https://cdn.whatsgabycooking.com/wp-content/uploads/2017/10/WGC-Quinoa-Bake-copy-2.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 ½ cups uncooked multi-colored quinoa",
                "2 cups shredded colby jack cheese divided",
                "1 cup shredded mozzarella cheese divided",
                "1 cup canned black beans rinsed and drained",
                "1 cup frozen charred corn trader joes",
                "1 4.5-ounce can chopped green chiles",
                "1 ½ cup Gaby's chipotle or tomatillo salsa",
                "Kosher salt and pepper to taste",
                "Finely chopped scallions and cilantro as garnish",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat the oven to 375 degrees F.\nCook the quinoa according to the package directions. Once cooked, remove from heat and transfer the cooked quinoa into a large bowl.\nFold in 1 1/2 cups of the shredded colby jack cheese, ½ cup of the shredded mozzarella, black beans, corn, green chiles and salsa. Season the entire mixture with salt and pepper and stir to combine.\nLightly spray a medium sized skillet with non-stick spray, and transfer the mixture into the skillet. Top with the remaining shredded cheeses and bake for about 20-25 minutes until the top layer of cheese is bubbly and melted.\nRemove the baking dish from the oven and garnish with green onions and cilantro and serve.",
            self.harvester_class.instructions(),
        )
