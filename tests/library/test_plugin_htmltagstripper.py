import unittest

from recipe_scrapers.plugins import HTMLTagStripperPlugin


class TestHTMLTagStripperPlugin(unittest.TestCase):
    def sample_ingredients_method(self, *args, **kwargs):
        return [
            "3 tbsp. <p>extra-virgin olive oil, divided</p>",
            "<p>Juice of 1 lemon</p>",
            "3 <p>cloves garlic, minced</p>",
        ]

    def sample_title_method(self, *args, **kwargs):
        return "Sticky Pomegranate &amp;amp; Black Pepper Chicken Wing"

    def sample_instructions_method(self, *args, **kwargs):
        return """
            blah blah \n\n
            blah <p>should remove ps</p>
        """

    def test_sample_ingredients_method(self):
        # the default method is intact
        self.assertEqual(
            self.sample_ingredients_method(),
            [
                "3 tbsp. <p>extra-virgin olive oil, divided</p>",
                "<p>Juice of 1 lemon</p>",
                "3 <p>cloves garlic, minced</p>",
            ],
            "Original method should be as defined in the test class",
        )

        # we "decorate" our  sample_instructions_method as we would in _abstract.py with the
        # HTMLTagStripper plugin if it is used. Note how the result returned from the method
        # is changed as the plugin kicks in
        name = "sample_ingredients_method"
        setattr(
            self.__class__,
            name,
            HTMLTagStripperPlugin.run(getattr(self.__class__, name)),
        )

        return self.assertEqual(
            self.sample_ingredients_method(),
            [
                "3 tbsp. extra-virgin olive oil, divided",
                "Juice of 1 lemon",
                "3 cloves garlic, minced",
            ],
            "Result must have html tags stripped when invoked after plugin used",
        )

    def test_sample_instructions_method(self):
        # the default method is intact
        self.assertEqual(
            self.sample_instructions_method(),
            """
            blah blah \n\n
            blah <p>should remove ps</p>
        """,
            "Original method should be as defined in the test class",
        )

        # we "decorate" our  sample_instructions_method as we would in _abstract.py with the
        # HTMLTagStripper plugin if it is used. Note how the result returned from the method
        # is changed as the plugin kicks in
        name = "sample_instructions_method"
        setattr(
            self.__class__,
            name,
            HTMLTagStripperPlugin.run(getattr(self.__class__, name)),
        )

        return self.assertEqual(
            self.sample_instructions_method(),
            """
            blah blah \n\n
            blah should remove ps
        """,
            "Result must have html tags stripped when invoked after plugin used",
        )

    def test_sample_title_method(self):
        self.assertEqual(
            self.sample_title_method(),
            "Sticky Pomegranate &amp;amp; Black Pepper Chicken Wing",
            "Original method should be as defined in the test class",
        )

        # we "decorate" our  sample_instructions_method as we would in _abstract.py with the
        # HTMLTagStripper plugin if it is used. Note how the result returned from the method
        # is changed as the plugin kicks in
        name = "sample_title_method"
        setattr(
            self.__class__,
            name,
            HTMLTagStripperPlugin.run(getattr(self.__class__, name)),
        )

        return self.assertEqual(
            self.sample_title_method(),
            "Sticky Pomegranate & Black Pepper Chicken Wing",
            "Result must have html tags stripped when invoked after plugin used",
        )
