from recipe_scrapers.paleorunningmomma import PaleoRunningMomma
from tests import ScraperTest


class TestPaleoRunningMommaScraper(ScraperTest):

    scraper_class = PaleoRunningMomma

    def test_host(self):
        self.assertEqual("paleorunningmomma.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Michele Rosen", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Paleo Beef Stroganoff {Whole30, Keto}",  # noqa
            self.harvester_class.title(),
        )

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.paleorunningmomma.com/wp-content/uploads/2020/12/beef-stroganoff-9.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "5 Tbsp ghee (divided)",
                "1.5 lb top sirloin or tenderloin (thinly sliced into 1/2” x 2” strips)",
                "1 large onion (thinly sliced)",
                "Sea salt and black pepper to taste",
                "8 oz mushrooms (sliced)",
                "3 cloves garlic (minced)",
                "2 cups beef broth",
                "1 Tbsp coconut aminos",
                "2 Tbsp arrowroot flour (or tapioca)",
                "Salt to taste and black pepper to taste",
                "1 cup coconut cream (canned, unsweetened)",
                "1 Tbsp fresh lemon juice",
                "1 tsp dijon mustard",
                "Pinch Sea salt",
                "Sea salt and black pepper to taste",
                "Minced parsley (for garnish)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "In a large deep skillet, melt 2 tablespoons of the ghee over medium-high heat.\nAdd the steak in a single layer, season with salt and pepper, and let it cook for 3 minutes to brown. Flip, and cook on the other side until browned, another 2 minutes. Then remove steak from pan with a slotted spoon, transfer to a plate, and set aside.\nLower the heat to medium and the remaining 3 tablespoons of ghee to the skillet. Once it has melted, add the onions and sauté for about 3 minutes, until soft and fragrant. Add mushrooms and sauté for an additional 5-7 minutes, stirring occasionally, or until the mushrooms are cooked and the onions are soft, then add the garlic and sauté 1 minute, stirring occasionally.\nIn a bowl or large measuring cup, whisk in together the beef broth, coconut aminos and arrowroot until smooth. Pour the mixture into the skillet and stir well to combine. Simmer for about 5 minutes, stirring occasionally. Meanwhile, in a separate small bowl whisk together the coconut cream, lemon juice, mustard and a pinch of sea salt. Stir the coconut cream mixture plus the cooked steak into the skillet and stir until combined. Taste and season with additional salt and pepper if needed, and cook just long enough to heat through.\nGarnish with parsley, if desired, and serve over cauliflower rice or your favorite veggie noodles. Enjoy!",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.15, self.harvester_class.ratings())
