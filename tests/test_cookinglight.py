from recipe_scrapers.cookinglight import CookingLight
from tests import ScraperTest


class TestCookingLight(ScraperTest):

    scraper_class = CookingLight

    def test_host(self):
        self.assertEqual("cookinglight.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.cookinglight.com/recipes/avocado-black-bean-and-charred-tomato-bowl",
            self.harvester_class.canonical_url(),
        )

    def test_image(self):
        self.assertEqual(
            "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimg1.cookinglight.timeinc.net%2Fsites%2Fdefault%2Ffiles%2Fstyles%2F4_3_horizontal_-_1200x900%2Fpublic%2F1542730855%2Favocado-black-bean-and-charred-tomato-bowl-detox-book-p28.jpg%3Fitok%3D7dflTpmM",
            self.harvester_class.image(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Avocado, Black Bean, and Charred Tomato Bowl"
        )

    def test_total_time(self):
        self.assertEqual(10, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("1 serving", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            "\n".join(
                [
                    "1/2 cup Savory Stewed Black Beans, warmed",
                    "1 teaspoon olive oil",
                    "1/2 cup grape tomatoes",
                    "1/4 cup fresh corn kernels (from 1 ear)",
                    "1/2 medium-sized ripe avocado, thinly sliced",
                    "1 medium radish, very thinly sliced",
                    "2 tablespoons fresh cilantro leaves",
                    "1/4 teaspoon kosher salt",
                    "1/8 teaspoon black pepper",
                ]
            ),
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Step 1 Place the black beans in a pile in the corner of a shallow bowl. Heat a small skillet over medium-high. Add the oil to the pan; swirl to coat. Add the tomatoes; cook until charred but not collapsing, about 3 minutes, shaking the pan once to turn the tomatoes. Place the tomatoes next to the beans in the bowl.",
                    "Step 2 Add the corn to the pan; cook until heated through, 2 to 3 minutes. Place the corn next to the tomatoes. Add the avocado slices, radish slices, and cilantro to the bowl. Sprinkle with the salt and pepper.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())
