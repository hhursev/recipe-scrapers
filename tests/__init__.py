import unittest
from typing import Any, Iterator, Optional, Tuple

import responses

from recipe_scrapers.settings import settings


class ScraperTest(unittest.TestCase):

    maxDiff = None
    test_file_name: Optional[str] = None
    test_file_extension = "testhtml"
    scraper_class: Any

    PLACEHOLDER_URL = "https://test.example.com"

    class TemporalScraper:
        @classmethod
        def _remove_temporal_prefix(cls, url):
            https, http = url.find("/https://"), url.find("/http://")
            if https > 0:
                return url[https + 1 :]
            if http > 0:
                return url[http + 1 :]

        def __init__(self, cls, url):
            if settings.TIMETRAVEL:
                temporal_datepath = settings.TIMETRAVEL.strftime("%Y%m%d%H%M%S")
                url = f"https://web.archive.org/web/{temporal_datepath}/{url}"
            self.scraper = cls(url=url)

        def __getattr__(self, attr):
            def wrapper(*args, **kwargs):
                return getattr(self.scraper, attr)(*args, **kwargs)

            return wrapper

        def canonical_url(self):
            return self._remove_temporal_prefix(self.scraper.canonical_url())

        def image(self):
            return self._remove_temporal_prefix(self.scraper.image())

    @classmethod
    def expected_requests(cls) -> Iterator[Tuple[str, str, str]]:
        """
        Descriptions of the expected requests that the scraper-under-test will make, as
        tuples of: HTTP method, URL, path-to-content-file
        """
        filename = cls.test_file_name or cls.scraper_class.__name__.lower()
        path = f"tests/test_data/{filename}.{cls.test_file_extension}"
        yield responses.GET, cls.PLACEHOLDER_URL, path

    @classmethod
    def setUpClass(cls):
        with responses.RequestsMock() as rsps:
            start_url = None
            for method, url, path in cls.expected_requests():
                start_url = start_url or url
                with open(path, encoding="utf-8") as f:
                    rsps.add(method, url, body=f.read())

            cls.harvester_class = cls.scraper_class(url=start_url)

        # When configured, use public temporal data for a given point-in-time
        if settings.TIMETRAVEL:
            canonical_url = cls.harvester_class.canonical_url()
            if canonical_url == cls.PLACEHOLDER_URL:
                raise unittest.SkipTest(
                    "Couldn't determine the canonical URL for a scraper during archive-based testing"
                )
            cls.harvester_class = cls.TemporalScraper(
                cls=cls.scraper_class, url=canonical_url
            )
