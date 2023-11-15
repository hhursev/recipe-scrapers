# mypy: allow-untyped-defs

from recipe_scrapers.justonecookbook import JustOneCookbook
from tests import ScraperTest


class TestJustOneCookbookScraper(ScraperTest):
    scraper_class = JustOneCookbook

    def test_host(self):
        self.assertEqual("justonecookbook.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.justonecookbook.com/yaki-onigiri-grilled-rice-ball/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Nami", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Yaki Onigiri (Grilled Rice Ball)", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Side Dish", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("9 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.justonecookbook.com/wp-content/uploads/2023/09/Yaki-Onigiri-Grilled-Rice-Ball-3074-I-1.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "2¼ cups uncooked Japanese short-grain white rice (3 rice cooker cups, 540 ml; to cook 2 rice cooker cups of rice instead, see measurements below) 3 540",
                "2½ cups water (for 2 rice cooker cups of rice, use 1⅔ cups (400 ml) water)",
                "3 Tbsp soy sauce (or use 2 Tbsp for 2 rice cooker cups of rice)",
                "1 Tbsp sugar (or 2 tsp for 2 rice cooker cups)",
                "1 Tbsp roasted sesame oil (or 2 tsp for 2 rice cooker cups)",
                "¼ tsp Diamond Crystal kosher salt (or ⅛ tsp for 2 rice cooker cups)",
                "1 Tbsp soy sauce",
                "1 tsp roasted sesame oil",
            ],
            self.harvester_class.ingredients(),
        )


