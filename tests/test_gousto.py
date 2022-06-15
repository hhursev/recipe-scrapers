from responses import GET

from recipe_scrapers.gousto import Gousto

from tests import ScraperTest


class TestGoustoScraper(ScraperTest):

    scraper_class = Gousto

    @property
    def expected_requests(self):
        yield GET, "https://www.foodnetwork.com/recipes/tyler-florence/chicken-marsala-recipe-1951778", "tests/test_data/gousto.testhtml"

    def test_host(self):
        self.assertEqual("gousto.co.uk", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Creamy Pork Tagliatelle")

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 onion",
                "150g chestnut mushrooms",
                "1 garlic clove",
                "10g fresh parsley",
                "30g rennet-free parmesan",
                "2 British pork loin steaks",
                "1 pot of double cream (227ml)",
                "1/2 beef stock cube",
                "200g linguine",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat the oven to 200°C/ 180°C (fan)/ 400°F/ Gas 6 Boil a kettle (used in steps 3 & 5)\nAdd 1-2 tbsp of olive oil to a pan on a high heat Once the oil is hot, sear the pork tenderloin for 2 min on each side, or until browned all over (keep the pan for step 6) Season to your taste with salt and pepper\nPlace the pork on an oven-proof tray and put in the oven for 8-10 min, or until cooked through Once done, remove from the oven, cover well and allow to rest until step 7 Dissolve half the (whole) beef stock cube in 100ml (200ml) of boiling water\nCut the mushrooms into quarters Peel the onion(s) and chop finely Crush the garlic with the side of a knife, peel it and chop finely Chop the parsley finely\nCook the pasta in a pot of boiling water and salt (optional) for 8-10 min or until the pasta is cooked to your taste, stirring occasionally, then drain\nReturn the pork pan to a medium-high heat, add the garlic and onion and cook for 1 min Add the mushrooms and cook for 1 min Reduce the heat, add the stock and 50ml (100ml) of cream and simmer for 5 min Add the parsley\nGrate the parmesan Cut the pork into slices (approx. 2cm) Season the mushroom sauce to your taste with salt and pepper\nAdd the pasta to the sauce and mix well Serve the pasta with the pork on top and sprinkle with parmesan Enjoy!",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())
