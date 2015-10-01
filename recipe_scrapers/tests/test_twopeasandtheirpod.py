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

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Red Velvet Cheesecake Cookies'
        )

    def test_total_time(self):
        # as it is written '12-15 minutes in our test case'
        self.assertEqual(
            13,
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
            "1. To make cookies, in a large bowl combine cake mix and flour. Whisk until clumps disappear. In the bowl of a stand mixer, mix together cake mix, flour, eggs, oil and vanilla extract. Mix until smooth. Wrap the dough in plastic wrap. The dough will be oily. Refrigerate for at least two hours.\n2. To make the cheesecake filling, using a mixer, combine cream cheese, powdered sugar, and vanilla extract. Mix until smooth. Using a teaspoon, scoop out cheesecake filling and place on a plate. Continue scooping out cheesecake filling into teaspoon balls until you have 10. Place plate in the freezer and freeze for at least two hours.\n3. Preheat oven to 350 degrees F. Line a large baking sheet with parchment paper or a silicone baking mat. To assemble the cookies, take about 1/4 cup of red velvet cookie dough and flatten in your hands. Place a teaspoon of cheesecake filling in the center and wrap the cookie dough around the filling. Gently roll into a ball and place on prepared baking sheet. Scoop onto lightly greased or parchment lined baking sheets. Only bake 3 cookies at a time. The cookies are large and will spread. Bake for 11-13 minutes or until the cookies begin to crackle. Let the cookies cool on the baking sheet for 5 minutes. Remove from baking sheet to a wire cooling rack and cool completely.\n4. Melt the white chocolate chips in a microwave safe bowl or over a double-boiler. Drizzle the white chocolate over the cooled cookies. Let the cookies set until the chocolate hardens. Serve and enjoy!\nNote: if you are going to store the cookies for more than a day, you may want to keep them in the refrigerator. You can make the cookies smaller. Just use less dough and filling. You want to make sure you completely wrap the cookie dough around the filling before baking-so it doesn't leak. Enjoy!",
            self.harvester_class.instructions()
        )
