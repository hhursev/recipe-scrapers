from recipe_scrapers.recipietineats import RecipieTinEats
from tests import ScraperTest


class TestRecipieTinEatsScraper(ScraperTest):

    scraper_class = RecipieTinEats

    def test_host(self):
        self.assertEqual("recipietineats.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.recipetineats.com/vietnamese-caramel-pork/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Vietnamese Caramel Pork")

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.recipetineats.com/wp-content/uploads/2017/10/Vietnamese-Caramel-Pork_-2.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1/2 cup / 100g brown sugar, tightly packed",
                "1 tbsp water",
                '1 kg / 2 lb pork shoulder ((butt) or boneless skinless pork belly, cut into 3 cm / 1.2" pieces (Note 1a))',
                "1 1/4 cups / 375 ml coconut water ((Note 1b))",
                "1 eschallot / shallot (, very finely sliced (Note 2))",
                "2 garlic cloves (, minced)",
                "1 1/2 tbsp fish sauce",
                "1/4 tsp white pepper",
                "Red chilli and finely sliced shallots/green onions",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Place sugar and water in a large pot over medium heat. Stir, then when it bubbles and the sugar is melted (it looks like caramel), add the rest of the ingredients.\nStir, then adjust the heat so it is simmering fairly energetically. Not rapidly, not a slow simmer (I use medium heat on a weak stove, between medium and low on a strong stove).\nSimmer for 1.5 hours, uncovered. Stir once or twice while cooking.\nAt around 1.5 hours, when the liquid has reduced down and the pork is tender, (see Note 3 if pork is not yet tender), the fat will separate (see video).\nStir and the pork will brown and caramelise in the fat.\nOnce the liquid is all gone and it's now stuck on the pork pieces, it's ready.\nServe over rice, garnished with fresh chilli and shallots. Simple pickled vegetables are ideal for a side because the fresh acidity pairs well with the rich pork.",
            self.harvester_class.instructions(),
        )
