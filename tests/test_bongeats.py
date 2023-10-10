import unittest

from recipe_scrapers.bongeats import BongEats
from tests import ScraperTest


class TestBongEatsScraper(ScraperTest):

    scraper_class = BongEats

    def test_host(self):
        self.assertEqual("bongeats.com", self.harvester_class.host())

    @unittest.skip("canonical_url will not pass with testhtml (uses example.com)")
    def test_canonical_url(self):
        self.assertEqual(
            "https://www.bongeats.com/recipe/lau-chingri",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Lau Chingri")

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_cook_time(self):
        self.assertEqual(40, self.harvester_class.cook_time())

    def test_prep_time(self):
        self.assertEqual(20, self.harvester_class.prep_time())

    def test_yields(self):
        self.assertEqual("5 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://uploads-ssl.webflow.com/5c481361c604e53624138c2f/648b92c0b448da06bede4a4e_lau%20chingri%2016-9.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 kg lau (bottle gourd, 5-mm sticks)",
                "100 g kucho chingri (tiny freshwater prawns, cleaned and deveined with head on)",
                "45 g mustard oil",
                "1 dried red chilli",
                "1 bay leaf",
                "1 cardamom pod",
                "1 clove",
                "1 cinnamon",
                "½ tsp cumin seeds",
                "½ tsp cumin powder",
                "¼ tsp turmeric",
                "6 g ginger paste",
                "4 green chillies (slit)",
                "10 g salt",
                "18 g sugar",
                "2 tsp ghee",
                "1 pinch gorom moshla",
                "6 g coriander leaves (chopped)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Clean and devein the prawns. Smear them with ¼ tsp each of salt and turmeric. Set aside.\n"
            "Peel the lau, and chop it in 5-mm thick strips, 4 cm long.\n"
            "Place an empty kadai on the stove. Once it has heated up fully, add mustard oil. Wait for it to give off a gentle smoke and turn pale yellow.\n"
            "Fry the marinated prawns in it for 30 seconds. Don’t overfry, or they will become tough. Remove from the oil and set aside.\n"
            "Temper the same (now-prawn-flavoured) oil with a dried red chilli, bay leaf, cinnamon, cardamom, cloves and cumin seeds.\n"
            "Add cumin powder and turmeric. Fry these on low heat for 2 minutes before adding the ginger paste. Fry for another 2 minutes. If the spices start sticking to the pan, you may add splashes of water and continue frying.\n"
            "Add lau, green chillies and salt. Mix everything and cover the pan with a lid.\n"
            "You will now have to cook this, stirring occasionally, until the spices are well braised and the lau has ‘reduced’. This can take anything from 25–40 minutes.\n"
            "Add sugar and continue cooking until the liquid has more or less dried up.\n"
            "Add the fried prawns and continue braising until a very light caramelisation stage is reached.\n"
            "Finish with ghee, Bengali garam masala and chopped coriander leaves.",
            self.harvester_class.instructions(),
        )

    def test_author(self):
        return self.assertEqual("Bong Eats", self.harvester_class.author())

    def test_description(self):
        return self.assertEqual(
            "This dry, curried bottle-gourd recipe is a family favourite, and can be cooked with or without the shrimp!",
            self.harvester_class.description(),
        )

    def test_cuisine(self):
        return self.assertEqual("Indian", self.harvester_class.cuisine())

    def test_nutrients(self):
        return self.assertEqual({"calories": "154"}, self.harvester_class.nutrients())
