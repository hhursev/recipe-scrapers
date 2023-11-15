from recipe_scrapers.downshiftology import Downshiftology
from tests import ScraperTest


class TestDownshiftologyScraper(ScraperTest):
    scraper_class = Downshiftology

    def test_host(self):
        self.assertEqual("downshiftology.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            self.harvester_class.canonical_url(),
            "https://downshiftology.com/recipes/greek-chicken-kabobs/",
        )

    def test_author(self):
        self.assertEqual("Lisa Bryan", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Greek Chicken Kabobs", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(55, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://i2.wp.com/www.downshiftology.com/wp-content/uploads/2020/09/Greek-Chicken-Kabobs-main-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "¼ cup olive oil",
                "2 tablespoons red wine vinegar",
                "3 tablespoons lemon juice",
                "1 teaspoon Dijon mustard",
                "3 garlic cloves (minced)",
                "1 teaspoon dried oregano",
                "½ teaspoon salt",
                "¼ teaspoon black pepper",
                "1 ½ pounds boneless skinless chicken breasts (about 3 large chicken breasts, cut into 1 ½-inch pieces.)",
                "1 red bell pepper (seeded, cut into 1 ½-Inch pieces)",
                "1 yellow bell pepper (seeded, cut into 1 ½-inch pieces)",
                "1 red onion (cut into 1 ½-inch chunks)",
                "1 zucchini (sliced)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Make marinade\nMake the marinade. In a bowl, whisk together the olive oil, red wine vinegar, lemon juice, Dijon mustard, minced garlic, dried oregano, salt, and pepper.\nMarinate chicken\nMarinate the chicken. Place chicken pieces in a glass dish and pour the marinade over the chicken. Cover and marinate in the fridge for at least one hour.\nThread skewers. Light a gas or charcoal grill on medium-high heat. Thread the skewers with pieces of red onion, chicken, zucchini, and bell pepper. You can alternate the order.\nGrill kabobs\nGrill the skewers. Place the kabobs on the preheated grill, and cook about 4 to 5 minutes per side. The kabobs are done when the chicken is cooked through and the vegetables are lightly charred, about 15 minutes.\nServe with lemon wedges and tzatziki sauce.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
