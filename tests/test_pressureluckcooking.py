# mypy: allow-untyped-defs

from recipe_scrapers.pressureluckcooking import PressureLuckCooking
from tests import ScraperTest

# Data from https://pressureluckcooking.com/instant-pot-jeffreys-favorite-chicken/


class TestPressureLuckCookingScraper(ScraperTest):
    scraper_class = PressureLuckCooking

    def test_host(self):
        self.assertEqual("pressureluckcooking.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://pressureluckcooking.com/instant-pot-jeffreys-favorite-chicken/",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Jeffrey", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Instant Pot Jeffrey's Favorite Chicken", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Poultry", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://pressureluckcooking.com/wp-content/uploads/2023/01/Jeffreys-Favorite-Chicken-IG-1-scaled-720x720.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 1/2 - 2 pounds boneless, skinless chicken cutlets (breasts sliced into 1/4-inch thick fillets)",
                "1/4 cup of one of the following: all-purpose flour, whole wheat flour, coconut flour, or quinoa flour (with a few pinches garlic powder, peppers and salt mixed in with a fork)",
                "1/4 cup extra-virgin olive oil",
                "2 teaspoons ghee or 1 tablespoon salted butter, divided (see Jeff's Tips)",
                "2 large shallots, diced",
                "8 ounces baby bella or white mushrooms, sliced",
                "6 cloves (2 tablespoons) garlic, minced or pressed",
                "1/2 cup dry white wine (like a sauvignon blanc) or additional broth",
                "Juice of 1/2 lemon",
                "1/2 cup low-sodium chicken broth",
                "1 teaspoon Italian seasoning",
                "1 teaspoon seasoned salt",
                "5-8 ounces baby spinach",
                "1 tablespoon cornstarch + 1 tablespoon cold water",
                "1/4 cup any milk of your choice (or an unsweetened nondairy milk such as almond, oat or soy)",
                "1 (10-ounce) jar sun-dried tomatoes, drained and roughly chopped",
                "1 (14-ounce) can artichoke hearts, drained and chopped",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Dredge the chicken cutlets in the flour mixture so they're lightly coated and set aside on a plate.\nAdd the olive oil and half the butter/ghee, hit Sauté and Adjust to the More or High setting. After 3 minutes of heating, add the chicken to the pot in batches and sear on each side for about 45-60 seconds, until just ever so lightly browned. Use tongs to remove and rest the seared on a plate.\nAdd the remaining half of butter/ghee. (NOTE: If the olive oil is totally gone from searing the chicken, you can add 1 additional tablespoon). Once the butter's melted, add the shallots and mushrooms and sauté for 2 minutes. Add the garlic and sauté for 1 minute longer.\nAdd the wine (or additional 1/2 cup of broth) and lemon juice and simmer for 2 minutes, scraping the bottom of the pot to loosen any browned bits so it's nice and smooth.\nAdd the broth, Italian seasoning, seasoned salt and stir. Return the seared chicken to the pot and top with the spinach (if it seems piled high, don't worry. It cooks down to nothing).\nSecure the lid, movie the valve to the sealing position, and hit Cancel followed by Pressure Cook or Manual at High Pressure for 5 minutes. Quick release when done. Using tongs, transfer the chicken to a serving dish.\nMix together the cornstarch and water to form a slurry.\nHit Cancel followed by Sauté and Adjust to the More or High setting. Stir in the slurry and it will thicken the sauce immediately. Stir in the milk, sun-dried tomatoes and artichokes. Hit Cancel to turn the pot off.\nLadle the sauce over the chicken and serve!",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(4.4, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "A fervent believer in giving folks what they ask for, I recently polled my readers for the next dish they wanted me to make. The winner was chicken and I felt it only fitting to finally put one of my favorite recipes that in my Lighter (blue) book on the blog. In fact, it's called Jeffrey's Favorite Chicken for a reason and seeing how it's tender cutlets in a light, yet rich and hearty lemon-wine sauce loaded with mushrooms, spinach, artichokes and sun-dried tomatoes, can you blame me? It can also easily be keto, paleo, gluten-free and dairy-free (see Jeff's Tips).",
            self.harvester_class.description(),
        )
