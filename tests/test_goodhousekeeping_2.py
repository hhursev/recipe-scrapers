# mypy: allow-untyped-defs

from recipe_scrapers.goodhousekeeping import GoodHousekeeping
from tests import ScraperTest


class TestGoodHousekeepingScraper(ScraperTest):
    scraper_class = GoodHousekeeping
    test_file_name = "goodhousekeeping_2"

    def test_host(self):
        self.assertEqual("goodhousekeeping.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Ailsa Burt", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Vegetarian fajitas", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("vegetarian,dinner", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://hips.hearstapps.com/hmg-prod/images/vegetarian-fajitas-1545043586.jpg?crop=0.497xw:0.884xh;0,0.0638xh&resize=1200:*",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 tsp. garlic granules",
                "1 tsp. ground cumin",
                "3/4 tsp. ground coriander",
                "1 tsp. smoked paprika",
                "1/2 tsp. mild chilli powder",
                "1 tsp. dried oregano",
                "250 g block halloumi, cut into strips",
                "1 red onion, sliced thickly",
                "2 peppers, cut into strips",
                "1 tbsp. vegetable oil",
                "Tortilla wraps",
                "Soured cream",
                "Guacamole",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        instructions = [
            "1. Preheat oven to 200°C (180°C fan) mark 6. In a small bowl mix together the garlic granules, cumin, coriander, paprika, chilli powder and oregano.",
            "2. Add the halloumi, red onion and peppers to a large baking tray. Toss with the vegetable oil and the spice mix. Cook for 20min or until the halloumi is evenly browned.",
            "3. Serve with tortillas, sour cream and guacamole.",
        ]
        self.assertEqual("\n".join(instructions), self.harvester_class.instructions())

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_nutrients(self):
        self.assertEqual(
            {
                "calories": "508cals",
                "fatContent": "35g",
                "fiberContent": "5g",
                "proteinContent": "31g",
                "saturatedFatContent": "21g",
                "sugarContent": "13g",
                "carbohydrateContent": "14g",
            },
            self.harvester_class.nutrients(),
        )

    def test_description(self):
        self.assertEqual(
            "These veggie fajitas are packed full of halloumi, and are SUPER easy to throw together!",
            self.harvester_class.description(),
        )
