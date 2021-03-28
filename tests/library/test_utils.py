import unittest

from recipe_scrapers._utils import get_minutes


class TestUtils(unittest.TestCase):
    def test_get_minutes_english_description(self):
        text = "1 hour 15 mins"
        result = get_minutes(text)

        assert result == 75

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
