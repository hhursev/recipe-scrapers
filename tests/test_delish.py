import os 
import unittest

from recipe_scrapers.delish import Delish


class TestDelishScraper(unittest.TestCase):
    def setUp(self):
        #tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'delish.testhtml'
        )) as file_opened:
            self.harvester_class = Delish(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            self.harvester_class.host(),
            'delish.com'   
        )
    
    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Pumpkin Cheesecake Roll'
        )
    
    def test_total_time(self):
        self.assertEqual(
            self.harvester_class.total_time(),
            60
        )
    
    def test_yields(self):
        self.assertEqual(
            self.harvester_class.yields(),
            '8 serving(s)'
        )
    
    def test_image(self):
        self.assertEqual(
            self.harvester_class.image(),
            'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-190814-pumpkin-roll-0029-portrait-pf-1567187757.jpg?crop=1.00xw:0.667xh;0,0.0545xh&resize=768:*'
        )

    def test_ingredients(self):
        self.assertEqual(
            self.harvester_class.ingredients(),
            [
                'Cooking spray', 
                '1 c. granulated sugar', 
                '3/4 c. all-purpose flour', 
                '1/2 tsp. kosher salt', 
                '1 tsp. baking soda', 
                '1/2 tsp. pumpkin spice', 
                '3 large eggs', 
                '2/3 c. pumpkin puree', 
                'Powdered sugar, for rolling', 
                '12 oz. cream cheese, softened', 
                '1 tbsp. melted butter', 
                '1 tsp. pure vanilla extract', 
                '1 1/4 c. powdered sugar', 
                '1/2 tsp. kosher salt'
            ]
        )
    
    def test_instructions(self):
        self.assertEqual(
            self.harvester_class.instructions(),
            'Preheat oven to 350°. Line a 15” x 10” jelly roll pan with parchment and grease with cooking spray. In a large bowl, combine sugar, flour, salt, baking soda, pumpkin spice, eggs, and pumpkin puree until just combined. Spread into prepared pan and bake until a toothpick inserted in center of cake comes out clean, 15 minutes.\nMeanwhile, lay out a large kitchen towel on your counter (try to use one with little to no texture) and dust with powdered sugar. When cake is done baking, flip onto kitchen towel and gently peel off parchment paper.\nStarting at a short end, gently but tightly roll cake into a log. Let cool completely.\nMeanwhile, make filling: In a large bowl, combine cream cheese, melted butter, vanilla, powdered sugar, and salt. Using a hand mixer, whip until smooth.\nWhen cake is cooled, gently unroll (it’s ok if it remains slightly curled) and spread with cream cheese filling. Roll back up and dust with more powdered sugar. Slice and serve.'
        )
    