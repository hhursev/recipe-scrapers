# mypy: allow-untyped-defs

from recipe_scrapers.goodfooddiscoveries import GoodFoodDiscoveries
from tests import ScraperTest


class TestGoodFoodDiscoveriesScraper(ScraperTest):

    scraper_class = GoodFoodDiscoveries

    def test_host(self):
        self.assertEqual("goodfooddiscoveries.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Magda", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Lemon Risotto", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Sides,Dinner", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_prep_time(self):
        self.assertEqual(5, self.harvester_class.prep_time())

    def test_cook_time(self):
        self.assertEqual(25, self.harvester_class.cook_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://goodfooddiscoveries.com/wp-content/uploads/2023/03/lemon-parmesan-risotto.jpeg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 1/2 cups (300g) Arborio rice",
                "4 cups (960ml) chicken or vegetable broth",
                "1/2 cup (120ml) dry white wine",
                "1 small onion, finely chopped",
                "2 cloves garlic, minced",
                "1/4 cup (60g) unsalted butter",
                "1/2 cup (60g) grated parmesan cheese",
                "2 tbsp (30ml) extra virgin olive oil",
                "1 lemon, zest and juice",
                "Salt and pepper, to taste",
                "Fresh parsley, for serving",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            """In a medium saucepan, heat the broth over low heat until it's warm.\nIn a large saucepan or Dutch oven, heat the olive oil over medium heat. Add the onion and garlic, and sauté until the onion is soft and translucent, about 3-4 minutes.\nAdd the Arborio rice to the pan and stir to coat it in the oil. Cook for 2-3 minutes, stirring occasionally, until the rice is lightly toasted.\nAdd the white wine to the pan and stir until it's absorbed by the rice.\nBegin adding the warm broth to the rice mixture, one cup at a time, stirring constantly until each cup of broth is absorbed before adding the next. Continue to stir frequently to ensure that the rice doesn't stick to the pan.\nWhen the rice is tender and the mixture is creamy, after about 20-25 minutes, remove the pan from heat.\nAdd the butter, parmesan cheese, lemon zest, and lemon juice to the pan and stir until the butter is melted and the cheese is fully incorporated.\nSeason the risotto with salt and pepper to taste. If the risotto is too thick, add additional broth or water, one tablespoon at a time, until it reaches your desired consistency.\nServe the lemon risotto hot, garnished with fresh parsley.""",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            """Lemon Parmesan risotto is a classic Italian dish that features creamy Arborio rice cooked in a flavorful broth and infused with fresh lemon zest and juice, butter, and grated Parmesan cheese.""",
            self.harvester_class.description(),
        )
