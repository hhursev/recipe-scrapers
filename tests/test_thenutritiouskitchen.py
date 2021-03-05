from recipe_scrapers.thenutritiouskitchen import TheNutritiousKitchen
from tests import ScraperTest


class TestTheNutritiousKitchenScraper(ScraperTest):

    scraper_class = TheNutritiousKitchen

    def test_host(self):
        self.assertEqual("thenutritiouskitchen.co", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("The Nutritious Kitchen", self.harvester_class.author())

    def test_canonical_url(self):
        self.assertEqual(
            "https://thenutritiouskitchen.co/healthy-fig-pecan-crumble-bars/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Healthy Fig Pecan Crumble Bars")

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://thenutritiouskitchen.co/wp-content/uploads/2020/09/figpecanbars-10-of-17-225x225.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 cups finely ground almond flour",
                "3 TBSP cassava flour or coconut flour",
                "Cinnamon + Sea salt to taste",
                "1/2 cup pecan butter or cashew butter (runny)",
                "1/4 cup melted coconut oil",
                "1/4 cup maple syrup",
                "16 oz. fresh figs",
                "Optional: 1 tbsp. maple syrup",
                "Handful of chopped pecans for topping",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat oven to 350 degrees Fahrenheit. Line an 8×8 baking tray with parchment paper and set aside.\nIn a large bowl whisk together almond flour, cassava, sea salt + cinnamon. In a separate bowl whisk pecan butter, melted coconut oil + maple syrup until a thick glaze forms.\nPour into dry ingredients and mix together with a frosting spatula until dough forms. Press into baking tray, reserving about 1/4 cup for the topping. Use hands to spread out if needed.\nIn a microwave-safe bowl, heat up figs for about 1 minute then crush with a fork to make quick “jam”. Mix in optional tbsp of maple syrup.\nLayer jam then the remaining dough into “crumbles” Top with pecans.\nBake for about 20-25 minutes depending on your oven. Allow to cool in pan then cool completely on a rack before slicing into 12 squares.\nStore covered in the fridge up to 5 days. They are great served chilled or warm!",
            self.harvester_class.instructions(),
        )
