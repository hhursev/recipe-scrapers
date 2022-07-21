from recipe_scrapers.eatingwell import EatingWell
from tests import ScraperTest


class TestEatingWell(ScraperTest):
    scraper_class = EatingWell

    def test_host(self):
        self.assertEqual("eatingwell.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Cheesy Ground Beef & Cauliflower Casserole"
        )

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F44%2F2021%2F08%2F16%2Fcheesy-ground-beef-and-cauliflower-casserole.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 tablespoon extra-virgin olive oil",
                "½ cup chopped onion",
                "1 medium green bell pepper, chopped",
                "1 pound lean ground beef",
                "3 cups bite-size cauliflower florets",
                "3 cloves garlic, minced",
                "2 tablespoons chili powder",
                "2 teaspoons ground cumin",
                "1 teaspoon dried oregano",
                "½ teaspoon salt",
                "¼ teaspoon ground chipotle",
                "1 (15 ounce) can no-salt-added petite-diced tomatoes",
                "2 cups shredded extra-sharp Cheddar cheese",
                "⅓ cup sliced pickled jalapeños",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            """Position rack in upper third of oven. Preheat broiler to high.
Heat oil in a large oven-safe skillet over medium heat. Add onion and bell pepper; cook, stirring, until softened, about 5 minutes. Add beef and cauliflower; cook, stirring and breaking the beef up into smaller pieces, until it is no longer pink, 5 to 7 minutes. Stir in garlic, chili powder, cumin, oregano, salt and chipotle; cook until fragrant, about 1 minute. Add tomatoes and their juices; bring to a simmer and cook, stirring occasionally, until liquid is reduced and the cauliflower is tender, about 3 minutes more. Remove from heat.
Sprinkle cheese over the beef mixture and top with sliced jalapeños. Broil until the cheese is melted and browned in spots, 2 to 3 minutes.""",
            self.harvester_class.instructions(),
        )

    def test_total_time(self):
        return self.assertEqual(30, self.harvester_class.total_time())
