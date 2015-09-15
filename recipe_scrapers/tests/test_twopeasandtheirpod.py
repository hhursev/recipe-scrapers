import os
import unittest

from recipe_scrapers.twopeasandtheirpod import TwoPeasAndTheirPod


class TestTwoPeasAndTheirPodScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'twopeasandtheirpod.html'
        )) as file_opened:
            self.harvester_class = TwoPeasAndTheirPod(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'twopeasandtheirpod.com',
            self.harvester_class.host()
        )

    def test_publisher_site(self):
        self.assertEqual(
            'http://twopeasandtheirpod.com/',
            self.harvester_class.publisher_site()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Red Velvet Cheesecake Cookies'
        )

    def test_total_time(self):
        # as it is written '12-15 minutes in our test case'
        self.assertEqual(
            0,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                '1 box red velvet cake mix (I used Duncan Hines)',
                '2 tablespoons all-purpose flour',
                '2 large eggs',
                '1/2 cup canola oil',
                '1 teaspoon vanilla extract',
                '4 oz cream cheese, at room temperature',
                '2 cups powdered sugar',
                '1 teaspoon vanilla extract',
                '1 1/2 cups white chocolate chips, melted'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            "1. To make cookies, in a large bowl combine\n cake mix and flour. Whisk until clumps disappear. In the bowl of a \nstand mixer, mix together cake mix, flour, eggs, oil and vanilla \nextract. Mix until smooth. Wrap the dough in plastic wrap. The dough \nwill be oily. Refrigerate for at least two hours. \n2. To make the cheesecake filling, using a mixer, combine cream \ncheese, powdered sugar, and vanilla extract. Mix until smooth. Using a \nteaspoon, scoop out cheesecake filling and place on a plate. Continue \nscooping out cheesecake filling into teaspoon balls until you have 10. \nPlace plate in the freezer and freeze for at least two hours. \n3. Preheat oven to 350 degrees F. Line a large baking sheet with \nparchment paper or a silicone baking mat. To assemble the cookies, take \nabout 1/4 cup of red velvet cookie dough and flatten in your hands. \nPlace a teaspoon of cheesecake filling in the center and wrap the cookie\n dough around the filling. Gently roll into a ball and place on prepared\n baking sheet. Scoop onto lightly greased or parchment lined baking \nsheets. Only bake 3 cookies at a time. The cookies are large and will \nspread. Bake for 11-13 minutes or until the cookies begin to crackle. \nLet the cookies cool on the baking sheet for 5 minutes. Remove from \nbaking sheet to a wire cooling rack and cool completely. \n4. Melt the white chocolate chips in a microwave safe bowl or over a \ndouble-boiler. Drizzle the white chocolate over the cooled cookies. Let \nthe cookies set until the chocolate hardens. Serve and enjoy!\nNote: if you are going to store the cookies for more than a day, you \nmay want to keep them in the refrigerator. You can make the cookies \nsmaller. Just use less dough and filling. You want to make sure you \ncompletely wrap the cookie dough around the filling before baking-so it \ndoesn't leak. Enjoy!\n",
            self.harvester_class.instructions()
        )
