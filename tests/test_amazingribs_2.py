from recipe_scrapers._grouping_utils import IngredientGroup
from recipe_scrapers.amazingribs import AmazingRibs
from tests import ScraperTest


class TestAmazingRibsScraper(ScraperTest):
    scraper_class = AmazingRibs
    test_file_name = "amazingribs_2"

    def test_host(self):
        self.assertEqual("amazingribs.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://amazingribs.com/brisket-burnt-ends/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Meathead, BBQ Hall of Famer", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Brisket Burnt Ends Recipe", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(610, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://amazingribs.com/wp-content/uploads/2022/02/Screen-Shot-2022-02-08-at-12.38.59-PM.png",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        expected_ingredients = [
            "6 pound brisket point",
            "3 teaspoons Morton Coarse Kosher Salt ((approximately ½ teaspoon per pound))",
            "¼ cup Big Bad Beef Rub",
            "¼ cup Kansas City style barbecue sauce",
            "¼ tablespoon brown sugar",
            "¼ cup beef broth",
        ]
        self.assertEqual(expected_ingredients, self.harvester_class.ingredients())

    def test_ingredient_groups(self):
        self.assertEqual(
            [
                IngredientGroup(
                    ingredients=[
                        "6 pound brisket point",
                        "3 teaspoons Morton Coarse Kosher Salt ((approximately ½ teaspoon per pound))",
                        "¼ cup Big Bad Beef Rub",
                        "¼ cup Kansas City style barbecue sauce",
                        "¼ tablespoon brown sugar",
                    ],
                    purpose="Burnt Ends",
                ),
                IngredientGroup(
                    ingredients=["¼ cup beef broth"],
                    purpose="Texas Crutch",
                ),
            ],
            self.harvester_class.ingredient_groups(),
        )

    def test_instructions(self):
        expected_instructions = [
            "Prep. Trim any excess fat off of the brisket point. Refrigerate the trimmings to use when finishing the burnt ends.",
            "Salt the meat about 12 to 24 hours in advance so it can work its way in, 2 to 4 hours minimum. After salting, sprinkle the Big Bad Beef Rub liberally on all areas of the meat and rub it in, setting aside any remaining rub to use once the meat has been smoked cubed. Keep the meat chilled until just before you cook it. Chilled meat attracts more smoke. I strongly recommend you use a remote digital thermometer and insert the probe with the tip centered in the thickest part of the meat furthest from the heat.",
            "Fire up. Pre-heat your smoker, or if you are using a grill, set it up for indirect cooking. Click here to see how to set up a gas grill, here to set up a charcoal grill, or here to set up a bullet smoker like the Weber Smokey Mountain. Get the cooker temp stabilized at about 235°F (113°C). We want to cook at about 225°F (107°C), but the temp will drop a bit once you open the lid and load in the cold meat.",
            "Cook. Put the meat on the cooker. On a smoker with a water pan, put the meat right above the water. Place the oven temp probe on the grate next to the meat. Add about 2 cups (4 ounces (113 g)) of wood right after the meat goes on. When the smoke stops, add 4 ounces more during the first 2 hours, which usually means adding some every 30 minutes or so. Keep an eye on the water in the pan. Don't let it dry out. After 3 hours, turn the meat over if the color is different from top to bottom. Otherwise, leave the meat alone. No need to mop, baste, or spritz. It just lowers the temp of the meat and softens the bark.",
            "When the meat's internal temperature reaches 155°F (68.3°C) and has taken on a nice dark hue, take the meat off of the smoker or grill and wrap it tightly in a double layer of heavy-duty foil. Add the beef broth, crimp the foil tight, and put the wrapped meat back on the smoker or grill over indirect heat. This step, called the Texas Crutch, slightly braises and steams the meat, but most importantly, it prevents the surface evaporation that cools down the meat and causes the stall (read more about the stall here).",
            "Prep again. When the meat temp hits 195°F (95°C), carefully remove it from the foil, reserving the liquid to use later. Cut the point into cubes about 1-inch on all sides. Set aside any pieces that are too fatty or just eat them. Dust them with rub and a little sugar to accelerate browning and bark formation. Tumble them onto a grill topper on a hot grill over direct heat for a few minutes to caramelize the sugars and brown the cut edges.",
            "Cook again. In a frying pan, render the beef fat that you trimmed from the brisket point. Or better still, use bacon fat or duck fat. You can do this over hot coals. Move the cubes to the pan and gently fry them until they are crunchy on the outside, turning them a few times. Drain the fat and add about 1/4 cup of your favorite BBQ sauce and 1/4 cup of the drippings from the foil used for the Texas Crutch. Put the pan back on the grill and stir every 5 minutes or so. Let the cubes absorb most of the liquid and start to sizzle, but don't let them burn.",
            "Serve. When they're done, serve them before they go soft. You can just present them in a pile on a plate, or on a bun. I like to make a banh mi type sandwich with quick pickled onions on a garlic bread baguette sandwich.",
        ]
        self.assertEqual(
            expected_instructions, self.harvester_class.instructions_list()
        )

    def test_ratings(self):
        self.assertEqual(4.72, self.harvester_class.ratings())
