from recipe_scrapers.thekitchn import TheKitchn
from tests import ScraperTest


class TestKitchnScraper(ScraperTest):
    scraper_class = TheKitchn

    def test_host(self):
        self.assertEqual("thekitchn.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.thekitchn.com/manicotti-22949270",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "How To Make the Best Beef and Cheese Manicotti",
        )

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Meghan Splawn")

    def test_total_time(self):
        self.assertEqual(65, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://cdn.apartmenttherapy.info/image/upload/f_jpg,q_auto:eco,c_fill,g_auto,w_1500,ar_16:9/k%2FPhoto%2FRecipes%2F2019-10-how-to-beef-manicotti%2F2019-10-04_Kitchn86818_HT-Beef-Manicotti",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 tablespoons olive oil",
                "12 ounces lean ground beef",
                "1 large shallot, finely chopped",
                "4 cloves garlic, minced",
                "3 cups marinara sauce, divided",
                "Cooking spray",
                "14 dried manicotti pasta tubes (8 ounces)",
                "1 (15 to 16-ounce) container full-fat ricotta cheese",
                "2 cups shredded part-skim mozzarella cheese, divided",
                "1/2 cup finely grated Parmesan cheese, divided",
                "1/2 cup chopped fresh parsley leaves, divided",
                "1 large egg, lightly beaten",
                "1 teaspoon kosher salt",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Step 1\nCook the beef for the filling. Heat the oil in a large skillet over medium-high heat until shimmering. Add the ground beef and cook until the meat begins to brown, about 5 minutes. Add the shallot and garlic, cook until the shallot is translucent and the beef is cooked through, about 5 minutes more. Transfer to a large bowl and set aside to cool to room temperature.\nStep 2\nHeat the oven to 375ºF and prepare the baking dish. Arrange a rack in the middle of the the oven and heat the oven to 375ºF. Meanwhile, bring a large pot of heavily salted water to a boil. Coat a 9x13-inch baking dish with cooking spray. Spread about 1 1/2 cups of the marinara sauce in the bottom of the dish and set aside.\nStep 3\nBoil the manicotti shells. Add the manicotti to the water and boil until they are al dente, about 8 minutes. Drain and set aside.\nStep 4\nMix up the filling. Add the ricotta, half of mozzarella, half of the Parmesan, half of the parsley, the egg, and the salt to the cooled beef mixture and stir to combine well.\nStep 5\nFill the shells. Transfer the beef and cheese mixture to a piping bag or gallon size ziptop bag. Snip off a 1/2-inch hole in one bottom corner of the bag, then pipe the filling into each manicotti tube (about generous 1/3 cup each). Nestle each filled manicotti in the sauce, packed them tightly together in a single layer.\nStep 6\nTop the filled shells with the remaining sauce and cheeses. Pour the remaining 1 1/2 cups sauce evenly over the manicotti and sprinkle with the remaining mozzarella and Parmesan.\nStep 7\nBake for 35 to 40 minutes. Bake uncovered until the sauce is bubbly, the cheese is browned, and the noodles are very tender, 35 to 40. Let cool for about 10 minutes before serving. Sprinkle with the remaining parsley just before serving.",
            self.harvester_class.instructions(),
        )
