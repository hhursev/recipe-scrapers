import unittest
from typing import Any, Iterator, Optional, Tuple

import responses


class ScraperTest(unittest.TestCase):

    maxDiff = None
    test_file_name: Optional[str] = None
    test_file_extension = "testhtml"
    scraper_class: Any

    @classmethod
    def expected_requests(cls) -> Iterator[Tuple[str, str, str]]:
        """
        Descriptions of the expected requests that the scraper-under-test will make, as
        tuples of: HTTP method, URL, path-to-content-file
        """
        filename = cls.test_file_name or cls.scraper_class.__name__.lower()
        path = f"tests/test_data/{filename}.{cls.test_file_extension}"
        yield responses.GET, "https://test.example.com", path

    @classmethod
    def setUpClass(cls):
        with responses.RequestsMock() as rsps:
            start_url = None
            for method, url, path in cls.expected_requests():
                start_url = start_url or url
                with open(path, encoding="utf-8") as f:
                    rsps.add(method, url, body=f.read())

            cls.harvester_class = cls.scraper_class(url=start_url)
