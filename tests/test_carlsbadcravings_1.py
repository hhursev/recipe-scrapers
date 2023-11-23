# mypy: allow-untyped-defs

from recipe_scrapers.carlsbadcravings import CarlsBadCravings
from tests import ScraperTest


class TestCarlsBadCravingsScraper(ScraperTest):
    scraper_class = CarlsBadCravings
    test_file_name = "carlsbadcravings_1"

    def test_host(self):
        self.assertEqual("carlsbadcravings.com", self.harvester_class.host())

    def canonical_url(self):
        self.assertEqual(
            "https://carlsbadcravings.com/brown-sugar-glazed-ham/",
            self.harvester_class.host(),
        )

    def test_author(self):
        self.assertEqual("Jen", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Brown Sugar Glazed Ham", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(130, self.harvester_class.total_time())

    def test_image(self):
        self.assertEqual(
            "https://carlsbadcravings.com/wp-content/uploads/2018/03/Brown-Sugar-Glazed-Ham-10.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 (8-11 pounds) bone-in, fully cooked spiral-sliced ham",
                "Aluminum foil",
                "Roasting pan",
                "Thermometer",
                "1 cup packed light brown sugar",
                "1/2 cup clover honey",
                "3 tablespoons cider vinegar",
                "2 tablespoons Dijon mustard",
                "2 tablespoons yellow mustard",
                "1 teaspoon ground cinnamon",
                "1/2 tsp EACH onion powder, garlic powder, ground sage, dried parsley, ground nutmeg ground ginger, ground cloves, paprika",
                "1/4 tsp EACH pepper, ancho chili powder",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Remove ham from refrigerator and let sit at room temperature for 2 hours.",
                    "Preheat oven to 325 degrees F. Adjust oven rack to lowest position. Pour 2 of cups water into bottom of roasting pan with a roasting rack. (Skip step if you don’t have a roasting rack.)",
                    "Whisk together all of the Brown Sugar Glaze ingredients in a medium saucepan. Bring to a simmer, stirring often, until brown sugar dissolves, about 1-2 minutes. Set aside.",
                    "Roll out 2 large pieces of foil to wrap your ham in, making sure they overlap in the center. Place ham on foil, flat side up, and brush ham all over with approximately 1/3 of the Glaze, including in between slices. Tightly wrap ham with foil and place ham FLAT/FACE SIDE DOWN on the roasting rack (or bottom of pan).",
                    "Bake ham at 325 degrees F until the center registers 100-110 degrees F, (approx. 10-14 minutes per pound). Remove ham from oven and increase oven temperature to 400 degrees F.",
                    "Carefully unwrap ham from foil and discard foil. Spoon juices from the bottom of the pan all over ham. Brush ham all over with 1/3 Glaze (Glaze will have thickened so return to heat to loosen, about 30 seconds).",
                    "Leave ham uncovered to caramelize surface and bake until the ham reaches an internal temperature of around 140 degrees F, approximately 20-30 minutes, spooning juices over ham every 10 minutes.*** Turn oven to broil for more caramelized edges if desired watching closely so they don’t burn.",
                    "Remove ham from oven and spoon juices from bottom of pan/foil again all over ham and brush again with Glaze. Loosely cover with foil. Let rest for 15 minutes then spoon more juices over ham and serve with any remaining Glaze (and my husband loves it with a side of Dijon as well).",
                    "Optional: Serve with Easter or Christmas sides linked below recipe.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_yields(self):
        self.assertEqual("10 servings", self.harvester_class.yields())

    def test_description(self):
        self.assertEqual(
            "Brown Sugar Glazed Ham is beautifully juicy, seeping with flavor, with crispy caramelized edges and the BEST Brown Sugar Glaze you will ever sink your teeth into - the perfect centerpiece for Easter and Christmas! This Baked Ham Recipe made with brown, sugar, honey, mustard and spices is sweet, smoky and dripping with flavor AND it only takes minutes of hands on prep time!",
            self.harvester_class.description(),
        )
