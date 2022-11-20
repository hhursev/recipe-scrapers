# mypy: allow-untyped-defs

from recipe_scrapers.rosannapansino import RosannaPansino
from tests import ScraperTest


class TestRosannaPansinoScraper(ScraperTest):

    scraper_class = RosannaPansino

    def test_host(self):
        self.assertEqual("rosannapansino.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual("Marshmallow Fondant", self.harvester_class.title())

    def test_image(self):
        self.assertEqual(
            "http://cdn.shopify.com/s/files/1/0163/5948/9636/articles/1Y6A6281_grande.jpg?v=1567109086",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 bag (10 ounces) mini marshmallows",
                "3 tablespoons water",
                "6 cups powdered sugar",
                "Oil, for greasing your hands",
                "Food coloring gel (optional)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Pour the marshmallows into a microwave-safe bowl. Stir in the water to evenly coat the marshmallows.\nMicrowave for 30 seconds, then stir. Repeat this process two more times, or until the mixture is smooth.\nSift 3 cups of the powdered sugar into a large bowl and make a hole in the center.\nPour the melted marshmallow mixture onto the powdered sugar.\nSift the rest of the powdered sugar on top of the marshmallows.\nOil your hands to prevent the marshmallow from sticking to you. Knead in the sugar until you have the consistency of soft taffy and the fondant no longer sticks to your hands. If you are tinting the fondant, add food coloring now and knead until the color is fully incorporated. (Coat your hands with shortening so the colors don't stain them.)\nIf you are not using the fondant right away, store it tightly wrapped or in a plastic bag at room temperature.",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "A delicious and easy Marshmallow Fondant recipe!\nMakes 24 ounces",
            self.harvester_class.description(),
        )
