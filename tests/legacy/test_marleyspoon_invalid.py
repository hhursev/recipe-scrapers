import unittest

import responses

from recipe_scrapers._exceptions import RecipeScrapersExceptions
from recipe_scrapers.marleyspoon import MarleySpoon


class TestFaultyAPIURLResponse(unittest.TestCase):

    @responses.activate
    def test_invalid_scraper(self):
        valid_url = "https://marleyspoon.de/menu/113813-glasierte-veggie-burger-mit-roestkartoffeln-und-apfel-gurken-salat"
        with open("tests/legacy/test_data/faulty.testhtml") as faulty_data:
            faulty_response = faulty_data.read()

        responses.add(
            method=responses.GET,
            url=valid_url,
            body=faulty_response,
        )

        with self.assertRaises(RecipeScrapersExceptions):
            MarleySpoon(url=valid_url)
