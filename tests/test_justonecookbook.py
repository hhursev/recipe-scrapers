from recipe_scrapers.justonecookbook import JustOneCookbook
from tests import ScraperTest


class TestJustOneCookbook(ScraperTest):

    scraper_class = JustOneCookbook

    def test_host(self):
        self.assertEqual("justonecookbook.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.justonecookbook.com/yaki-onigiri-grilled-rice-ball/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Yaki Onigiri (Grilled Rice Ball)"
        )

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_image(self):
        self.assertEqual(
            "https://www.justonecookbook.com/wp-content/uploads/2020/03/Yaki-Onigiri-Grilled-Rice-Ball-9532-I.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 rice cooker cups uncooked Japanese short-grain rice",
                "400 ml water",
                "1 Tbsp kosher/sea salt (I use Diamond Crystal; use half for table salt) ((you do not need to use all of it))",
                "1 Tbsp neutral-flavored oil (vegetable, rice bran, canola, etc)",
                "soy sauce ((I love using my homemade unagi sauce))",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Gather all the ingredients. Cook the rice with a rice cooker, a pot over the stove, an instant pot, or a donabe. Let the cooked rice cool a little bit until you can hold rice without burning your hands. Do not let the rice completely cool down.\nTo Make Rice Balls\nFirst, wet both of your hands with water so the rice won’t stick.\nThen put some salt in your hands and rub to spread all around.\nScoop about a half cup of rice onto your palm.\nCover the rice with the other hand and gently form the rice into a triangle.\nMake sure the covering hand (my right hand) should be forming a triangle shape. When forming the onigiri shape, your hands should be just firm enough so the onigiri doesn't fall apart. You don't want to squeeze the rice too tight.\nI use three fingers (thumb, index finger, middle finger) to cover the area to make a nice triangle shape. Then rotate onigiri to make a perfect triangle.\nWhile you squeeze onigiri firmly with both hands, one of your hands has to press onigiri to keep a nice form.\nGently squeeze the center of the triangle on both sides so there is a slight indentation (for grilling onigiri). Now onigiri is ready! You can tell I’m not a good onigiri maker – no matter how many years I have been practicing.\nTo Grill Rice Ball\nLightly oil a cast-iron skillet and put it on medium heat.\nGrill onigiri until all sides are crispy and lightly browned. Rice will release itself when it forms a nice crust. Don’t flip it quickly. Just work on one side at a time and avoid turning over frequently, which may end up breaking into pieces.\nOnce all nicely toasted and lightly brown, lower heat to medium-low heat. Brush all sides with soy sauce (or unagi sauce). Rotate to make sure all sides become crispy. Be careful not to burn onigiri after you brush it with the sauce.\nTo Store\nRice gets hard when you refrigerate. You can individually wrap the Yaki Onigiri in plastic wrap and cover them with a thick kitchen towel and store in the refrigerator for up to 2 days. The towel will prevent the rice from getting too cold and keep the food stay cool but not cold. When you're ready to eat, bring it back to room temperature and reheat in a microwave or frying pan.",
            self.harvester_class.instructions(),
        )
