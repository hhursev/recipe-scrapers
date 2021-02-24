from recipe_scrapers.greatbritishchefs import GreatBritishChefs
from tests import ScraperTest


class TestGreatBritishChefsScraper(ScraperTest):

    scraper_class = GreatBritishChefs

    def test_host(self):
        self.assertEqual("greatbritishchefs.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.greatbritishchefs.com/recipes/picadillo-recipe",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Picadillo")

    def test_total_time(self):
        self.assertEqual(50, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "http://gbc-cdn-public-media.azureedge.net/img73858.768x512.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "Picadillo",
                "500g of beef mince",
                "1 onion, diced",
                "2 garlic cloves, sliced",
                "1 carrot, finely diced",
                "1 potato, finely diced",
                "1 bay leaf",
                "1 tsp ground cumin",
                "1 tsp ground coriander",
                "1 tsp smoked paprika",
                "2 tbsp of tomato purée",
                "100g of raisins",
                "300ml of chicken stock",
                "300g of tomatillo salsa",
                "1 tsp honey",
                "lime juice, to taste",
                "1 handful of coriander, chopped",
                "salt, to taste",
                "olive oil",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "To begin, heat a splash of olive oil in a large pan and add the mince. Cook until nicely browned – you may need to do this in batches to avoid overcrowding the mince\nDecant the mince into a bowl and sweat the onions, garlic, carrot and potato in the same pan you used to brown the mince. Add the bay leaf and spices\nOnce the onions are translucent, return the mince to the pan and add the tomato purée, raisins, chicken stock and tomatillo salsa. Turn down the heat and simmer for 30 minutes\nSeason with the honey, lime juice and salt. Stir through the coriander and serve with rice or as a taco filling",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())

    def test_description(self):
        self.assertEqual(
            "This simple picadillo recipe has the perfect balance of sweetness and spice. A pleasing tanginess comes from the addition of vibrant tomatillo salsa for a great depth of flavour. Serve in tacos or with rice for a hearty Mexican-inspired midweek meal.",
            self.harvester_class.description(),
        )
