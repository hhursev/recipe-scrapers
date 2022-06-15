import unittest

from recipe_scrapers._utils import get_minutes


class TestUtils(unittest.TestCase):
    def test_get_minutes_english_description(self):
        text = "1 hour 15 mins"
        self.assertEqual(75, get_minutes(text))

    def test_get_minutes_english_description_with_and(self):
        text = "1h and 15mins"
        self.assertEqual(75, get_minutes(text))

    def test_get_minutes_english_abbreviation(self):
        text = "3h10m"
        self.assertEqual(190, get_minutes(text))

    def test_get_minutes_short_iso_format(self):
        text = "PT2H30M"
        self.assertEqual(150, get_minutes(text))

    def test_get_minutes_long_iso_format(self):
        text = "P0DT1H10M"
        self.assertEqual(70, get_minutes(text))

    def test_get_minutes_int_in_string_literal(self):
        text = "90"
        self.assertEqual(90, get_minutes(text))

    def test_get_minutes_fraction_in_hours_with_dot_notation(self):
        text = "1.5 hours"
        self.assertEqual(90, get_minutes(text))

    def test_get_minutes_fraction_with_fraction_unicode_character_halves(self):
        text = "1½ hours"
        self.assertEqual(90, get_minutes(text))

    def test_get_minutes_fraction_with_fraction_unicode_character_three_fours(self):
        text = "1¾ hours"
        self.assertEqual(105, get_minutes(text))

    def test_get_minutes_fraction_with_fraction_unicode_character_one_fours(self):
        text = "1¼ hours"
        self.assertEqual(75, get_minutes(text))

    def test_get_minutes_fraction_with_fraction_unicode_character_two_thirds(self):
        text = "1⅔ hours"
        self.assertEqual(100, get_minutes(text))

    def test_get_minutes_fraction_with_fraction_digits_with_slash(self):
        text = "1 1/2 hours"
        self.assertEqual(90, get_minutes(text))

    def test_get_minutes_fraction_with_fraction_digits_with_slash_three_fours(self):
        text = "1 3/4 hours"
        self.assertEqual(105, get_minutes(text))

    def test_get_minutes_fraction_with_fraction_digits_with_slash_one_fours(self):
        text = "1 1/4 hours"
        self.assertEqual(75, get_minutes(text))

    def test_get_minutes_fraction_with_fraction_digits_with_slash_two_thirds(self):
        text = "1 2/3 hours"
        self.assertEqual(100, get_minutes(text))

    def test_get_minutes_handles_dashes(self):
        text = "15 - 20 minutes"
        self.assertEqual(20, get_minutes(text))

    def test_get_minutes_handles_to(self):
        text = "15 to 20 minutes"
        self.assertEqual(20, get_minutes(text))
