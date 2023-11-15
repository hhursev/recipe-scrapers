from recipe_scrapers.eatingwell import EatingWell
from tests import ScraperTest


class TestEatingWell(ScraperTest):
    scraper_class = EatingWell

    def test_host(self):
        self.assertEqual("eatingwell.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            self.harvester_class.canonical_url(),
            "https://www.eatingwell.com/recipe/7919044/cheesy-ground-beef-cauliflower-casserole/",
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Cheesy Ground Beef & Cauliflower Casserole"
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Carolyn Casner")

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.eatingwell.com/thmb/32d8L6W6cwt652tjjXAHosP3ViE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/cheesy-ground-beef-and-cauliflower-casserole-8791b22c92404d958e2ac5aa92af8aa7.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 tablespoon extra-virgin olive oil",
                "0.5 cup chopped onion",
                "1 medium green bell pepper, chopped",
                "1 pound lean ground beef",
                "3 cups bite-size cauliflower florets",
                "3 cloves garlic, minced",
                "2 tablespoons chili powder",
                "2 teaspoons ground cumin",
                "1 teaspoon dried oregano",
                "0.5 teaspoon salt",
                "0.25 teaspoon ground chipotle",
                "1 (15 ounce) can no-salt-added petite-diced tomatoes",
                "2 cups shredded extra-sharp Cheddar cheese",
                "0.333 cup sliced pickled jalapeños",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            """Position rack in upper third of oven. Preheat broiler to high.
Heat oil in a large broiler-safe skillet over medium heat. Add onion and bell pepper; cook, stirring, until softened, about 5 minutes. Add beef and cauliflower; cook, stirring and breaking the beef up into smaller pieces, until it is no longer pink, 5 to 7 minutes. Stir in garlic, chili powder, cumin, oregano, salt and chipotle; cook until fragrant, about 1 minute. Add tomatoes and their juices; bring to a simmer and cook, stirring occasionally, until liquid is reduced and the cauliflower is tender, about 3 minutes more. Remove from heat.
Sprinkle cheese over the beef mixture and top with sliced jalapeños. Broil until the cheese is melted and browned in spots, 2 to 3 minutes.""",
            self.harvester_class.instructions(),
        )

    def test_total_time(self):
        return self.assertEqual(30, self.harvester_class.total_time())
