from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.bbcgoodfood import BBCGoodFood
from tests import ScraperTest


class TestBBCGoodFoodScraper(ScraperTest):
    scraper_class = BBCGoodFood

    def test_host(self):
        self.assertEqual("bbcgoodfood.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.bbcgoodfood.com/recipes/summer-meatballs-spaghetti",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Summer meatballs & spaghetti")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Elena Silcock")

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/summer-meatballs-spaghetti-bd04f10.jpg?resize=768,574",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 tbsp olive oil",
                "1 onion , finely chopped",
                "2 garlic cloves , crushed",
                "1 tsp fennel seeds",
                "250g pork mince",
                "large handful parsley , leaves chopped, stalks finely chopped",
                "1 large courgette , peeled into ribbons all around the edge, centre grated or finely chopped",
                "200g spaghetti",
                "½ a lemon , zested and juiced",
                "grated parmesan , to serve",
            ],
            self.harvester_class.ingredients(),
        )

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "2 tbsp olive oil",
                        "1 onion , finely chopped",
                        "2 garlic cloves , crushed",
                        "1 tsp fennel seeds",
                        "250g pork mince",
                        "large handful parsley , leaves chopped, stalks finely chopped",
                        "1 large courgette , peeled into ribbons all around the edge, centre grated or finely chopped",
                        "200g spaghetti",
                        "½ a lemon , zested and juiced",
                        "grated parmesan , to serve",
                    ],
                    purpose=None,
                )
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Heat ½ tbsp of the olive oil in a large frying pan over a medium heat. Add the onion and soften for 5 mins, then add the garlic and fennel and cook for 2 mins longer. Tip into a bowl. Add the pork mince, parsley stalks and grated courgette to the bowl, season well, mix, and shape into 10 meatballs. Heat the remaining oil in the frying pan, add the meatballs and fry for 5-8 mins, turning occasionally, until golden brown and cooked through. Set the pan aside.\nBring a pan of salted water to the boil and cook the spaghetti for 1 min less than pack instructions. Using tongs, transfer the pasta to the pan of meatballs, sloshing in some of the cooking water as you go. Add the courgette ribbons to the pan and put it back over the heat. Toss the pasta and meatballs with the courgette ribbons in the pan with a ladleful of pasta water and add the lemon juice. Season well, tip into bowls and scatter over the chopped parsley leaves, lemon zest and a generous grating of parmesan.",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "Make a quick and easy meal for two with these pork meatballs, served with spaghetti, courgette ribbons, lemon and parmesan – perfect for summer evenings",
            self.harvester_class.description(),
        )
