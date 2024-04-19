import unittest

import responses

from recipe_scrapers._exceptions import RecipeScrapersExceptions
from recipe_scrapers.marleyspoon import MarleySpoon


class TestFaultyAPIURLResponse(unittest.TestCase):

    @responses.activate
    def test_faulty_response(self):
        url = "https://marleyspoon.de/menu/113813-glasierte-veggie-burger-mit-roestkartoffeln-und-apfel-gurken-salat"
        with open("tests/legacy/test_data/faulty.testhtml") as faulty_data:
            faulty_response = faulty_data.read()

        responses.add(
            method=responses.GET,
            url=url,
            body=faulty_response,
        )

        with self.assertRaises(RecipeScrapersExceptions):
            MarleySpoon(url=url)

    @responses.activate
    def test_relative_api_url(self):
        url = "https://marleyspoon.de/menu/113813-glasierte-veggie-burger-mit-roestkartoffeln-und-apfel-gurken-salat"
        with open("tests/legacy/test_data/relative_url.testhtml") as relative_url_data:
            relative_url_response = relative_url_data.read()

        responses.add(
            method=responses.GET,
            url=url,
            body=relative_url_response,
        )

        with self.assertRaises(Exception):
            MarleySpoon(
                url=url
            )  # currently this raises an requests.exceptions.MissingSchema exception
