from recipe_scrapers.ohsheglows import OhSheGlows
from tests import ScraperTest


class TestOhSheGlowsScraper(ScraperTest):

    scraper_class = OhSheGlows

    def test_host(self):
        self.assertEqual("ohsheglows.com", self.harvester_class.host())

    def test_image(self):
        self.assertEqual(
            "https://ohsheglows.com/gs_images/2019/06/Flourless-Peanut-Butter-Cookie-Ice-Cream-00950-3.jpg",
            self.harvester_class.image(),
        )

    def test_canonical_url(self):
        self.assertEqual(
            "https://ohsheglows.com/2019/06/29/obsession-worthy-peanut-butter-cookie-ice-cream/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Obsession-Worthy Peanut Butter Cookie Ice Cream",
        )

    def test_ratings(self):
        self.assertEqual(self.harvester_class.ratings(), 4.67)

    def test_total_time(self):
        self.assertEqual(22, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 batch Flourless Peanut Butter Cookies, divided",
                "2 (14-ounce/398 mL) cans full-fat coconut milk*",
                "1/2 cup (105 g) natural cane sugar",
                "3 tablespoons (45 mL) smooth natural peanut butter",
                "2 teaspoons (10 mL) pure vanilla extract",
                "1/4 + 1/8 teaspoon fine sea salt, or to taste",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Chill the ice cream bowl in the freezer overnight, or for at least 12 hours. This step is very important to ensure the ice cream thickens properly.\nPrepare the Flourless Peanut Butter Cookies. After baking, cool the cookies for 10 to 15 minutes, then transfer each one to a plate. Place in the freezer on a flat surface for a minimum of 25 minutes. As soon as you transfer the cookies to the freezer, get started on the ice cream.\nAdd the ice cream ingredients (entire cans of coconut milk, sugar, peanut butter, vanilla, and salt) to a blender and blend for about 8 to 10 seconds, until smooth (be sure not to blend longer than 10 seconds, as it may effect the final texture of your ice cream).\nPlace the frozen ice cream bowl into the ice cream maker, insert the churning arm, cover with the lid, and turn on the machine (if the instructions for your ice cream maker are different, please follow the directions that came with your machine). Slowly pour the mixture into the bowl as it churns. Churn for about 22 minutes, until the mixture has thickened into a very thin, soft-serve texture.\nOnce the cookies have been in the freezer for 25 minutes, chop 6 of the cookies into small, almond-sized chunks. Reserve the remaining 7 cookies, at room temperature, for later.\nAfter 22 minutes of churning, slowly add the chopped cookies, a handful at a time, to the mixture while the machine is still churning. I like to use a fork to gently push the chopped cookies into the ice cream and help it along. Churn another 5 to 8 minutes, until the ice cream has thickened a bit more. It will have a thick, soft-serve texture when ready. There will be some hardened ice cream along the inside of the bowl...I like to think of this as the chef’s extra helping (wink, wink)! Serve immediately, or for a firmer texture, transfer the ice cream to a loaf pan or airtight container and spread out smooth. At this stage, I like to crumble an extra cookie all over the top (and gently push it into the ice cream) to make it look extra-enticing, but this is optional. Cover and freeze for 2 hours for a more traditional ice cream firmness.\nTo serve, scoop into bowls or ice cream cones. Or, if you're feeling wild, make ice cream sandwiches with the leftover cookies...oh yea!!\nStorage tip: Leftovers can be stored in an airtight container in the freezer for 3 to 4 weeks. Be sure to cover the ice cream with a piece of wrap to prevent freezer burn. To soften, let the container rest on the counter for 20 to 30 minutes before scooping.",
            self.harvester_class.instructions(),
        )


# https://ohsheglows.com/2019/06/29/obsession-worthy-peanut-butter-cookie-ice-cream/
