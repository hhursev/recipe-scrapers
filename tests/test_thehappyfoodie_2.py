from recipe_scrapers.thehappyfoodie import TheHappyFoodie
from tests import ScraperTest


class TestTheHappyFoodie(ScraperTest):

    scraper_class = TheHappyFoodie
    test_file_name = "thehappyfoodie_2"

    def test_host(self):
        self.assertEqual("thehappyfoodie.co.uk", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "The Ottolenghi Test Kitchen’s M.E. Mac ‘n’ Cheese with Za’atar Pesto",
        )

    def test_total_time(self):
        self.assertEqual(55, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "300g dried cavatappi or fusilli pasta",
                "600–700ml whole milk",
                "65g unsalted butter, cut into roughly 3cm cubes",
                "3 garlic cloves, crushed",
                "⅛ tsp ground turmeric",
                "1½ tsp cumin seeds, toasted and roughly crushed with a pestle and mortar",
                "75ml double cream",
                "150g mature cheddar, roughly grated",
                "180g Greek feta, roughly crumbled",
                "salt and black pepper",
                "45g crispy onions or shallots, store-bought or homemade (see intro), to serve",
                "1 large lemon",
                "3 tbsp za’atar",
                "20g fresh coriander, roughly chopped",
                "1 garlic clove, roughly chopped",
                "40g pine nuts, lightly toasted",
                "90ml olive oil",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            [
                "Put the pasta, 600ml of milk, 350ml of water, the butter, garlic, turmeric, 1 teaspoon of salt and a good grind of pepper into a large sauté pan on a medium-high heat. Bring to a simmer, then turn the heat down to medium and cook, stirring occasionally, for 10–14 minutes, or until the pasta is al dente and the sauce has thickened from the pasta starches (it will still be quite saucy). If using cavatappi, you might need to add the extra 100ml of milk at this stage depending on how saucy you like your mac ’n’ cheese. Turn the heat down to low and stir through the cumin, cream and both cheeses until the cheddar is nicely melted.",
                "While the pasta is cooking, make the pesto. Finely grate the lemon to give you 1 teaspoon of zest. Then use a small, sharp knife to peel and segment the lemon and roughly chop the segments. Place in a bowl with the lemon zest and set aside. Put the za’atar, coriander, garlic, pine nuts, ⅛ teaspoon of salt, a good grind of pepper and half the oil into a food processor and pulse a few times until you have a coarse paste. Add to the chopped lemon in the bowl and stir in the remaining oil.",
                "Transfer the mac ’n’ cheese to a large serving platter with a lip or a shallow bowl, dot all over with the pesto, then top with the crispy onions.",
                "Get ahead: Make the mac ’n’ cheese ahead of time if you like, adding a splash of water to thin out when reheating.",
                "Make it your own:",
                "– Play with different cheeses and spices.",
                "– Use different pasta shapes like macaroni, adjusting liquid levels as necessary.",
            ],
            self.harvester_class.instructions().splitlines(),
        )

    def test_author(self):
        return self.assertEqual("Yotam Ottolenghi", self.harvester_class.author())

    def test_image(self):
        return self.assertEqual(
            "https://thehappyfoodie.co.uk/wp-content/uploads/2022/02/Ottolenghi-Middle-Eastern-Mac-and-Cheese-scaled.jpg",
            self.harvester_class.image(),
        )

    def test_cuisine(self):
        return self.assertEqual("Middle Eastern", self.harvester_class.cuisine())

    def test_category(self):
        return self.assertEqual("Main Course", self.harvester_class.category())
