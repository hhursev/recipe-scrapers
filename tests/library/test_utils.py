import unittest

from recipe_scrapers._utils import get_minutes


class UtilsTest(unittest.TestCase):
    def test_get_minutes_english_description(self):
        text = "1 hour 15 mins"
        result = get_minutes(text)

        assert result == 75

    def test_get_minutes_english_abbreviation(self):
        text = "3h10m"
        result = get_minutes(text)

        assert result == 190

    def test_get_minutes_short_iso_format(self):
        text = "PT2H30M"
        result = get_minutes(text)

        assert result == 150

    def test_get_minutes_long_iso_format(self):
        text = "P0DT1H10M"
        result = get_minutes(text)

        assert result == 70
