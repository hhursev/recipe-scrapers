from recipe_scrapers.thehappyfoodie import TheHappyFoodie
from tests import ScraperTest


class TestTheHappyFoodie(ScraperTest):

    scraper_class = TheHappyFoodie

    def test_host(self):
        self.assertEqual("thehappyfoodie.co.uk", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Poulet rôti au vin rouge (Roast Red Wine Chicken)",
        )

    def test_total_time(self):
        self.assertEqual(90, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "150ml red wine",
                "100g tomato paste",
                "3 sprigs of thyme, leaves picked",
                "3 sprigs of marjoram, leaves picked, or ½ teaspoon dried",
                "100ml red wine vinegar",
                "1 whole chicken cut into 8 pieces (approx. 1.5kg)",
                "Salt and ground black pepper",
                "500g baby potatoes, washed",
                "3 onions, peeled and cut into quarters",
                "6 carrots, peeled and cut into quarters lengthways",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Mix together the red wine, tomato paste, herbs and red wine vinegar. Season the chicken pieces with plenty of salt and pepper then place in a bag with the marinade. Shake the bag to make sure each piece is well coated. Place in the fridge for at least 30 minutes.\nIn the meantime, place the potatoes in a pan of cold water, put the lid on top and bring up to the boil. Boil for 1–2 minutes, then drain in a colander. Place the onions, carrots and potatoes in a large baking dish or tray (big enough to fit the chicken and the vegetables) and pour over 125ml of water. Preheat the oven to 200°C. Remove the chicken from the fridge and arrange the pieces, skin side up, in a layer on top of the vegetables in the dish. Pour the rest of the marinade over the chicken. Cover with a sheet of baking paper or foil and roast in the preheated oven for 30 minutes. Remove the baking paper or foil and baste the chicken with the cooking liquid. Roast, uncovered, for another 15 minutes or until the skin is crisp. Serve immediately.\nLes petits conseils – tips: Buying a whole chicken always works out more affordable. If you aren’t up for dissecting it yourself, ask your butcher to cut it into pieces for you. Otherwise if there’s no knife-wielding butcher about you can always cheat and go for chicken thighs. If you’re unsure whether the chicken is cooked through, pierce with a sharp knife and the juices from the chicken should come out clear.\nFaire en avance – get ahead: The veg and chicken can be prepared up to a day in advance, then simply pop it all in the baking tray and cook as indicated in the recipe.\nMarinating time: 30 minutes – overnight\n",
            self.harvester_class.instructions(),
        )

    def test_author(self):
        return self.assertEqual("Rachel Khoo", self.harvester_class.author())

    def test_image(self):
        return self.assertEqual(
            "https://thehappyfoodie.co.uk/wp-content/uploads/2021/08/9780718177478_roast_red_wine_chicken_s900x0_c3840x2243_l0x1385.jpg",
            self.harvester_class.image(),
        )

    def test_cuisine(self):
        return self.assertEqual("French", self.harvester_class.cuisine())

    def test_category(self):
        return self.assertEqual("Dinner, Main Course", self.harvester_class.category())
