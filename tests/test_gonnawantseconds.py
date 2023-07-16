from recipe_scrapers.gonnawantseconds import GonnaWantSeconds
from tests import ScraperTest


class TestGonnaWantSeconds(ScraperTest):

    scraper_class = GonnaWantSeconds

    def test_host(self):
        self.assertEqual("gonnawantseconds.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.gonnawantseconds.com/white-chicken-enchiladas/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "White Chicken Enchiladas",
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Kathleen")

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.gonnawantseconds.com/wp-content/uploads/2020/08/White-Chicken-Enchiladas-01.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "8-10 small flour tortillas",
                "3 cups cooked chicken (shredded or chopped)",
                "3 cups Monterey jack cheese (shredded-divided)",
                "3 tablespoons unsalted butter",
                "3 tablespoons flour",
                "2 cups chicken broth",
                "1 cup sour cream",
                "1 (4-ounce can) diced green chilies mild",
                "2-3 tablespoons green onions (sliced)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Spray a 9 X 13-inch baking dish with cooking spray and set aside. Preheat oven to 350 degrees.\nIn a small bowl, combine chicken and 1 cup of Monterey Jack cheese. Fill tortillas with this mixture and roll each one up then place seam side down in the prepared pan.\nMelt the butter in a skillet. Sprinkle flour over melted butter and whisk to combine. Cook for 1 minute to remove the flour taste. Remove the skillet from heat and whisk in broth. Place back on the heat and cook until the mixture has thickened and is bubbly. Cool sauce for 3-5 minutes. (Don't skip this step- if the sauce is too hot and you add the sour cream it will curdle it-yuck!) Add sour cream and chilies and stir until sauce is smooth and sour cream is completely dissolved.\nPour sauce over enchiladas and add remaining cheese over top. Bake in preheated oven for 20-25 minutes or until enchiladas are heated through and sauce is bubbly. Turn on the broiler and broil until the top is nicely golden. Top with chopped green onions and serve.",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "Whip up the cheesiest, dreamiest dinner you've ever had with my sensational White Chicken Enchiladas! Guaranteed to please even the pickiest eaters!",
            self.harvester_class.description(),
        )
