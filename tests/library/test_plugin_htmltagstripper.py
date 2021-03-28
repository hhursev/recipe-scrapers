import unittest

from recipe_scrapers.plugins import HTMLTagStripperPlugin


class TestHTMLTagStripperPlugin(unittest.TestCase):
    def sample_ingredients_method(self, *args, **kwargs):
        return [
            "3 tbsp. <p>extra-virgin olive oil, divided</p>",
            "<p>Juice of 1 lemon</p>",
            "3 <p>cloves garlic, minced</p>",
            "1 tsp. <p>dried oregano</p>",
            "1 lb. <p>chicken thighs</p>",
            "<p>kosher salt</p>",
            "<p>Freshly ground black pepper</p>",
            "1/2 lb. <p>asparagus, ends removed</p>",
            "1 <p>zucchini, sliced into half moons</p>",
            "1 <p>lemon, sliced</p>",
        ]

    def sample_instructions_method(self, *args, **kwargs):
        return """
            blah blah \n\n
            blah <p>should remove ps</p>
            blah blah \n\n
        """

    def test_sample_ingredients_method(self):
        # the default method is intact
        self.assertEqual(
            self.sample_ingredients_method(),
            [
                "3 tbsp. <p>extra-virgin olive oil, divided</p>",
                "<p>Juice of 1 lemon</p>",
                "3 <p>cloves garlic, minced</p>",
                "1 tsp. <p>dried oregano</p>",
                "1 lb. <p>chicken thighs</p>",
                "<p>kosher salt</p>",
                "<p>Freshly ground black pepper</p>",
                "1/2 lb. <p>asparagus, ends removed</p>",
                "1 <p>zucchini, sliced into half moons</p>",
                "1 <p>lemon, sliced</p>",
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
                "1 tsp. dried oregano",
                "1 lb. chicken thighs",
                "kosher salt",
                "Freshly ground black pepper",
                "1/2 lb. asparagus, ends removed",
                "1 zucchini, sliced into half moons",
                "1 lemon, sliced",
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
            blah blah \n\n
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
            blah blah \n\n
        """,
            "Result must have html tags stripped when invoked after plugin used",
        )
