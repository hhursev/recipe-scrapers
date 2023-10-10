from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.altonbrown import AltonBrown
from tests import ScraperTest


class TestAltonBrownScraper(ScraperTest):

    scraper_class = AltonBrown
    test_file_name = "altonbrown_2"

    def test_host(self):
        self.assertEqual("altonbrown.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://altonbrown.com/recipes/filipino-style-pork-skewers-with-vinegar-sauce/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Penny McCord Jewell", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Filipino-Style Pork Skewers with Vinegar Sauce",
            self.harvester_class.title(),
        )

    def test_category(self):
        self.assertEqual("Appetizers", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(280, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://altonbrown.com/wp-content/uploads/2023/04/IMG_0345-scaled.jpeg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "1 1/2 pounds pork (Boston) butt, cut into 1-inch cubes",
            "2 tablespoons freshly squeezed lemon juice",
            "1/2 cup soy sauce",
            "1/2 cup cane vinegar",
            "1/4 cup pineapple juice",
            "1/4 cup ginger ale",
            "1 tablespoon ketchup",
            "2 tablespoons hoisin sauce",
            "6 cloves garlic, minced",
            "1/4 cup palm or coconut sugar",
            "2 teaspoons freshly ground black pepper",
            "2 teaspoons vegetable oil",
            "1/2 cup cane vinegar",
            "1/4 cup soy sauce",
            "1 tablespoon palm or coconut sugar",
            "1/4 cup red onion, minced",
            "1 clove garlic, minced",
            "1 Thai chili, thinly sliced",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "1 1/2 pounds pork (Boston) butt, cut into 1-inch cubes",
                        "2 tablespoons freshly squeezed lemon juice",
                        "1/2 cup soy sauce",
                        "1/2 cup cane vinegar",
                        "1/4 cup pineapple juice",
                        "1/4 cup ginger ale",
                        "1 tablespoon ketchup",
                        "2 tablespoons hoisin sauce",
                        "6 cloves garlic, minced",
                        "1/4 cup palm or coconut sugar",
                        "2 teaspoons freshly ground black pepper",
                        "2 teaspoons vegetable oil",
                    ],
                    purpose="Pork Software:",
                ),
                IngredientGroup(
                    ingredients=[
                        "1/2 cup cane vinegar",
                        "1/4 cup soy sauce",
                        "1 tablespoon palm or coconut sugar",
                        "1/4 cup red onion, minced",
                        "1 clove garlic, minced",
                        "1 Thai chili, thinly sliced",
                    ],
                    purpose="Dipping Sauce Software:",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = "Place the pork cubes in a 1-gallon zip top bag. Combine the marinade ingredients in a 2-cup measuring cup or medium bowl and whisk until the sugar dissolves. Pour into the bag and seal, squeezing out as much air as possible. Squish everything around to ensure even coat-age, then refrigerate for at least 4 hours or up to overnight.\nWhen ready to cook, remove the pork from the bag (reserving the marinade), and place on a rack over a sheet pan (or paper towels), to catch any drips. Skewer 5-6 cubes of pork per stick and set aside until ready to grill.\nPour the reserved marinade into a 1-quart saucepan over medium-high heat and boil for 10 minutes until slightly thickened and reduced by half.\nPrepare a small charcoal grill for direct heat. While you wait for the coals, prepare the dipping sauce.\nCombine the cane vinegar, soy sauce, sugar, red onion, garlic, and chili in a small bowl. Set aside until ready to serve.\nWhen the coals are good and hot, arrange the pork skewers on the grill and cook for 8-10 minutes, brushing with the reduced marinade, until nicely charred and cooked through. Turn them often to create even charring. (I tend to flip mine almost every 30 seconds.)\nRemove to a platter and serve immediately with the dipping sauce.\nNote: My favorite grill for satay, or kushiyake is known as a Konro. Frequently seen in yakitori restaurants, it's basically a fairly narrow box made of diatomaceous earth. Konros can be used with grill grates, (which I prefer) or, if you're using flat skewers (which prevent rolling) you can simply rest the ends on the sides of the grill. I have two Konros and I love the short one (a mere 12\" x 9\") so much that I've written several sonnets to it. When loaded with Japanese binchotan charcoal, it's simply the perfect grill for small pieces of food and skewers.If you have yet to acquire a Konro, I suggest building a small charcoal fire on your grill's coal grate, between four fireplace bricks arranged thusly...and topped with a small, steel cooling grate. In any case the fire should be medium hot so that a hand held an inch over the grate can only be kept there for a second, (unless you're like Gary Busey's character in Lethal Weapon, in which case I can't help you). If you don't want to mess with the bricks fine...weave two folded over (2-ply) strips of heavy-duty aluminum foil through your grill grates, parallel to each other at a distance that matches the length of the skewers taken up by the meat. Lay a small metal cooling rack on top (so that the skewers don't fall through the grates) and cook over a hot fire. The foil should protect the ends of the skewers from full on combustion.And yet another note: Since they tend to float, I soak my skewers in a plastic water bottle. When I need one, I just open the lid and kinda pour them out. This is far more efficient than soaking in a loaf pan or baking dish."
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Filipino", self.harvester_class.cuisine())

    def test_description(self):
        expected_description = "Although most of the satay recipes I've seen, from predominately Islamic Indonesia and Malayasia, feature chicken and fish, many from the Philippines call for pork, which perfectly aligns with my palate's southern sensibilities. Although there's plenty of sweetness in the marinade (sodas like ginger ale are frequent additions), it's framed by the acidic heat of a dipping sauce which, with its vinegar and garlic, reminds me of quite a few Eastern Carolina barbecue sauces. As with any of the Filipino-inspired dishes you'll find on this site — Pork Adobo, Lumpia Shanghai, and Arroz Caldo, we owe this one to our test kitchen's Lynne Calamia, whose mom is from Quezon City, Philippines.Recipe and photo by Lynne Calamia"
        self.assertEqual(expected_description, self.harvester_class.description())
