import os
from typing import Dict
import unittest

import responses


class ScraperTest(unittest.TestCase):

    maxDiff = None
    online = False
    test_file_name = None
    test_file_extension = "testhtml"

    @property
    def expected_requests(self) -> Dict[str, str]:
        """
        A mapping of expected HTTP GET URLs to filenames that contain response content.
        """
        filename = self.test_file_name or self.scraper_class.__name__.lower()
        path = f"tests/test_data/{filename}.{self.test_file_extension}"
        yield "https://test.example.com", path

    def setUp(self):
        os.environ[
            "RECIPE_SCRAPERS_SETTINGS"
        ] = "tests.test_data.test_settings_module.test_settings"

        with responses.RequestsMock() as rsps:
            start_url = None
            for url, path in self.expected_requests:
                start_url = start_url or url
                content = open(path, encoding="utf-8").read()
                response = responses.Response(responses.GET, url, body=content)
                response.passthrough = self.online
                rsps.add(response)

            self.harvester_class = self.scraper_class(url=start_url)
