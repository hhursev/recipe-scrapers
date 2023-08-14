# mypy: allow-untyped-defs

from recipe_scrapers.tasteau import TasteAU
from tests import ScraperTest


class TestTasteAUScraper1(ScraperTest):

    scraper_class = TasteAU
    test_file_name = "tasteau_1"

    def test_host(self):
        self.assertEqual("taste.com.au", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Katrina Woodman", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Mexican chicken pasta bake recipe", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("dinner", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(70, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://img.taste.com.au/g-jb09b4/taste/2021/05/mexican-chicken-pasta-bake-171430-2.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "250g Coles Durum Wheat Macaroni Pasta",
                "18.20 gm extra virgin olive oil",
                "1 small red onion, finely chopped",
                "1 small red capsicum, deseeded, finely chopped",
                "2 garlic cloves, crushed",
                "120g sachet Mexican spice seasoning",
                "1/2 barbecued chicken, skin and bones removed, meat shredded",
                "400g can crushed tomatoes",
                "420g can black beans, rinsed, drained",
                "170g (11/2 cups) Mexican cheese blend",
                "80g Dairy Cheese Fetta Australian Style, crumbled",
                "Coles Sour Cream, to serve",
                "Thinly sliced jalapeños, to serve (optional)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        instructions = (
            "Preheat oven to 200C/180C fan forced. Grease an 18 x 22cm (base measurement) baking dish. Cook the pasta in a large saucepan of salted boiling water until just al dente. Drain.\n"
            "Wipe saucepan dry. Heat the oil over medium heat. Add the onion, capsicum and garlic. Cook, stirring occasionally, for 5 minutes or until softened. Add the seasoning and cook, stirring, for 2 minutes or until aromatic. Add the chicken, tomato, beans and 125ml (1/2 cup) water. Bring to the boil. Reduce heat to low. Simmer, covered, for 5 minutes. Uncover and simmer for a further 5 minutes or until thickened. Add pasta and stir until well combined. Remove from heat.\n"
            "Combine the cheese blend and feta in a small bowl. Add 3/4 cup cheese mixture to the pasta mixture. Stir to combine. Spoon into the prepared dish. Sprinkle with remaining cheese and bake for 25-30 minutes or until melted and golden. Set aside for 10 minutes to cool slightly. Top with sour cream and jalapeños, if using, to serve."
        )
        self.assertEqual(instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(4.5, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("mexican", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "We've turned fajitas into a pasta bake (and added heaps of cheese). Even better, it's made using shortcut ingredients like barbecue chicken and bought spice mix so you can prep it in just 15 minutes.",
            self.harvester_class.description(),
        )
