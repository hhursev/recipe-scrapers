# mypy: allow-untyped-defs

from recipe_scrapers.maangchi import Maangchi
from tests import ScraperTest


class TestMaangchiScraper(ScraperTest):
    scraper_class = Maangchi

    def test_host(self):
        self.assertEqual("maangchi.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.maangchi.com/recipe/yuringi",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Maangchi", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Pepper fried chicken (Yuringi: 유린기)", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Main", self.harvester_class.category())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://i.ytimg.com/vi/JhE4ToJOPcc/maxresdefault.jpg?meta=og:image",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 pound boneless & skinless chicken thighs",
                "½ teaspoon kosher salt",
                "¼ teaspoon ground black pepper",
                "2 inch of white part of dae-pa (or 2 to 3 regular green onions), thinly sliced lengthwise",
                "¼ of small onion (about 2 tablespoons), thinly sliced",
                "2 cups grape seeds oil (or vegetable oil, corn oil) for frying",
                "4 to 5 lettuce leaves",
                "3 to 4 spicy green and red chili peppers (or non-spicy peppers, green and red bell pepper), thinly sliced",
                "2 tablespoons grape seeds oil (or vegetable oil)",
                "1 teaspoon crushed chili pepper (or 2 small dried red chili peppers or Korean hot pepper flakes)",
                "3 tablespoons soy sauce",
                "3 tablespoons white vinegar (or apple cider vinegar)",
                "3 tablespoons Turbinado sugar (or white or brown sugar)",
                "2 tablespoons water",
                "4 garlic cloves, minced",
                "1 teaspoon toasted sesame oil",
                "¼ cup potato starch",
                "⅛ teaspoon kosher salt",
                "1 large egg",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Pat the chicken thighs dry with paper towels. Score a crosshatch patten on both sides of the chicken pieces.\nPound the thighs to an even thickness with a meat tenderizer or with the back of your kitchen knife.\nSprinkle both sides with salt and ground black pepper.\nSet aside or refrigerate until ready to use.\nPlace the shredded green onion and onion in a bowl and add cold water. Let it sit.\nHeat the vegetable oil in a small pan until it begins to smoke, about 30 seconds to 1 minute.\nRemove from the heat. Stir in the pepper flakes until they are slightly brown. Strain the oil into a medium sized stainless steel bowl.\nAdd the soy sauce, vinegar, sugar, water, garlic, and sesame oil.\nStir well until the sugar is completely dissolved.\nPrepare a shallow and wide bowl (I use my large, shallow plastic bowl).\nAdd the starch and salt. Crack in an egg.\nMix well with a spoon or a whisk.\nHeat the oil in a large, deep pan over medium-high heat until it reaches about 340° to 350° F. If you don’t have a kitchen thermometer, test the oil temperature by dipping a tip of a chicken piece into it. If it bubbles, it’s ready.\nDip a chicken piece into the batter and wipe off the excess with the side of the bowl. Add it to the oil one piece at a time, working in batches if your pan is small. My 12 inch large pan is perfect for frying 4 pieces of chicken thighs at a time. Repeat with the rest of the chicken pieces until all are in the pan.\nDeep-fry, turning the chicken with tongs, until all sides are light golden brown and crunchy, about 5 to 6 minutes. As each piece is done, transfer it to a strainer over a bowl to drain the excess oil.\nReheat the oil for about 1 minute and add all the chicken again. It will look a little soggy at first. Deep-fry, turning occasionally, until all the chicken pieces are dark golden brown and very crunchy, another 5 to 6 minutes.\nTransfer the chicken pieces to the strainer over the bowl to drain. Let them cool for a few minutes until you can handle them.\nAdd the sliced chili pepper to the sauce and mix it together.\nDrain the soaking green onion and onion through a strainer set in your sink. Rinse it under cold running water, turning it over by hand for 10 seconds. Drain well.\nCut the chicken into bite size pieces and put them on a large plate lined with the lettuce. Spoon the peppers out of the sauce and put them on top of the chicken.\nAdd the shredded green onion and onion and gently pour the rest of the sauce all over top.\nServe right away.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Korean", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "Today I'm introducing you to another Korean Chinese dish called yuringi (pronounced yu-rin-gi). It's fried chicken with peppers and a light sweet sour sauce. A piece of crunchy chicken soaked in sweet, sour, salty sauce tastes so crispy and juicy! The chopped spicy fresh pepper served with this...",
            self.harvester_class.description(),
        )
