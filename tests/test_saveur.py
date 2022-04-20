from recipe_scrapers.saveur import Saveur
from tests import ScraperTest


class TestSaveurScraper(ScraperTest):

    scraper_class = Saveur

    def test_host(self):
        self.assertEqual("saveur.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual(None, self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Baked Saffron Yogurt Rice with Chicken (Tahcheen-e Morgh)",
            self.harvester_class.title(),
        )

    def test_total_time(self):
        self.assertEqual(285, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.saveur.com/app/uploads/2019/03/11/SI4KF6ISWT2J7XCCEZRWOH7DFY.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "3 cups extra-long white basmati rice (1 lb. 4 oz.)",
                "1⁄4 cup plus 2 Tbsp. kosher salt, divided, plus more as needed",
                "1⁄4 tsp. saffron, lightly ground between your fingers, plus more for sprinkling",
                "3 tbsp. extra-virgin olive oil",
                "1 large yellow onion, halved and sliced ¼-inch-thick",
                "4 medium garlic cloves, finely chopped (1 Tbsp.)",
                "10 boneless, skinless chicken thighs (2 lb. 3 oz.), halved",
                "1⁄4 tsp. freshly ground black pepper",
                "1⁄4 cup fresh lemon juice",
                "1 cup plain whole-milk Greek yogurt",
                "1 large egg",
                "5 tbsp. unsalted butter, divided",
                "1 tbsp. unsalted butter",
                "1⁄2 cup dried barberries, picked, soaked in cold water for 15 minutes, then drained (or substitute finely chopped dried cranberries)",
                "1 tsp. sugar (omit if using cranberries)",
                "1⁄3 cup raw pistachios, coarsely chopped",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """Parboil the rice by following steps 1 and 2 of the Steamed Saffron Rice with Tahdig recipe (p. 36). Set the rice aside to drain as you prepare the dish’s other components.\nIn a small bowl, add the saffron and 2 tablespoons hot water. (Be sure to pre-soak your barberries now, too. See toppings list.)\nIn a large, deep skillet, add the olive oil and set over medium heat. Once hot, add the onion and ¼ teaspoon salt, and cook, stirring occasionally, until soft and golden, about 20 minutes. Add the garlic and cook until fragrant, 2 minutes. Add the chicken thighs, 2¾ teaspoons salt, and the pepper. Cook, turning the chicken as needed, until the pieces begin to brown slightly, about 6 minutes total. Add the lemon juice and saffron water, and turn the chicken to coat well. Lower the heat to medium-low, partially cover the pot, and let simmer, stirring occasionally, until the chicken is tender and just cooked through, 20–25 minutes. Remove from the heat and let cool slightly. Cut the chicken into ½-inch-long strips, return them to the pan, and toss to coat in the onions and pan juices. Remove the pan from the heat and set aside while you finish the rice.\nPreheat the oven to 400°F and set a rack in the lowest position.\nIn a large bowl, combine the yogurt, egg, and a tiny pinch of ground saffron. Add half of the rice and stir well to combine. Set the mixture aside.\nIn a 9-by-13-inch glass baking dish (preferably clear), add 3 tablespoons of butter; set the dish in the oven to melt the butter, about 3 minutes. Remove the dish, swirling the melted butter all over the bottom and sides. Spread the yogurt-rice mixture evenly along the bottom of the dish, packing it down firmly. Add the chicken pieces evenly over the rice, then sprinkle the remaining plain rice over the chicken in an even layer. Drizzle with 2 tablespoons of chicken juices and dot with the remaining 2 tablespoons of butter. Cover tightly with aluminum foil, transfer to the oven, and bake until the bottom of the rice is crispy and golden, 80–90 minutes. (If using a clear glass dish, carefully lift it to check the bottom.) Remove the baking dish and let the rice rest at room temperature for 5 minutes.\nWhile the tahcheen rests, prepare the topping: In a small pot, melt the butter over medium heat. Stir in the drained barberries, pistachios, and sugar (if using), and cook until the berries are just plumped, about 2 minutes. Remove from the heat.\nRun a knife along the sides of the baking dish to help release the rice. Place a large rectangular serving platter, baking tray, or cutting board over the tahcheen, take a deep breath, and quickly and confidently flip the baking dish over to unmold. You should hear a swish when the tahdig releases. Remove the baking dish and sprinkle the crispy surface of the rice with the barberry topping. Cut into pieces and serve.""",
            self.harvester_class.instructions(),
        )
