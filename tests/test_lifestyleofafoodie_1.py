# mypy: allow-untyped-defs

from recipe_scrapers.lifestyleofafoodie import LifestyleOfAFoodie
from tests import ScraperTest


class TestLifestyleOfAFoodieScraper(ScraperTest):

    scraper_class = LifestyleOfAFoodie
    test_file_name = "lifestyleofafoodie_1"

    def test_host(self):
        self.assertEqual("lifestyleofafoodie.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Chahinez", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Frozen strawberry margaritas", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Drinks", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(5, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://lifestyleofafoodie.com/wp-content/uploads/2023/06/Frozen-strawberry-margarita-5.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "3 cup frozen strawberries",
                "4 ounces tequila (add more if you'd like)",
                "1/4 cup Lime juice",
                "2 tablespoon agave syrup (taste and add more if needed. )",
                "1/2-1 cup ice cubes (as needed)",
                "Lime wedges for garnish (optional)",
                "Salt or sugar for rimming the glass (optional)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        expected_output = (
            "Rim the glass with salt if desired. Rub a lime wedge around the rim of the glass, then dip it into a plate with salt, rotating to coat the rim evenly. Set the glass aside.\n"
            "In a blender, combine the frozen strawberries, ice, tequila, lime juice, and agave syrup and blend until smooth. If needed, add a splash of water or more lime juice to adjust the consistency. Want it thicker, add some ice.\n"
            "Taste the margarita and adjust the sweetness or tartness by adding more agave syrup or lime juice, if desired.\n"
            "Once the frozen mango margarita is ready, pour it into the rimmed glass. Garnish with a lime wedge, mint, slices, or mango if desired. Serve immediately and enjoy!"
        )
        actual_output = self.harvester_class.instructions()
        self.assertEqual(expected_output, actual_output)

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("American", self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(
            "These delicious frozen strawberry margaritas are the perfect drink to add to your summer drink rotation.",
            self.harvester_class.description(),
        )