def test_instructions(self):
    self.assertEqual(
        "Before You Start...\n"
        "Japanese short-grain white rice requires a soaking time of 20–30 minutes. The rice-to-water ratio is 1 to 1.1 (or 1.2) for short-grain white rice. Please note that 2¼ cups (450 g, 3 rice cooker cups) of uncooked Japanese short-grain rice yield 6⅔ cups (990 g) of cooked white rice. This is enough for 9 onigiri rice balls (typically 110 g each). Optional: To make 5–6 rice balls, cook 1½ cups (300 g, 2 rice cooker cups) of uncooked Japanese short-grain rice in 1⅔ cups water (400 ml) to yield 4⅓ cups (660 g) of cooked white rice.\n"
        "Cook the rice; see how with a rice cooker, pot over the stove, Instant Pot, or donabe. To my rice cooker, I added 2½ cups water to 2¼ cups uncooked Japanese short-grain white rice. Once the rice is cooked, gather all the ingredients.\n"
        "To Season the Rice\n"
        "Combine 3 Tbsp soy sauce and 1 Tbsp sugar in a small bowl and microwave until the mixture is hot, about 30–60 seconds. Whisk it all together until the sugar dissolves.\n"
        "Add 1 Tbsp roasted sesame oil and ¼ tsp Diamond Crystal kosher salt and mix it all together.\n"
        "Transfer the hot cooked rice to a large bowl and add the seasoning mixture.\n"
        "With a rice paddle, use a slicing motion to combine the seasoning and cooked rice well. Now, you‘re ready to shape the rice balls. Note: Be sure to let the cooked rice cool a little bit until you can hold it without burning your hands. Rice must be hot or warm when making onigiri in order to hold its shape.\n"
        "To Shape the Rice Balls\n"
        "First, wet both of your hands with water so the rice won’t stick.\n"
        "Then put some salt in your hands and rub to spread all around.\n"
        "Scoop about a half cup of rice onto your palm.\n"
        "Cover the rice with the other hand and gently form the rice into a triangle.\n"
        "Make sure the covering hand (my right hand) should be forming a triangle shape. When forming the onigiri shape, your hands should be just firm enough so the onigiri doesn't fall apart. You don't want to squeeze the rice too tight.\n"
        "I use three fingers (thumb, index finger, middle finger) to cover the area to make a nice triangle shape. Then rotate onigiri to make a perfect triangle.\n"
        "While you squeeze onigiri firmly with both hands, one of your hands has to press onigiri to keep a nice form.\n"
        "Gently squeeze the center of the triangle on both sides so there is a slight indentation (for grilling onigiri). Now onigiri is ready! You can tell I’m not a good onigiri maker – no matter how many years I have been practicing.\n"
        "To Grill Rice Ball\n"
        "Lightly oil a cast-iron skillet and put it on medium heat.\n"
        "Grill onigiri until all sides are crispy and lightly browned. Rice will release itself when it forms a nice crust. Don’t flip it quickly. Just work on one side at a time and avoid turning over frequently, which may end up breaking into pieces.\n"
        "Once all nicely toasted and lightly brown, lower heat to medium-low heat. Brush all sides with soy sauce (or unagi sauce). Rotate to make sure all sides become crispy. Be careful not to burn onigiri after you brush it with the sauce.\n"
        "With an Onigiri Mold: Prepare a small bowl filled with water. Soak the onigiri mold and lid in the water to moisten so the rice doesn‘t stick to it. Remove the mold and drain the excess water.\n"
        "Fill the onigiri mold with the hot seasoned rice all the way to the top edge, making sure to fill the corners. Cover with the lid and push down firmly. You should feel a slight resistance; if not, you may want to add a bit more rice.\n"
        "Remove the lid. Flip over the mold onto a baking sheet or plate lined with parchment paper. Then, push the “button” on the mold‘s bottom to release your onigiri. Tip: Always dip your fingers in water before touching the onigiri to prevent the rice from sticking to them.\n"
        "Repeat with the remaining rice.\n"
        'Now, firmly hand-press the rice balls to keep them from falling apart while grilling. For Yaki Onigiri, you‘ll want to press the rice ball a bit more tightly than you would a regular onigiri. First, moisten both palms with a bit of water to prevent the rice from sticking. Then, pick up a rice ball in your left (non-dominant) hand. Place your right (dominant) hand on top of the rice in a “mountain" shape and gently press the triangle corner. At the same time, squeeze the fingers and heel of your bottom (left) hand to gently press the sides flat.Now, rotate the triangle corner you just pressed toward you (clockwise, if you‘re right-handed). The tip of the second corner will now be pointing up. Repeat the above “press and rotate” steps to hand press the second triangle corner and then the third, always keeping your left hand on the bottom and your right hand on top. Press and rotate a final 2–3 more times to finish.\n'
        "In the image below, the top row is hand pressed while the bottom row is not.\n"
        "If you don‘t want to touch the rice with your hands, you can press the onigiri with plastic wrap. Place a piece of plastic wrap on the working surface, wet your fingers, and place the onigiri in the middle.\n"
        "Gather the corners of the plastic wrap and twist it a few times to tighten it around the rice. Form the rice into a triangle shape in the same manner that I described above.\n"
        "Without an Onigiri Mold: You also can use plastic wrap to shape the onigiri instead of using a mold. Place a piece of plastic film on the working surface, wet your fingers, and put the rice on top. Gather the corners of the plastic film and twist it a few times to tighten it around the rice.\n"
        "Form the rice into a triangle shape through the plastic in the same manner that I described above for hand-pressing the onigiri. Repeat with the remaining rice. Tip: To shape the onigiri with your hands the traditional way, see the step-by-step instructions and images in my Onigiri (Japanese Rice Balls) post.\n"
        "To Pan-Grill the Onigiri\n"
        "Combine 1 T",
        self.harvester_class.instructions(),
    )

    def test_ratings(self):
        self.assertEqual(4.67, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Japanese", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "A favorite at Izakaya restaurants, Yaki Onigiri are Japanese grilled rice balls covered in savory soy sauce. With a crispy crust on the outside and soft sticky rice on the inside, these rice balls are simply irresistible and easy to make at home!",
            self.harvester_class.description(),
        )
